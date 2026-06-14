# CMP_SALARY_PAY_COMPONENTS

Pay rates are an itemization of a person salary typically consisting of a base amount plus ancillary amounts.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarypaycomponents-9061.html#cmpsalarypaycomponents-9061](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarypaycomponents-9061.html#cmpsalarypaycomponents-9061)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_SALARY_PAY_COMPONENTS_PK | SALARY_PAY_COMPONENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SALARY_PAY_COMPONENT_ID | NUMBER |  | 18 | Yes | SALARY_PAY_COMPONENT_ID |
| RATE_ADJUSTMENT_AMOUNT | NUMBER |  |  |  | RATE_ADJUSTMENT_AMOUNT |
| RATE_ADJUSTMENT_PERCENT | NUMBER |  |  |  | RATE_ADJUSTMENT_PERCENT |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | LEGISLATIVE_DATA_GROUP_ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| WORK_TERM_ID | NUMBER |  | 18 |  | WORK_TERM_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| ASSIGNMENT_TYPE | VARCHAR2 | 230 |  |  | ASSIGNMENT_TYPE |
| SALARY_BASIS_ID | NUMBER |  | 18 | Yes | SALARY_BASIS_ID |
| SALARY_ID | NUMBER |  | 18 | Yes | SALARY_ID |
| SALARY_DATE_FROM | DATE |  |  | Yes | SALARY_DATE_FROM |
| SALARY_DATE_TO | DATE |  |  | Yes | SALARY_DATE_TO |
| PAY_RATE_DEFINITION_ID | NUMBER |  | 18 | Yes | PAY_RATE_DEFINITION_ID |
| RATE_SCALE | NUMBER |  | 18 |  | RATE_SCALE |
| RATE_ROUNDING_CODE | VARCHAR2 | 30 |  |  | RATE_ROUNDING_CODE |
| RATE_TYPE | VARCHAR2 | 30 |  |  | RATE_TYPE |
| RATE_ENTERABLE | VARCHAR2 | 30 |  |  | RATE_ENTERABLE |
| RATE_FACTOR_ENTERABLE | VARCHAR2 | 30 |  |  | RATE_FACTOR_ENTERABLE |
| RATE_CURRENCY_CODE | VARCHAR2 | 30 |  |  | RATE_CURRENCY_CODE |
| RATE_PERIODICITY_CODE | VARCHAR2 | 30 |  |  | RATE_PERIODICITY_CODE |
| RATE_BASE_SALARY_FLAG | VARCHAR2 | 30 |  |  | RATE_BASE_SALARY_FLAG |
| RATE_OVERALL_SALARY_FLAG | VARCHAR2 | 30 |  |  | RATE_OVERALL_SALARY_FLAG |
| RATE_PREV_AMOUNT | NUMBER |  |  |  | RATE_PREV_AMOUNT |
| RATE_AMOUNT | NUMBER |  |  |  | RATE_PREV_AMOUNT |
| RATE_MAX_AMOUNT | NUMBER |  |  |  | RATE_MAX_AMOUNT |
| RATE_MIN_AMOUNT | NUMBER |  |  |  | RATE_MIN_AMOUNT |
| RATE_FACTOR | NUMBER |  |  |  | RATE_FACTOR |
| RATE_ANNUAL_AMOUNT | NUMBER |  |  |  | RATE_ANNUAL_AMOUNT |
| RATE_ANNUAL_FT_AMOUNT | NUMBER |  |  |  | RATE_ANNUAL_FT_AMOUNT |
| RATE_DEFAULT_AMOUNT | NUMBER |  |  |  | RATE_DEFAULT_AMOUNT |
| RATE_DEFAULT_STYLE | VARCHAR2 | 30 |  |  | RATE_DEFAULT_STYLE |
| RATE_USED_FOR_METRICS | VARCHAR2 | 1 |  |  | RATE_USED_FOR_METRICS |
| RATE_DISPLAY_SEQUENCE | NUMBER |  | 3 |  | RATE_DISPLAY_SEQUENCE |
| VALUE_REQUIRED | VARCHAR2 | 30 |  |  | VALUE_REQUIRED |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_PAY_COMPONENTS_N1 | Non Unique | Default | SALARY_ID |
| CMP_PAY_COMPONENTS_N2 | Non Unique | Default | ASSIGNMENT_ID, SALARY_DATE_FROM |
| CMP_PAY_COMPONENTS_N3 | Non Unique | Default | ASSIGNMENT_ID, PAY_RATE_DEFINITION_ID, SALARY_DATE_FROM |
| CMP_SALARY_PAY_COMPONENTS_PK | Unique | Default | SALARY_PAY_COMPONENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
