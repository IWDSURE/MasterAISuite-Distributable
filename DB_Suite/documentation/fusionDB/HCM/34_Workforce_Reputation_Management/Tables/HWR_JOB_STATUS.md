# HWR_JOB_STATUS

This job table stores jobs that run for connectors.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrjobstatus-16433.html#hwrjobstatus-16433](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrjobstatus-16433.html#hwrjobstatus-16433)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_JOB_STATUS_PK | JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_ID | NUMBER |  | 18 | Yes | This is the primary key for the job table. |
| SOURCE_ID | NUMBER |  | 18 |  | This is the source ID related with the job. |
| IS_ACTIVE | VARCHAR2 | 4 |  |  | A flag indicating if the Job is active. Use Y for active or N for inactive |
| JOB_TYPE | VARCHAR2 | 30 |  |  | This is the type of the  job. |
| JOB_NAME | VARCHAR2 | 255 |  |  | This is the name of the job. |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | This is the full description of the job. |
| JOB_UUID | VARCHAR2 | 255 |  |  | This is the UUID of the job. |
| JOB_STATUS | VARCHAR2 | 30 |  |  | This is the current status of the job. |
| LAST_RUN | NUMBER |  |  |  | This is the last run timestamp of the job. |
| SCHEDULE | VARCHAR2 | 2000 |  |  | This is the schedule information of the job. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_JOB_STATUS_U1 | Unique | FUSION_TS_TX_DATA | JOB_ID |
| HWR_JOB_STATUS_U2 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, JOB_TYPE, JOB_NAME |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
