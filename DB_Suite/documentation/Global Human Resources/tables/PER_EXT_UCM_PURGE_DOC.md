# PER_EXT_UCM_PURGE_DOC

Extract Table for capturing UCM document failed cases

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextucmpurgedoc-17634.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextucmpurgedoc-17634.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_UCM_PURGE_DOC_PK | ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTRY_ID | NUMBER |  | 18 | Yes | ENTRY_ID |
| UCM_PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | UCM_PAYROLL_ACTION_ID |
| PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_ACTION_ID |
| EXT_DELIVERY_OPTION_ID | NUMBER |  | 18 |  | EXT_DELIVERY_OPTION_ID |
| INTEGRATION_NAME | VARCHAR2 | 256 |  |  | INTEGRATION_NAME |
| UCM_CONTENT_ID | VARCHAR2 | 30 |  |  | UCM_CONTENT_ID |
| RETRIES | NUMBER |  | 18 |  | RETRIES |
| ERROR | VARCHAR2 | 4000 |  |  | ERROR |
| DELIVERY_TYPE | VARCHAR2 | 20 |  |  | DELIVERY_TYPE |
| UCM_RETENTION_DAYS | NUMBER |  |  |  | UCM_RETENTION_DAYS |
| ERROR_TYPE | VARCHAR2 | 60 |  |  | ERROR_TYPE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EXT_UCM_PURGE_DOC_N1 | Non Unique | Default | PAYROLL_ACTION_ID, UCM_PAYROLL_ACTION_ID |
| PER_EXT_UCM_PURGE_DOC_N2 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_EXT_UCM_PURGE_DOC_PK | Unique | Default | ENTRY_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
