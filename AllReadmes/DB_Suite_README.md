# Oracle Fusion Database (DB) Command Center — User Manual

**🤖 MISSION CRITICAL: THIS IS THE ONLY INTERFACE FOR AUTOMATED AND MANUAL DATABASE TASKS.**

You are using the **Fusion Database CLI (`db.exe`)**. This standalone command-line tool, coupled with the rich local **File-Based Source Library**, is your sole gateway to navigating, validating, and querying the Oracle Fusion Cloud database schema. You do not need to manage database connections, drivers, or local query servers. All discovery, schema inspection, and SQL executions are performed through this unified binary and local library.

---

## 🏗️ 1. Dual-Path Verification Architecture: Zero Guessing

Oracle Fusion Cloud features an incredibly complex database schema with over **5,600 Tables and Views**. In database operations, **guessing table names, column names, or join keys is an absolute failure state**. AI agents must never construct SQL queries based on assumptions. 

To maintain 100% execution accuracy, this suite provides a **Dual-Path Verification Architecture** to cross-reference and validate all schema assumptions before executing queries. You can utilize either path—or a hybrid of both—depending on your current task requirements.

```text
                               ┌──────────────────────────────┐
                               │     AI Agent Requirement     │
                               └──────────────────────────────┘
                                    │                    │
                   ┌────────────────┘                    └────────────────┐
                   ▼                                                      ▼
     【PATH A: SEMANTIC QUERY HELPER】                     【PATH B: FILE-BASED SOURCE LIBRARY】
     • Live CLI exploration                               • Static local verification
     • `db.exe discover "Salary History"`                 • Explore: `documentation/fusionDB/`
     • Match scores & database comments                   • Read keyword Indexes (`*_Index.md`)
                   │                                                      │
                   └────────────────┐                    ┌────────────────┘
                                    ▼                    ▼
                               ┌──────────────────────────────┐
                               │   Cross-Checked SQL Schema   │
                               └──────────────────────────────┘
```

---

## 🚀 2. Path A: The Semantic Query Helper (CLI)

The `db.exe` binary is your live exploration client. It communicates with a vector-enabled metadata engine to perform conceptual searches and return column contracts.

### **The Three Core Commands**
| Subcommand | Goal | Primary Output |
| :--- | :--- | :--- |
| **`discover`** | Semantic and keyword search of the schema metadata. | Candidate Tables & Views. |
| **`inspect`** | Retrieve column names, data types, keys, and comments. | Detailed column definitions. |
| **`run`** | Execute safe database queries. | JSON or CSV data output. |

#### **`discover` (Concept Explorer)**
Finds tables and views matching a business concept without needing exact filenames.
- **Usage**:
  `.\db.exe discover "where is bank account info stored?"`

#### **`inspect` (Contract Inspector)**
Returns the columns, types, primary keys, and developer comments for a specific object.
- **Usage**:
  `.\db.exe inspect "PER_ALL_PEOPLE_F"`

#### **`run` (Query Execution)**
Executes queries. (Read-only; any `INSERT`, `UPDATE`, `DELETE`, `DROP`, or `ALTER` is blocked).
- **Usage**:
  `.\db.exe run -q "SELECT person_number FROM PER_ALL_PEOPLE_F WHERE ROWNUM <= 5" -o csv -out "workspace\tmp\people.csv"`

---

## 📚 3. Path B: The File-Based Source Library

For complete offline capability, or to perform high-speed local keyword searches, you can leverage the **File-Based Source Library** located in `documentation/fusionDB/`. This folder contains a comprehensive mirror of the database metadata, with every table and view documented in **JSON** and **Markdown** format.

### **The Module Hierarchy**
Inside `documentation/fusionDB/HCM/`, the schema is organized into logical functional modules:
- `1_Global_Common_Features`
- `2_Global_Human_Resources`
- `3_Absence_Management`
- `4_Benefits`
- `5_Payroll` (and 30+ others)

### **The `_Index.md` Files: Your Keyword Entry Point**
Inside each module directory, you will find tabular index files (e.g., `3_Absence_Management_Tables_Index.md` and `3_Absence_Management_Views_Index.md`).
*   **The Metadata Table**: These files contain a complete list of all tables/views in that module along with their official description.
*   **Keyword Discovery**: This is an excellent starting point for search. If you are looking for absence configurations, search these markdown index files for terms like "absence plans" to quickly locate `ANC_ABSENCE_PLANS_F` and see its primary description.
*   **Detailed Specs**: The table names are hyperlinked to detailed markdown spec sheets inside the `Tables/` and `Views/` folders, containing raw JSON schemas, column explanations, and foreign keys.

### **The Fast Reference Lists**
For fast regex matching or module overview, use:
- `Tables.txt`: Plain text list of all tables in the module.
- `Views.txt`: Plain text list of all views in the module.

---

## 🕵️ 4. The Golden Path: Step-by-Step Data Retrieval Workflow

You must follow this exact sequence for every database query task. Bypassing validation will result in runtime errors.

### **Step 1: Concept Discovery (Dual-Path)**
Find candidate tables or views.
*   *Option A (CLI)*: Run `.\db.exe discover "absence accrual plans"`
*   *Option B (Local File)*: Open `documentation/fusionDB/HCM/3_Absence_Management/3_Absence_Management_Tables_Index.md` and search for "accrual".
*   *Identified*: `ANC_PER_ABS_PLAN_ENTRIES`.

### **Step 2: Technical Inspection & Cross-Checking**
Verify columns, datatypes, and primary keys.
*   *Option A (CLI)*: Run `.\db.exe inspect "ANC_PER_ABS_PLAN_ENTRIES"`
*   *Option B (Local File)*: Open `documentation/fusionDB/HCM/3_Absence_Management/Tables/ANC_PER_ABS_PLAN_ENTRIES.md`.
*   *Cross-Check*: Verify that `PERSON_ID`, `ABSENCE_PLAN_ID`, `ACCRUAL_VAL` are correct, exist, and review their column descriptions to ensure they match the business logic.

### **Step 3: Perform a 5-Row Probe**
Verify active data formats and make sure records exist.
```bash
.\db.exe run -q "SELECT person_id, accrual_val FROM ANC_PER_ABS_PLAN_ENTRIES WHERE ROWNUM <= 5"
```

### **Step 4: Execute & Persist**
Construct the final query, specify the output format, and save the dataset to your designated workspace folder.
```bash
.\db.exe run -q "SELECT person_id, accrual_val FROM ANC_PER_ABS_PLAN_ENTRIES WHERE accrual_val > 10" -o json -out "workspace\tmp\accrual_output.json"
```

---

## 🧠 5. Specialized Oracle Fusion Schema Intelligence

To construct accurate queries, you must understand these critical database design patterns:

### **The Effective Dating Trap**
Almost all transactional HCM tables in Oracle Fusion use **Effective Dating** (date-tracked records). If you query without date filters, you will receive multiple historical records for a single entity.
- **Standard Rule**: To get the **current active record**, always append this date-track filter:
```sql
WHERE TRUNC(SYSDATE) BETWEEN effective_start_date AND effective_end_date
```
- **Example**:
```sql
SELECT assignment_number, job_id 
FROM   PER_ALL_ASSIGNMENTS_M 
WHERE  person_id = 300000001234567 
AND    TRUNC(SYSDATE) BETWEEN effective_start_date AND effective_end_date
```

### **Virtual Language Views (`_VL`) vs. Translation Tables (`_TL`)**
- **The Trap**: Tables ending in `_TL` (Translation) contain a record for every supported language in the system. Joining these directly causes major row multiplication.
- **The Standard**: Always look for a view ending in `_VL` (Virtual Language). These views automatically join the base table and `_TL` table, and filter for the user's active session language.
- **Rule**: **Always prefer `_VL` views over `_TL` tables.**

---

## ⚠️ 6. Troubleshooting & Diagnostic Protocol

| Observation | Cause | Action |
| :--- | :--- | :--- |
| **Connection Error (401)** | Expired or incorrect credentials. | Check local `config.json` next to `db.exe`. |
| **Object Not Found (404)** | Case mismatch or invalid table name. | Confirm exact casing using `discover` or local index files before calling `inspect`. |
| **Duplicate Row Extraction** | Missing date-track or language filter. | Check if the object is effectively dated (use `inspect` or open its local `.md` file) and apply `effective_start_date` filters. |
| **Command Denied (DML/DDL)** | Attempted to modify the database. | The suite only allows `SELECT` operations. Adjust your query. |

---

## 🔒 7. Operational Guidelines & Safety

1.  **Configuration**: `db.exe` expects `config.json` in its same folder. Ensure these remain paired.
2.  **Row Limiters**: Never request unbounded `SELECT *` from massive tables. Always apply `ROWNUM` or specific `WHERE` filters to keep network payloads small.
3.  **DML Block**: Any attempts to run `INSERT`, `UPDATE`, `DELETE`, `DROP`, or `ALTER` will be blocked at the binary level.

---
*Oracle Fusion DB Unified CLI — Professional Handover Build*
*Master Executable: `db.exe`*
