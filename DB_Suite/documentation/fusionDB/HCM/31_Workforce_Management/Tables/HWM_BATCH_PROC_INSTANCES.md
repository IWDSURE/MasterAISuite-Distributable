# HWM_BATCH_PROC_INSTANCES

Instances of a process execution to load time records into the workforce management repository

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmbatchprocinstances-9172.html#hwmbatchprocinstances-9172](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmbatchprocinstances-9172.html#hwmbatchprocinstances-9172)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_BATCH_PROC_INSTANCES_PK | BATCH_PROC_INSTANCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_PROC_INSTANCE_ID | NUMBER |  | 18 | Yes | TRANSACTION_ID |
| PARENT_BATCH_PROC_INSTANCE_ID | NUMBER |  | 18 |  | Store the parent proc instance id |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| BATCH_PROCESS_ID | NUMBER |  | 18 |  | BATCH_PROCESS_ID |
| BATCH_PROCESS_CD | VARCHAR2 | 30 |  |  | BATCH_PROCESS_CD |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| PARENT_REQUEST_ID | NUMBER |  | 18 |  | PARENT_REQUEST_ID |
| NUM_OF_THREADS | NUMBER |  | 9 |  | NUM_OF_THREADS |
| NUM_OF_OBJ_TOTAL | NUMBER |  | 9 |  | NUM_OF_OBJ_TOTAL |
| NUM_OF_OBJ_SUCCESS | NUMBER |  | 9 |  | NUM_OF_OBJ_SUCCESS |
| NUM_OF_OBJ_ERRORED | NUMBER |  | 9 |  | NUM_OF_OBJ_ERRORED |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_BATCH_PROC_INST_FK1 | Non Unique | Default | BATCH_PROCESS_ID |
| HWM_BATCH_PROC_INST_N1 | Non Unique | Default | PARENT_BATCH_PROC_INSTANCE_ID |
| HWM_BATCH_PROC_INST_N2 | Non Unique | Default | REQUEST_ID |
| HWM_BATCH_PROC_INST_PK | Unique | Default | BATCH_PROC_INSTANCE_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
