# 🤖 Fusion Web Services (FWS) Diagnostic Suite — Agent Protocol

This suite is a standalone toolset for interacting with Oracle Fusion REST APIs. It is designed for **Knowledge-Driven Execution**, where the agent uses local metadata to construct precise API calls.

---

## 🏗 1. The Core Ecosystem

The suite consists of three critical components. You MUST use them in sequence:

1.  **`catalog/` (The Map)**: A directory of Markdown files. Search these files first to find the "Resource Path" (e.g., `/workers` or `/absences`).
2.  **`swagger/` (The Technical Manual)**: A directory of JSON schemas. Once you have a path, find the matching JSON file here to see filterable fields (`q` parameters) and child resources (`expand`).
3.  **`fws.exe` (The Engine)**: The only interface for execution. It handles all authentication and headers automatically.

---

## 🛠 2. Command Reference: `fws.exe`

Standard Execution: `fws.exe <COMMAND> [OPTIONS]`

### COMMAND: `call`
Executes a REST request to the Fusion environment.
*   `-p, --path`: (Required) The service path (e.g., `/hcmRestApi/resources/latest/workers`).
*   `-m, --method`: HTTP Method. Defaults to `GET`.
*   `-q, --query`: JSON string for URL parameters. 
    *   *Common keys*: `q` (for filtering), `expand` (for nested data), `limit`.
*   `-b, --body`: JSON string for POST/PATCH payloads.
*   `-o, --output`: Save the JSON response to a file path.

---

## 🔄 3. The Golden Workflow (Step-by-Step)

### Step 1: Discover the Resource
Search the `.md` files in `catalog/` for business terms (e.g., "Salary", "Bonus", "Assignment").
*   *Action*: Identify the REST path and the associated documentation file.

### Step 2: Inspect the Schema
Open the corresponding `.json` file in `swagger/`.
*   *Action*: Find the `"parameters"` section. Look for the attribute named `"q"`. It will list which fields you can filter by (e.g., `PersonNumber`, `AssignmentId`).
*   *Action*: Find the `"links"` section to see which child records can be retrieved using the `expand` parameter.

### Step 3: Execute the Call
Construct your `fws.exe` command using the intelligence gathered and use `-o` to persist the results for analysis.
*   **CRITICAL**: String values inside the `q` parameter must be wrapped in **single quotes**.
*   **PRO TIP**: You can use single quotes for the JSON object in the CLI for easier typing: `{'q': 'Attribute=''Value'''}`.

---

## 💡 4. Critical Technical Rules (The "Quote Trap")

Oracle Fusion REST APIs have strict quoting requirements. You must follow these exactly:

1.  **Filter Quoting**: String values *inside* a filter query must use **single quotes**.
    *   *Correct*: `q=PersonNumber='HR1001'`
    *   *Incorrect*: `q=PersonNumber="HR1001"`
2.  **CLI Quoting**: The CLI is flexible. You can use standard JSON or a simplified format using single quotes.
    *   *Template*: `fws.exe call -p "/path" -q "{'q': 'Attribute=''Value'''}"`

---

## 📖 5. Example Use Cases

### Use Case A: Retrieve Recent Absences for a Person
1.  **Knowledge**: `catalog/hcm_catalog.md` shows path `/absences`.
2.  **Schema**: `swagger/hcm/services/Absences.json` shows `personId` is a filterable field.
3.  **Command**:
    ```bash
    fws.exe call -p "/hcmRestApi/resources/latest/absences" -q "{'q': 'personId=1000000123', 'limit': '5'}" -o "absences.json"
    ```

### Use Case B: Get Worker Details with Assignment Expansion
1.  **Knowledge**: `catalog/hcm_catalog.md` shows path `/workers`.
2.  **Schema**: `swagger/hcm/services/Workers.json` shows a link for `workRelationships`.
3.  **Command**:
    ```bash
    fws.exe call -p "/hcmRestApi/resources/latest/workers" -q "{'q': 'PersonNumber=''HR100019''', 'expand': 'workRelationships.assignments'}" -o "worker_details.json"
    ```

### Use Case C: Fetch Element Entries for an Assignment
1.  **Knowledge**: `catalog/hcm_catalog.md` shows path `/elementEntries`.
2.  **Command**:
    ```bash
    fws.exe call -p "/hcmRestApi/resources/latest/elementEntries" -q "{'q': 'AssignmentNumber=''EHR100019''', 'expand': 'elementEntryValues'}" -o "element_entries.json"
    ```

---

## 🚑 6. Troubleshooting for Agents

*   **Error 401**: Check `config.json` for host/credentials.
*   **Error 400 (Bad Request)**: Usually a typo in a field name. Re-read the `swagger/` JSON carefully; fields are case-sensitive.
*   **Empty Items List**: The filter worked, but no records matched. Double-check your `PersonNumber` or `AssignmentNumber`.

---
*Maintained by HRD TechCarrot — AI Suite Standards v1.0*
