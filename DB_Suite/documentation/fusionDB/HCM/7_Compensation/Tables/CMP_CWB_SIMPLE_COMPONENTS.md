# CMP_CWB_SIMPLE_COMPONENTS

Child entity for salary simple rates defined for salary record

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbsimplecomponents-26161.html#cmpcwbsimplecomponents-26161](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbsimplecomponents-26161.html#cmpcwbsimplecomponents-26161)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_SIMPLE_COMPONENTS_PK | PERSON_EVENT_ID, SIMPLE_SALARY_COMPNT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | PERSON_EVENT_ID |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |
| SIMPLE_SALARY_COMPNT_ID | NUMBER |  | 18 | Yes | SIMPLE_SALARY_COMPNT_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| SALARY_ID | NUMBER |  | 18 | Yes | SALARY_ID |
| SALARY_BASIS_ID | NUMBER |  | 18 |  | SALARY_BASIS_ID |
| SALARY_DATE_FROM | DATE |  |  |  | SALARY_DATE_FROM |
| SALARY_DATE_TO | DATE |  |  |  | SALARY_DATE_TO |
| BASIS_SIMPLE_COMPONENT_ID | NUMBER |  | 18 | Yes | BASIS_SIMPLE_COMPONENT_ID |
| DISPLAY_SEQUENCE | NUMBER |  | 3 |  | DISPLAY_SEQUENCE |
| PROCESSING_SEQUENCE | NUMBER |  | 3 |  | PROCESSING_SEQUENCE |
| COMPONENT_TYPE | VARCHAR2 | 30 |  |  | COMPONENT_TYPE |
| COMPONENT_CODE | VARCHAR2 | 30 |  |  | COMPONENT_CODE |
| BASED_ON_COMPONENT_CODE | VARCHAR2 | 30 |  |  | BASED_ON_COMPONENT_CODE |
| OVERALL_SALARY_AFFECT | VARCHAR2 | 30 |  |  | OVERALL_SALARY_AFFECT |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | INPUT_VALUE_ID |
| USER_SELECTED_COMPONENT | VARCHAR2 | 30 |  |  | USER_SELECTED_COMPONENT |
| DEFAULT_AMOUNT | NUMBER |  |  |  | DEFAULT_AMOUNT |
| PREV_AMOUNT | NUMBER |  |  |  | PREV_AMOUNT |
| PREV_ADJUSTMENT_AMOUNT | NUMBER |  |  |  | PREV_ADJUSTMENT_AMOUNT |
| PREV_ADJUSTMENT_PERCENT | NUMBER |  |  |  | PREV_ADJUSTMENT_PERCENT |
| AMOUNT | NUMBER |  |  | Yes | AMOUNT |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | CURRENCY_CODE |
| FREQUENCY_CODE | VARCHAR2 | 30 |  |  | FREQUENCY_CODE |
| SCALE | NUMBER |  | 3 |  | SCALE |
| ROUNDING_CODE | VARCHAR2 | 20 |  |  | ROUNDING_CODE |
| ADJUSTMENT_AMOUNT | NUMBER |  |  |  | ADJUSTMENT_AMOUNT |
| ADJUSTMENT_PERCENT | NUMBER |  |  |  | ADJUSTMENT_PERCENT |
| PERCENTAGE | NUMBER |  |  |  | PERCENTAGE |
| ANNUAL_FACTOR | NUMBER |  |  |  | ANNUAL_FACTOR |
| ANNUAL_AMOUNT | NUMBER |  |  |  | ANNUAL_AMOUNT |
| ANNUAL_FT_AMOUNT | NUMBER |  |  |  | ANNUAL_FT_AMOUNT |
| MINIMUM_AMOUNT | NUMBER |  |  |  | MINIMUM_AMOUNT |
| MAXIMUM_AMOUNT | NUMBER |  |  |  | MAXIMUM_AMOUNT |
| OVERRIDE_GSP_RATE | VARCHAR2 | 30 |  |  | OVERRIDE_GSP_RATE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PERSON_RUN_ID | NUMBER |  | 18 |  | PERSON_RUN_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_SIMPLE_COMPONENTS_N1 | Non Unique | Default | SALARY_ID, PERSON_EVENT_ID |
| CMP_CWB_SIMPLE_COMPONENTS_PK | Unique | Default | PERSON_EVENT_ID, SIMPLE_SALARY_COMPNT_ID |
| CMP_CWB_SIMPLE_COMPONENTS_U1 | Unique | Default | PERIOD_ID, PLAN_ID, ASSIGNMENT_ID, SIMPLE_SALARY_COMPNT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
