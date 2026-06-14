# HRG_MASS_REQ_ASSIGNMENTS

Stores the assignment details used in "Goal plan generation" and "Goal mass assignment"

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgmassreqassignments-20549.html#hrgmassreqassignments-20549](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgmassreqassignments-20549.html#hrgmassreqassignments-20549)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_MASS_REQ_ASSIGNMENTS_PK | MASS_REQ_ASSIGNMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MASS_REQ_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| MASS_REQUEST_ID | NUMBER |  | 18 | Yes | Foreign key to HRG_GOAL_MASS_REQUESTS |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_ASSIGNMENTS_M, which holds the worker's assignment. |
| PERSON_ID | NUMBER |  | 18 |  | Person Id of the person to whom the goal is to be assigned. |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Reference to the organization to which goal plan is being created. |
| GOAL_PLAN_ID | NUMBER |  | 18 |  | Stores the goal plan id of goal plan to be assigned to individual assignments |
| GOAL_PLAN_SET_ID | NUMBER |  | 18 |  | Stores the goal plan set id of goal plan to be assigned to individual assignments |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ALLOW_KEY_ATTR_UPDATE_FLAG | VARCHAR2 | 30 |  |  | Key attribute modification is allowed or not. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_MASS_REQ_ASSIGNMENTS_FK1 | Non Unique | Default | MASS_REQUEST_ID |
| HRG_MASS_REQ_ASSIGNMENTS_PK | Unique | Default | MASS_REQ_ASSIGNMENT_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
