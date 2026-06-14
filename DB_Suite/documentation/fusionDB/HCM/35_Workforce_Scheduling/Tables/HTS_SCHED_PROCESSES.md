# HTS_SCHED_PROCESSES

Schedules processes submitted as asynchronous batch requests

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprocesses-14276.html#htsschedprocesses-14276](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprocesses-14276.html#htsschedprocesses-14276)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_PROCESSES_PK | SCHED_PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_PROCESS_ID | NUMBER |  | 18 | Yes | Primary key identifiying the process record |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| PROCESS_TYPE | NUMBER |  | 2 | Yes | Type of process to be executed (for instance Publish, or Reset to Last Published) |
| SCHEDULER_ID | NUMBER |  | 18 |  | User ID of the scheduler submitting the job |
| SCHED_PROFILE_ID | NUMBER |  | 18 |  | Scheduler Pofile ID of the user submitting the job; null value corresponds to the default scheduler pofile (scheduling a manager's directs) |
| PEOPLE_LIST_TYPE | NUMBER |  | 2 |  | PEOPLE_LIST_TYPE |
| START_DATE | DATE |  |  |  | Start date for the range of the schedule data being processed |
| END_DATE | DATE |  |  |  | End date for the range of the schedule data being processed |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| REQUEST_TIME | TIMESTAMP |  |  |  | Indicates the request submission time  of the batch job submitted to execute the process |
| PROCESS_STATUS | NUMBER |  | 2 |  | Status of the job execution |
| EXEC_START_TIME | TIMESTAMP |  |  |  | Indicates the start time of execution of the main batch job that executes the process |
| EXEC_END_TIME | TIMESTAMP |  |  |  | Indicates the end time of execution of the main batch job that executed the process |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_PROCESSES_N1 | Non Unique | FUSION_TS_TX_IDX | SCHEDULER_ID, START_DATE, END_DATE, PEOPLE_LIST_TYPE, SCHED_PROFILE_ID |
| HTS_SCHED_PROCESSES_U1 | Unique | FUSION_TS_TX_IDX | SCHED_PROCESS_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
