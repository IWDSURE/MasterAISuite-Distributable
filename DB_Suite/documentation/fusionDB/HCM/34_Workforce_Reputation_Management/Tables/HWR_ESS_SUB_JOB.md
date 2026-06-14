# HWR_ESS_SUB_JOB

This is the table to save the info of sub job from each running ess job

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwresssubjob-3692.html#hwresssubjob-3692](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwresssubjob-3692.html#hwresssubjob-3692)

## Primary Key

| Name | Columns |
|------|----------|
| hwr_ess_sub_job_PK | PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_ID | NUMBER |  | 18 | Yes | This is the primary key for the process table. |
| SUB_JOB_NAME | VARCHAR2 | 255 |  |  | The name of the sub job |
| JOB_RUN_ID | NUMBER |  | 18 |  | The parent job ID of the sub job |
| PARAMETERS | VARCHAR2 | 4000 |  |  | The key-value of the job parameters |
| STATUS | VARCHAR2 | 255 |  |  | The current status of the sub job - in progress, completed, or failed |
| RESULT | VARCHAR2 | 4000 |  |  | This is the result of the job execution. |
| START_DATE | TIMESTAMP |  |  |  | This is the date that the sub job starts |
| END_DATE | TIMESTAMP |  |  |  | The end date for the sub job |
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
| hwr_ess_sub_job_U1 | Unique | Default | PROCESS_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
