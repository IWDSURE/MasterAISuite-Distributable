# HWR_ESS_JOB_RUN

This is the table to store the running ESS job info

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwressjobrun-16128.html#hwressjobrun-16128](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwressjobrun-16128.html#hwressjobrun-16128)

## Primary Key

| Name | Columns |
|------|----------|
| hwr_ess_job_run_PK | JOB_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_RUN_ID | NUMBER |  | 18 | Yes | This is the primary key for this table. The number should be generated from the sequence. |
| JOB_NAME | VARCHAR2 | 255 |  |  | This is the name of the running ess job. |
| JOB_TYPE | VARCHAR2 | 30 |  |  | This is the type of the scheduled job. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| PARAMETERS | VARCHAR2 | 4000 |  |  | This is the key-value parameters of the job. |
| STATUS | VARCHAR2 | 255 |  |  | This is running status of the job. |
| RESULT | VARCHAR2 | 4000 |  |  | This is the result of the job execution. |
| START_DATE | TIMESTAMP |  |  |  | This is the date that this job starts to run. |
| END_DATE | TIMESTAMP |  |  |  | This is the end date of the running job execution |
| JOB_ATTR_1 | VARCHAR2 | 100 |  |  | JOB_ATTR_1. This is the extra attribute in case if needed. |
| JOB_ATTR_2 | VARCHAR2 | 100 |  |  | JOB_ATTR_2. This is the extra attribute in case if needed. |
| JOB_ATTR_3 | VARCHAR2 | 100 |  |  | JOB_ATTR_3. This is the extra attribute in case if needed. |
| JOB_ATTR_4 | VARCHAR2 | 100 |  |  | JOB_ATTR_4. This is the extra attribute in case if needed. |
| JOB_ATTR_5 | VARCHAR2 | 100 |  |  | JOB_ATTR_5. This is the extra attribute in case if needed. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hwr_ess_job_run_U1 | Unique | Default | JOB_RUN_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
