# HRG_GOAL_PLAN_SETS_B

Stores the goal plan set details.

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalplansetsb-31755.html#hrggoalplansetsb-31755](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalplansetsb-31755.html#hrggoalplansetsb-31755)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_GOAL_PLAN_SETS_B_PK | GOAL_PLAN_SET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_PLAN_SET_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| GOAL_PLAN_SET_EXT_ID | VARCHAR2 | 250 |  | Yes | Unique Code to identify the record |
| START_DATE | DATE |  |  | Yes | Goal Plan Set start date |
| END_DATE | DATE |  |  | Yes | Goal Plan Set end date |
| MASS_REQUEST_ID | NUMBER |  | 18 |  | Foreign key to HRG_GOAL_MASS_REQUESTS |
| GOAL_PLAN_SET_ACTIVE_FLAG | VARCHAR2 | 30 |  | Yes | This colum is to decide whether goal plan set  is active or not |
| REQUEST_UI_CONTEXT_CODE | VARCHAR2 | 30 |  |  | Code to identify the request context for a goal plan set. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| REVIEW_PERIOD_ID | NUMBER |  | 18 |  | Foreign key to HRT_REVIEW_PERIODS_B |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| REQUEST_STATUS | VARCHAR2 | 30 |  |  | Stores request status of the last ESS job submitted for this goal plan set |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_GOAL_PLAN_SETS_B_FK1 | Non Unique | Default | MASS_REQUEST_ID |
| HRG_GOAL_PLAN_SETS_B_N1 | Non Unique | Default | START_DATE |
| HRG_GOAL_PLAN_SETS_B_N2 | Non Unique | Default | END_DATE |
| HRG_GOAL_PLAN_SETS_B_PK | Unique | Default | GOAL_PLAN_SET_ID |
| HRG_GOAL_PLAN_SETS_B_UK1 | Unique | Default | GOAL_PLAN_SET_EXT_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
