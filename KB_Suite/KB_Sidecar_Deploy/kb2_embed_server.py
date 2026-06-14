"""
KB2 Embedding Sidecar Server
=============================
Keeps the sentence-transformers model warm in memory.
Reduces semantic search from ~35s (cold subprocess) to <500ms (warm inference).

USAGE:
  python kb2_embed_server.py            # start on default port 5002
  python kb2_embed_server.py --port 5002

ENDPOINTS:
  GET /health              -> {"status":"ok","model":"BAAI/bge-base-en-v1.5"}
  GET /semantic?q=<text>&limit=10 → same JSON format as kb2_gateway semantic --json

START WITH WEBAPP:
  Run this once before (or alongside) the kb2-webapp backend.
  The webapp backend (semantic.js) calls this sidecar first;
  falls back to Python subprocess if sidecar is not running.

STOP: Ctrl+C
"""

from __future__ import annotations

import sys
import os
import json
import logging
import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# ── UTF-8 stdout on Windows PowerShell ───────────────────────────────────────
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

# ── Locate kb2_gateway.py (same directory as this script) ────────────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(
    level=logging.INFO,
    format='[kb2-sidecar] %(asctime)s %(message)s',
    datefmt='%H:%M:%S',
)
log = logging.getLogger()

# ── Startup: load model and gateway once ─────────────────────────────────────
log.info("Loading KB2 gateway...")
try:
    import kb2_gateway
    log.info(f"Loaded gateway from: {kb2_gateway.__file__}")
    from kb2_gateway import KB2, _get_embed_model
except ImportError as e:
    log.error(f"Cannot import kb2_gateway: {e}")
    sys.exit(1)

log.info("Loading embedding model 'BAAI/bge-base-en-v1.5' (once — stays warm)...")
model = _get_embed_model()
if model is None:
    log.error("sentence-transformers not installed. Run: pip install sentence-transformers")
    sys.exit(1)

log.info("Model ready. Initialising KB2 connection...")
kb = KB2()
log.info("KB2 ready.")


# ─────────────────────────────────────────────────────────────────────────────
# HTTP Handler
# ─────────────────────────────────────────────────────────────────────────────

class SidecarHandler(BaseHTTPRequestHandler):

    def log_message(self, fmt, *args):
        log.info(fmt % args)

    def send_json(self, code: int, data: dict) -> None:
        body = json.dumps(data, default=str).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        # ── /health ──────────────────────────────────────────────────────────
        if parsed.path == '/health':
            s = kb.stats()
            self.send_json(200, {
                'status':  'ok',
                'model':   'BAAI/bge-base-en-v1.5',
                'dims':    768,
                'db':      'Oracle 26ai',
                'nodes':   s.get('total_nodes'),
                'chunks':  s.get('total_chunks'),
                'vectors': s.get('nodes_embedded'),
            })

        # ── /embed?text=... ──────────────────────────────────────────────────
        elif parsed.path == '/embed':
            text = (params.get('text', [''])[0]).strip()
            if not text:
                self.send_json(400, {'error': 'text parameter required'})
                return
            try:
                # Generate embedding using the warm model via gateway helper
                from kb2_gateway import _make_vec
                vec = _make_vec(text)
                if vec is None:
                    self.send_json(500, {'error': 'Embedding failed (model unavailable)'})
                else:
                    self.send_json(200, {'text': text, 'vec': list(vec)})
            except Exception as e:
                log.error(f"embed error: {e}")
                self.send_json(500, {'error': str(e)})

        # ── /semantic?q=...&limit=10 ─────────────────────────────────────────
        elif parsed.path == '/semantic':
            q     = (params.get('q',     [''])[0]).strip()
            limit = int(params.get('limit', ['10'])[0])

            if not q:
                self.send_json(400, {'error': 'q parameter required'})
                return

            try:
                results = kb.semantic_search(q, limit=limit)
                # Normalise keys to UPPERCASE for frontend consistency
                rows = [{
                    'ID':              r.get('id'),
                    'TITLE':          r.get('title'),
                    'KIND':           r.get('kind'),
                    'SUMMARY':        r.get('summary'),
                    'IMPORTANCE_SCORE': r.get('importance_score'),
                    'SOURCE':         r.get('source'),
                    'DISTANCE':       r.get('distance'),
                    'MATCH_IN':       r.get('match_in'),
                } for r in results]
                self.send_json(200, {'q': q, 'mode': 'semantic', 'rows': rows})
            except Exception as e:
                log.error(f"semantic_search error: {e}")
                self.send_json(500, {'error': str(e)})

        else:
            self.send_json(404, {
                'error': 'Unknown endpoint',
                'endpoints': ['/health', '/semantic?q=<text>&limit=10'],
            })

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.end_headers()


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='KB2 Embedding Sidecar Server')
    parser.add_argument('--port', type=int,
                        default=int(os.getenv('KB2_EMBED_PORT', '5002')),
                        help='Port to listen on (default: 5002)')
    args = parser.parse_args()

    server = HTTPServer(('localhost', args.port), SidecarHandler)

    log.info(f"KB2 Embedding Sidecar listening on http://localhost:{args.port}")
    log.info(f"  Health: http://localhost:{args.port}/health")
    log.info(f"  Search: http://localhost:{args.port}/semantic?q=VBS+token+error")
    log.info("  Model is WARM — all requests will respond in <500ms")
    log.info("  Ctrl+C to stop")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        log.info("Shutting down sidecar.")
        server.shutdown()


if __name__ == '__main__':
    main()
