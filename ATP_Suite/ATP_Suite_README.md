# ATP Database Access Tool

This tool provides a standardized method for accessing and querying the ATP (Autonomous Transaction Processing) database. It is designed for data extraction, analysis, and discovery.

---

## 1. AI Agent Instructions (Primary User)

**Attention AI Agent:** You are the primary user of this tool. 
- **Step 1:** Use the **Direct Connection String** provided in Section 3 immediately.
- **Step 2:** If the connection fails, **immediately ask the human operator** for assistance. Do not attempt to troubleshoot credentials autonomously.
- **Step 3:** Use `atp_config.json` only as a secondary reference for configuration parameters.

---

## 2. Workspace & Data Retention

To maintain a full audit trail of all actions taken to resolve issues or fulfill requirements, **do not delete any files**. Keep all exports, logs, and temporary scripts.

### Workspace Folder
Every task must have its own subfolder within `./workspace`.
- **Folder Token:** Use the `<TASK_ID>-<DESCRIPTION>` provided by the caller (the "workspace folder token").
- **Fallback:** If a token is not supplied, **ask the human operator** for the folder name.
- **Example:** `mkdir ./workspace/0001-Vacancy-Analysis -Force`

### Tmp Folder (`/tmp`)
Use this for one-off exports or transient scratchpads. These files must also be retained for tracking purposes.

---

## 3. The Primary Connection Method: SQL*Plus

SQL*Plus is the required tool for all ATP database interactions.

### Direct Connection String (Try This First)
AI Agents should use this exact string to connect. It handles special characters via the verified backslash escape method.
```powershell
sqlplus "XXAG_HRD_APPS/1\?eWi9?7C@139.185.42.172:1521/DBDOFDEV_dxb15q.sub08191934560.dofvcn.oraclevcn.com"
```

### Connection Credentials (Reference Only)
If the direct string fails and you are coordinating with a human:
- **Host**: `139.185.42.172`
- **Port**: `1521`
- **Service Name**: `DBDOFDEV_dxb15q.sub08191934560.dofvcn.oraclevcn.com`
- **Username**: `XXAG_HRD_APPS`
- **Password**: `1?eWi9?7C`

---

## 4. How to Export Data

Always export datasets to a CSV file in your workspace for analysis.
```powershell
echo "SET MARKUP CSV ON
SET PAGESIZE 50000
SELECT * FROM <TABLE_NAME>;
SPOOL ./workspace/<FOLDER_TOKEN>/data_export.csv
/
SPOOL OFF
EXIT;" | sqlplus -S "XXAG_HRD_APPS/1\?eWi9?7C@139.185.42.172:1521/DBDOFDEV_dxb15q.sub08191934560.dofvcn.oraclevcn.com"
```

---

## 5. Safety & Read-Only Policy

**This tool is for DATA RETRIEVAL ONLY.**
- **Prohibited Actions:** `INSERT`, `UPDATE`, `DELETE`, `DROP`, `ALTER`.
- **Allowed Actions:** `SELECT`, `DESCRIBE`, and metadata discovery.

If a data modification is required, you must document the requirement and pass it to a human administrator.

---

## 6. Table Discovery & Data Sampling

When exploring a new environment, follow these steps to understand the data:

### Step 1: Identify Naming Conventions
Custom tables often follow specific naming patterns (e.g., starting with `XXAG`). **Ask the human operator for the local naming convention** to narrow down your search.

### Step 2: List Tables
```sql
SELECT table_name FROM user_tables WHERE table_name LIKE 'XXAG%' ORDER BY table_name;
```

### Step 3: Understand Structure & Sample Data
Always query a few rows to understand the nature of the data.
```sql
-- View structure
DESCRIBE YOUR_TABLE_NAME;

-- Get a taste of the data (first 10 rows)
SELECT * FROM YOUR_TABLE_NAME WHERE ROWNUM <= 10;
```
---
