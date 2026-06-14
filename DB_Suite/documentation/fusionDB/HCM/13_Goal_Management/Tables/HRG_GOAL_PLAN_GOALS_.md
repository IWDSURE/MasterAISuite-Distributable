# HRG_GOAL_PLAN_GOALS_

Stores the relationship of goal, goal plan.

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalplangoals-24993.html#hrggoalplangoals-24993](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalplangoals-24993.html#hrggoalplangoals-24993)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_GOAL_PLAN_GOALS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, GOAL_PLAN_GOAL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_PLAN_GOAL_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |
| DISPLAY_SEQUENCE | NUMBER |  | 9 |  | Sequence in which goals will be displayed in a goal plan |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_BUSINESS_GROUPS |
| GOAL_ID | NUMBER |  | 18 |  | Foreign key to HRG_GOALS, which represents the goal for which action is created. |
| GOAL_PLAN_ID | NUMBER |  | 18 |  | Foreign key to HRG_GOAL_PLANS_B, which holds ID of goal plan. |
| WEIGHTING | NUMBER |  | 5 |  | weight or importance of a goal relative to other goals expressed in percentage. |
| PRIORITY_CODE | VARCHAR2 | 30 |  |  | Priority of goal. Possible values are High, Medium and Low. |
| EFFECTIVE_START_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| GOAL_PLAN_SET_ID | NUMBER |  | 18 |  | Foreign key to HRG_GOAL_PLAN_SETS_B |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Denormalized column ASSIGNMENT_ID.  Added for use by OTBI VOs only - value is never populated on this table. |
| REVIEW_PERIOD_ID | NUMBER |  | 18 |  | Review period id needed for filtering goals added to primary goal plan |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_GOAL_PLAN_GOALSN1_ | Non Unique | Default | GOAL_PLAN_GOAL_ID |
| HRG_GOAL_PLAN_GOALSU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, GOAL_PLAN_GOAL_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
