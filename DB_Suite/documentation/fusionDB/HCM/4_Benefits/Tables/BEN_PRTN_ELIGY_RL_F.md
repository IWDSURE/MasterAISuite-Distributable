# BEN_PRTN_ELIGY_RL_F

BEN_PRTN_ELIGY_RL_F  contains rules that are applied for eligibility to participate in a plan or program.   A program or plan may specify one or more BEN_PRTN_ELIGY_RL_F instead of or in addition to specifying one or more profiles.  BEN_PRTN_ELIGY_RL_F are always applied in addition to any eligibility profiles and the rules that apply to the profiles.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprtneligyrlf-22981.html#benprtneligyrlf-22981](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprtneligyrlf-22981.html#benprtneligyrlf-22981)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PRTN_ELIGY_RL_F_PK | PRTN_ELIGY_RL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRTN_ELIGY_RL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| PRTN_ELIG_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PRTN_ELIG_F. |
| FORMULA_ID | NUMBER |  | 18 | Yes | Foreign key to FF_FORMULAS_F. |
| DRVBL_FCTR_APLS_FLAG | VARCHAR2 | 30 |  | Yes | Derivable factors apply Y or N. |
| MNDTRY_FLAG | VARCHAR2 | 30 |  | Yes | Mandatory Y or N. |
| ORDR_TO_APLY_NUM | NUMBER |  | 18 |  | Order to apply. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PRTN_ELIGY_RL_F_N2 | Non Unique | Default | PRTN_ELIG_ID |
| BEN_PRTN_ELIGY_RL_F_PK | Unique | Default | PRTN_ELIGY_RL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
