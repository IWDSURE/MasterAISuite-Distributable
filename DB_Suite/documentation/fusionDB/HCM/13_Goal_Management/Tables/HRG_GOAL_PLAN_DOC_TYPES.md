# HRG_GOAL_PLAN_DOC_TYPES

stores the relation of goal plan and performance document types

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalplandoctypes-29339.html#hrggoalplandoctypes-29339](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalplandoctypes-29339.html#hrggoalplandoctypes-29339)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_GOAL_PLAN_DOC_TYPES_PK | GOAL_PLAN_DOC_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_PLAN_DOC_TYPE_ID | NUMBER |  | 18 | Yes | System generated unique key |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| GOAL_PLAN_ID | NUMBER |  | 18 | Yes | Foreign key of Goal Plan. |
| DOC_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key of Document Type. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_GOAL_PLAN_DOC_TYPES_N1 | Non Unique | Default | GOAL_PLAN_ID, DOC_TYPE_ID |
| HRG_GOAL_PLAN_DOC_TYPES_U1 | Unique | Default | GOAL_PLAN_DOC_TYPE_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
