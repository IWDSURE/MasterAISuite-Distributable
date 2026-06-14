# CMP_ATTRIBUTE_SALARY_BASIS

Stores salary basis details configured from setup when manager does not enter rates option is selected.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpattributesalarybasis-20862.html#cmpattributesalarybasis-20862](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpattributesalarybasis-20862.html#cmpattributesalarybasis-20862)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_ATTRIBUTE_SALARY_BASIS_PK | ATTR_SALARY_BASIS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTR_SALARY_BASIS_ID | NUMBER |  | 18 | Yes | ATTR_SALARY_BASIS_ID |
| PLAN_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | PLAN_ATTRIBUTE_ID |
| PLAN_ID | NUMBER |  | 18 |  | PLAN_ID |
| SALARY_BASIS_ID | NUMBER |  | 18 | Yes | SALARY_BASIS_ID |
| ORDER_NUM | NUMBER |  |  |  | ORDER_NUM |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| DO_NOT_POST_FLAG | VARCHAR2 | 1 |  |  | DO_NOT_POST_FLAG |
| SALARY_BASIS_TYPE | VARCHAR2 | 30 |  |  | SALARY_BASIS_TYPE |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_ATTRIBUTE_SALARY_BASIS_N1 | Non Unique | Default | PLAN_ATTRIBUTE_ID |
| CMP_ATTRIBUTE_SALARY_BASIS_N2 | Non Unique | Default | PLAN_ID, SALARY_BASIS_ID |
| CMP_ATTRIBUTE_SALARY_BASIS_PK | Unique | Default | ATTR_SALARY_BASIS_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
