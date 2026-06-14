# HTS_SCHEDULE_TASKS

This table is used to track the ESS jobs submitted from application and manage auto resubmit on failure if task allows.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsscheduletasks-9608.html#htsscheduletasks-9608](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsscheduletasks-9608.html#htsscheduletasks-9608)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHEDULE_TASKS_PK | TASK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a task. |
| TASK_CODE | VARCHAR2 | 150 |  | Yes | Indicates the task code relevant to the process. |
| JOB_NAME | VARCHAR2 | 200 |  | Yes | Indicates the ESS job name for which this task is created. |
| ALLOW_RESUBMIT | VARCHAR2 | 1 |  | Yes | Indicates whether this task allows resubmit on failure. |
| JOB_REQUEST_ID | NUMBER |  | 18 |  | Indicates the ESS job identifier. |
| STATUS | VARCHAR2 | 50 |  |  | Indicates the status of the task. |
| PROCESSED_DATE | TIMESTAMP |  |  |  | Indicates the timestamp when the processing is done. |
| PARENT_TASK_ID | NUMBER |  | 18 |  | Indicates the failed task identifier for which this task was submitted. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Indicates enterprise identifier. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHEDULE_TASKS_N1 | Non Unique | Default | CREATION_DATE |
| HTS_SCHEDULE_TASKS_PK | Unique | Default | TASK_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
