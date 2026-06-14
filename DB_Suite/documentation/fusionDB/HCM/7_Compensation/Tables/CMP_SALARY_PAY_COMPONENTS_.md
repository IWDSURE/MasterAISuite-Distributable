# CMP_SALARY_PAY_COMPONENTS_

Pay rates are an itemization of a person salary typically consisting of a base amount plus ancillary amounts.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarypaycomponents-17305.html#cmpsalarypaycomponents-17305](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarypaycomponents-17305.html#cmpsalarypaycomponents-17305)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_SALARY_PAY_COMPONENTS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, SALARY_PAY_COMPONENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SALARY_PAY_COMPONENT_ID | NUMBER |  | 18 | Yes | SALARY_PAY_COMPONENT_ID |
| RATE_ADJUSTMENT_AMOUNT | NUMBER |  |  |  | RATE_ADJUSTMENT_AMOUNT |
| RATE_ADJUSTMENT_PERCENT | NUMBER |  |  |  | RATE_ADJUSTMENT_PERCENT |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | BUSINESS_GROUP_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| WORK_TERM_ID | NUMBER |  | 18 |  | WORK_TERM_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| ASSIGNMENT_TYPE | VARCHAR2 | 230 |  |  | ASSIGNMENT_TYPE |
| SALARY_BASIS_ID | NUMBER |  | 18 |  | SALARY_BASIS_ID |
| SALARY_ID | NUMBER |  | 18 |  | SALARY_ID |
| SALARY_DATE_FROM | DATE |  |  |  | SALARY_DATE_FROM |
| SALARY_DATE_TO | DATE |  |  |  | SALARY_DATE_TO |
| PAY_RATE_DEFINITION_ID | NUMBER |  | 18 |  | PAY_RATE_DEFINITION_ID |
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
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_SALARY_PAY_COMPONENTN1_ | Non Unique | Default | SALARY_PAY_COMPONENT_ID, LAST_UPDATE_DATE |
| CMP_SALARY_PAY_COMPONENTS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, SALARY_PAY_COMPONENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
