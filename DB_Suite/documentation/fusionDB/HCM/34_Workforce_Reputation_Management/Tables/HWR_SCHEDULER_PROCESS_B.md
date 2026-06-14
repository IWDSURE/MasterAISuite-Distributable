# HWR_SCHEDULER_PROCESS_B

The process table stores processes representing a job running over a time period.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrschedulerprocessb-27810.html#hwrschedulerprocessb-27810](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrschedulerprocessb-27810.html#hwrschedulerprocessb-27810)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SCHEDULER_PROCESS_B_PK | PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_ID | NUMBER |  | 18 | Yes | This is the primary key for the process table. |
| NAME | VARCHAR2 | 255 |  |  | The descriptive name of the process. |
| START_TIME | NUMBER |  |  |  | The start timestamp of the process as a single integer value. |
| FINISH_TIME | NUMBER |  |  |  | The finish timestamp of the process as a single integer value. |
| STATUS | VARCHAR2 | 255 |  |  | The current status of the process - not started, in progress, completed, or failed. |
| PARAMETERS | VARCHAR2 | 4000 |  |  | The parameters passed to the process. |
| JOB_ID | NUMBER |  | 18 |  | The ID of the job run the process is associated with. |
| PERCENTAGE | NUMBER |  |  |  | Fills in the percentage of existing rows in process table |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SCHEDULER_PROCESS_B_U1 | Unique | Default | PROCESS_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
