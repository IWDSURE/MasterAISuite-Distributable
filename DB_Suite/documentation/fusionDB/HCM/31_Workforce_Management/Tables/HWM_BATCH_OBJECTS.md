# HWM_BATCH_OBJECTS

Instances of a process execution to load time records into the workforce management repository

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmbatchobjects-30069.html#hwmbatchobjects-30069](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmbatchobjects-30069.html#hwmbatchobjects-30069)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_BATCH_OBJECTS_PK | BATCH_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_OBJECT_ID | NUMBER |  | 18 | Yes | TRANSACTION_ID |
| SYNC_OBJ_SEQ | NUMBER |  | 9 |  | SYNC_OBJ_SEQ |
| SYNC_OBJ_ID | NUMBER |  | 18 |  | SYNC_OBJ_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| BATCH_PROC_INSTANCE_ID | NUMBER |  | 18 |  | BATCH_PROCESS_ID |
| OBJ_SEQ_NUM | NUMBER |  | 9 |  | NUM_OF_THREADS |
| REF_OBJECT_ID | NUMBER |  | 18 |  | REF_OBJECT_ID |
| START_REF_OBJECT_ID | NUMBER |  | 18 |  | START_REF_OBJECT_ID |
| END_REF_OBJECT_ID | NUMBER |  | 18 |  | END_REF_OBJECT_ID |
| OBJECT_TYPE | VARCHAR2 | 30 |  |  | OBJECT_TYPE |
| THREAD_PROC_INSTANCE_ID | NUMBER |  | 18 |  | THREAD_PROC_INSTANCE_ID |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| ADDL_INFORMATION | VARCHAR2 | 4000 |  |  | Extra Information to be used by the consumers of WFM Threaded Process. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_BATCH_OBJECTS_N1 | Non Unique | Default | BATCH_PROC_INSTANCE_ID, REF_OBJECT_ID |
| HWM_BATCH_OBJECTS_N2 | Non Unique | Default | THREAD_PROC_INSTANCE_ID |
| HWM_BATCH_OBJECTS_N3 | Non Unique | Default | BATCH_PROC_INSTANCE_ID, OBJ_SEQ_NUM |
| HWM_BATCH_OBJECTS_N4 | Non Unique | Default | BATCH_PROC_INSTANCE_ID, SYNC_OBJ_ID |
| HWM_BATCH_OBJECTS_PK | Unique | Default | BATCH_OBJECT_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
