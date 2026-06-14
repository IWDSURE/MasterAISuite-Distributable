# HWR_TASK_B

The task table stores tasks which are part of projects.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrtaskb-14117.html#hwrtaskb-14117](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrtaskb-14117.html#hwrtaskb-14117)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_TASK_B_PK | TASK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_ID | NUMBER |  | 18 | Yes | This is the primary key for the task table. |
| PAR_TASK_ID | VARCHAR2 | 500 |  |  | This stores the Parent Task Id of The Task. |
| PROJECT_KEY | VARCHAR2 | 500 |  | Yes | This is the unique project key of the project containing the task. |
| TASK_KEY | VARCHAR2 | 500 |  | Yes | This is the unique key of the task. |
| TASK_NAME | VARCHAR2 | 500 |  | Yes | This is the unique name of the task. |
| START_DATE | DATE |  |  |  | This stores the start date of the task. |
| END_DATE | DATE |  |  |  | This stores the end date of the task. |
| TASK_DURATION | NUMBER |  |  |  | This stores the duration of the task. |
| TASK_HOURS_OF_WORK | NUMBER |  |  |  | This is the total hours of work of the task. |
| IS_ROLLUP_TASK | VARCHAR2 | 1 |  | Yes | This stores whether the task is rollup or not. |
| IS_MILESTONE | VARCHAR2 | 1 |  | Yes | This stores whether the given task is a milestone or not. |
| OUTLINE_NUMBER | VARCHAR2 | 50 |  |  | This stores the outline number of the task. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_TASK_B_U1 | Unique | FUSION_TS_TX_DATA | TASK_ID |
| HWR_TASK_B_U2 | Unique | FUSION_TS_TX_DATA | PROJECT_KEY, TASK_KEY |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
