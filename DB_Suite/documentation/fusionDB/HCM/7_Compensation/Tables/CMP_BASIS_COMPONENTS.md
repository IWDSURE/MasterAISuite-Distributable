# CMP_BASIS_COMPONENTS

Components itemize base pay into different change reasons.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbasiscomponents-8681.html#cmpbasiscomponents-8681](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbasiscomponents-8681.html#cmpbasiscomponents-8681)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_BASIS_COMPONENTS_PK | BASIS_COMPONENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BASIS_COMPONENT_ID | NUMBER |  | 18 | Yes | BASIS_COMPONENT_ID |
| SALARY_BASIS_ID | NUMBER |  | 18 | Yes | SALARY_BASIS_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| DISPLAY_SEQUENCE | NUMBER |  | 3 |  | DISPLAY_SEQUENCE |
| COMPONENT_CODE | VARCHAR2 | 30 |  | Yes | COMPONENT_CODE |
| AVAILABLE_START_DATE | DATE |  |  |  | AVAILABLE_START_DATE |
| AVAILABLE_END_DATE | DATE |  |  |  | AVAILABLE_END_DATE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_BASIS_COMPONENTS_PK | Unique | Default | BASIS_COMPONENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
