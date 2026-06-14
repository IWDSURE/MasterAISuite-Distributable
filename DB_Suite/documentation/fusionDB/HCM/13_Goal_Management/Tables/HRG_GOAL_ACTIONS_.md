# HRG_GOAL_ACTIONS_

Stores the details of Goal Tasks (Intially termed as 'Actions').

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalactions-24195.html#hrggoalactions-24195](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalactions-24195.html#hrggoalactions-24195)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_GOAL_ACTIONS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, GOAL_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_ACTION_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |
| MIN_TARGET | NUMBER |  | 18 |  | Minimum Target for Measurable task |
| TARGET_PERCENTAGE | NUMBER |  | 18 |  | Target Percentage for Measurable Task |
| MAX_TARGET | NUMBER |  | 18 |  | Maximum target for Measurable Task |
| ACHIEVED_WEIGHT | NUMBER |  | 18 |  | Achieved Weight of Measurable task |
| ACTUAL_VALUE | NUMBER |  | 18 |  | Actual value of Measurable Task |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Description of Goal Action |
| ACTUAL_COMPLETION_DATE | DATE |  |  |  | Actual Completion Date of Goal Action |
| COMPLETION_STATUS | VARCHAR2 | 30 |  |  | Current Status of the Goal Action |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_BUSINESS_GROUPS |
| GOAL_ID | NUMBER |  | 18 |  | Foreign key to HRG_GOALS, which represents the goal for which action is created. |
| ACTION_NAME | VARCHAR2 | 240 |  |  | Name of the goal action |
| ACTION_TYPE_CODE | VARCHAR2 | 30 |  |  | Type of goal action |
| PRIORITY_CODE | VARCHAR2 | 30 |  |  | Priority of goal action. Possible values are High, Medium and Low. |
| START_DATE | DATE |  |  |  | Start date of goal action |
| TARGET_COMPLETION_DATE | DATE |  |  |  | Target date to achieve goal action. |
| PERCENT_COMPLETE_CODE | VARCHAR2 | 30 |  |  | Action percent complete code |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Status of action. Possible values are Not Started, In Progress, Completed, Overdue, Incomplete. |
| ACTION_URL | VARCHAR2 | 4000 |  |  | URL to lunch a page related to action. |
| COMMENTS | VARCHAR2 | 4000 |  |  | To capture comments for tasks progress |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| UOM_CODE | VARCHAR2 | 30 |  |  | UOM code for measurable action. |
| TARGET_TYPE | VARCHAR2 | 30 |  |  | Target type for measurable action. |
| TARGET_VALUE | NUMBER |  | 20 |  | Target value for measurable action. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_GOAL_ACTIONSN1_ | Non Unique | Default | GOAL_ACTION_ID |
| HRG_GOAL_ACTIONSU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, GOAL_ACTION_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
