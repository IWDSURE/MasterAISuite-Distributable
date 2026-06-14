# PAY_JOB_SUBMISSIONS

This table stores the details of the last job submission from the Event System for certain Actions.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payjobsubmissions-20061.html#payjobsubmissions-20061](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payjobsubmissions-20061.html#payjobsubmissions-20061)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_SUBMISSION_ID | NUMBER |  | 18 | Yes | Primary Key |
| JOB_NAME | VARCHAR2 | 240 |  | Yes | Name of the Job |
| SUBMISSION_TIME | DATE |  |  | Yes | Date and time of the submission. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise Identifier |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_JOB_SUBMISSIONS_N1 | Non Unique | Default | JOB_NAME |
| PAY_JOB_SUBMISSIONS_PK | Unique | Default | JOB_SUBMISSION_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
