# BEN_ELIG_SUPPL_ROLE_PRTE

BEN_ELIG_SUPPL_ROLE_PRTE
BEN_ELIG_SUPPL_ROLE_PRTE
BEN_ELIG_SUPPL_ROLE_PRTE

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligsupplroleprte-12275.html#beneligsupplroleprte-12275](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligsupplroleprte-12275.html#beneligsupplroleprte-12275)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_SUPPL_ROLE_PRTE_PK | ELIG_SUPPL_ROLE_PRTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_SUPPL_ROLE_PRTE_ID | NUMBER |  | 18 | Yes | ELIG_SUPPL_ROLE_PRTE_ID |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | ELIGY_PRFL_ID |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | EXCLD_FLAG |
| JOB_ID | NUMBER |  | 18 |  | JOB_ID |
| JOB_GROUP_ID | NUMBER |  | 18 |  | JOB_GROUP_ID |
| ORDR_NUM | NUMBER |  | 18 |  | ORDR_NUM |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CRITERIA_SCORE | NUMBER |  |  |  | CRITERIA_SCORE |
| CRITERIA_WEIGHT | NUMBER |  |  |  | CRITERIA_WEIGHT |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_SUPPL_ROLE_PRTE_N1 | Non Unique | Default | ELIGY_PRFL_ID |
| BEN_ELIG_SUPPL_ROLE_PRTE_PK | Unique | Default | ELIG_SUPPL_ROLE_PRTE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
