# Oracle BI Publisher (BIP) Command Center — User Manual

**🤖 MISSION CRITICAL: THIS IS THE ONLY INTERFACE FOR AUTOMATED AND MANUAL TASKS.**

You are using the **BIP Unified CLI (`bip.exe`)**. This standalone command-line tool is your sole gateway to interacting with Oracle BI Publisher. You do not need to manage underlying code, network libraries, or manual environment configurations. All discovery, logic extraction, and execution tasks are performed through this unified binary.

---

## 🏗️ 1. Capabilities & Subcommands

The `bip.exe` command is a multi-mode tool designed to let you discover catalog structures, extract business queries, and execute reports. 

### **Global Entry Point**
```bash
# In Windows PowerShell or CMD
.\bip.exe <subcommand> [options]
```

### **The Five Subcommands**
| Subcommand | Goal | Primary Output |
| :--- | :--- | :--- |
| **`test`** | Verify connection and credentials are valid. | Connection status confirmation. |
| **`ls`** | Discover reports, data models, and folders. | JSON file or Text table listing. |
| **`inspect`** | Identify required parameters and allowed formats. | JSON metadata file. |
| **`forensics`** | Extract the internal database query (SQL) and joins. | JSON dataset + Markdown analysis report. |
| **`run`** | Execute report and save the raw results. | CSV, XML, or PDF file output. |

---

## 🕵️ 2. The Golden Path: Step-by-Step Diagnostic Workflow

You must follow this standard operating sequence for every report task. Operating blindly without gathering parameters or schema logic first will result in execution failures.

```text
 ┌───────────────┐      ┌────────────────┐      ┌────────────────┐      ┌───────────────┐
 │   DISCOVER    │ ───> │    INSPECT     │ ───> │   FORENSICS    │ ───> │    EXECUTE    │
 │ (ls command)  │      │(inspect cmd)   │      │(forensics cmd) │      │ (run command) │
 └───────────────┘      └────────────────┘      └────────────────┘      └───────────────┘
  Find exact paths       Get parameters &        Extract the SQL        Verify with live
  & filenames            default formats         and query joins         data output
```

### **Step 1: Discover Paths**
Find the exact location and name of the report in the catalog. Catalog names are case-sensitive.
```bash
.\bip.exe ls -d "/Custom/Integrations/hcm/Transfer Extension" -o "workspace\tmp\discovery.json"
```

### **Step 2: Inspect Requirements**
Retrieve the technical contract of the report (what parameters does it need to run, and what is its default format?).
```bash
.\bip.exe inspect -r "/Custom/Integrations/hcm/Transfer Extension/DEP_PROGRAM_REPORT.xdo" -o "workspace\tmp\meta.json"
```

### **Step 3: Extract Internal Logic**
Download and extract the SQL query driving the report to understand how it pulls data:
```bash
.\bip.exe forensics "/Custom/Integrations/hcm/Transfer Extension/DEP_PROGRAM_REPORT.xdo" -o "workspace\tmp\analysis\"
```
Review the generated Markdown file in `analysis\` to map the underlying tables and filters.

### **Step 4: Execute & Verify**
Run the report with verified parameters to produce a live local data snapshot:
```bash
.\bip.exe run -r "/Custom/Integrations/hcm/Transfer Extension/DEP_PROGRAM_REPORT.xdo" -p "{\"P_ORGANIZATION_ID\":\"300000009946223\", \"P_LANG\":\"US\"}" -f csv -o "workspace\tmp\live_data.csv" --approved
```

---

## 🛠️ 3. Command Reference (Full Details)

### **`test` (Connection Check)**
Verifies if `bip.exe` can authenticate and browse the environment.
- **Flags**:
    - `--folder <path>` (Optional): Probe a specific folder to verify access. Defaults to `/Custom`.
- **Usage**:
  `.\bip.exe test`

### **`ls` (Catalog Listing)**
Browses the directory structure.
- **Flags**:
    - `-d <path>` (Required): The catalog folder path (starts with `/Custom`).
    - `-o <file>` (Optional): Save results. If the path ends in `.json`, it saves structured data.
- **Usage**:
  `.\bip.exe ls -d "/Custom/AG HCM" -o "workspace\tmp\hcm_listing.json"`

### **`inspect` (Contract Gathering)**
Fetches templates, output formats, and parameter details.
- **Flags**:
    - `-r <path>` (Required): Path to the `.xdo` report.
    - `-o <file>` (Optional): Path to save metadata as a JSON file.
- **Usage**:
  `.\bip.exe inspect -r "/Custom/Report.xdo" -o "workspace\tmp\meta.json"`

### **`forensics` (Logic Extraction)**
Extracts raw SQL queries, value sets (LOVs), triggers, and parameters from the report's Data Model.
- **Flags**:
    - `report_path` (Required): Path to the `.xdo` report.
    - `-o <dir>` (Optional): Directory to save analysis reports.
- **Usage**:
  `.\bip.exe forensics "/Custom/Report.xdo" -o "workspace\tmp\my_analysis\"`

### **`run` (Report Execution)**
Generates and downloads live data.
- **Flags**:
    - `-r <path>` (Required): Path to the `.xdo` report.
    - `-p <json>` (Optional): JSON parameter string (e.g., `'{"P_LANG":"US"}'`).
    - `-f <format>` (Optional): Output format (e.g., `csv`, `xml`, `pdf`).
    - `-o <file>` (Required): Output file path to save data.
    - `--approved` (Required): Explicit flag confirming you have user consent to execute.
- **Usage**:
  `.\bip.exe run -r "/Custom/Report.xdo" -p "{\"P_ID\":\"123\"}" -f csv -o "output.csv" --approved`

---

## ⚠️ 4. Troubleshooting & Diagnostic Protocol

| Observation | Cause | Action |
| :--- | :--- | :--- |
| **Connection Failed (401)** | Credentials are expired or invalid. | Update the local `config.json` next to `bip.exe`. |
| **No folder contents found** | Path is missing or requires prefix. | Try adding `/shared` to the front of the path (e.g. `/shared/Custom/...`). |
| **Invalid format requested** | The report does not support that format. | Run `inspect` to check the allowed `default_format`. |
| **JSON Parameter Parsing Error** | Bad JSON escaping in parameters. | Ensure keys and values are enclosed in escaped quotes (e.g., `\"Key\":\"Value\"`). |

---

## 🔒 5. Operational Security & Guidelines

1.  **Configuration File**: `bip.exe` always reads `config.json` in its local directory. Keep these files together.
2.  **No Silent Runs**: Never execute the `run` command without presenting the parameters to the human user first.
3.  **Read-Only Operations**: This tool is built strictly for analysis and data retrieval. Do not attempt to use it to modify, upload, or delete catalog items.

---
*Oracle BIP Unified CLI — Professional Handover Build*
*Master Executable: `bip.exe`*
