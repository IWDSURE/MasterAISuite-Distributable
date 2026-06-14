# CMP_CWB_POST_SAL_RATES

stores Salary rates for a person with Rate based salary type

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpostsalrates-19295.html#cmpcwbpostsalrates-19295](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpostsalrates-19295.html#cmpcwbpostsalrates-19295)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_POST_SAL_RATES_PK | PERSON_RUN_ID, PAY_RATE_DEFINITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_RUN_ID | NUMBER |  | 18 | Yes | PERSON_RUN_ID |
| SALARY_ID | NUMBER |  | 18 | Yes | SALARY_ID |
| SALARY_DATE_FROM | DATE |  |  | Yes | SALARY_DATE_FROM |
| SALARY_DATE_TO | DATE |  |  | Yes | SALARY_DATE_TO |
| PAY_RATE_DEFINITION_ID | NUMBER |  | 18 | Yes | PAY_RATE_DEFINITION_ID |
| RATE_SCALE | NUMBER |  | 18 |  | RATE_SCALE |
| RATE_CURRENCY_CODE | VARCHAR2 | 30 |  |  | RATE_CURRENCY_CODE |
| RATE_PERIODICITY_CODE | VARCHAR2 | 30 |  |  | RATE_PERIODICITY_CODE |
| RATE_PREV_AMOUNT | NUMBER |  |  |  | RATE_PREV_AMOUNT |
| RATE_AMOUNT | NUMBER |  |  |  | RATE_AMOUNT |
| RATE_FACTOR | NUMBER |  |  |  | RATE_FACTOR |
| RATE_ANNUAL_AMOUNT | NUMBER |  |  |  | RATE_ANNUAL_AMOUNT |
| RATE_ANNUAL_FT_AMOUNT | NUMBER |  |  |  | RATE_ANNUAL_FT_AMOUNT |
| RATE_DISPLAY_SEQUENCE | NUMBER |  | 3 |  | RATE_DISPLAY_SEQUENCE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_POST_SAL_RATES_PK | Unique | Default | PERSON_RUN_ID, PAY_RATE_DEFINITION_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
