# BEN_ELIG_PERF_RTNG_PRTE

BEN_ELIG_PERF_RTNG_PRTE_F identifies which performance ratings are included (most typical usage) or excluded from (least typical) an eligibility profile. These criteria must be satisfied in order for the person to be eligible to participate in the compensation object.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligperfrtngprte-18361.html#beneligperfrtngprte-18361](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligperfrtngprte-18361.html#beneligperfrtngprte-18361)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_PERF_RTNG_PRTE_PK | ELIG_PERF_RTNG_PRTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ELIG_PERF_RTNG_PRTE_ID | NUMBER |  | 18 | Yes | System generated primary key column. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS | Active |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ELIGY_PRFL_F. | Active |
| START_DATE | DATE |  |  |  | Effective start date. | Active |
| END_DATE | DATE |  |  |  | Effective end date. | Active |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. | Active |
| EVENT_TYPE | VARCHAR2 | 30 |  | Yes | Event type. | Active |
| PERF_TMPL_ID | NUMBER |  | 18 |  | Foreign Key to PERFORMANCE TEMPLATE DEFINITION |  |
| RATING_MODEL_ID | NUMBER |  | 18 |  | Foreign Key to RATING_MODEL |  |
| MOST_RECENT_FLAG | VARCHAR2 | 30 |  |  | Evaluate eligibility based on the most recent performance document rating Y or N. |  |
| TMPL_PERIOD_ID | NUMBER |  | 18 |  | Identifies Template period for the Template |  |
| RATING_LEVEL_ID | NUMBER |  | 18 |  | Foreign Key to RATING_LEVEL |  |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | Exclude Y or N. | Active |
| CRITERIA_SCORE | NUMBER |  |  |  | Criteria Score | Active |
| CRITERIA_WEIGHT | NUMBER |  |  |  | Criteria Weight | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| BEN_ELIG_PERF_RTNG_PRTE_N1 | Non Unique | FUSION_TS_TX_DATA | ELIGY_PRFL_ID | Active |
| BEN_ELIG_PERF_RTNG_PRTE_PK | Unique | FUSION_TS_TX_DATA | ELIG_PERF_RTNG_PRTE_ID | Active |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
