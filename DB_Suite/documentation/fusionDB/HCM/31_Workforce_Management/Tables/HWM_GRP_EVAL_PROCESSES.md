# HWM_GRP_EVAL_PROCESSES

Contains Group Evaluation Process Run Details

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpevalprocesses-14096.html#hwmgrpevalprocesses-14096](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpevalprocesses-14096.html#hwmgrpevalprocesses-14096)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_GRP_EVAL_PROCESSES_PK | GRP_EVAL_PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GRP_EVAL_PROCESS_ID | NUMBER |  | 18 | Yes | GRP_EVAL_PROCESS_ID |
| ERROR_TEXT | VARCHAR2 | 4000 |  |  | ERROR_TEXT |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| GRP_ID | NUMBER |  | 18 |  | GRP_ID |
| PROCESS_DT | TIMESTAMP |  |  |  | PROCESS_DATE |
| RUN_TYPE | VARCHAR2 | 30 |  |  | RUN_TYPE |
| NUM_DAYS_PREV | NUMBER |  | 9 |  | NUM_DAYS_PREV |
| NUM_DAYS_NEXT | NUMBER |  | 9 |  | NUM_DAYS_NEXT |
| EVAL_STATUS_CD | VARCHAR2 | 30 |  |  | EVAL_STATUS_CD |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_GRP_EVAL_PROCESSES_U1 | Unique | FUSION_TS_TX_DATA | GRP_EVAL_PROCESS_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
