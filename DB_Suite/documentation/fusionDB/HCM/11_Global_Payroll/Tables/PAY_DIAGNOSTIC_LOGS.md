# PAY_DIAGNOSTIC_LOGS

This table will be used to capture details of diagnostics

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydiagnosticlogs-12923.html#paydiagnosticlogs-12923](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydiagnosticlogs-12923.html#paydiagnosticlogs-12923)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DIAGNOSTIC_LOGS_PK | LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOG_ID | NUMBER |  | 18 | Yes | This column is the primary key of the table pay_diagnostic_logs. |
| SOURCE_ID | NUMBER |  | 18 | Yes | Identifier for source of the logs. |
| LOG_LEVEL | VARCHAR2 | 1 |  | Yes | This column represents the level of the logs. |
| LOG_TEXT | VARCHAR2 | 4000 |  |  | This column represents the message of the logs. |
| LOG_DETAILS | CLOB |  |  |  | This column represents the details of the logs. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_DIAGNOSTIC_LOGS_PK | Unique | Default | LOG_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
