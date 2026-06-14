# HRG_GOAL_PLANS_TL

Translation table of Goal Plan.

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalplanstl-21395.html#hrggoalplanstl-21395](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalplanstl-21395.html#hrggoalplanstl-21395)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_GOAL_PLANS_TL_PK | GOAL_PLAN_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_PLAN_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| GOAL_PLAN_NAME | VARCHAR2 | 400 |  | Yes | Name of goal plan |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Description of Goal Plan |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRG_GOAL_PLANS_TL_FK1 | Non Unique | Default | GOAL_PLAN_ID | Obsolete |
| HRG_GOAL_PLANS_TL_N1 | Non Unique | Default | UPPER("GOAL_PLAN_NAME") |  |
| HRG_GOAL_PLANS_TL_PK | Unique | Default | GOAL_PLAN_ID, LANGUAGE |  |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
