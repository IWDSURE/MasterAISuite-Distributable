# CMP_SALARY_BATCH_CHANGE

This entity will insert new or corrected salary record details when the salary basis is based on the salary rates.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarybatchchange-29431.html#cmpsalarybatchchange-29431](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarybatchchange-29431.html#cmpsalarybatchchange-29431)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_SALARY_BATCH_CHANGE_PK | SALARY_BATCH_CHANGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SALARY_BATCH_CHANGE_ID | NUMBER |  | 18 | Yes | SALARY_BATCH_CHANGE_ID |
| SALARY_ASG_INFO_ID | NUMBER |  | 18 | Yes | SALARY_ASG_INFO_ID |
| PROCESS_MODE_CODE | VARCHAR2 | 30 |  | Yes | PROCESS_MODE_CODE |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| ASSIGNMENT_TYPE | VARCHAR2 | 30 |  | Yes | ASSIGNMENT_TYPE |
| SALARY_DML_TYPE | VARCHAR2 | 30 |  | Yes | SALARY_DML_TYPE |
| SALARY_ID | NUMBER |  | 18 |  | SALARY_ID |
| SALARY_OVN | NUMBER |  | 9 |  | SALARY_OVN |
| PROPOSED_DATE_FROM | DATE |  |  | Yes | PROPOSED_DATE_FROM |
| PROPOSED_DATE_TO | DATE |  |  | Yes | PROPOSED_DATE_TO |
| PROPOSED_SALARY_AMOUNT | NUMBER |  |  | Yes | PROPOSED_SALARY_AMOUNT |
| PREVIOUS_SALARY_AMOUNT | NUMBER |  |  |  | PREVIOUS_SALARY_AMOUNT |
| SALARY_CHANGED | VARCHAR2 | 30 |  |  | SALARY_CHANGED |
| SALARY_PRECISION | NUMBER |  | 3 |  | SALARY_PRECISION |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | CURRENCY_CODE |
| SALARY_BASIS_ID | NUMBER |  | 18 | Yes | SALARY_BASIS_ID |
| ACTION_ID | NUMBER |  | 18 | Yes | ACTION_ID |
| ACTION_REASON_ID | NUMBER |  | 18 |  | ACTION_REASON_ID |
| SALARY_BASIS_CODE | VARCHAR2 | 30 |  |  | SALARY_BASIS_CODE |
| SALARY_BASIS_TYPE | VARCHAR2 | 30 |  |  | SALARY_BASIS_TYPE |
| SALARY_FACTOR | NUMBER |  |  |  | SALARY_FACTOR |
| PROPOSED_ADJUSTMENT_AMOUNT | NUMBER |  |  |  | PROPOSED_ADJUSTMENT_AMOUNT |
| PROPOSED_ADJUSTMENT_PERCENTAGE | NUMBER |  |  |  | PROPOSED_ADJUSTMENT_PERCENTAGE |
| PROPOSED_ANNUAL_SALARY | NUMBER |  |  |  | PROPOSED_ANNUAL_SALARY |
| PROPOSED_ANNUAL_FT_SALARY | NUMBER |  |  |  | PROPOSED_ANNUAL_FT_SALARY |
| PROPOSED_QUARTILE | VARCHAR2 | 30 |  |  | PROPOSED_QUARTILE |
| PROPOSED_QUINTILE | VARCHAR2 | 30 |  |  | PROPOSED_QUINTILE |
| PROPOSED_COMPA_RATIO | NUMBER |  |  |  | PROPOSED_COMPA_RATIO |
| PROPOSED_RANGE_POSITION | NUMBER |  |  |  | PROPOSED_RANGE_POSITION |
| FTE_VALUE | NUMBER |  |  |  | FTE_VALUE |
| GRADE_ID | NUMBER |  | 18 |  | GRADE_ID |
| GRADE_LADDER_ID | NUMBER |  | 18 |  | GRADE_LADDER_ID |
| GRADE_STEP_ID | NUMBER |  | 18 |  | GRADE_STEP_ID |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| RATE_ID | NUMBER |  | 18 |  | RATE_ID |
| RATE_FACTOR | NUMBER |  |  |  | RATE_FACTOR |
| RATE_MIN_AMOUNT | NUMBER |  |  |  | RATE_MIN_AMOUNT |
| RATE_MID_AMOUNT | NUMBER |  |  |  | RATE_MID_AMOUNT |
| RATE_MAX_AMOUNT | NUMBER |  |  |  | RATE_MAX_AMOUNT |
| RATE_DEFAULT_AMOUNT | NUMBER |  |  |  | RATE_DEFAULT_AMOUNT |
| RANGE_ERROR_WARNING | VARCHAR2 | 30 |  |  | RANGE_ERROR_WARNING |
| PAYROLL_FACTOR | NUMBER |  |  |  | PAYROLL_FACTOR |
| PAYROLL_FREQUENCY_CODE | VARCHAR2 | 60 |  |  | PAYROLL_FREQUENCY_CODE |
| PAYROLL_ASSIGNMENT_ID | NUMBER |  | 18 |  | PAYROLL_ASSIGNMENT_ID |
| PAYROLL_TERM_ID | NUMBER |  | 18 |  | PAYROLL_TERM_ID |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | PAYROLL_RELATIONSHIP_ID |
| SALARY_ROUNDING_CODE | VARCHAR2 | 30 |  |  | SALARY_ROUNDING_CODE |
| RANGE_ROUNDING_CODE | VARCHAR2 | 30 |  |  | RANGE_ROUNDING_CODE |
| ANNUAL_ROUNDING_CODE | VARCHAR2 | 30 |  |  | ANNUAL_ROUNDING_CODE |
| RANGE_PRECISION | NUMBER |  | 3 |  | RANGE_PRECISION |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_SALARY_BATCH_CHANGE_N1 | Non Unique | Default | ASSIGNMENT_ID, PROPOSED_DATE_FROM |
| CMP_SALARY_BATCH_CHANGE_N2 | Non Unique | Default | SALARY_ASG_INFO_ID, ASSIGNMENT_ID, PERSON_ID |
| CMP_SALARY_BATCH_CHANGE_N3 | Non Unique | Default | ASSIGNMENT_ID, SALARY_ID |
| CMP_SALARY_BATCH_CHANGE_U1 | Unique | Default | SALARY_BATCH_CHANGE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
