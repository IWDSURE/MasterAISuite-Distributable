# HRG_MASS_REQ_HIERARCHIES

Stores the hierarchy details, which is used to get population in "Goal plan generation" and "Goal mass assignment" process.

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgmassreqhierarchies-11588.html#hrgmassreqhierarchies-11588](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgmassreqhierarchies-11588.html#hrgmassreqhierarchies-11588)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_MASS_REQ_HIERARCHIES_PK | MASS_REQUEST_HIERARCHY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MASS_REQUEST_HIERARCHY_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| MASS_REQUEST_ID | NUMBER |  | 18 | Yes | Foreign key to HRG_GOAL_MASS_REQUESTS |
| MANAGER_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ALL_PEOPLE_F which holds thi ID of Manager. |
| MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Assignment ID of the manager |
| HIERARCHY_TYPE_CODE | VARCHAR2 | 30 |  |  | Type of hierarchy. Possible values are Supervisory Based
Position Based
Organization Based
Supervisor Assignment Based |
| CASCADING_LEVEL | NUMBER |  | 18 |  | Number of levels a goal should be assigned under a manager. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_MASS_REQ_HIERARCHIES_FK1 | Non Unique | Default | MASS_REQUEST_ID |
| HRG_MASS_REQ_HIERARCHIES_PK | Unique | Default | MASS_REQUEST_HIERARCHY_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
