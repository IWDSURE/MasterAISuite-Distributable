# BEN_ELIG_LOS_PRTE

BEN_ELIG_LOS_PRTE_F identifies that a person must satisfy a minimum and or maximum length of service  period in order to be eligible or in some cases be excluded from eligibility for a compensation  object.  . BEN_ELIG_LOS_PRTE_F is the intersection of BEN_ELIGY_PRFL_F and BEN_LOS_FCTR.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneliglosprte-29412.html#beneliglosprte-29412](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneliglosprte-29412.html#beneliglosprte-29412)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_LOS_PRTE_PK | ELIG_LOS_PRTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_LOS_PRTE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| START_DATE | DATE |  |  |  | Effective start date. |
| END_DATE | DATE |  |  |  | Effective end date. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LOS_FCTR_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_LOFS_FCTR_F. |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ELIGY_PRFL_F. |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | Exclude Y or N. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CRITERIA_SCORE | NUMBER |  |  |  | Criteria Score |
| CRITERIA_WEIGHT | NUMBER |  |  |  | Criteria Weight |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_LOS_PRTE_N1 | Non Unique | FUSION_TS_TX_IDX | ELIGY_PRFL_ID |
| BEN_ELIG_LOS_PRTE_PK | Unique | FUSION_TS_TX_IDX | ELIG_LOS_PRTE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
