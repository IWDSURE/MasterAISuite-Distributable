# KB2 (Knowledge Base 2) — AI Agent Gateway Interface Manual
## Master Suite Distribution v2.0 — "Trust Through Lineage"

> **Audience:** Autonomous AI Agents & Developers  
> **Interface:** Standalone Executable Binary `kb2.exe`  
> **Design Pattern:** Standalone Client, Immutable Graph Evolution, Logical Chunking  
> **Maintained by:** HRD TechCarrot — Oracle Fusion Master AI Suite

---

## 1. Operating Philosophy: Trust is Binary

In an enterprise integration landscape, a knowledge base is either **100% trustworthy** or it is **noise**. If an AI agent relies on stale, incorrect, or unverified documentation, it will make incorrect automated decisions, leading to production pipeline failures in Oracle Integration Cloud (OIC) or Business Intelligence Publisher (BIP).

To maintain absolute reliability over time, KB2 enforces an **Immutable Evolutionary Pattern**:

1.  **Do Not Overwrite Stale Nodes:** If a technical spec or business process changes, do not update the old node's text directly. Overwriting destroys the audit trail of *how* the knowledge evolved.
2.  **Node-As-Commit Pattern:** Instead, create a **new node** with the updated details and draw a relationship edge (e.g., `SUPERSEDES` or `EVOLVED_FROM`) pointing back to the old node.
3.  **Logical Chunking:** Large, monolithic blocks of text are forbidden. All information must be broken into self-contained **Logical Chunks** to maximize search precision and token efficiency.

---

## 2. Technical Context & Sidecar Architecture

The compiled executable `kb2.exe` is a standalone, lightweight, high-performance binary interface. 

*   **Database connection:** Configured via `config.json` in the same directory, communicating directly with the Oracle 23ai database.
*   **Vector Embeddings & Semantic Search:** Handled via the warm **KB2 Embedding Sidecar Server** (listening on `http://localhost:5002`). 
*   **The Golden Rule for Semantic Search:** When you execute `kb2.exe semantic "query"`, the binary makes a fast, lightweight call to the sidecar to generate the query's vector representation.
    *   ⚠️ **CRITICAL STOP-FLAG:** If semantic search returns an error, fails to respond, or gives zero results, **the sidecar server is not running!** You MUST stop execution immediately and prompt a human operator: *"The KB2 Embedding Sidecar is down. Please execute START.ps1 in the knowledge-system-graph-based directory to boot the model."* Agents must never attempt to resolve this manually.

---

## 3. Subcommand Specifications

Every subcommand supports saving its raw or formatted outputs to a specified file via the `-o` / `--output` flag. This is extremely powerful for agents to persist state across turns.

### `search` (Full-Text Search)
Fast, pattern-based search across node titles, summaries, and chunk contents.
```bash
kb2.exe search "<keyword>" [--limit <int>] [--json] [--verbose] [-o <file_path>]
```
*   *Verbose Flag (`--verbose` / `-v`):* If specified, the CLI retrieves and displays the **full node details and content chunks inline** for each search result in a single call, preventing the need to run separate `get` commands.

### `semantic` (Deep Meaning Search)
High-precision semantic similarity search. Prominent and preferred for initial discovery!
```bash
kb2.exe semantic "<natural language question>" [--limit <int>] [--json] [--verbose] [-o <file_path>]
```
*   *Behavior:* Explores both **Node-level summaries** and **Individual CLOB Chunks**! It identifies buried technical steps even if they use different terminology (e.g. searching "transfer payroll" can resolve "direct deposit costing mapping").
*   *Distance Score:* Outputs a cosine distance (0.0 = exact match, 1.0 = completely different). Distances below `0.35` indicate extremely high relevance.
*   *Verbose Flag (`--verbose` / `-v`):* If specified, the CLI retrieves and displays the **full node details and content chunks inline** for each semantic match, enabling instant, one-step full-context retrieval.

### `get` (Fetch Node Details)
Retrieve a complete node, its full relationships, and all its split logical chunks.
```bash
kb2.exe get <node_id> [--verbose] [--json] [-o <file_path>]
```
*   *Flags:* Without `--verbose`, it displays chunk summaries and a 200-character preview. Use `--verbose` or `-v` to extract the full text of all chunks (essential before making editing decisions!).
*   *Metadata Hints:* Displays the **`CREATED AT`** timestamp, enabling agents to assess the age and potential decay of the knowledge.

### `neighbors` (Graph Traversal)
Traverse the graph 1-hop away from a specific node to map dependencies.
```bash
kb2.exe neighbors <node_id> [--json] [-o <file_path>]
```
*   *Behavior:* Outputs all incoming (`IN`) and outgoing (`OUT`) relationship edges.

### `list` (List/Browse)
Browse nodes with page-level paginations and optional type filters.
```bash
kb2.exe list [--kind <KIND>] [--source <source>] [--page <int>] [--limit <int>] [-o <file_path>]
```

### `stats` & `vecstats` (Health Metrics)
Audit the database population and model vector coverage.
```bash
kb2.exe stats [-o <file_path>]
kb2.exe vecstats [-o <file_path>]
```

---

## 4. The Content Architecture: The Chunking Mandate

Large, monolithic blocks of text are forbidden. Break content into 2 to 5 chunks depending on its `KIND`. Each chunk must represent a single, clear aspect of the knowledge.

#### Standard Templates by KIND:

*   **KIND: `LESSON`**
    *   **Chunk 1 (Symptom):** The error code, logs, and observable behavior (e.g., `ORA-01722`).
    *   **Chunk 2 (Root Cause):** The forensic investigation details (e.g., "The ATP view mapped numbers as character strings").
    *   **Chunk 3 (Resolution):** Step-by-step instructions to fix (e.g., the corrected SQL view definition).
    *   **Chunk 4 (Prevention):** Defensive checks for future runs.

*   **KIND: `TECHNICAL_ARTIFACT`**
    *   **Chunk 1 (Context):** System version, environment, endpoint paths, and parameters.
    *   **Chunk 2 (Implementation):** The code block, XSLT stylesheet, or JSON payload.
    *   **Chunk 3 (Verification):** Test conditions and output verifications.

---

## 5. The Golden Path for Knowledge Creation & Evolution

Whenever you need to create a new node, refine an existing one, or apply a technical correction, you **MUST** follow this explicit 3-step sequence. Bypassing this workflow leads to duplication or orphaned knowledge.

### **Step 1: Deep Re-query (The Discovery Step)**
Before initiating any write operation, exhaustively search the graph using both text and semantic subcommands to find existing, related nodes:
```bash
kb2.exe semantic "Topic of interest" --limit 5
kb2.exe search "Topic keyword" --limit 5
```
Evaluate the creation dates (`CREATED AT`) and importance scores of all returned nodes.

### **Step 2: Strategy Evaluation (The Planning Step)**
Assess how your new knowledge aligns with what was retrieved in Step 1:
*   *Scenario A: No related nodes found.* → Your plan is **NEW_LEAF** (independent node).
*   *Scenario B: Node found, but it lacks modern parameters or has minor gaps.* → Your plan is **REFINEMENT** (add a new, evolved node and link it).
*   *Scenario C: Node found, but its facts are wrong or deprecated.* → Your plan is **CORRECTION** (add a new, corrected node and link it with a `SUPERSEDES` relation).

### **Step 3: Precise Link Determination (The Execution Step)**
Determine the target node IDs from your query in Step 1, push your new structured node and chunks, and execute the exact edge creations to preserve history and trust.

---

## 6. Guiding Use Cases (Step-by-Step)

### Use Case 1: Searching and Analyzing an Issue (Read-Only)
**Requirement:** Locate information regarding an `ORA-01722` error occurring in an HR module transfer program.

1.  **Run Semantic Search first** to see if any lesson matches the intent:
    ```bash
    kb2.exe semantic "invalid number ORA-01722 HRD Transfer" --limit 3
    ```
    *Output returns Node ID 182 with distance 0.187 (highly relevant) and its creation date.*
2.  **Retrieve Node Metadata and Chunk Summary:**
    ```bash
    kb2.exe get 182
    ```
    *You see the node contains 3 chunks: "Symptom: ORA-01722", "Cause: DEP_PROGRAM_REPORT view", and "Resolution: SQL Typecast".*
3.  **Dump Chunks and Neighbors to a Workspace file** for processing:
    ```bash
    kb2.exe get 182 --verbose -o workspace/lesson_182_details.txt
    kb2.exe neighbors 182 -o workspace/lesson_182_edges.txt
    ```
4.  **Extract the solution:** Read `workspace/lesson_182_details.txt` to find the exact SQL fix without wasting network tokens or clashing terminal display buffers.

---

### Use Case 2: Evolving Knowledge via Refinement (Write/Link)
**Requirement:** You are an automated deployment agent. You have modified the VBS Employee Transfer application to support a new optional field `LegalEntityID` (Node 181 already exists as a base specification). You need to add this new learning.

1.  **Step 1: Re-query the Graph.**
    ```bash
    kb2.exe semantic "VBS employee transfer vacancy automation" --verbose
    ```
    *Identifies Node ID 181, created on 2026-06-11.*
2.  **Step 2: Evaluate & Plan.**
    *   Node 181 exists and is correct, but needs a modern extension. Plan: **REFINEMENT** pointing back to `181`.
3.  **Step 3: Create the Refinement Node** (The Header):
    ```bash
    kb2.exe push --title "VBS Vacancy Automation: LegalEntityID Extension" --kind EXPERIENCE --summary "Adds LegalEntityID optional field mapping to Employee Transfer VBS screen" --source AI_AGENT --importance 8
    ```
    *Database returns new Node ID: **505***
4.  **Push the logical Chunks to Node 505:**
    *   *Chunk 1 (Extension Context):*
        ```bash
        kb2.exe push_chunk 505 --summary "Functional Scope" --content "In June 2026, the transfer screen was modified to allow legal entity selection. This filters vacancies dynamically before execution."
        ```
    *   *Chunk 2 (Technical Mapping):*
        ```bash
        kb2.exe push_chunk 505 --summary "JSON Payload Changes" --content "The outbound REST call now appends 'LegalEntityId': value to the request payload."
        ```
5.  **Link Node 505 back to the ancestral Node 181** to represent evolution:
    ```bash
    kb2.exe link 505 181 --type EVOLVED_FROM --weight 9 --note "Adds LegalEntityId field selection logic to the vacancy automation screen"
    ```
6.  **Verify the newly evolved lineage:**
    ```bash
    kb2.exe get 505
    ```

---

### Use Case 3: Negating/Superseding Faulty Knowledge (Correction)
**Requirement:** You discover Node 112 states that the OIC Transfer API URL is `https://oic.design/v1/transfer`. However, R13 deprecated v1, and the current active live API is `https://oic.design/v2/transfer-engine`. Node 112 is active and wrong.

1.  **Step 1: Re-query the Graph.**
    ```bash
    kb2.exe semantic "OIC Transfer API URL" --verbose
    ```
    *Identifies Node ID 112, created on 2026-06-02.*
2.  **Step 2: Evaluate & Plan.**
    *   Node 112 is wrong/deprecated. Plan: **CORRECTION** with a `SUPERSEDES` link.
3.  **Step 3: Create the Correction Node:**
    ```bash
    kb2.exe push --title "OIC Transfer API v2 Endpoint Correction" --kind TECHNICAL_ARTIFACT --summary "Deprecated OIC v1 endpoint and maps active v2 transfer-engine" --source AI_AGENT --importance 10
    ```
    *Returns Node ID: **510***
4.  **Add Chunks to Node 510:**
    *   *Chunk 1 (Deprecation Details):*
        ```bash
        kb2.exe push_chunk 510 --summary "v1 Deprecation" --content "API endpoint /v1/transfer is completely deprecated. Calling this endpoint now returns 404 Resource Not Found."
        ```
    *   *Chunk 2 (Active Endpoint Specs):*
        ```bash
        kb2.exe push_chunk 510 --summary "v2 Specs" --content "Base URL: https://oic.design/v2/transfer-engine. Payload remains identical, but requires an active OIC Gen3 instance."
        ```
5.  **Supersede Node 112:** Connect the correction with a high-weight edge:
    ```bash
    kb2.exe link 510 112 --type SUPERSEDES --weight 10 --note "Deprecated v1 endpoint and maps active v2 endpoint"
    ```
6.  **Audit Trace:** Future searchers of "OIC Transfer API" will see BOTH 112 and 510, with 510 clearly marked as **SUPERSEDES** 112, keeping the entire history logical, transparent, and trustworthy.

---

## 7. Anti-Patterns: What AI Agents MUST NOT Do

*   ❌ **The "Silent Update":** Never run random SQL DML statements to bypass the gateway when updating facts. Always use `push` and `link` so the graph remains semantically linked.
*   ❌ **The "Ghost Node":** Do not push a node into the database without creating at least one link to a project, lesson, or ancestor node. An unlinked node is an orphaned node and degrades semantic walk efficiency.
*   ❌ **The "Infinite Loop":** If semantic search fails with connection errors, **do not retry indefinitely**. The sidecar is down. Hand off immediately to a human operator.
*   ❌ **The "Garbage Tag":** Do not add redundant or arbitrary tags (e.g., `#cool`, `#stuff`). Use standard tags corresponding to modules (`oic`, `bip`, `fusion`, `vbs`, `atp`).
*   ❌ **The "Mega Chunk":** Do not bypass the standard by creating a multi-chunk node but putting 95% of the text in Chunk 1 and blank notes in Chunks 2 and 3. Ensure the text distribution is balanced and logical.
*   ❌ **Autonomous Refactoring:** Do not attempt to autonomously split or refactor other nodes' chunks, as this carries a risk of textual corruption or loss of functional meaning. Leave structure refactorings to Human Operators.

---
*Maintained by HRD TechCarrot — AI Suite Standards v2.0*
*Master Executable: `kb2.exe`*
