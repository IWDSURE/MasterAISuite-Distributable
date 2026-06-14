# 🤖 VB Diagnostic Suite — Machine-Readable Protocol & Execution Manual (v2.1)

This document is the **Primary System Directive** for autonomous agents and LLMs utilizing the `vb.exe` suite. It defines the deterministic logic, data schemas, and execution cycles required for 100% reliable Visual Builder operations.

---

## 🏗 1. System Identity & State Model

The `vb.exe` utility is a standalone, directory-aware command-line interface. It functions as a bridge between high-level diagnostic intent and the Oracle Visual Builder Suite (VBS) REST API. 

### A. Core Architectural Mandate
The suite operates under a **Path-Invariant** model. It explicitly resolves configuration and token paths relative to its own binary location. This ensures that even when invoked from deep within a local workspace or nested script, it maintains its environment identity.

### B. Execution Context
The tool must be executed in an environment containing a valid `config.json`. 
- **Workspace Isolation**: All persistence operations (downloads) are routed into a standard `./workspace/` sub-directory or the user-provided `--out` path. 
- **Persistence Strategy (Incremental)**: The tool adopts a strict **Zero-Deletion Policy**. If a target extraction folder already exists and contains data, the tool will automatically increment the folder name (e.g., `App_1.0.5_1`, `App_1.0.5_2`) to prevent data loss.

### C. Local State Persistence File-Map
| File | Role | Authority Tier | Agent Action on Failure |
| :--- | :--- | :--- | :--- |
| `config.json` | Environment Identity | Static / Mandatory | **HALT**: Verify `vb_host` and `idcs_host`. |
| `token.txt` | **Manual User Token** | **TIER 1 (PRIMARY)** | **HITL**: Request fresh Bearer token from human if 401/403. |
| `token.json` | Automated Client Token| TIER 2 (FALLBACK) | Run `vb token fetch` if `token.txt` is absent. |

### D. Configuration Schema (`config.json`)
Agents must verify these specific keys are non-empty before initiating any REST-dependent cycle:
```json
{
  "vb_host": "https://oic-vbcs...oraclecloud.com",
  "idcs_host": "https://idcs-xxx.identity.oraclecloud.com",
  "client_id": "...",
  "client_secret": "...",
  "scope": "...",
  "auth_mode": "oauth"
}
```

---

## 🛠 2. Command Protocol Specification

Standard Syntax: `vb.exe <GROUP> <COMMAND> [OPTIONS]`

### 🟢 Group: `token` (Identity & Session)
Agents must establish session authority before attempting persistence tasks.

- **`vb token check`**: Verifies if the current session (txt or json) is alive.
  - *Internal Logic*: Checks JWT expiration (`exp` claim) and validates connectivity to the host.
  - *Agent Strategy*: Always run this first. If it returns `ACTIVE`, proceed. If `FAIL`, attempt repair.
- **`vb token fetch`**: Attempts a Client Credentials grant.
  - *Logical Constraint*: Use this for `list` commands. It **WILL FAIL** for `download app` due to OIC service provider restrictions.
- **`vb token save --value <TOKEN>`**: Manually persists a Bearer string to `token.txt`.

### 🔵 Group: `list` (Discovery & Inventory)
- **`vb list apps`**: Catalogs all Visual Applications in the instance.
  - *Data Schema*: Returns a table with `ID` (System Identifier), `Version`, and `Name` (Friendly Title).
  - *Operational Constraint*: Use the exact semantic version (e.g., `1.0.5`) in subsequent commands. Casing is critical.

### 🟡 Group: `download` (Persistence & Extraction)
- **`vb download app <ID> <VERSION> [--out <PATH>]`**:
  - **GOLD STANDARD**: Retrieves the application source ZIP and extracts it.
  - *Non-Destructive*: Automatically detects existing folders and uses suffixes (`_1`, `_2`, etc.) to preserve previous syncs.
  - *Deep Extraction*: The tool unzips everything including `webApps`, `mobileApps`, and `resources`.
  - *Authority Requirement*: Requires a **User-Delegated Bearer Token** (Service Administrator). **Client tokens will return 403.**

### 🔴 Group: `analyze` (Diagnostic Inference)
- **`vb analyze logs <FILE>`**: Performs pattern-matching on browser console logs.
  - *Pattern Matching*: Scans for HTTP 4xx/5xx errors, JSON parsing failures, and JS exceptions.
  - *Report Structure*:
    - Error Counts (Total failures)
    - Network Reference Trace (API endpoints called)
    - Critical Error Gallery (Snippet of first 10 major errors)

---

## 🔄 3. Optimized Execution Cycles (Workflows)

### Cycle A: High-Reliability Source Extraction
This workflow is used when an agent needs to analyze the source code of a specific application to debug logic or service connections.
1.  **Identity Verification**: Execute `vb token check`.
2.  **Session Repair**: If status is `FAIL`, execute `vb token fetch`.
3.  **Discovery**: Execute `vb list apps`. Identify the target `<ID>` and `<VERSION>`.
4.  **Download Command**: Execute `vb download app <ID> <VERSION>`.
5.  **Authority Check**: If `HTTP 403` occurs, the agent must emit: *"VB Application Export requires a User Token. Please provide a fresh Bearer token in token.txt."*
6.  **Validation**: Verify directory `./workspace/<ID>_<VERSION>/` (or with highest numeric suffix) contains the subdirectory `webApps`.

### Cycle B: Automated Console Error Resolution
This workflow is used when a human reports a UI bug and provides a console log file.
1.  **Ingestion**: Execute `vb analyze logs path/to/log.txt`.
2.  **Inference**: Identify the failing REST endpoint from the "Network Activity" section of the analysis output.
3.  **Sync**: Use Cycle A to download the app source.
4.  **Synthesis**: Locate the Service Connection in the source code matching the failing endpoint to identify misconfigured headers or base URLs. Search inside `./webApps/<AppID>/services/`.

---

## 🚑 4. Deterministic Repair Matrix (Error Handling)

Agents must not improvise on errors. Follow this matrix for deterministic resolution:

| Observed CLI Output | Possible Root Cause | Mandatory Agent Action |
| :--- | :--- | :--- |
| `HTTP 401 Unauthorized` | Token expired or invalid. | 1. `vb token fetch`. 2. If persists, **ASK HUMAN** for fresh Bearer token. |
| `HTTP 403 Forbidden` | Restricted Token detected. | **HALT**: Signal that a **User-Delegated** token is required. Ask human to provide one in `token.txt`. |
| `[DEBUG] Missing config keys`| Incomplete `config.json`.| **HALT**: Instruct human to fill `client_id` and `client_secret` in `config.json`. |
| `HTTP 404 Not Found` | ID/Version mismatch. | 1. `vb list apps`. 2. Verify exact casing. Ensure no spaces are present in the version string. |
| `Download error: [SSL...]` | Network/Proxy block. | Signal human to check VPN status or internal proxy settings. |

---

## 🌟 5. Exhaustive Use-Case Gallery

### Scenario 1: Targeted Version Discovery
**Goal**: Find if version `1.0.15` of the "HCM_App" exists.
```bash
vb.exe list apps
```
*Agent Processing*: Search the output table for `HCM_App` and check the version column. If `1.0.15` is not found, do not attempt to guess; report it as missing.

### Scenario 2: Emergency Source Backup (to custom path)
**Goal**: Export an app to a specific audit directory with absolute pathing.
```bash
vb.exe download app AJMAN_HRD_APP 1.0.22 --out D:/Work/Backups
```
*Note*: The tool will create `D:/Work/Backups/AJMAN_HRD_APP_1.0.22/`. If it exists, it creates `..._1.0.22_1/`.

### Scenario 3: Initial Connectivity Test
**Goal**: Confirm the system is ready for the day's operations.
```bash
vb.exe token check
```
*Decision Tree*:
- If `Active: True` (Source: Automated) -> Good for listing, but prepare for HITL if download is needed.
- If `Active: True` (Source: Manual) -> Fully ready for all operations including persistence.
- If `Active: False` -> Run `vb token fetch` immediately.

---

## 📝 6. Deep Technical Specifications for Agents

### A. Machine-to-Machine Interaction Protocol
1.  **No Guessing**: If a command fails with `HTTP 403`, do not attempt to retry with different versions or IDs. This is a permission boundary defined by VBS.
2.  **Token Dominance**: The existence of `token.txt` overrides everything. The tool will NOT automatically refresh tokens if `token.txt` is present to avoid overwriting a human's high-privilege session with a low-privilege automated one.
3.  **Parameter Safety**: When passing JSON strings to future CLI updates, always use single quotes `'` for the flag value and double quotes `"` for internal keys to ensure the shell doesn't misinterpret the braces.
4.  **Directory Preservation**: The tool **never deletes** existing data. Agents must be aware that multiple syncs of the same app version will result in multiple numbered folders. Prioritize the folder with the highest suffix for the most recent state.
5.  **Pathing Standardization**: **ALWAYS** use forward slashes `/` in paths (e.g., `D:/data/logs.txt`) even on Windows. The underlying libraries handle these correctly, and it prevents the "double-backslash" escaping hell in JSON and regex processing.
6.  **HITL Trigger Conditions**:
    - **Session Renewal**: Request `token.txt` from human.
    - **Bootstrap**: Request configuration details if `config.json` is malformed.
    - **Ambiguity**: Request clarification if `list apps` returns multiple IDs with similar names.

---

## 🔬 7. VB Application Internals (Cheat Sheet for Agents)
When you successfully download an app, its structure is typically:
- `./webApps/<AppName>/`: The main source directory.
- `.../pages/`: Contains JSON and HTML files for UI definitions.
- `.../services/`: Contains Service Connection metadata (API endpoints).
- `.../flows/`: Contains application logic and action chains.

*Agent Instruction*: After download, prioritize searching the `services/` folder to map UI errors to their respective backend REST calls.

---

## 📊 8. Protocol Versioning
| Version | Release Date | Update Highlights |
| :--- | :--- | :--- |
| 1.0 | 2026-05-15 | Initial Standalone Release. |
| 2.0 | 2026-06-05 | Path-Invariant logic; Formal HITL triggers; Console Log Analysis. |
| 2.1 | 2026-06-05 | Incremental Naming Strategy; Strict Zero-Deletion Policy. |

---
*Visual Builder Diagnostic Suite Agent Protocol v2.1 — HRD TechCarrot*
