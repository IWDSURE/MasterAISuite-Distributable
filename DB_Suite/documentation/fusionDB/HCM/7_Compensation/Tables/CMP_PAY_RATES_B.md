# CMP_PAY_RATES_B

Pay rates are an itemization of a person salary typically consisting of a base amount plus ancillary amounts.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmppayratesb-19808.html#cmppayratesb-19808](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmppayratesb-19808.html#cmppayratesb-19808)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_PAY_RATES_B_PK | PAY_RATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_RATE_ID | NUMBER |  | 18 | Yes | PAY_RATE_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | LEGISLATIVE_DATA_GROUP_ID |
| AVAILABLE_FROM_DATE | DATE |  |  |  | AVAILABLE_FROM_DATE |
| RATE_STATUS | VARCHAR2 | 30 |  |  | RATE_STATUS |
| PAY_RATE_CODE | VARCHAR2 | 80 |  | Yes | PAY_RATE_CODE |
| RATE_GROUP_CODE | VARCHAR2 | 80 |  |  | RATE_GROUP_CODE |
| REPRESENTS_BASE | VARCHAR2 | 1 |  |  | REPRESENTS_BASE |
| ADDS_TO_OVERALL_PAY | VARCHAR2 | 1 |  |  | ADDS_TO_OVERALL_PAY |
| RATE_TYPE | VARCHAR2 | 30 |  |  | RATE_TYPE |
| AMOUNT_ROUNDING_CODE | VARCHAR2 | 30 |  |  | AMT_ROUNDING_CODE |
| AMOUNT_SCALE | NUMBER |  | 3 |  | AMOUNT_SCALE |
| PERCENT_SCALE | NUMBER |  | 3 |  | PERCENT_SCALE |
| POINT_SCALE | NUMBER |  | 3 |  | POINT_SCALE |
| DEFAULT_TYPE | VARCHAR2 | 30 |  |  | DEFAULT_TYPE |
| DEFAULT_SOURCE | VARCHAR2 | 30 |  |  | DEFAULT_SOURCE |
| DEFAULT_FORMULA_ID | NUMBER |  | 18 |  | DEFAULT_FORMULA_ID |
| DEFAULT_GRADE_RATE_ID | NUMBER |  | 18 |  | DEFAULT_GRADE_RATE_ID |
| DEFAULT_AMOUNT | NUMBER |  |  |  | DEFAULT_AMOUNT |
| DEFAULT_PERCENT | NUMBER |  |  |  | DEFAULT_PERCENT |
| DEFAULT_POINTS | NUMBER |  |  |  | DEFAULT_POINTS |
| CURRENCY_SOURCE_CODE | VARCHAR2 | 30 |  |  | CURRENCY_SOURCE_CODE |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | CURRENCY_CODE |
| FREQUENCY_SOURCE | VARCHAR2 | 30 |  |  | FREQUENCY_SOURCE |
| FREQUENCY_CODE | VARCHAR2 | 30 |  |  | FREQUENCY_CODE |
| ANNUALIZATION_FACTOR | NUMBER |  |  |  | ANNUALIZATION_FACTOR |
| CHANGE_DEFAULT_AMOUNT | VARCHAR2 | 1 |  |  | CHANGE_DEFAULT_AMOUNT |
| CHANGE_DEFAULT_PERCENT | VARCHAR2 | 1 |  |  | CHANGE_DEFAULT_PERCENT |
| CHANGE_DEFAULT_POINTS | VARCHAR2 | 1 |  |  | CHANGE_DEFAULT_POINTS |
| VALUE_REQUIRED | VARCHAR2 | 1 |  |  | VALUE_REQUIRED |
| ZERO_IF_VALUE_BLANK | VARCHAR2 | 1 |  |  | ZERO_IF_VALUE_BLANK |
| LOWER_LIMIT | NUMBER |  |  |  | LOWER_LIMIT |
| UPPER_LIMIT | NUMBER |  |  |  | UPPER_LIMIT |
| VALIDATION_FORMULA_ID | NUMBER |  | 18 |  | VALIDATION_FORMULA_ID |
| IGNORE_LIMITS_CHECK | VARCHAR2 | 1 |  |  | IGNORE_LIMITS_CHECK |
| LIMIT_VIOLATION_BEHAVIOR | VARCHAR2 | 30 |  |  | LIMIT_VIOLATION_BEHAVIOR |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | ELEMENT_TYPE_ID |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | INPUT_VALUE_ID |
| ENTRY_CREATION | VARCHAR2 | 1 |  |  | ENTRY_CREATION |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_PAY_RATES_B_PK | Unique | Default | PAY_RATE_ID |
| CMP_PAY_RATES_B_U1 | Unique | Default | PAY_RATE_CODE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
