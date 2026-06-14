# CMP_DYNAMIC_FILTER

Stores compensation Dynamic Filter Expresision information.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpdynamicfilter-26558.html#cmpdynamicfilter-26558](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpdynamicfilter-26558.html#cmpdynamicfilter-26558)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_DYNAMIC_FILTER_PK | FILTER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FILTER_ID | NUMBER |  | 18 | Yes | FILTER_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PLAN_ID | NUMBER |  | 18 |  | PLAN_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| DEFAULT_FLAG | VARCHAR2 | 1 |  |  | DEFAULT_FLAG |
| FILTER_NAME | VARCHAR2 | 100 |  |  | FILTER_NAME |
| EXPR_COND | VARCHAR2 | 2000 |  |  | EXPR_COND |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| DISPLAY_FLAG | VARCHAR2 | 1 |  |  | DISPLAY_FLAG |
| HIDE_FROM_MANAGER_FLAG | VARCHAR2 | 1 |  |  | HIDE_FROM_MANAGER_FLAG |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_DYNAMIC_FILTER_N1 | Non Unique | Default | PLAN_ID, PERSON_ID |
| CMP_DYNAMIC_FILTER_U1 | Unique | Default | FILTER_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
