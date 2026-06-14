# HWR_MNTR_PLAN_GOAL_TASKS_B

This table stores mentor plan goal tasks.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmntrplangoaltasksb-27919.html#hwrmntrplangoaltasksb-27919](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmntrplangoaltasksb-27919.html#hwrmntrplangoaltasksb-27919)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_MNTR_PLAN_GOAL_TASKS_B_PK | TASK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_ID | NUMBER |  | 18 | Yes | This is the primary key for this table. |
| TARGET_COMPLETION_DATE | TIMESTAMP |  |  | Yes | Target completion date of the tasks. |
| GOAL_ID | NUMBER |  | 18 | Yes | This is the goal id. |
| STATUS | VARCHAR2 | 5 |  | Yes | Status of the task. |
| PERSON_ID | NUMBER |  | 18 | Yes | This is the person id. |
| TASKS_ATTR_1 | VARCHAR2 | 400 |  |  | This is the mentor plan task attribute 1. |
| TASKS_ATTR_2 | VARCHAR2 | 400 |  |  | This is the mentor plan task attribute 2. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_MNTR_PLAN_GOAL_TASKS_B_U1 | Unique | Default | TASK_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
