# HWM_BATCH_RANGES

Instances of a process execution to load time records into the workforce management repository

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmbatchranges-24094.html#hwmbatchranges-24094](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmbatchranges-24094.html#hwmbatchranges-24094)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_BATCH_RANGES_PK | BATCH_RANGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_RANGE_ID | NUMBER |  | 18 | Yes | TRANSACTION_ID |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| BATCH_PROC_INSTANCE_ID | NUMBER |  | 18 |  | BATCH_PROCESS_ID |
| START_BATCH_SEQ_NUM | NUMBER |  | 9 |  | NUM_OF_THREADS |
| END_BATCH_SEQ_NUM | NUMBER |  | 9 |  | END_BATCH_SEQ_NUM |
| THREAD_INDEX_NUM | NUMBER |  | 9 |  | OBJECT_TYPE |
| THREAD_PROC_INSTANCE_ID | NUMBER |  | 18 |  | THREAD_PROC_INSTANCE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_BATCH_RANGES_FK1 | Non Unique | Default | BATCH_PROC_INSTANCE_ID |
| HWM_BATCH_RANGES_PK | Unique | Default | BATCH_RANGE_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
