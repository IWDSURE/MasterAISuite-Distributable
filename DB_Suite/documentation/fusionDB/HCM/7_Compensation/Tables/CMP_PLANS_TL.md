# CMP_PLANS_TL

Stores plan's translation attributes.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplanstl-9684.html#cmpplanstl-9684](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplanstl-9684.html#cmpplanstl-9684)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_PLANS_TL_PK | PLAN_ID, LANGUAGE, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| PLAN_NAME | VARCHAR2 | 80 |  |  | PLAN_NAME |
| DESCRIPTION | VARCHAR2 | 300 |  |  | DESCRIPTION |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PLAN_INFO_TASK_NAME | VARCHAR2 | 60 |  |  | PLAN_INFO_TASK_NAME |
| STMT_GLOBAL_NAME | VARCHAR2 | 80 |  |  | STMT_GLOBAL_NAME |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_PLANS_TL_UK1 | Unique | Default | PLAN_ID, LANGUAGE, BUSINESS_GROUP_ID |
| CMP_PLANS_TL_UK2 | Unique | Default | BUSINESS_GROUP_ID, LANGUAGE, PLAN_NAME |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
