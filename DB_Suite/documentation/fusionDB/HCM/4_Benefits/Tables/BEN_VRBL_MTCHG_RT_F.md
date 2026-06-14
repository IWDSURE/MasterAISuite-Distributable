# BEN_VRBL_MTCHG_RT_F

BEN_VRBL_MTCHG_RT_F identifies a rate or rates  the plan sponsor adds to a participant's activity rate, based upon the activity rate the participant elects, where the amount the plan sponsor contributes varies by some factor, such as compensation or a rule that determines whether the person is highly compensated.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvrblmtchgrtf-13965.html#benvrblmtchgrtf-13965](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvrblmtchgrtf-13965.html#benvrblmtchgrtf-13965)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_VRBL_MTCHG_RT_F_PK | VRBL_MTCHG_RT_ID, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VRBL_MTCHG_RT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| NO_MX_PCT_OF_PY_NUM_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Percent Of Pay Number Y or N. |
| TO_PCT_VAL | NUMBER |  | 15 |  | To percent value. |
| NO_MX_AMT_OF_PY_NUM_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Amount Of Pay Number Y or N. |
| MX_PCT_OF_PY_NUM | NUMBER |  | 15 |  | Maximum percent of pay. |
| NO_MX_MTCH_AMT_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Match Amount Y or N. |
| ORDR_NUM | NUMBER |  | 18 | Yes | Order number. |
| PCT_VAL | NUMBER |  | 15 |  | Percent value. |
| MX_MTCH_AMT | NUMBER |  |  |  | Maximum match amount. |
| MX_AMT_OF_PY_NUM | NUMBER |  |  |  | Maximum amount of pay. |
| MN_MTCH_AMT | NUMBER |  |  |  | Minimum match amount. |
| MTCHG_RT_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| CNTNU_MTCH_AFTR_MAX_RL_FLAG | VARCHAR2 | 30 |  | Yes | Continue matching after maximum rule Y or N. |
| FROM_PCT_VAL | NUMBER |  | 15 |  | From percent. |
| VRBL_RT_PRFL_ID | NUMBER |  | 18 |  | Foreign key to BEN_VRBL_RT_PRFL_F |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Columns |
|---|---|---|
| BEN_VRBL_MTCHG_RT_F_N1 | Non Unique | VRBL_RT_PRFL_ID |
| BEN_VRBL_MTCHG_RT_F_PK | Unique | VRBL_MTCHG_RT_ID, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
