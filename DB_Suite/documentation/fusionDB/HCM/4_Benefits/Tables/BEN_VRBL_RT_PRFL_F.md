# BEN_VRBL_RT_PRFL_F

BEN_VRBL_RT_PRFL_F identifies the values for a rate based on that fact that a person satisfies the criteria that have been defined for the profile.  BEN_VRBL_RT_PRFL_F are reusable and may be applied to one or more standard rates, credits, imputed income, coverage or premiums.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvrblrtprflf-16030.html#benvrblrtprflf-16030](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvrblrtprflf-16030.html#benvrblrtprflf-16030)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_VRBL_RT_PRFL_F_PK | VRBL_RT_PRFL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VRBL_RT_PRFL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ACTY_TYP_CD | VARCHAR2 | 30 |  |  | Activity type. |
| RT_TYP_CD | VARCHAR2 | 30 |  |  | Rate type. |
| BNFT_RT_TYP_CD | VARCHAR2 | 30 |  |  | Benefit rate type. |
| TX_TYP_CD | VARCHAR2 | 30 |  | Yes | Tax type. |
| VRBL_RT_TRTMT_CD | VARCHAR2 | 30 |  | Yes | Variable rate treatment. |
| ACTY_REF_PERD_CD | VARCHAR2 | 30 |  | Yes | Activity reference period. |
| MLT_CD | VARCHAR2 | 30 |  | Yes | Multiply code. |
| INCRMNT_ELCN_VAL | NUMBER |  |  |  | Increment election value. |
| DFLT_ELCN_VAL | NUMBER |  |  |  | Default election value. |
| MX_ELCN_VAL | NUMBER |  |  |  | Maximum election value. |
| MN_ELCN_VAL | NUMBER |  |  |  | Minimum election value. |
| VAL | NUMBER |  |  |  | Value. |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the variable rate profile. |
| NO_MN_ELCN_VAL_DFND_FLAG | VARCHAR2 | 30 |  | Yes | No Minimum Election Value Defined Y or N. |
| NO_MX_ELCN_VAL_DFND_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Election Value Defined Y or N. |
| VAL_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| VRBL_RT_PRFL_STAT_CD | VARCHAR2 | 30 |  |  | Variable rate profile status. |
| VRBL_USG_CD | VARCHAR2 | 30 |  |  | Variable rate usage. |
| RNDG_CD | VARCHAR2 | 30 |  |  | Rounding code. |
| RNDG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| LWR_LMT_VAL | NUMBER |  |  |  | Lower limit value. |
| LWR_LMT_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| UPR_LMT_VAL | NUMBER |  |  |  | Upper limit value. |
| UPR_LMT_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ANN_MN_ELCN_VAL | NUMBER |  |  |  | Annual maximum election value. |
| ANN_MX_ELCN_VAL | NUMBER |  |  |  | Annual minimum election value. |
| COMP_LVL_FCTR_ID | NUMBER |  | 18 |  | Foreign Key to BEN_COMP_LVL_FCTR_F. |
| PL_TYP_OPT_TYP_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_TYP_OPT_TYP_F. |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| OIPL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OIPL_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ALWYS_SUM_ALL_CVG_FLAG | VARCHAR2 | 30 |  | Yes | Allows Sum of all Coverages Y or N. |
| ALWYS_CNT_ALL_PRTTS_FLAG | VARCHAR2 | 30 |  | Yes | Allows count all participants Y or N. |
| ASMT_TO_USE_CD | VARCHAR2 | 30 |  | Yes | Assignment to use. |
| ULTMT_UPR_LMT | NUMBER |  |  |  | Ultimate upper limit. |
| ULTMT_LWR_LMT | NUMBER |  |  |  | Ultimate lower limit. |
| ULTMT_UPR_LMT_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ULTMT_LWR_LMT_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Eligibility Profile ID.
NOTE: Only 1 Eligibility Profile can be attached to a Variable Rate Profile. |
| MULTIPLIER | NUMBER |  | 18 |  | This column in used for calculation method in variable rates. In all the calculations methods either the Flat Value or Multiplier is shown to the user, and the value of both the fields goes to the database column VAL only. But for calculation method "Flat Amount Plus Multiple of Compensation" both these fields appears on the screen, and this time value of Multiplier is going to the column "Mn_Elcn_Val"(which is not actually meant to store the value of multiplier and seems like a workaround) so we want to have separate column "Multiplier". |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use. |
| TYPE_ID | NUMBER |  | 18 |  | This column is Foreign Key to BEN_TYPES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_VRBL_RT_PRFL_F_FK1 | Non Unique | Default | COMP_LVL_FCTR_ID |
| BEN_VRBL_RT_PRFL_F_N1 | Non Unique | Default | OIPL_ID |
| BEN_VRBL_RT_PRFL_F_N2 | Non Unique | Default | PL_ID |
| BEN_VRBL_RT_PRFL_F_N3 | Non Unique | Default | PL_TYP_OPT_TYP_ID |
| BEN_VRBL_RT_PRFL_F_N4 | Non Unique | Default | UPPER("NAME") |
| BEN_VRBL_RT_PRFL_F_N5 | Non Unique | Default | NAME, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| BEN_VRBL_RT_PRFL_F_PK | Unique | Default | VRBL_RT_PRFL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
