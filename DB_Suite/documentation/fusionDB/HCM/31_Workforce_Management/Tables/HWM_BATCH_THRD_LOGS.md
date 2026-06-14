# HWM_BATCH_THRD_LOGS

State of an object to be stored during process execution to load time records into the workforce management repository

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmbatchthrdlogs-11008.html#hwmbatchthrdlogs-11008](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmbatchthrdlogs-11008.html#hwmbatchthrdlogs-11008)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_BATCH_THRD_LOGS_PK | HWM_BATCH_THRD_LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HWM_BATCH_THRD_LOG_ID | NUMBER |  | 18 | Yes | HWM_BATCH_THRD_LOG_ID |
| BATCH_PROC_INSTANCE_ID | NUMBER |  | 18 | Yes | BATCH_PROC_INSTANCE_ID |
| THREAD_PROC_INSTANCE_ID | NUMBER |  | 18 | Yes | THREAD_PROC_INSTANCE_ID |
| THREAD_INDEX_NUM | NUMBER |  | 9 |  | THREAD_INDEX_NUM |
| THREAD_PARAMS | BLOB |  |  |  | THREAD_PARAMS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_BATCH_THRD_LOGS_N1 | Non Unique | Default | BATCH_PROC_INSTANCE_ID |
| HWM_BATCH_THRD_LOGS_N2 | Non Unique | Default | THREAD_PROC_INSTANCE_ID |
| HWM_BATCH_THRD_LOGS_U1 | Unique | Default | HWM_BATCH_THRD_LOG_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
