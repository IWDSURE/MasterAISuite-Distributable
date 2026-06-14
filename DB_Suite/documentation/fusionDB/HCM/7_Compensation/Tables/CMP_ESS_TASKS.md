# CMP_ESS_TASKS

this object for defining ess process

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpesstasks-25322.html#cmpesstasks-25322](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpesstasks-25322.html#cmpesstasks-25322)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_ESS_TASK_PK | TASK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_ID | NUMBER |  | 18 | Yes | TASK_ID |
| EFFECTIVE_DATE | DATE |  |  |  | EFFECTIVE_DATE |
| MODE_CODE | VARCHAR2 | 30 |  |  | MODE_CODE |
| KEY1 | NUMBER |  | 18 |  | KEY1 |
| KEY2 | NUMBER |  | 18 |  | KEY2 |
| KEY3 | NUMBER |  | 18 |  | KEY3 |
| AUDIT_LOG_FLAG | VARCHAR2 | 1 |  |  | AUDIT_LOG_FLAG |
| VALIDATE_FLAG | VARCHAR2 | 1 |  |  | VALIDATE_FLAG |
| STATUS_CODE | VARCHAR2 | 255 |  |  | STATUS_CODE |
| RESTARTED_FLAG | VARCHAR2 | 1 |  |  | RESTARTED_FLAG |
| RESTARTED_STATUS | VARCHAR2 | 4000 |  |  | RESTARTED_STATUS |
| INFORMATION1 | VARCHAR2 | 255 |  |  | INFORMATION1 |
| INFORMATION2 | VARCHAR2 | 255 |  |  | INFORMATION2 |
| INFORMATION3 | VARCHAR2 | 255 |  |  | INFORMATION3 |
| INFORMATION4 | VARCHAR2 | 255 |  |  | INFORMATION4 |
| INFORMATION5 | VARCHAR2 | 255 |  |  | INFORMATION5 |
| INFORMATION6 | VARCHAR2 | 255 |  |  | INFORMATION6 |
| INFORMATION7 | VARCHAR2 | 255 |  |  | INFORMATION7 |
| INFORMATION8 | VARCHAR2 | 255 |  |  | INFORMATION8 |
| INFORMATION9 | VARCHAR2 | 255 |  |  | INFORMATION9 |
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
| CMP_ESS_TASKS_N1 | Non Unique | Default | MODE_CODE, EFFECTIVE_DATE |
| CMP_ESS_TASKS_N2 | Non Unique | Default | KEY1, KEY2, KEY3 |
| CMP_ESS_TASKS_N3 | Non Unique | Default | REQUEST_ID |
| CMP_ESS_TASKS_N4 | Non Unique | Default | MODE_CODE, REQUEST_ID |
| cmp_ess_tasks_U1 | Unique | Default | TASK_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
