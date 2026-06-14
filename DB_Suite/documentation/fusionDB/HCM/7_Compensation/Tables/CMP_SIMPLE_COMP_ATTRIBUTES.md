# CMP_SIMPLE_COMP_ATTRIBUTES

Components itemize base pay into different change reasons.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsimplecompattributes-24780.html#cmpsimplecompattributes-24780](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsimplecompattributes-24780.html#cmpsimplecompattributes-24780)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_SIMPLE_COMP_ATTRIBUTES_PK | SIMPLE_COMP_ATTRIBUTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SIMPLE_COMP_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | SIMPLE_COMP_ATTRIBUTE_ID |
| SIMPLE_COMP_ATTRIBUTE_CODE | VARCHAR2 | 30 |  | Yes | SIMPLE_COMP_ATTRIBUTE_CODE |
| SALARY_BASIS_ID | NUMBER |  | 18 | Yes | SALARY_BASIS_ID |
| PARENT_SIMPLE_COMP_ID | NUMBER |  | 18 | Yes | PARENT_SIMPLE_COMP_ID |
| PARENT_SIMPLE_COMP_CODE | VARCHAR2 | 30 |  |  | PARENT_SIMPLE_COMP_CODE |
| PARENT_SIMPLE_COMP_TYPE | VARCHAR2 | 30 |  |  | PARENT_SIMPLE_COMP_TYPE |
| PROCESSING_SEQUENCE | NUMBER |  | 3 | Yes | PROCESSING_SEQUENCE |
| BASED_ON_SIMPLE_COMP_ID | NUMBER |  | 18 | Yes | BASED_ON_SIMPLE_COMP_ID |
| BASED_ON_SIMPLE_COMP_CODE | VARCHAR2 | 30 |  |  | BASED_ON_SIMPLE_COMP_CODE |
| BASED_ON_SIMPLE_COMP_TYPE | VARCHAR2 | 30 |  |  | BASED_ON_SIMPLE_COMP_TYPE |
| COMPONENT_IMPACT | VARCHAR2 | 30 |  | Yes | COMPONENT_IMPACT |
| COMPONENT_FACTOR | NUMBER |  |  | Yes | COMPONENT_FACTOR |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_SIMPLE_COMP_ATTRIBUTES_N1 | Non Unique | Default | SALARY_BASIS_ID, PARENT_SIMPLE_COMP_ID |
| CMP_SIMPLE_COMP_ATTRIBUTES_N2 | Non Unique | Default | SALARY_BASIS_ID, PARENT_SIMPLE_COMP_CODE, BASED_ON_SIMPLE_COMP_CODE |
| CMP_SIMPLE_COMP_ATTRIBUTES_N3 | Non Unique | Default | SALARY_BASIS_ID, SIMPLE_COMP_ATTRIBUTE_CODE, PARENT_SIMPLE_COMP_CODE |
| CMP_SIMPLE_COMP_ATTRIBUTES_PK | Unique | Default | SIMPLE_COMP_ATTRIBUTE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
