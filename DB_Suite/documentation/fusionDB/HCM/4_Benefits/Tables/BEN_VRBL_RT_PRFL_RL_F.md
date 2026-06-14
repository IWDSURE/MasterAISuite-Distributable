# BEN_VRBL_RT_PRFL_RL_F

BEN_VRBL_RT_PRFL_RL_F identifies a rule  that may be used to determine the criteria, such as whether a person is a key employee,which is not available through the criteria delivered for BEN_VRBL_RT_PRFL_F.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvrblrtprflrlf-9402.html#benvrblrtprflrlf-9402](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvrblrtprflrlf-9402.html#benvrblrtprflrlf-9402)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_VRBL_RT_PRFL_RL_F_PK | VRBL_RT_PRFL_RL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VRBL_RT_PRFL_RL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| VRBL_RT_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_VRBL_RT_PRFL_F |
| FORMULA_ID | NUMBER |  | 18 | Yes | Foreign key to FF_FORMULAS_F. |
| ORDR_TO_APLY_NUM | NUMBER |  | 18 |  | Order to apply. |
| DRVBL_FCTR_APLS_FLAG | VARCHAR2 | 30 |  | Yes | Derivable factors apply Y or N. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Columns |
|---|---|---|
| BEN_VRBL_RT_PRFL_RL_F_N2 | Non Unique | VRBL_RT_PRFL_ID |
| BEN_VRBL_RT_PRFL_RL_F_PK | Unique | VRBL_RT_PRFL_RL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
