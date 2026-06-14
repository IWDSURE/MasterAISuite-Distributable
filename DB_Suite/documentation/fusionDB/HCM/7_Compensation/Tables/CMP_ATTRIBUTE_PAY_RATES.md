# CMP_ATTRIBUTE_PAY_RATES

Stores pay rate details for the selected salary basis.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpattributepayrates-19461.html#cmpattributepayrates-19461](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpattributepayrates-19461.html#cmpattributepayrates-19461)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_ATTRIBUTE_PAY_RATES_PK | ATTR_PAY_RATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTR_PAY_RATE_ID | NUMBER |  | 18 | Yes | ATTR_PAY_RATE_ID |
| ATTR_SALARY_BASIS_ID | NUMBER |  | 18 | Yes | ATTR_SALARY_BASIS_ID |
| PAY_RATE_ID | NUMBER |  | 18 | Yes | PAY_RATE_ID |
| SALARY_BASIS_ID | NUMBER |  | 18 | Yes | SALARY_BASIS_ID |
| RATE_APPLICATION_RESULT | VARCHAR2 | 40 |  |  | RATE_APPLICATION_RESULT |
| VALUE | NUMBER |  |  |  | VALUE |
| AMOUNT_ENTERABLE | VARCHAR2 | 30 |  |  | AMOUNT_ENTERABLE |
| FACTOR_ENTERABLE | VARCHAR2 | 30 |  |  | FACTOR_ENTERABLE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| RATE_TYPE | VARCHAR2 | 10 |  | Yes | RATE_TYPE |
| DISPLAY_SEQUENCE | NUMBER |  | 3 |  | DISPLAY_SEQUENCE |
| STORAGE_TYPE | VARCHAR2 | 230 |  |  | STORAGE_TYPE |
| CONTRIBUTOR_FLAG | VARCHAR2 | 1 |  |  | CONTRIBUTOR_FLAG |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_ATTRIBUTE_PAY_RATES_N1 | Non Unique | Default | ATTR_SALARY_BASIS_ID |
| CMP_ATTRIBUTE_PAY_RATES_PK | Unique | Default | ATTR_PAY_RATE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
