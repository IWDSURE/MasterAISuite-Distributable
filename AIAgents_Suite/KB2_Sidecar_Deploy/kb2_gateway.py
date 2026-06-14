"""
KB2 Knowledge Base 2.0 — Python Agent Gateway
==============================================
Gives AI agents direct, structured access to the KB2 graph knowledge base.
Running on Oracle AI Database 26ai with native VECTOR support.

CAPABILITIES:
  - search(term)           : Full-text keyword search across titles, summaries, chunk content
  - semantic_search(query) : Semantic/meaning-based search using Oracle 26ai VECTOR_DISTANCE
  - get_node(id)           : Get full node with all content chunks + relationships
  - get_neighbors(id)      : Get directly connected nodes (1-hop graph traversal)
  - list_nodes(kind, src)  : Browse nodes by kind or source
  - push_node(...)         : Contribute new knowledge (auto-embeds if model available) [alias: add]
  - push_chunk(...)        : Add content chunk to an existing node (auto-embeds)
  - push_edge(...)         : Create a relationship between two nodes [alias: link]
  - stats()                : System-wide stats including vector coverage
  - vector_stats()         : Detailed embedding coverage report

USAGE (import):
  from kb2_gateway import KB2
  kb = KB2()

  # Keyword search (always works)
  results = kb.search("XSLT namespace")

  # Semantic search (requires: pip install sentence-transformers + run kb2_embed.py)
  results = kb.semantic_search("how to fix VBS authentication errors")

  node = kb.get_node(66)
  kb.push_node("My New Finding", kind="LESSON", summary="...", content="...", tags="oic,xslt")

USAGE (CLI):
  python kb2_gateway.py search "XSLT namespace"         # keyword search
  python kb2_gateway.py semantic "VBS auth token error" # semantic search
  python kb2_gateway.py get 66
  python kb2_gateway.py get 66 --verbose
  python kb2_gateway.py neighbors 66
  python kb2_gateway.py list --kind DOCUMENT
  python kb2_gateway.py stats
  python kb2_gateway.py vecstats                        # vector embedding coverage
  python kb2_gateway.py push --title "My Lesson" --kind LESSON --summary "..." --content "Full text" --tags "oic,hcm"
  python kb2_gateway.py add  --title "My Lesson" --kind LESSON --content @myfile.md
  python kb2_gateway.py link 66 68 --type RELATED_TO --weight 8 --note "related"
  python kb2_gateway.py push --title "From file" --content @myfile.md

SEMANTIC SEARCH SETUP:
  pip install sentence-transformers
  python kb2_embed.py          # populate vec columns (run once)
  python kb2_gateway.py vecstats

CONNECTION (optional overrides — defaults work out of the box):
  python kb2_gateway.py --dsn localhost:1521/FREEPDB1 search "term"
  python kb2_gateway.py --user ctx_user --password ctx_pass123 stats

CREDENTIALS: Loaded automatically from the .env file. No manual setup needed.

MAINTENANCE POLICY: AI agents must NOT modify this file.
  Report bugs to the system maintainer. Do not attempt self-fixes.
"""

from __future__ import annotations  # Python 3.9 compatibility for type hints

import os
import sys
import json
import argparse
import textwrap
from typing import Optional, List, Dict, Any

# ── Fix 1: Unicode resilience ──────────────────────────────────────────────────
# PowerShell and some terminals default to non-UTF-8 encoding.
# Reconfigure stdout/stderr to UTF-8 so emoji and special chars print cleanly.
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass  # Never crash on I/O config — degrade gracefully

try:
    import oracledb
except ImportError:
    print("ERROR: oracledb not installed. Run: pip install oracledb")
    sys.exit(1)

# ── Fix 2: LOB connection persistence ─────────────────────────────────────────
# fetch_lobs=False tells oracledb to inline LOB data during fetch, so CLOB
# values are returned as plain Python strings — no separate .read() call needed,
# and no DPY-1001 "not connected" error when reading after connection closes.
oracledb.defaults.fetch_lobs = False

try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), 'kb2-webapp', 'backend', '.env'))
except ImportError:
    pass  # dotenv optional

# ─────────────────────────────────────────────────────────────
# Default Configuration (overridable via CLI or constructor)
# ─────────────────────────────────────────────────────────────
DB_USER = os.getenv("DB_USER", "ctx_user")
DB_PASS = os.getenv("DB_PASS", "ctx_pass123")
DB_DSN  = os.getenv("DB_DSN",  "localhost:1521/FREEPDB1")

# ─────────────────────────────────────────────────────────────
# Semantic Search — Embedding Model Cache
# ─────────────────────────────────────────────────────────────
# The model is loaded once per process and cached here.
# sentence-transformers is an optional dependency — all other
# gateway functions work fine without it.

_embed_model = None   # module-level singleton


def _get_embed_model():
    """
    Load and cache the BAAI/bge-base-en-v1.5 embedding model.
    Returns the model, or None if sentence-transformers is not installed.
    First call downloads model; subsequent calls are instant (cached).
    """
    global _embed_model
    if _embed_model is not None:
        return _embed_model
    try:
        from sentence_transformers import SentenceTransformer
        _embed_model = SentenceTransformer('BAAI/bge-base-en-v1.5')
        return _embed_model
    except ImportError:
        return None
    except Exception:
        return None


def _make_vec(text: str):
    """
    Generate a 768-dim FLOAT32 vector for the given text.
    Returns array.array('f', ...) or None if model unavailable.
    """
    import array as _array
    model = _get_embed_model()
    if model is None:
        return None
    text = (text or '').strip() or 'empty'
    embedding = model.encode(text, normalize_embeddings=True, show_progress_bar=False)
    return _array.array('f', embedding.tolist())


# ─────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────

def _row_to_dict(cursor, row):
    """Convert a cursor row to a dict using lowercase column names."""
    return {col[0].lower(): val for col, val in zip(cursor.description, row)}


def _safe_print(text: str) -> None:
    """Print with fallback for terminals that can't handle certain characters."""
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode('ascii', errors='replace').decode('ascii'))


# ─────────────────────────────────────────────────────────────
# KB2 Gateway Class
# ─────────────────────────────────────────────────────────────

class KB2:
    """
    AI Agent gateway to the KB2 Knowledge Base.

    Thin-mode Oracle connection — no Oracle Client installation required.
    No credentials needed — configured automatically from environment.

    Usage:
        kb = KB2()
        results = kb.search("XSLT")
        node = kb.get_node(66)
        node_id = kb.push_node("Title", kind="LESSON", summary="...", content="...")
    """

    def __init__(self, user: str = DB_USER, password: str = DB_PASS,
                 dsn: str = DB_DSN):
        self._user = user
        self._password = password
        self._dsn = dsn
        self._conn = None

    def _connect(self):
        if getattr(self, '_conn', None) is not None:
            try:
                self._conn.ping()
                return self._conn
            except Exception as e:
                try:
                    self._conn.close()
                except Exception:
                    pass
                self._conn = None
        self._conn = oracledb.connect(user=self._user, password=self._password,
                                      dsn=self._dsn)
        return self._conn

    def _execute(self, sql: str, params=None, fetch_all: bool = True) -> list:
        """Execute SQL and return list of dicts. Commits DML automatically."""
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params or [])
                if not cur.description:
                    conn.commit()
                    return []
                rows = cur.fetchall() if fetch_all else [cur.fetchone()]
                return [_row_to_dict(cur, r) for r in rows if r]

    # ─────────────────────────────────────────────────────────
    # SEARCH
    # ─────────────────────────────────────────────────────────

    def search(self, term: str, limit: int = 30) -> list:
        """
        Full-text search across titles (relevance 10), summaries (7),
        and all CLOB chunk content (4).

        Args:
            term:  Search term — case-insensitive, partial match
            limit: Max results returned (default 30)

        Returns:
            List of dicts: {id, title, kind, summary, importance_score,
                            source, match_in, relevance}
            match_in is one of: TITLE | SUMMARY | CONTENT

        Example:
            for r in kb.search("XSLT namespace"):
                print(f"[{r['match_in']}] {r['id']}: {r['title']}")
        """
        u = term.upper()
        pattern = f'%{u}%'
        sql = """
            SELECT id, title, kind, summary, importance_score, source,
                   match_in, relevance
            FROM (
                SELECT n.id, n.title, n.kind, n.summary,
                       n.importance_score, n.source,
                       'TITLE' AS match_in, 10 AS relevance
                FROM KB2_NODE n
                WHERE UPPER(n.title) LIKE :1

                UNION

                SELECT n.id, n.title, n.kind, n.summary,
                       n.importance_score, n.source,
                       'SUMMARY' AS match_in, 7 AS relevance
                FROM KB2_NODE n
                WHERE UPPER(n.summary) LIKE :2
                  AND UPPER(n.title) NOT LIKE :3

                UNION

                SELECT DISTINCT n.id, n.title, n.kind, n.summary,
                       n.importance_score, n.source,
                       'CONTENT' AS match_in, 4 AS relevance
                FROM KB2_NODE n
                JOIN KB2_NODE_CONTENT c ON c.node_id = n.id
                WHERE DBMS_LOB.INSTR(UPPER(c.content), :4) > 0
                  AND UPPER(n.title)   NOT LIKE :5
                  AND UPPER(n.summary) NOT LIKE :6
            )
            ORDER BY relevance DESC, importance_score DESC
            FETCH FIRST :7 ROWS ONLY
        """
        return self._execute(sql, [pattern, pattern, pattern, u, pattern, pattern, limit])

    # ─────────────────────────────────────────────────────────
    # GET NODE
    # ─────────────────────────────────────────────────────────

    def get_node(self, node_id: int, include_chunks: bool = True,
                 include_edges: bool = True) -> dict | None:
        """
        Retrieve a complete node with all content chunks and relationships.

        With oracledb.defaults.fetch_lobs=False, CLOB content is returned
        as plain Python strings — no connection persistence issues.

        Args:
            node_id:        Node ID to retrieve
            include_chunks: Include all content chunks (default True)
            include_edges:  Include relationships/edges (default True)

        Returns:
            Dict with node metadata, 'chunks' list, and 'edges' list.
            Returns None if node not found.

        Example:
            node = kb.get_node(66)
            for chunk in node['chunks']:
                print(chunk['chunk_summary'])
                print(chunk['content'])    # Full CLOB as string, no read() needed
        """
        nodes = self._execute(
            "SELECT id, title, kind, summary, importance_score, source, "
            "metadata, created_at, last_used_at FROM KB2_NODE WHERE id = :1",
            [node_id]
        )
        if not nodes:
            return None

        node = nodes[0]

        # Track last usage (best-effort, non-fatal)
        try:
            with self._connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "UPDATE KB2_NODE SET last_used_at = CURRENT_TIMESTAMP WHERE id = :1",
                        [node_id]
                    )
                    conn.commit()
        except Exception:
            pass

        if include_chunks:
            # fetch_lobs=False means content is already a string — no .read() needed
            node['chunks'] = self._execute(
                "SELECT id, node_id, chunk_seq, chunk_summary, content, created_at "
                "FROM KB2_NODE_CONTENT WHERE node_id = :1 ORDER BY chunk_seq",
                [node_id]
            )
        else:
            node['chunks'] = []

        node['edges'] = self.get_neighbors(node_id) if include_edges else []

        return node

    # ─────────────────────────────────────────────────────────
    # NEIGHBORS
    # ─────────────────────────────────────────────────────────

    def get_neighbors(self, node_id: int) -> list:
        """
        Get all directly connected nodes (1 hop).

        Returns both outgoing (OUT) and incoming (IN) edges with the
        title, kind, and summary of each connected node.

        Returns:
            List of dicts: {direction, edge_id, relation_type, weight, note,
                            related_id, related_title, related_kind, related_summary}
        """
        sql = """
            SELECT 'OUT' AS direction, e.id AS edge_id,
                   e.relation_type, e.weight, e.note,
                   n.id AS related_id, n.title AS related_title,
                   n.kind AS related_kind, n.summary AS related_summary
            FROM KB2_EDGE e JOIN KB2_NODE n ON n.id = e.to_id
            WHERE e.from_id = :1
            UNION ALL
            SELECT 'IN' AS direction, e.id AS edge_id,
                   e.relation_type, e.weight, e.note,
                   n.id AS related_id, n.title AS related_title,
                   n.kind AS related_kind, n.summary AS related_summary
            FROM KB2_EDGE e JOIN KB2_NODE n ON n.id = e.from_id
            WHERE e.to_id = :2
            ORDER BY weight DESC
        """
        return self._execute(sql, [node_id, node_id])

    # ─────────────────────────────────────────────────────────
    # LIST NODES
    # ─────────────────────────────────────────────────────────

    def list_nodes(self, kind: str = None, source: str = None,
                   page: int = 1, limit: int = 20) -> list:
        """
        Browse nodes with optional filters, sorted by importance.

        Args:
            kind:   Filter by kind (DOCUMENT, RESOURCE, LESSON, NOTE, DECISION, EXPERIENCE)
            source: Filter by source (KS_RESOURCES, AI_AGENT, etc.)
            page:   Page number, 1-indexed
            limit:  Results per page
        """
        offset = (page - 1) * limit
        conditions, params = [], []
        if kind:
            conditions.append("kind = :k")
            params.append(kind)
        if source:
            conditions.append("source = :s")
            params.append(source)

        where = ("WHERE " + " AND ".join(conditions)) if conditions else ""
        sql = f"""
            SELECT id, title, kind, summary, importance_score, source,
                   created_at, last_used_at
            FROM KB2_NODE
            {where}
            ORDER BY importance_score DESC, created_at DESC
            OFFSET {offset} ROWS FETCH NEXT {limit} ROWS ONLY
        """
        return self._execute(sql, params)

    # ─────────────────────────────────────────────────────────
    # PUSH / ADD NODE
    # ─────────────────────────────────────────────────────────

    def push_node(self, title: str, kind: str = 'NOTE', summary: str = None,
                  source: str = 'AI_AGENT', importance: int = 5,
                  content: str = None, content_summary: str = None,
                  tags: str = None) -> int:
        """
        Push new knowledge into the KB2 system. Alias: add_node()

        Args:
            title:           Concise, searchable node title
            kind:            NOTE | LESSON | RESOURCE | DOCUMENT | DECISION | EXPERIENCE | CONCEPT
            summary:         1-2 sentences shown in lists and search results (searchable)
            source:          Creator identifier (default: AI_AGENT)
            importance:      Score 1-10 (default 5). Use 8-9 for hard-won lessons.
            content:         Full content stored as a CLOB chunk (no size limit, searchable)
            content_summary: Label for the content chunk (default: 'Main Content')
            tags:            Comma-separated tags stored in metadata (e.g. 'oic,xslt,hcm')

        Returns:
            New node ID (int)

        Example:
            node_id = kb.push_node(
                title="OIC: XSLT choose block pattern",
                kind="LESSON",
                summary="Use nested xsl:choose instead of variables in OIC Mapper",
                content="Full explanation...",
                tags="oic,xslt,mapper",
                importance=8
            )
        """
        # Pack tags into metadata JSON if provided
        metadata = None
        if tags:
            tag_list = [t.strip() for t in tags.split(',') if t.strip()]
            metadata = json.dumps({"tags": tag_list})

        with self._connect() as conn:
            with conn.cursor() as cur:
                out_id = cur.var(oracledb.NUMBER)
                cur.execute(
                    "INSERT INTO KB2_NODE "
                    "(title, kind, summary, source, importance_score, metadata, created_at) "
                    "VALUES (:1, :2, :3, :4, :5, :6, CURRENT_TIMESTAMP) RETURNING id INTO :7",
                    [title, kind, summary, source, importance, metadata, out_id]
                )
                node_id = int(out_id.getvalue()[0])
                conn.commit()

        # Auto-embed if sentence-transformers is available (best-effort, never blocks push)
        try:
            vec = _make_vec(f"{title}. {summary or ''}")
            if vec is not None:
                with self._connect() as conn:
                    with conn.cursor() as cur:
                        cur.execute("UPDATE KB2_NODE SET vec = :1 WHERE id = :2",
                                    [vec, node_id])
                        conn.commit()
        except Exception:
            pass

        if content:
            self.push_chunk(node_id, content_summary or "Main Content", content)

        return node_id

    # Alias for intuitive naming
    add_node = push_node

    def push_chunk(self, node_id: int, summary: str, content: str) -> None:
        """
        Add a content chunk to an existing node.

        Args:
            node_id: Target node ID
            summary: Short label for this chunk (shown in web UI)
            content: Full text (CLOB — no practical size limit)
        """
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT NVL(MAX(chunk_seq), 0) + 1 FROM KB2_NODE_CONTENT WHERE node_id = :1",
                    [node_id]
                )
                next_seq = cur.fetchone()[0]

                # Auto-embed chunk if model available
                vec = _make_vec(f"{summary or ''}. {str(content or '')[:1200]}")

                cur.execute(
                    "INSERT INTO KB2_NODE_CONTENT "
                    "(node_id, chunk_seq, chunk_summary, content, vec, created_at) "
                    "VALUES (:1, :2, :3, :4, :5, CURRENT_TIMESTAMP)",
                    [node_id, next_seq, summary, content, vec]
                )
                conn.commit()

    def push_edge(self, from_id: int, to_id: int,
                  relation_type: str = 'RELATED_TO',
                  weight: int = 5, note: str = None) -> None:
        """
        Create a relationship between two nodes (idempotent — skips duplicates).

        Args:
            from_id:       Source node ID
            to_id:         Target node ID
            relation_type: RELATED_TO | PARENT_OF | DEPENDS_ON | CONTRADICTS | EXTENDS
            weight:        Relationship strength 1-10
            note:          Why these nodes are related (helps future agents)
        """
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT COUNT(*) FROM KB2_EDGE "
                    "WHERE from_id=:1 AND to_id=:2 AND relation_type=:3",
                    [from_id, to_id, relation_type]
                )
                if cur.fetchone()[0] == 0:
                    cur.execute(
                        "INSERT INTO KB2_EDGE "
                        "(from_id, to_id, relation_type, weight, note, created_at) "
                        "VALUES (:1, :2, :3, :4, :5, CURRENT_TIMESTAMP)",
                        [from_id, to_id, relation_type, weight, note]
                    )
                    conn.commit()

    # Alias
    link = push_edge

    def stats(self) -> dict:
        """Return system-wide counts including vector embedding coverage."""
        rows = self._execute(
            "SELECT "
            "(SELECT COUNT(*) FROM KB2_NODE) AS total_nodes, "
            "(SELECT COUNT(*) FROM KB2_EDGE) AS total_edges, "
            "(SELECT COUNT(*) FROM KB2_NODE_CONTENT) AS total_chunks, "
            "(SELECT COUNT(*) FROM KB2_NODE WHERE vec IS NOT NULL) AS nodes_embedded, "
            "(SELECT COUNT(*) FROM KB2_NODE_CONTENT WHERE vec IS NOT NULL) AS chunks_embedded "
            "FROM DUAL"
        )
        return rows[0] if rows else {}

    def vector_stats(self) -> dict:
        """Detailed embedding coverage — how many nodes/chunks have vec populated."""
        rows = self._execute(
            "SELECT "
            "(SELECT COUNT(*) FROM KB2_NODE) AS total_nodes, "
            "(SELECT COUNT(*) FROM KB2_NODE WHERE vec IS NOT NULL) AS nodes_embedded, "
            "(SELECT COUNT(*) FROM KB2_NODE WHERE vec IS NULL) AS nodes_pending, "
            "(SELECT COUNT(*) FROM KB2_NODE_CONTENT) AS total_chunks, "
            "(SELECT COUNT(*) FROM KB2_NODE_CONTENT WHERE vec IS NOT NULL) AS chunks_embedded, "
            "(SELECT COUNT(*) FROM KB2_NODE_CONTENT WHERE vec IS NULL) AS chunks_pending "
            "FROM DUAL"
        )
        return rows[0] if rows else {}

    # ─────────────────────────────────────────────────────────
    # SEMANTIC SEARCH (Oracle 26ai VECTOR_DISTANCE)
    # ─────────────────────────────────────────────────────────

    def semantic_search(self, query: str, limit: int = 10) -> list:
        """
        Semantic similarity search using Oracle 26ai VECTOR_DISTANCE().

        Finds nodes whose meaning is similar to the query — even when exact
        words don't match. Searches both node-level and chunk-level embeddings.

        Requires:
          1. pip install sentence-transformers
          2. python kb2_embed.py  (populate vec columns — run once)

        Args:
            query: Natural language query (e.g. "VBS authentication token error")
            limit: Max results to return (default 10)

        Returns:
            List of dicts: {id, title, kind, summary, importance_score, source,
                            match_in, distance}
            distance: 0.0 = identical, 1.0 = completely different (COSINE)
            match_in: 'NODE' (summary matched) or 'CHUNK' (content matched)

        Example:
            for r in kb.semantic_search("how to resolve VBS 403 errors"):
                print(f"[dist={r['distance']:.3f}] {r['title']}")
        """
        query_vec = _make_vec(query)
        if query_vec is None:
            sys.stderr.write("[ERROR] semantic_search requires sentence-transformers.\n")
            sys.stderr.write("        Run: pip install sentence-transformers\n")
            sys.stderr.write("        Then: python kb2_embed.py\n")
            return []

        results = []
        seen_ids = set()
        conn = self._connect()

        # 1. Node-level: embed summary similarity
        node_sql = """
            SELECT n.id, n.title, n.kind, n.summary, n.importance_score, n.source,
                   'NODE' AS match_in,
                   VECTOR_DISTANCE(n.vec, :1, COSINE) AS distance
            FROM KB2_NODE n
            WHERE n.vec IS NOT NULL
            ORDER BY distance ASC
            FETCH FIRST :2 ROWS ONLY
        """
        try:
            with conn.cursor() as cur:
                cur.execute(node_sql, [query_vec, limit])
                cols = [c[0].lower() for c in cur.description]
                for row in cur.fetchall():
                    d = dict(zip(cols, row))
                    results.append(d)
                    seen_ids.add(d['id'])
        except Exception as e:
            sys.stderr.write(f"[WARN] Node vector search failed: {e}\n")
            sys.stderr.write("       Run 'python kb2_embed.py' to populate vectors.\n")
            return []

        # 2. Chunk-level: finds knowledge buried in content chunks
        chunk_sql = """
            SELECT n.id, n.title, n.kind, n.summary, n.importance_score, n.source,
                   'CHUNK' AS match_in,
                   MIN(VECTOR_DISTANCE(c.vec, :1, COSINE)) AS distance
            FROM KB2_NODE_CONTENT c
            JOIN KB2_NODE n ON n.id = c.node_id
            WHERE c.vec IS NOT NULL
            GROUP BY n.id, n.title, n.kind, n.summary, n.importance_score, n.source
            ORDER BY distance ASC
            FETCH FIRST :2 ROWS ONLY
        """
        try:
            with conn.cursor() as cur:
                cur.execute(chunk_sql, [query_vec, limit])
                cols = [c[0].lower() for c in cur.description]
                for row in cur.fetchall():
                    d = dict(zip(cols, row))
                    if d['id'] not in seen_ids:
                        results.append(d)
                        seen_ids.add(d['id'])
                    else:
                        # Keep whichever has lower (better) distance
                        for r in results:
                            if r['id'] == d['id'] and d['distance'] < r['distance']:
                                r['distance'] = d['distance']
                                r['match_in'] = 'CHUNK'
        except Exception as e:
            sys.stderr.write(f"[WARN] Chunk vector search failed: {e}\n")

        # Re-sort merged results by distance, take top-N
        results.sort(key=lambda x: float(x.get('distance') or 1.0))
        return results[:limit]


# ─────────────────────────────────────────────────────────────
# CLI Display Helpers
# ─────────────────────────────────────────────────────────────

def _print_node_card(node: dict, verbose: bool = False) -> None:
    """Print a formatted node summary card."""
    _safe_print(f"\n{'='*70}")
    _safe_print(f"  NODE ID   : {node.get('id')}")
    _safe_print(f"  TITLE     : {node.get('title')}")
    _safe_print(f"  KIND      : {node.get('kind')}  |  IMPORTANCE: {node.get('importance_score')}/10")
    _safe_print(f"  SOURCE    : {node.get('source')}")

    meta = node.get('metadata')
    if meta:
        try:
            m = json.loads(meta) if isinstance(meta, str) else meta
            if m.get('tags'):
                _safe_print(f"  TAGS      : {', '.join(m['tags'])}")
        except Exception:
            pass

    _safe_print(f"  SUMMARY   : {textwrap.fill(str(node.get('summary') or ''), 65, subsequent_indent='              ')}")

    chunks = node.get('chunks', [])
    if chunks:
        _safe_print(f"\n  CONTENT ({len(chunks)} chunk{'s' if len(chunks) != 1 else ''}):")
        for c in chunks:
            _safe_print(f"\n    [{c.get('chunk_seq')}] {c.get('chunk_summary')}")
            content = str(c.get('content') or '')
            if verbose:
                wrapped = textwrap.fill(content, 66, initial_indent='        ',
                                        subsequent_indent='        ')
                _safe_print(wrapped)
            else:
                preview = content[:200].replace('\n', ' ')
                _safe_print(f"        {preview}{'...' if len(content) > 200 else ''}")

    edges = node.get('edges', [])
    if edges:
        _safe_print(f"\n  RELATIONSHIPS ({len(edges)}):")
        for e in edges:
            arrow = '-->' if e.get('direction') == 'OUT' else '<--'
            _safe_print(f"    [{e.get('direction')}] {arrow}[{e.get('relation_type')}]"
                        f"--> Node {e.get('related_id')}: {e.get('related_title')}")

    _safe_print(f"{'='*70}\n")


def _print_search_results(results: list, term: str) -> None:
    """Print formatted search results."""
    _safe_print(f"\n[SEARCH] \"{term}\" -- {len(results)} result(s)\n")
    _safe_print(f"{'─'*70}")
    for r in results:
        match_label = {
            'TITLE':   '[TITLE]  ',
            'SUMMARY': '[SUMMARY]',
            'CONTENT': '[CONTENT]',
        }.get(r.get('match_in', '').upper(), '[?]     ')
        _safe_print(f"  {match_label}  [{str(r.get('kind') or ''):10}] ID={r.get('id'):4}  |  {r.get('title')}")
        summary = str(r.get('summary') or '')
        if summary:
            _safe_print(f"               {summary[:80]}{'...' if len(summary) > 80 else ''}")
    _safe_print(f"{'─'*70}\n")
    _safe_print(f"  Get full details: python kb2_gateway.py get <ID>")
    _safe_print(f"  Get neighbors:    python kb2_gateway.py neighbors <ID>\n")


# ─────────────────────────────────────────────────────────────
# CLI Entry Point
# ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='KB2 Knowledge Base Gateway -- AI Agent CLI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
        Examples:
          python kb2_gateway.py search "XSLT namespace"
          python kb2_gateway.py get 66
          python kb2_gateway.py get 66 --verbose
          python kb2_gateway.py neighbors 66
          python kb2_gateway.py list
          python kb2_gateway.py list --kind LESSON
          python kb2_gateway.py stats
          python kb2_gateway.py push --title "My Lesson" --kind LESSON --summary "Brief" --content "Full text" --tags "oic,xslt"
          python kb2_gateway.py add  --title "My Lesson" --kind LESSON --content @myfile.md
          python kb2_gateway.py link 66 68 --type RELATED_TO --weight 8 --note "Both about OIC mapper"

        Connection override (optional -- defaults work out of the box):
          python kb2_gateway.py --dsn localhost:1521/FREEPDB1 search "term"
        """)
    )

    # ── Fix 3: Global connection override flags ─────────────────────────────
    parser.add_argument('--dsn',      default=None, help='DB connection string (default: from env)')
    parser.add_argument('--user',     default=None, help='DB username (default: from env)')
    parser.add_argument('--password', default=None, help='DB password (default: from env)')

    sub = parser.add_subparsers(dest='command')

    # search
    p_search = sub.add_parser('search', help='Full-text search across all nodes and chunks')
    p_search.add_argument('term', help='Search term (case-insensitive, partial match)')
    p_search.add_argument('--limit', type=int, default=30, help='Max results (default: 30)')
    p_search.add_argument('--json', action='store_true', help='Output raw JSON')

    # get
    p_get = sub.add_parser('get', help='Get full node details with content chunks')
    p_get.add_argument('id', type=int, help='Node ID')
    p_get.add_argument('--verbose', '-v', action='store_true', help='Show full chunk content (not preview)')
    p_get.add_argument('--json', action='store_true', help='Output raw JSON')

    # neighbors
    p_nb = sub.add_parser('neighbors', help='Get connected nodes (1-hop graph traversal)')
    p_nb.add_argument('id', type=int, help='Node ID')
    p_nb.add_argument('--json', action='store_true')

    # list
    p_list = sub.add_parser('list', help='List/browse nodes with optional filters')
    p_list.add_argument('--kind', help='Filter: DOCUMENT | LESSON | RESOURCE | NOTE | DECISION | EXPERIENCE')
    p_list.add_argument('--source', help='Filter by source (e.g. AI_AGENT, KS_RESOURCES)')
    p_list.add_argument('--page', type=int, default=1)
    p_list.add_argument('--limit', type=int, default=20)
    p_list.add_argument('--json', action='store_true')

    # stats
    p_stats = sub.add_parser('stats', help='System-wide stats (node/edge/chunk counts + vector coverage)')
    p_stats.add_argument('--json', action='store_true')

    # vecstats
    p_vs = sub.add_parser('vecstats', help='Vector embedding coverage report')
    p_vs.add_argument('--json', action='store_true')

    # semantic
    p_sem = sub.add_parser('semantic', help='Semantic similarity search (Oracle 26ai VECTOR_DISTANCE)')
    p_sem.add_argument('query', help='Natural language query')
    p_sem.add_argument('--limit', type=int, default=10, help='Max results (default: 10)')
    p_sem.add_argument('--json', action='store_true', help='Output raw JSON')

    # ── Fix 4 & 5: push + add alias, plus --tags ────────────────────────────
    def _add_push_args(p):
        p.add_argument('--title',    required=True, help='Node title (concise, searchable)')
        p.add_argument('--kind',     default='NOTE',
                       help='LESSON | RESOURCE | DOCUMENT | DECISION | EXPERIENCE | NOTE | CONCEPT')
        p.add_argument('--summary',  default=None,
                       help='1-2 sentence description (shown in search results)')
        p.add_argument('--content',  default=None,
                       help='Full content text, or @filename to read from file')
        p.add_argument('--tags',     default=None,
                       help='Comma-separated tags: --tags "oic,xslt,hcm"')
        p.add_argument('--source',   default='AI_AGENT',
                       help='Creator identifier (default: AI_AGENT)')
        p.add_argument('--importance', type=int, default=5,
                       help='Score 1-10. Use 8-9 for hard-won lessons (default: 5)')

    p_push = sub.add_parser('push', help='Push new knowledge node to KB2')
    _add_push_args(p_push)

    # 'add' is a natural alias for 'push' — same arguments
    p_add = sub.add_parser('add', help='Add new knowledge node (alias for push)')
    _add_push_args(p_add)

    # link
    p_link = sub.add_parser('link', help='Create a relationship (edge) between two nodes')
    p_link.add_argument('from_id', type=int, help='Source node ID')
    p_link.add_argument('to_id',   type=int, help='Target node ID')
    p_link.add_argument('--type',   default='RELATED_TO', dest='rel_type',
                        help='RELATED_TO | PARENT_OF | DEPENDS_ON | CONTRADICTS | EXTENDS')
    p_link.add_argument('--weight', type=int, default=5, help='Strength 1-10')
    p_link.add_argument('--note',   default=None, help='Why these nodes are related')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # Instantiate with optional connection overrides
    kb = KB2(
        user     = args.user     or DB_USER,
        password = args.password or DB_PASS,
        dsn      = args.dsn      or DB_DSN,
    )

    # ── Command dispatch ────────────────────────────────────────────────────

    if args.command == 'search':
        results = kb.search(args.term, args.limit)
        if args.json:
            print(json.dumps(results, default=str, indent=2))
        else:
            _print_search_results(results, args.term)

    elif args.command == 'get':
        node = kb.get_node(args.id)
        if not node:
            _safe_print(f"Node {args.id} not found.")
            return
        if args.json:
            print(json.dumps(node, default=str, indent=2))
        else:
            _print_node_card(node, verbose=args.verbose)

    elif args.command == 'neighbors':
        neighbors = kb.get_neighbors(args.id)
        if args.json:
            print(json.dumps(neighbors, default=str, indent=2))
        else:
            _safe_print(f"\nNeighbors of node {args.id} ({len(neighbors)} relationships):\n")
            for n in neighbors:
                arrow = '-->' if n.get('direction') == 'OUT' else '<--'
                _safe_print(f"  [{n['direction']}] {arrow}[{n['relation_type']}] "
                            f"Node {n['related_id']}: {n['related_title']}")

    elif args.command == 'list':
        nodes = kb.list_nodes(kind=args.kind, source=args.source,
                              page=args.page, limit=args.limit)
        if args.json:
            print(json.dumps(nodes, default=str, indent=2))
        else:
            kind_label = f" kind={args.kind}" if args.kind else ""
            _safe_print(f"\nNodes{kind_label} (page {args.page}, {len(nodes)} results):\n")
            for n in nodes:
                _safe_print(f"  ID={n['id']:4}  [{str(n['kind'] or ''):10}]  "
                            f"imp={n['importance_score']}  {n['title']}")

    elif args.command == 'stats':
        s = kb.stats()
        if args.json:
            print(json.dumps(s, default=str, indent=2))
        else:
            _safe_print(f"\n  KB2 System Stats  (Oracle 26ai)")
            _safe_print(f"  {'─'*30}")
            _safe_print(f"  Nodes:  {s.get('total_nodes', '?')}")
            _safe_print(f"  Edges:  {s.get('total_edges', '?')}")
            _safe_print(f"  Chunks: {s.get('total_chunks', '?')}")
            n_emb = s.get('nodes_embedded', '?')
            c_emb = s.get('chunks_embedded', '?')
            _safe_print(f"  Vector: {n_emb} nodes embedded, {c_emb} chunks embedded\n")

    elif args.command == 'vecstats':
        vs = kb.vector_stats()
        if args.json:
            print(json.dumps(vs, default=str, indent=2))
        else:
            _safe_print(f"\n  KB2 Vector Coverage  (Oracle 26ai)")
            _safe_print(f"  {'─'*34}")
            _safe_print(f"  Nodes:  {vs.get('nodes_embedded','?'):>4} / {vs.get('total_nodes','?'):>4} embedded  "
                        f"({vs.get('nodes_pending','?')} pending)")
            _safe_print(f"  Chunks: {vs.get('chunks_embedded','?'):>4} / {vs.get('total_chunks','?'):>4} embedded  "
                        f"({vs.get('chunks_pending','?')} pending)")
            if vs.get('nodes_pending', 0) > 0 or vs.get('chunks_pending', 0) > 0:
                _safe_print(f"\n  Run: python kb2_embed.py  (to fill pending)\n")
            else:
                _safe_print(f"\n  All vectors populated. Semantic search is fully operational.\n")

    elif args.command == 'semantic':
        results = kb.semantic_search(args.query, args.limit)
        if args.json:
            print(json.dumps(results, default=str, indent=2))
        else:
            _safe_print(f"\n[SEMANTIC] \"{args.query}\" -- {len(results)} result(s)\n")
            _safe_print(f"{'─'*70}")
            for r in results:
                dist  = r.get('distance', '?')
                dist_s = f"{float(dist):.3f}" if dist != '?' else '?'
                kind  = str(r.get('kind') or '').ljust(10)
                match = r.get('match_in', '?').ljust(5)
                _safe_print(f"  [dist={dist_s}] [{kind}] [{match}] ID={r.get('id'):>4}  {r.get('title')}")
                summary = str(r.get('summary') or '')
                if summary:
                    _safe_print(f"                 {summary[:80]}{'...' if len(summary) > 80 else ''}")
            _safe_print(f"{'─'*70}\n")
            _safe_print(f"  Get full details: python kb2_gateway.py get <ID>\n")

    elif args.command in ('push', 'add'):
        content = args.content
        if content and content.startswith('@'):
            fname = content[1:]
            with open(fname, 'r', encoding='utf-8') as f:
                content = f.read()

        node_id = kb.push_node(
            title    = args.title,
            kind     = args.kind,
            summary  = args.summary,
            source   = args.source,
            importance = args.importance,
            content  = content,
            tags     = args.tags,
        )
        _safe_print(f"\nNode created: ID={node_id}\n")
        _safe_print(f"   python kb2_gateway.py get {node_id} --verbose\n")

    elif args.command == 'link':
        kb.push_edge(args.from_id, args.to_id, args.rel_type, args.weight, args.note)
        _safe_print(f"\nEdge created: {args.from_id} --[{args.rel_type}]--> {args.to_id}\n")


if __name__ == '__main__':
    main()
