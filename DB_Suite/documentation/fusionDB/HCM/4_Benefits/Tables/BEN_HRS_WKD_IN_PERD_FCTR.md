# BEN_HRS_WKD_IN_PERD_FCTR

BEN_HRS_WKD_IN_PERD_FCTR  identifies how to calculate a person's hours worked in a period for such purposes as determining eligibility and calculating rates, in those cases when hours worked in a period is a factor.  In addition, it identifies a range of hours worked, again for eligibility and rate purposes.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benhrswkdinperdfctr-28122.html#benhrswkdinperdfctr-28122](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benhrswkdinperdfctr-28122.html#benhrswkdinperdfctr-28122)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_HRS_WKD_IN_PERD_FCTR_PK | HRS_WKD_IN_PERD_FCTR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HRS_WKD_IN_PERD_FCTR_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the hours worked factor. |
| HRS_SRC_CD | VARCHAR2 | 30 |  |  | Hours worked source. |
| RNDG_CD | VARCHAR2 | 30 |  |  | Rounding code. |
| RNDG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| HRS_WKD_DET_CD | VARCHAR2 | 30 |  |  | Hours worked determination code. |
| HRS_WKD_DET_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| PYRL_FREQ_CD | VARCHAR2 | 30 |  |  | Payroll frequency. |
| HRS_WKD_BNDRY_PERD_CD | VARCHAR2 | 30 |  |  | Hours worked boundary period. |
| NO_MN_HRS_WKD_FLAG | VARCHAR2 | 30 |  | Yes | No Minimum Hours Worked Y or N. |
| MX_HRS_NUM | NUMBER |  |  |  | Maximum number of hours. |
| NO_MX_HRS_WKD_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Hours Worked Y or N. |
| ONCE_R_CNTUG_CD | VARCHAR2 | 30 |  |  | Once or continuing. |
| MN_HRS_NUM | NUMBER |  |  |  | Minimum number of hours. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| HRS_ALT_VAL_TO_USE_CD | VARCHAR2 | 30 |  |  | Hours worked alternative value to use code. |
| HRS_WKD_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| BNFTS_BAL_ID | NUMBER |  | 18 |  | Foreign key to BEN_BNFTS_BAL_F. |
| DEFINED_BALANCE_ID | NUMBER |  | 18 |  | Foreign key to PAY_DEFINED_BALANCE. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_HWI_PD_FCTR_N1 | Non Unique | Default | HRS_WKD_DET_RL |
| BEN_HWI_PD_FCTR_N2 | Non Unique | Default | RNDG_RL |
| BEN_HWI_PD_FCTR_N3 | Non Unique | Default | BNFTS_BAL_ID |
| BEN_HWI_PD_FCTR_PK | Unique | Default | HRS_WKD_IN_PERD_FCTR_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
