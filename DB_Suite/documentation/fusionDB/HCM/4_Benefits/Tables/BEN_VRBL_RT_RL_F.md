# BEN_VRBL_RT_RL_F

BEN_VRBL_RT_RL_F identifiesa rule  that may be used to calculate an additional amount to adjust the values determined by BEN_ACTY_BASE_RT_F.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvrblrtrlf-24329.html#benvrblrtrlf-24329](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvrblrtrlf-24329.html#benvrblrtrlf-24329)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_VRBL_RT_RL_F_PK | VRBL_RT_RL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| VRBL_RT_RL_ID | NUMBER |  | 18 | Yes | System generated primary key column. | Active |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. | Active |
| DRVBL_FCTR_APLS_FLAG | VARCHAR2 | 30 |  | Yes | Derivable factors apply Y or N. | Active |
| RT_TRTMT_CD | VARCHAR2 | 30 |  |  | Rate treatment. | Active |
| ORDR_TO_APLY_NUM | NUMBER |  | 18 |  | Order to apply. | Active |
| FORMULA_ID | NUMBER |  | 18 | Yes | Foreign key to FF_FORMULAS_F. | Active |
| ACTY_BASE_RT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTY_BASE_RT_F. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| BEN_VRBL_RT_RL_F_N1 | Non Unique | Default | ACTY_BASE_RT_ID |  |
| BEN_VRBL_RT_RL_F_PK | Unique | Default | VRBL_RT_RL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE | Active |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
