# HRG_GOAL_PLAN_SET_PLANS

Stores the relationship of goal plan set and goal plan.

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalplansetplans-22126.html#hrggoalplansetplans-22126](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalplansetplans-22126.html#hrggoalplansetplans-22126)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_GOAL_PLAN_SET_PLANS_PK | GOAL_PLAN_SET_PLAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_PLAN_SET_PLAN_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| GOAL_PLAN_SET_ID | NUMBER |  | 18 | Yes | Foreign key to HRG_GOAL_PLAN_SET_B, which represents the goal plan set for which action is created. |
| GOAL_PLAN_ID | NUMBER |  | 18 | Yes | Foreign key to HRG_GOAL_PLANS_B, which holds ID of goal plan. |
| WEIGHTING | NUMBER |  | 5 |  | weight or importance of a goal plan relative to other goal plans  expressed in percentage. |
| MASS_REQUEST_ID | NUMBER |  | 18 |  | Foreign key to HRG_GOAL_MASS_REQUESTS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_GOAL_PLAN_SET_PLANS_FK1 | Non Unique | Default | GOAL_PLAN_ID |
| HRG_GOAL_PLAN_SET_PLANS_FK2 | Non Unique | Default | GOAL_PLAN_SET_ID |
| HRG_GOAL_PLAN_SET_PLANS_PK | Unique | Default | GOAL_PLAN_SET_PLAN_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
