# CMP_BASIS_SIMPLE_COMPONENTS

Stores mapping information between salary basis and simple components.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbasissimplecomponents-20139.html#cmpbasissimplecomponents-20139](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbasissimplecomponents-20139.html#cmpbasissimplecomponents-20139)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_BASIS_SIMPLE_COMPONENTS_PK | BASIS_SIMPLE_COMPONENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BASIS_SIMPLE_COMPONENT_ID | NUMBER |  | 18 | Yes | BASIS_SIMPLE_COMPONENT_ID |
| SALARY_BASIS_ID | NUMBER |  | 18 | Yes | SALARY_BASIS_ID |
| SIMPLE_COMPONENT_CODE | VARCHAR2 | 30 |  |  | SIMPLE_COMPONENT_CODE |
| DISPLAY_SEQUENCE | NUMBER |  | 3 |  | DISPLAY_SEQUENCE |
| PROCESSING_SEQUENCE | NUMBER |  | 3 |  | PROCESSING_SEQUENCE |
| COMPONENT_TYPE | VARCHAR2 | 30 |  |  | COMPONENT_TYPE |
| OVERALL_SALARY_IMPACT | VARCHAR2 | 30 |  |  | OVERALL_SALARY_IMPACT |
| DEFAULT_VALUE | NUMBER |  |  |  | DEFAULT_VALUE |
| MINIMUM_VALUE | NUMBER |  |  |  | MINIMUM_VALUE |
| MAXIMUM_VALUE | NUMBER |  |  |  | MAXIMUM_VALUE |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | INPUT_VALUE_ID |
| USER_SELECTED_COMPONENT | VARCHAR2 | 30 |  |  | USER_SELECTED_COMPONENT |
| OVERRIDE_GSP_RATE | VARCHAR2 | 30 |  |  | OVERRIDE_GSP_RATE |
| BASED_ON_COMPONENT_CODE | VARCHAR2 | 30 |  |  | BASED_ON_COMPONENT_CODE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_BASIS_SIMPLE_COMPONENTS_PK | Unique | Default | BASIS_SIMPLE_COMPONENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
