# BEN_ELIG_TTL_PRTT_PRTE

BEN_ELIG_TTL_PRTT_PRTE_F identifies the total participation that is included (most typical usage) or excluded from (least typical) an eligibility profile. These criteria must be satisfied in order for the person to be eligible to participate in the compensation object.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligttlprttprte-27076.html#beneligttlprttprte-27076](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligttlprttprte-27076.html#beneligttlprttprte-27076)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_TTL_PRTT_PRTE_PK | ELIG_TTL_PRTT_PRTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_TTL_PRTT_PRTE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| START_DATE | DATE |  |  |  | Effective start date. |
| END_DATE | DATE |  |  |  | Effective end date. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Legal Employer |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | Exclude Y or N. |
| NO_MN_PRTT_NUM_APLS_FLAG | VARCHAR2 | 30 |  | Yes | No minimum participation applies Y or N. |
| NO_MX_PRTT_NUM_APLS_FLAG | VARCHAR2 | 30 |  | Yes | No maximum participation applies Y or N. |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ELIGY_PRFL_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |
| MN_PRTT_NUM | NUMBER |  | 18 |  | Minimum participation. |
| MX_PRTT_NUM | NUMBER |  | 18 |  | Maximum participation. |
| PRTT_DET_CD | VARCHAR2 | 30 |  |  | Participation determination. |
| PRTT_DET_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_TTL_PRTT_PRTE_N1 | Non Unique | Default | ELIGY_PRFL_ID |
| BEN_ELIG_TTL_PRTT_PRTE_PK | Unique | Default | ELIG_TTL_PRTT_PRTE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
