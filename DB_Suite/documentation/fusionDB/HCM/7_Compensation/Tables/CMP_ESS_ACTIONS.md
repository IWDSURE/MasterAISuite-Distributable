# CMP_ESS_ACTIONS

This objet stores person or assignment information for ESS threading

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpessactions-22539.html#cmpessactions-22539](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpessactions-22539.html#cmpessactions-22539)

## Primary Key

| Name | Columns |
|------|----------|
| cmp_ess_actions_PK | ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_ID | NUMBER |  | 18 | Yes | ACTION_ID |
| TASK_ID | NUMBER |  | 18 | Yes | TASK_ID |
| RANGE_ID | NUMBER |  | 18 |  | RANGE_ID |
| KEY1 | NUMBER |  | 18 |  | PRIME_ID |
| KEY2 | NUMBER |  | 18 |  | SECOND_ID |
| STATUS_CODE | VARCHAR2 | 30 |  |  | STATUS_CODE |
| PROCESS_REQUEST_ID | NUMBER |  | 18 |  | PROCESS_REQUEST_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| REF_REQUEST_ID | NUMBER |  | 18 |  | REF_REQUEST_ID |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| REF_REQUEST_DATE | TIMESTAMP |  |  |  | REF_REQUEST_DATE |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_ESS_ACTION_N1 | Non Unique | Default | ACTION_ID, STATUS_CODE |
| CMP_ESS_ACTION_N2 | Non Unique | Default | TASK_ID, KEY1, KEY2 |
| CMP_ESS_ACTION_U1 | Unique | Default | ACTION_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
