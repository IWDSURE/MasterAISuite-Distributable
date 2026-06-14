# BEN_PRTN_ELIG_PRFL_F

BEN_PRTN_ELIG_PRFL_F identifies one or more eligibility profiles to a  program, plan type in program, plan in program, plan, or option in plan for the purpose of determining a person's eligibility to participate.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprtneligprflf-23560.html#benprtneligprflf-23560](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprtneligprflf-23560.html#benprtneligprflf-23560)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PRTN_ELIG_PRFL_F_PK | PRTN_ELIG_PRFL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRTN_ELIG_PRFL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| MNDTRY_FLAG | VARCHAR2 | 30 |  | Yes | Mandatory Y or N. |
| PRTN_ELIG_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PRTN_ELIG_F. |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ELIGY_PRFL_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ELIG_PRFL_TYPE_CD | VARCHAR2 | 30 |  |  | Eligibility Profile usage - Eligibility or Ranking |
| COMPUTE_SCORE_FLAG | VARCHAR2 | 30 |  | Yes | Compute Score Flag |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PRTN_ELIG_PRFL_F_N1 | Non Unique | Default | ELIGY_PRFL_ID |
| BEN_PRTN_ELIG_PRFL_F_N2 | Non Unique | Default | PRTN_ELIG_ID |
| BEN_PRTN_ELIG_PRFL_F_PK | Unique | Default | PRTN_ELIG_PRFL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
