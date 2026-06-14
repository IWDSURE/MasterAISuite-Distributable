# CMP_ATTR_SIMPLE_COMPONENTS

Stores salary simple component details for the selected salary basis.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpattrsimplecomponents-16280.html#cmpattrsimplecomponents-16280](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpattrsimplecomponents-16280.html#cmpattrsimplecomponents-16280)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_ATTR_SIMPLE_COMPONENTS_PK | ATTR_SIMPLE_COMPONENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTR_SIMPLE_COMPONENT_ID | NUMBER |  | 18 | Yes | ATTR_SIMPLE_COMPONENT_ID |
| ATTR_SALARY_BASIS_ID | NUMBER |  | 18 | Yes | ATTR_SALARY_BASIS_ID |
| SALARY_BASIS_ID | NUMBER |  | 18 | Yes | SALARY_BASIS_ID |
| BASIS_SIMPLE_COMPONENT_ID | NUMBER |  | 18 | Yes | BASIS_SIMPLE_COMPONENT_ID |
| COMPONENT_TYPE | VARCHAR2 | 30 |  |  | COMPONENT_TYPE |
| SIMPLE_COMPONENT_CODE | VARCHAR2 | 30 |  |  | SIMPLE_COMPONENT_CODE |
| BASED_ON_COMPONENT_CODE | VARCHAR2 | 30 |  |  | BASED_ON_COMPONENT_CODE |
| RATE_APPLICATION_RESULT | VARCHAR2 | 40 |  |  | RATE_APPLICATION_RESULT |
| VALUE | NUMBER |  |  |  | VALUE |
| DISPLAY_SEQUENCE | NUMBER |  | 3 |  | DISPLAY_SEQUENCE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_ATTR_SIMPLE_COMPONENTS_N1 | Non Unique | Default | ATTR_SALARY_BASIS_ID |
| CMP_ATTR_SIMPLE_COMPONENTS_PK | Unique | Default | ATTR_SIMPLE_COMPONENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
