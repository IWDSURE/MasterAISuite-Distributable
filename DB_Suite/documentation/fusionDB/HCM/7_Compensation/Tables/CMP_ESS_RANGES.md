# CMP_ESS_RANGES

This object for defining the ESS process range of actions

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpessranges-3000.html#cmpessranges-3000](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpessranges-3000.html#cmpessranges-3000)

## Primary Key

| Name | Columns |
|------|----------|
| CM_ESS_RANGE_PK | RANGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RANGE_ID | NUMBER |  | 18 | Yes | RANGE_ID |
| TASK_ID | NUMBER |  | 18 | Yes | TASK_ID |
| STARTING_ID | NUMBER |  | 18 |  | STARTING_ID |
| ENDING_ID | NUMBER |  | 18 |  | ENDING_ID |
| STATUS_CODE | VARCHAR2 | 30 |  |  | STATUS_CODE |
| PROCESS_REQUEST_ID | NUMBER |  | 18 |  | PROCESS_REQUEST_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_ESS_RANGES_N1 | Non Unique | Default | TASK_ID, STATUS_CODE |
| cmp_ess_ranges_U1 | Unique | Default | RANGE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
