"""
KB Embedding Sidecar Server
=============================
Keeps the sentence-transformers model warm in memory.
Reduces semantic search from ~35s (cold subprocess) to <500ms (warm inference).

USAGE:
  python KB_embed_server.py            # start on default port 5002
  python KB_embed_server.py --port 5002

ENDPOINTS:
  GET /health              -> {"status":"ok","model":"BAAI/bge-base-en-v1.5"}
  GET /semantic?q=<text>&limit=10 â†’ same JSON format as KB_gateway semantic --json

START WITH WEBAPP:
  Run this once before (or alongside) the KB-webapp backend.
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

# â”€â”€ UTF-8 stdout on Windows PowerShell â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

# â”€â”€ Locate KB_gateway.py (same directory as this script) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(
    level=logging.INFO,
    format='[KB-sidecar] %(asctime)s %(message)s',
    datefmt='%H:%M:%S',
)
log = logging.getLogger()

# â”€â”€ Startup: load model and gateway once â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
log.info("Loading KB gateway...")
try:
    import KB_gateway
    log.info(f"Loaded gateway from: {KB_gateway.__file__}")
    from KB_gateway import KB, _get_embed_model
except ImportError as e:
    log.error(f"Cannot import KB_gateway: {e}")
    sys.exit(1)

log.info("Loading embedding model 'BAAI/bge-base-en-v1.5' (once â€” stays warm)...")
model = _get_embed_model()
if model is None:
    log.error("sentence-transformers not installed. Run: pip install sentence-transformers")
    sys.exit(1)

log.info("Model ready. Initialising KB connection...")
kb = KB()
log.info("KB ready.")


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# HTTP Handler
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

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

        # â”€â”€ /health â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
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

        # â”€â”€ /embed?text=... â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
        elif parsed.path == '/embed':
            text = (params.get('text', [''])[0]).strip()
            if not text:
                self.send_json(400, {'error': 'text parameter required'})
                return
            try:
                # Generate embedding using the warm model via gateway helper
                from KB_gateway import _make_vec
                vec = _make_vec(text)
                if vec is None:
                    self.send_json(500, {'error': 'Embedding failed (model unavailable)'})
                else:
                    self.send_json(200, {'text': text, 'vec': list(vec)})
            except Exception as e:
                log.error(f"embed error: {e}")
                self.send_json(500, {'error': str(e)})

        # â”€â”€ /semantic?q=...&limit=10 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
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


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# Entry point
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def main():
    parser = argparse.ArgumentParser(description='KB Embedding Sidecar Server')
    parser.add_argument('--port', type=int,
                        default=int(os.getenv('KB_EMBED_PORT', '5002')),
                        help='Port to listen on (default: 5002)')
    args = parser.parse_args()

    server = HTTPServer(('localhost', args.port), SidecarHandler)

    log.info(f"KB Embedding Sidecar listening on http://localhost:{args.port}")
    log.info(f"  Health: http://localhost:{args.port}/health")
    log.info(f"  Search: http://localhost:{args.port}/semantic?q=VBS+token+error")
    log.info("  Model is WARM â€” all requests will respond in <500ms")
    log.info("  Ctrl+C to stop")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        log.info("Shutting down sidecar.")
        server.shutdown()


if __name__ == '__main__':
    main()

