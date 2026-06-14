# HTS_SCHEDULE_UNIT_PROCESSES

table to store schedule unit process information

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsscheduleunitprocesses-29790.html#htsscheduleunitprocesses-29790](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsscheduleunitprocesses-29790.html#htsscheduleunitprocesses-29790)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_UNIT_PROCESSES_PK | SCHEDULE_UNIT_PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_UNIT_PROCESS_ID | NUMBER |  | 18 | Yes | System generated unique identifier for a schedule |
| SCHEDULE_PROCESS_ID | NUMBER |  | 18 | Yes | Schedule Generation profile Id |
| SCHEDULE_UNIT_ID | NUMBER |  | 18 | Yes | Scheduling unit identifier. |
| SCHEDULE_GEN_PROFILE_ID | NUMBER |  | 18 |  | Schedule Generation Profile Id of the Schedule Unit |
| JOB_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Name of schedule process job |
| START_DATE | DATE |  |  |  | Start time of the schedule generation of this schedule unit |
| END_DATE | DATE |  |  |  | End time of the schedule generation of this schedule unit |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Status of the processing of this unit |
| JOB_PARAMETERS | VARCHAR2 | 4000 |  |  | Job Parameters applicable to the given schedule unit |
| JOB_PARAMETERS_LOB | CLOB |  |  |  | Job Parameters, saved as CLOB, applicable to the given schedule unit |
| JOB_REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| PROCESS_START_TIME | TIMESTAMP |  |  |  | Start time when the schedule generation starts for this schedule unit |
| PROCESS_END_TIME | TIMESTAMP |  |  |  | End time of the schedule generation of this schedule unit. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | identifier of enterprise |
| SCHED_ENGINE_OPTIONS | VARCHAR2 | 4000 |  |  | SHOWS ALGORITHTM ON WHICH SCHEDULE IS GENERATED |
| PROCESS_ERROR_CODE | VARCHAR2 | 30 |  |  | Error code returned from the scheduling engine |
| PROCESS_ERROR_CATEGORY | VARCHAR2 | 30 |  |  | Error category returned from the scheduling engine |
| PROCESS_ERROR_MSG | VARCHAR2 | 1000 |  |  | Error message returned from the scheduling engine |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHEDULE_UNIT_PROCESSES_N1 | Non Unique | Default | SCHEDULE_PROCESS_ID |
| HTS_SCHEDULE_UNIT_PROCESSES_N2 | Non Unique | Default | SCHEDULE_UNIT_ID, START_DATE, END_DATE, STATUS_CODE, SCHEDULE_GEN_PROFILE_ID |
| HTS_SCHEDULE_UNIT_PROCESSES_U1 | Unique | Default | SCHEDULE_UNIT_PROCESS_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
