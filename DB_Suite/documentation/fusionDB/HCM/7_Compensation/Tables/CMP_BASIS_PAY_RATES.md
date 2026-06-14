# CMP_BASIS_PAY_RATES

Stores mapping information between salary basis and pay rates.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbasispayrates-6045.html#cmpbasispayrates-6045](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbasispayrates-6045.html#cmpbasispayrates-6045)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_BASIS_PAY_RATES_PK | BASIS_PAY_RATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BASIS_PAY_RATE_ID | NUMBER |  | 18 | Yes | BASIS_PAY_RATE_ID |
| SALARY_BASIS_ID | NUMBER |  | 18 | Yes | SALARY_BASIS_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| DISPLAY_SEQUENCE | NUMBER |  | 3 |  | DISPLAY_SEQUENCE |
| PAY_RATE_ID | NUMBER |  | 18 | Yes | PAY_RATE_ID |
| DEFAULT_STYLE | VARCHAR2 | 30 |  |  | DEFAULT_STYLE |
| USE_FOR_METRICS | VARCHAR2 | 1 |  |  | USE_FOR_METRICS |
| VALUE_REQUIRED | VARCHAR2 | 30 |  |  | VALUE_REQUIRED |
| ZERO_WHEN_BLANK | VARCHAR2 | 1 |  |  | ZERO_WHEN_BLANK |
| IGNORE_MIN_WHEN_ZERO | VARCHAR2 | 1 |  |  | IGNORE_MIN_WHEN_ZERO |
| HIDE_PERCENT | VARCHAR2 | 1 |  |  | HIDE_PERCENT |
| HIDE_POINTS | VARCHAR2 | 1 |  |  | HIDE_POINTS |
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
| CMP_BASIS_PAY_RATES_N1 | Non Unique | Default | SALARY_BASIS_ID, PAY_RATE_ID |
| CMP_BASIS_PAY_RATES_PK | Unique | Default | BASIS_PAY_RATE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
