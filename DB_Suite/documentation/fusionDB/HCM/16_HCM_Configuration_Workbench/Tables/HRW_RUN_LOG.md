# HRW_RUN_LOG

Table to store object details loaded via esc configuration

## Details

**Schema:** FUSION

**Object owner:** HRW

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwrunlog-30380.html#hrwrunlog-30380](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwrunlog-30380.html#hrwrunlog-30380)

## Primary Key

| Name | Columns |
|------|----------|
| HRW_RUN_LOG_PK | RUN_LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_LOG_ID | NUMBER |  | 18 | Yes | RUN_LOG_ID |
| RUN_ID | NUMBER |  | 18 |  | RUN_ID |
| STEP_CODE | VARCHAR2 | 100 |  |  | STEP_CODE |
| OBJECT_ID | NUMBER |  | 18 |  | OBJECT_ID |
| OBJECT_CODE | VARCHAR2 | 100 |  |  | OBJECT_CODE |
| OBJECT_NAME | VARCHAR2 | 250 |  |  | OBJECT_NAME |
| OBJECT_DESCR | VARCHAR2 | 1000 |  |  | OBJECT_DESCR |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| ERROR_TEXT | VARCHAR2 | 400 |  |  | ERROR_TEXT |
| ERROR_STACK | VARCHAR2 | 4000 |  |  | ERROR_STACK |
| COMPLETE_ERROR_STACK | CLOB |  |  |  | COMPLETE_ERROR_STACK |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRW_RUN_LOG_U1 | Unique | Default | RUN_LOG_ID |

---

[← Back to Index](../16_HCM_Configuration_Workbench_Tables_Index.md)
