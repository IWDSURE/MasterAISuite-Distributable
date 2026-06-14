# BEN_ELIG_HIREDT_PRTE

BEN_ELIG_HIREDT_PRTE  identifies which hire date specific components are included in (most typical usage) or excluded from (least typical) an eligibility  profile. These hire date specific components-related requirements must be satisfied in order for the person to be eligible to participate in the compensation  object.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benelighiredtprte-16072.html#benelighiredtprte-16072](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benelighiredtprte-16072.html#benelighiredtprte-16072)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_HIREDT_PRTE_PK | ELIG_HIREDT_PRTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_HIREDT_PRTE_ID | NUMBER |  | 18 | Yes | ELIG_HIREPROB_PRTE_ID |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Identifies eligibility profile that this criteria is associated with. Foreign Key to BEN_ELIGY_PRFL |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| START_DATE | DATE |  |  |  | Start date |
| END_DATE | DATE |  |  |  | end date |
| DATE_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Date type code to be mapped to the hire date. eg. original hire date, latest hire date etc. |
| OPERATOR | VARCHAR2 | 255 |  |  | identifies whether to use particular date components (day, month, year) or generic duration |
| DAY | NUMBER |  |  |  | Day number within the month |
| MONTH | VARCHAR2 | 255 |  |  | Month |
| YEAR | NUMBER |  |  |  | Year |
| DURATION | NUMBER |  |  |  | Duration |
| DURATION_UOM | VARCHAR2 | 30 |  |  | duration unit of measure |
| ORDR_NUM | NUMBER |  | 18 |  | Sequence number |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | Exclude |
| CRITERIA_SCORE | NUMBER |  |  |  | Criteria score |
| CRITERIA_WEIGHT | NUMBER |  |  |  | criteria weight |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_HIREDT_PRTE_N1 | Non Unique | Default | ELIGY_PRFL_ID |
| BEN_ELIG_HIREDT_PRTE_PK | Unique | Default | ELIG_HIREDT_PRTE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
