# PAY_ACTION_LOG_LINES

This table stores the log file line text for ADF processing.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactionloglines-7434.html#payactionloglines-7434](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactionloglines-7434.html#payactionloglines-7434)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ACTION_LOG_LINES_PK | ACTION_LOG_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_LOG_LINE_ID | NUMBER |  | 18 | Yes | Primary Key |
| ACTION_LOG_ID | NUMBER |  | 18 | Yes | Foreign Key to Action Logs |
| LINE_NUMBER | NUMBER |  | 18 | Yes | LINE_NUMBER |
| LINE_TEXT | VARCHAR2 | 3000 |  |  | LINE_TEXT |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ACTION_LOG_LINES_N1 | Non Unique | Default | ACTION_LOG_ID, LINE_NUMBER |
| PAY_ACTION_LOG_LINES_PK | Unique | Default | ACTION_LOG_LINE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
