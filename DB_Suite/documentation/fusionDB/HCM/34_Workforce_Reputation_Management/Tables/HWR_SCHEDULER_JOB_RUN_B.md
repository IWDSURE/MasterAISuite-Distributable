# HWR_SCHEDULER_JOB_RUN_B

The job run table stores information about each execution of a scheduled job.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrschedulerjobrunb-26082.html#hwrschedulerjobrunb-26082](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrschedulerjobrunb-26082.html#hwrschedulerjobrunb-26082)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SCHEDULER_JOB_RUN_B_PK | JOB_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_RUN_ID | NUMBER |  | 18 | Yes | This is the primary key for this table. The number should be generated from the sequence. |
| NAME | VARCHAR2 | 255 |  | Yes | This is the name of the scheduled job. |
| JOB_TYPE | VARCHAR2 | 30 |  |  | This is the type of the scheduled job. |
| START_DATE | TIMESTAMP |  |  |  | This is the date that this job is scheduled to start. |
| END_DATE | TIMESTAMP |  |  |  | The end date for this job, if it is recurring. |
| STATUS_CODE | VARCHAR2 | 30 |  | Yes | This is a code indicating the status of the scheduled job. |
| RESULT | CLOB |  |  |  | This is the result of the job execution. |
| PARAMETERS | VARCHAR2 | 4000 |  |  | This is the set of serialized parameters of the job. |
| IS_CANCELABLE | VARCHAR2 | 4 |  |  | This value indicates whether the job is cancelable. |
| APPLICATION_CODE | VARCHAR2 | 10 |  | Yes | This is the application code of the job. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SCHEDULER_JOB_RUN_B_U1 | Unique | Default | JOB_RUN_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
