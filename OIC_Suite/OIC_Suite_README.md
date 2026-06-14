# 🤖 OIC Diagnostic Suite — Comprehensive Machine-Readable Protocol & Use-Case Gallery (v3.1)

This document is the **Primary System Directive** for autonomous agents and LLMs utilizing the `oic.exe` suite. It defines the deterministic logic, data schemas, and execution cycles required for 100% reliable OIC operations.

---

## 🏗 1. System Identity & State Model

The suite is a stateless command-line interface that interacts with Oracle Integration Cloud (OIC) Gen3 instances. It maintains local state in the execution directory.

### Local State Files
| File | Role | Priority | Agent Action on Failure |
| :--- | :--- | :--- | :--- |
| `config.json` | Environment Metadata | CRITICAL | Verify `oic_host` and `instance_id`. |
| `token.txt` | **Manual User Token** | **HIGHEST** | **HUMAN-IN-THE-LOOP**: If 401/403 occurs, HALT and request a fresh Bearer token from a human. |
| `token.json` | Automated Client Token| FALLBACK | Use `oic token fetch` to refresh ONLY if `token.txt` is missing. |

### Configuration Schema (`config.json`)
```json
{
  "oic_host": "https://design.integration.<region>.ocp.oraclecloud.com",
  "instance_id": "<service_instance_name>",
  "auth_mode": "oauth",
  "idcs_host": "https://idcs-xxx.identity.oraclecloud.com",
  "client_id": "...",
  "client_secret": "...",
  "scope": "..."
}
```

---

## 🛠 2. Command Protocol Reference

Standard Execution: `oic.exe <GROUP> <COMMAND> [OPTIONS]`

### GROUP: `token` (Identity Management)
Agents must verify identity before high-value operations.
*   **`oic token check`**: Verifies connectivity.
    *   *Success Pattern*: `[OK] Token is ACTIVE and working.`
    *   *Logic*: Automatically respects `token.txt` override. Manual tokens **never** auto-refresh to prevent permission reduction.
*   **`oic token save --file <PATH>`**: Imports a token from a text file. Use this to bypass CLI character limits for long Bearer tokens.
*   **`oic token fetch`**: Uses Client Credentials to get a low-privilege token (suitable for listing, but often blocked for archives).

### GROUP: `list` (Discovery & Inventory)
*   **`list projects`**: Returns Table[ID, Name].
*   **`list integrations <PROJECT_ID>`**: Returns Table[ID, Version, Status].
*   **`list instances --id <CODE> --status FAILED --limit <N> --timewindow <T>`**:
    *   `timewindow` format: `3d` (3 days), `12h` (12 hours).
    *   Returns unique `id` required for log downloads.

### GROUP: `deployment` (Dynamic Management)
**Deployments are the primary mechanism for high-speed selective retrieval.**
*   **`deployment details <PROJECT> <DEPLOY_ID>`**:
    *   Returns the JSON list of integrations currently pinned to the deployment.
*   **`deployment update <PROJECT> <DEPLOY_ID> --integrations <LIST>`**:
    *   `<LIST>` format: `INT_A,INT_B:01.00.0005,INT_C`
    *   *Logic*: If version is omitted, the tool auto-resolves to the **latest** version in the project.

### GROUP: `download` (Persistence)
*Note: Always use `--out <PATH>` to isolate downloads.*
*   **`download deployment <PROJECT> <DEPLOY_ID> --archive`**:
    *   **GOLD STANDARD**: Exports a filtered Project ZIP containing only the integrations defined in the deployment.
    *   *Requirement*: Requires a User-Delegated Token (saved via `token.txt`).
*   **`download log <INSTANCE_ID>`**:
    *   Retrieves the full diagnostic ZIP (`icsflowlog`) or Activity Stream.

### GROUP: `analyze` (Deterministic Inference)
*These commands process local files and return structured insights for the Agent's context.*
*   **`analyze log --file <PATH>`**:
    *   Parses OIC flow logs. Extracts the exact node, error message, and payload content at the point of failure.
*   **`analyze deployment --folder <PATH>`**:
    *   Analyzes an extracted integration definition. Scans for mapper complexity and endpoint configurations.

---

## 🔄 3. Optimized Execution Cycles

### Cycle: High-Speed Selective Sync (Sync-to-Workspace)
This is the most efficient way for an agent to retrieve specific integration logic.
1.  **State Check**: Run `oic token check`. 
2.  **Token Health**: If `401/403` occurs, the agent **MUST NOT** attempt to guess tokens. It must emit a prompt: *"OIC Session Expired. Please provide a fresh Bearer token in token.txt to continue administrative operations."*
3.  **Naming**: **ASK HUMAN** for a unique temporary deployment code (e.g., `XX_COPY_MANAGER_01`). Do NOT reuse existing codes without confirmation.
4.  **Targeting**: Define target integrations (e.g., `INT_X:01.00.0000`).
5.  **Update**: Run `oic deployment update <PROJ> <HUMAN_CODE> --integrations <TARGETS>`.
6.  **Export**: Run `oic download deployment <PROJ> <HUMAN_CODE> --archive --out <DIR>`.

### Cycle: Automated Incident Root Cause Analysis (RCA)
1.  **Monitor**: `oic list instances --status FAILED --limit 1`.
2.  **Fetch**: `oic download log <ID> --out ./rca`.
3.  **Analyze**: `oic analyze log --file ./rca/downloads/log_<ID>/flow-log.json`.
4.  **Synthesize**: Map the `analyze` output to the integration source code to identify the logic bug.

---

## 🚑 4. Deterministic Error Handling (Agent Repair Logic)

| Observed Error | Root Cause | Agent Repair Action |
| :--- | :--- | :--- |
| `HTTP 401` | Token Expired. | 1. Attempt `oic token fetch`. 2. If failure persists, **ASK HUMAN** for fresh Bearer token. |
| `HTTP 403` | Permission Block. | Restricted Token detected. **ASK HUMAN** to provide a User Token with "Service Administrator" role. |
| `[FAIL] Workspace...` | Directory Error. | Verify disk space and path permissions. Use absolute paths to resolve. |
| `HTTP 404` | ID Mismatch. | Trigger `list` command for the specific group to verify ID existence and casing. |

---

## 🌟 5. Use Cases & Command Gallery

### Use Case 1: Emergency Selective Backup
**Scenario**: A critical bug is found in 3 integrations. The agent needs to download the current state of these specific 3 integrations immediately for local debugging.

*   **Step 1: Check Token**
    ```bash
    oic.exe token check
    ```
*   **Step 2: Update Temporary Deployment**
    ```bash
    oic.exe deployment update HR_PROJ TEMP_RCA_DEPLOY --integrations INT_PAYROLL:02.00.0000,INT_LEAVE:01.05.0000,INT_BENEFITS
    ```
    *(Note: INT_BENEFITS will auto-resolve to latest).*
*   **Step 3: Fast Archive Download**
    ```bash
    oic.exe download deployment HR_PROJ TEMP_RCA_DEPLOY --archive --out D:/Work/Emergency_Backup
    ```

### Use Case 2: Multi-Version Conflict Analysis
**Scenario**: The agent needs to compare version `01.00.0000` and `01.00.0005` of the same integration.

*   **Step 1: Retrieve v1**
    ```bash
    oic.exe deployment update DEV_PROJ COMP_A --integrations MY_INTEGRATION:01.00.0000
    oic.exe download deployment DEV_PROJ COMP_A --archive --out D:/compare/v1
    ```
*   **Step 2: Retrieve v5**
    ```bash
    oic.exe deployment update DEV_PROJ COMP_B --integrations MY_INTEGRATION:01.00.0005
    oic.exe download deployment DEV_PROJ COMP_B --archive --out D:/compare/v5
    ```

### Use Case 3: Failed Instance Log Extraction & Analysis
**Scenario**: An agent detects a spike in failures and needs to analyze the most recent one.

*   **Step 1: Locate ID**
    ```bash
    oic.exe list instances --status FAILED --limit 1 --timewindow 1h
    ```
*   **Step 2: Download Log**
    ```bash
    oic.exe download log 2_9PB186EfGL-PFFD3f16g --out ./incident_logs
    ```
*   **Step 3: Direct Analysis**
    ```bash
    oic.exe analyze log --file ./incident_logs/downloads/log_2_9PB186EfGL-PFFD3f16g/flow-log.json
    ```

---

## 📝 6. Detailed Technical Specifications

### A. Deployment Update Syntax Deep-Dive
The `--integrations` flag is a powerful parser. It accepts a comma-separated list where each item follows the grammar:
`<IDENTIFIER>[:<VERSION>]`

*   **Single Code**: `AJMAN_HRD_INT` -> Tool finds the integration in the project and picks the highest semantic version number.
*   **Pinned Version**: `AJMAN_HRD_INT:01.00.0005` -> Tool ignores all other versions and pins exactly to `01.00.0005`.
*   **Batch Mix**: `INT_1,INT_2:02.00.0000,INT_3` -> Resolves INT_1 and INT_3 to latest, pins INT_2.

### B. Workspace Isolation Protocol
The `--out` (or `--workspace`) parameter is critical for Agent safety. 
*   **Deterministic Pathing**: If `--out D:/data` is provided, the tool structure is:
    *   `D:/data/downloads/<PROJECT_ID>/<DEPLOYMENT_ID>_archive.zip`
    *   `D:/data/downloads/log_<INSTANCE_ID>/...`
*   **Auto-Cleaning**: Agents should clean their workspace directories before each session to ensure they are analyzing fresh data.

### C. Human-In-The-Loop (HITL) Trigger Conditions
Agents MUST stop and communicate with the Human Operator under the following "Blocked State" conditions:
1.  **Administrative Block**: `HTTP 401` or `HTTP 403` during an `archive` or `deployment update` operation. These APIs require User sessions.
2.  **Deployment Naming**: **ALWAYS** ask the human for a unique deployment code (e.g. `AGENT_TEMP_01`) before performing a `deployment update`. Agents must not generate or reuse these codes autonomously.
3.  **Environment Mismatch**: If `oic token check` fails connectivity even after `token fetch`.
4.  **Ambiguity**: If `deployment update` fails because an integration code exists in the OIC instance but **not** within the specified `projectId`.

### D. Operational Constraints & Safety
1.  **Throttling**: OIC APIs have rate limits. Agents should avoid loops that call `list instances` more than once every 30 seconds.
2.  **Payload Sensitivity**: `analyze log` outputs may contain PII (Personally Identifiable Information) from the flow-logs. Agents must handle this output according to their privacy directives.
3.  **No Concurrency on Same Deployment**: Since OIC deployments are global, multiple agents updating the same code will corrupt the state. The **Human-Provided Unique Code** is the mandatory mitigation for this risk.
4.  **Forward-Slash Standardization**: Agents must standardize all CLI paths to use `/` forward slashes to prevent escaping issues in JSON strings or shell parsers.

---

## 📊 7. Protocol Versioning
| Version | Update | Agent Requirement |
| :--- | :--- | :--- |
| 1.0 | Initial Release | Manual download only. |
| 2.0 | Unified CLI | Support for `download project --archive`. |
| 3.0 | Deployment Logic| Support for selective sync and dynamic management. |
| 3.1 | HITL & Use-Cases| Mandatory Human-In-The-Loop for Auth failures; Comprehensive Gallery. |

---
*OIC Diagnostic Suite Agent Protocol v3.1 — HRD TechCarrot*
