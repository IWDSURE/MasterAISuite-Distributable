# BEN_ACTY_BASE_RT_F

BEN_ACTY_BASE_RT_F identifies parameters which control how contributions into, distributions out of, or accrued benefits provided by comp objects are calculated.  Activity Rates are maintained at many  levels within the comp hierarchy, for example, program, plan, option in plan, plan type in program.   . Examples are employee payroll contributions in  the amount of $25.43 per month for a coverage option in a medical plan, employer payroll contributions in  the amount of $35.77 per month based on participant's age of 25 , for each thousand dollars of life insurance coverage, and employer payroll distribution of $50.00 per month for flex credits.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benactybasertf-28534.html#benactybasertf-28534](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benactybasertf-28534.html#benactybasertf-28534)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ACTY_BASE_RT_F_PK | ACTY_BASE_RT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ACTY_BASE_RT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| USES_CIR | VARCHAR2 | 30 |  |  | Flag to determine whether the rate information will be passed to elements or CIR |  |
| DIR_CARD_DEFINITION_ID | NUMBER |  | 18 |  | Payroll Card Definition Id- Foreign key to  pay_dir_card_definitions |  |
| DIR_CARD_COMP_DEF_ID | NUMBER |  | 18 |  | Payroll Component Definition Id- Foreign key to pay_dir_card_comp_defs_f |  |
| MAPPING_ID | NUMBER |  | 18 |  | Payroll Mapping Id- Foreign key to PAY_GI_MAPPINGS |  |
| VALUE_DEFINITION_BASE_NAME | VARCHAR2 | 128 |  |  | Base name of the Value Definition |  |
| EXTRA_VAL_DEF_RL | NUMBER |  | 18 |  | Extra Value Definition Rule- Foreign key to FF_FORMULAS_F |  |
| ALWS_RLVR_CRS_FLAG | VARCHAR2 | 30 |  |  | Rollover rate Y or N. |  |
| FLEX_PLC_HLDR_RATE_CD | VARCHAR2 | 30 |  |  | Flex Credit placeholder rate. |  |
| ADD_TO_PGM_POOL_FLAG | VARCHAR2 | 30 |  |  | Add to program pool flag Y or N. |  |
| ALWS_NGTV_USG_FLAG | VARCHAR2 | 30 |  |  | Allows overspending flag Y or N. |  |
| PCT_NGTV_USG_BY_TOTAL_POOL | NUMBER |  |  |  | Overspending limit as percent. |  |
| AUTO_ALCT_EXCS_FLAG | VARCHAR2 | 30 |  |  | Auto allocate excess credits Y or N. |  |
| EXCS_TRTMT_CD | VARCHAR2 | 30 |  |  | Excess credits treatment code. |  |
| EXCS_TRTMT_RL | NUMBER |  | 18 |  | Excess credits treatment formula. |  |
| CASH_DSTRBN_RSTRCN_CD | VARCHAR2 | 30 |  |  | Cash distribution limit code. |  |
| MN_CASH_DSTRBL_PCT | NUMBER |  |  |  | Min value allowed for cash distribution as percent. |  |
| MX_CASH_DSTRBL_PCT | NUMBER |  |  |  | Max value allowed for cash distribution as percent. |  |
| MN_CASH_DSTRBL_VAL | NUMBER |  |  |  | Min value allowed as cash distribution(amount). |  |
| MX_CASH_DSTRBL_VAL | NUMBER |  |  |  | Max value allowed as cash distribution (amount). |  |
| USES_NET_CRS_MTHD_FLAG | VARCHAR2 | 30 |  |  | USES_NET_CRS_MTHD_FLAG |  |
| MX_DFCIT_PCT_POOL_CRS_NUM | NUMBER |  |  |  | MX_DFCIT_PCT_POOL_CRS_NUM |  |
| MX_DFCIT_PCT_COMP_NUM | NUMBER |  |  |  | MX_DFCIT_PCT_COMP_NUM |  |
| CASH_RNDG_CD | VARCHAR2 | 30 |  |  | CASH_RNDG_CD |  |
| CASH_RNDG_RL | NUMBER |  | 18 |  | CASH_RNDG_RL |  |
| DFLT_EXCS_TRTMT_CD | VARCHAR2 | 30 |  |  | DFLT_EXCS_TRTMT_CD |  |
| DFLT_EXCS_TRTMT_RL | NUMBER |  | 18 |  | DFLT_EXCS_TRTMT_RL |  |
| EXCS_ALWYS_FFTD_FLAG | VARCHAR2 | 30 |  |  | EXCS_ALWYS_FFTD_FLAG |  |
| PGM_POOL_FLAG | VARCHAR2 | 30 |  |  | PGM_POOL_FLAG |  |
| USE_FOR_PGM_POOL_FLAG | VARCHAR2 | 30 |  |  | USE_FOR_PGM_POOL_FLAG |  |
| ALWS_NGTV_CRS_FLAG | VARCHAR2 | 30 |  |  | ALWS_NGTV_CRS_FLAG |  |
| RLOVR_RSTRCN_CD | VARCHAR2 | 30 |  |  | RLOVR_RSTRCN_CD |  |
| PCT_RNDG_CD | VARCHAR2 | 30 |  |  | PCT_RNDG_CD |  |
| PCT_RNDG_RL | NUMBER |  | 18 |  | PCT_RNDG_RL |  |
| VAL_RNDG_CD | VARCHAR2 | 30 |  |  | VAL_RNDG_CD |  |
| VAL_RNDG_RL | NUMBER |  | 18 |  | VAL_RNDG_RL |  |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  |  | Parent object identifier. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| ACTY_TYP_CD | VARCHAR2 | 30 |  |  | Activity type. |  |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |  |
| NAME | VARCHAR2 | 240 |  |  | Name of the activity base rate. |  |
| RT_TYP_CD | VARCHAR2 | 30 |  |  | Rate type. |  |
| BNFT_RT_TYP_CD | VARCHAR2 | 30 |  |  | Benefit rate type. |  |
| TX_TYP_CD | VARCHAR2 | 30 |  |  | Tax type. |  |
| USE_TO_CALC_NET_FLX_CR_FLAG | VARCHAR2 | 30 |  | Yes | Use to calculate net flexible credit Y or N. |  |
| ASN_ON_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | Assign on Enrollment Y or N. |  |
| ABV_MX_ELCN_VAL_ALWD_FLAG | VARCHAR2 | 30 |  | Yes | Indicates whether maximum elections value allowed Yor N. |  |
| BLW_MN_ELCN_ALWD_FLAG | VARCHAR2 | 30 |  | Yes | Below minimum elections allowed Y or N. |  |
| DSPLY_ON_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | Display on Enrollment Y or N. |  |
| PARNT_CHLD_CD | VARCHAR2 | 30 |  |  | Parent or child. |  |
| USE_CALC_ACTY_BS_RT_FLAG | VARCHAR2 | 30 |  | Yes | Use Calculation Activity Base Rate Y or N. |  |
| USES_DED_SCHED_FLAG | VARCHAR2 | 30 |  | Yes | Uses Deduction Schedule Y or N. |  |
| USES_VARBL_RT_FLAG | VARCHAR2 | 30 |  | Yes | Uses Variable Rate Y or N. |  |
| VSTG_SCHED_APLS_FLAG | VARCHAR2 | 30 |  | Yes | Vesting Schedule Applies Y or N. |  |
| RT_MLT_CD | VARCHAR2 | 30 |  |  | Rate multiply code. |  |
| PROC_EACH_PP_DFLT_FLAG | VARCHAR2 | 30 |  | Yes | Process Each Pay Period Default Y or N. |  |
| PRDCT_FLX_CR_WHEN_ELIG_FLAG | VARCHAR2 | 30 |  | Yes | Predict flexible credit when eligible Y or N. |  |
| NO_STD_RT_USED_FLAG | VARCHAR2 | 30 |  | Yes | No Standard Rate Used Y or N. |  |
| RCRRG_CD | VARCHAR2 | 30 |  |  | Recurring code. |  |
| MN_ELCN_VAL | NUMBER |  |  |  | Minimum election value. |  |
| MX_ELCN_VAL | NUMBER |  |  |  | Maximum election value. |  |
| USES_PYMT_SCHED_FLAG | VARCHAR2 | 30 |  | Yes | Uses Payment Schedule Y or N. |  |
| NNMNTRY_UOM | VARCHAR2 | 30 |  |  | Non-monentary unit of measure. |  |
| VAL | NUMBER |  |  |  | Value. |  |
| INCRMT_ELCN_VAL | NUMBER |  |  |  | Increment election value. |  |
| RNDG_CD | VARCHAR2 | 30 |  |  | Rounding code. |  |
| VAL_OVRID_ALWD_FLAG | VARCHAR2 | 30 |  | Yes | Value Override Allowed Y or N. |  |
| PRTL_MO_DET_MTHD_CD | VARCHAR2 | 30 |  |  | Partial month determination method. |  |
| ACTY_BASE_RT_STAT_CD | VARCHAR2 | 30 |  |  | Activity base rate status. |  |
| PROCG_SRC_CD | VARCHAR2 | 30 |  |  | Processing source. |  |
| DFLT_VAL | NUMBER |  |  |  | Default value. |  |
| DFLT_FLAG | VARCHAR2 | 30 |  | Yes | Default Y or N. |  |
| FRGN_ERG_DED_TYP_CD | VARCHAR2 | 30 |  |  | Foreign earnings or deduction. |  |
| FRGN_ERG_DED_NAME | VARCHAR2 | 180 |  |  | Foreign earnings deduction name. |  |
| FRGN_ERG_DED_IDENT | VARCHAR2 | 90 |  |  | Foreign earnings deduction identifier. |  |
| NO_MX_ELCN_VAL_DFND_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Election Value Defined Y or N. |  |
| PRTL_MO_DET_MTHD_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| ENTR_VAL_AT_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | Enter Value At Enrollment Y or N. |  |
| PRTL_MO_EFF_DT_DET_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| RNDG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| VAL_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| NO_MN_ELCN_VAL_DFND_FLAG | VARCHAR2 | 30 |  | Yes | No Minimum Election Value Defined Y or N. |  |
| PRTL_MO_EFF_DT_DET_CD | VARCHAR2 | 30 |  |  | Partial month effective date determination code. |  |
| ONLY_ONE_BAL_TYP_ALWD_FLAG | VARCHAR2 | 30 |  | Yes | Only One Balance Type Allowed Y or N. |  |
| ANN_MN_ELCN_VAL | NUMBER |  |  |  | Annual maximum election value. |  |
| ANN_MX_ELCN_VAL | NUMBER |  |  |  | Annual minimum election value. |  |
| ENTR_ANN_VAL_FLAG | VARCHAR2 | 30 |  | Yes | Enter Annual Value Y or N. |  |
| RT_USG_CD | VARCHAR2 | 30 |  |  | Rate usage. |  |
| LWR_LMT_VAL | NUMBER |  |  |  | Lower limit value. |  |
| LWR_LMT_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| UPR_LMT_VAL | NUMBER |  |  |  | Upper limit value. |  |
| UPR_LMT_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | Foreign key to PAY_ELEMENT_TYPES_F. |  |
| PGM_ID | NUMBER |  | 18 |  | Foreign key to BEN_PGM_F. |  |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |  |
| OIPL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OIPL_F. |  |
| PLIP_ID | NUMBER |  | 18 |  | Foreign key to BEN_PLIP_F. |  |
| PTIP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PTIP_F. |  |
| CMBN_PTIP_ID | NUMBER |  | 18 |  | Foreign key to BEN_CMBN_PTIP_F. |  |
| CMBN_PTIP_OPT_ID | NUMBER |  | 18 |  | Foreign key to BEN_CMBN_PTIP_OPT_F. |  |
| VSTG_FOR_ACTY_RT_ID | NUMBER |  | 18 |  | Foreign key to BEN_VSTG_FOR_ACTY_RT_F. |  |
| COMP_LVL_FCTR_ID | NUMBER |  | 18 |  | Foreign Key to BEN_COMP_LVL_FCTR_F. |  |
| PTD_COMP_LVL_FCTR_ID | NUMBER |  | 18 |  | Foreign key to BEN_PTD_COMP_LVL_FCTR_F. |  |
| CLM_COMP_LVL_FCTR_ID | NUMBER |  | 18 |  | Foreign Key to BEN_CLM_COMP_LVL_FCTR_F. |  |
| PARNT_ACTY_BASE_RT_ID | NUMBER |  | 18 |  | Foreign key to BEN_ACTY_BASE_RT_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| ABR_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| ABR_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rates Attributes (BEN_ACTY_BASE_RT_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | Foreign key to PAY_INPUT_VALUES_F. |  |
| SUBJ_TO_IMPTD_INCM_FLAG | VARCHAR2 | 30 |  |  | Subject To Imputed Income Y or N. |  |
| WSH_RL_DY_MO_NUM | NUMBER |  | 18 |  | Wash rule day of the month. |  |
| CMBN_PLIP_ID | NUMBER |  | 18 |  | Foreign key to BEN_CMBN_PLIP_F. |  |
| OIPLIP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OIPLIP_F. |  |
| ACTL_PREM_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTL_PREM_F. |  |
| ELE_RQD_FLAG | VARCHAR2 | 30 |  | Yes | Eligibility required Y or N. |  |
| ONE_ANN_PYMT_CD | VARCHAR2 | 30 |  |  | One annual payment code. |  |
| PRORT_MN_ANN_ELCN_VAL_CD | VARCHAR2 | 30 |  |  | Prorate minimum annual election value code. |  |
| PRORT_MN_ANN_ELCN_VAL_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| PRORT_MX_ANN_ELCN_VAL_CD | VARCHAR2 | 30 |  |  | Prorate maximum annual election value code. |  |
| PRORT_MX_ANN_ELCN_VAL_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| ASMT_TO_USE_CD | VARCHAR2 | 30 |  |  | Assignment to use. |  |
| DET_PL_YTD_CNTRS_CD | VARCHAR2 | 30 |  |  | Determine plan year to date contributions. |  |
| TTL_COMP_LVL_FCTR_ID | NUMBER |  | 18 |  | Foreign Key to BEN_COMP_LVL_FCTR. |  |
| COST_ALLOCATION_KEYFLEX_ID | NUMBER |  | 18 |  | Foreign Key To PAY_COST_ALLOCATION_KEYFLEX. |  |
| ALWS_CHG_CD | VARCHAR2 | 30 |  |  | Allows Change. |  |
| ELE_ENTRY_VAL_CD | VARCHAR2 | 30 |  |  | Element Entry Code. |  |
| OPT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OPT_F. |  |
| PL_TYP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_TYP_F |  |
| PAY_RATE_GRADE_RULE_ID | NUMBER |  | 18 |  | Grade point rate |  |
| INPUT_VA_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| ORDR_NUM | NUMBER |  | 18 |  | Order Number |  |
| SUB_ACTY_TYP_CD | VARCHAR2 | 30 |  |  | Sub Activity type Code. |  |
| RATE_PERIODIZATION_CD | VARCHAR2 | 30 |  |  | Rate Periodization Code |  |
| RATE_PERIODIZATION_RL | NUMBER |  |  |  | Rate Periodization Rule |  |
| MN_MX_ELCN_RL | NUMBER |  | 18 |  | Election Value Range Rule |  |
| MAPPING_TABLE_NAME | VARCHAR2 | 60 |  |  | Mapping Table Name |  |
| MAPPING_TABLE_PK_ID | NUMBER |  | 18 |  | Value of Primary Key column in the Mapping Table |  |
| CONTEXT_PGM_ID | NUMBER |  | 18 |  | CONTEXT_PGM_ID |  |
| CONTEXT_PL_ID | NUMBER |  | 18 |  | CONTEXT_PL_ID |  |
| CONTEXT_OPT_ID | NUMBER |  | 18 |  | CONTEXT_OPT_ID |  |
| CURRENCY_DET_CD | VARCHAR2 | 30 |  |  | Element Determination Rule to get the Element Type |  |
| ELEMENT_DET_RL | NUMBER |  | 18 |  | Determine  Currency for the Person Rates record |  |
| ABR_SEQ_NUM | NUMBER |  | 18 |  | ABR_SEQ_NUM |  |
| RATE_DISPLAY_CD | VARCHAR2 | 30 |  |  | Seeded lookup code with the values ???P???,???S??? and ???O??? will be used. |  |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template Id Field for future use. |  |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template Id Field for future use. |  |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template Id Field for future use. |  |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template Id Field for future use. |  |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template Id Field for future use. |  |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template Number Field for future use. |  |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template Number Field for future use. |  |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template Number Field for future use. |  |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template Number Field for future use. |  |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template Number Field for future use. |  |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template Char Field for future use. |  |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template Char Field for future use. |  |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template Char Field for future use. |  |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template Char Field for future use. |  |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template Char Field for future use. |  |
| CONFIG_DATE_1 | DATE |  |  |  | Template Date Field for future use. |  |
| CONFIG_DATE_2 | DATE |  |  |  | Template Date Field for future use. |  |
| CONFIG_DATE_3 | DATE |  |  |  | Template Date Field for future use. |  |
| CONFIG_DATE_4 | DATE |  |  |  | Template Date Field for future use. |  |
| CONFIG_DATE_5 | DATE |  |  |  | Template Date Field for future use. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| BEN_ACTY_BASE_RT_F_FK5 | Non Unique | Default | COMP_LVL_FCTR_ID |  |
| BEN_ACTY_BASE_RT_F_N1 | Non Unique | Default | ELEMENT_TYPE_ID |  |
| BEN_ACTY_BASE_RT_F_N14 | Non Unique | Default | PARNT_ACTY_BASE_RT_ID |  |
| BEN_ACTY_BASE_RT_F_N15 | Non Unique | Default | CMBN_PLIP_ID |  |
| BEN_ACTY_BASE_RT_F_N16 | Non Unique | Default | OIPLIP_ID |  |
| BEN_ACTY_BASE_RT_F_N17 | Non Unique | Default | ACTL_PREM_ID |  |
| BEN_ACTY_BASE_RT_F_N18 | Non Unique | Default | OPT_ID |  |
| BEN_ACTY_BASE_RT_F_N19 | Non Unique | Default | UPPER("NAME") |  |
| BEN_ACTY_BASE_RT_F_N2 | Non Unique | Default | PGM_ID |  |
| BEN_ACTY_BASE_RT_F_N20 | Non Unique | Default | OIPL_ID, PL_ID, PGM_ID, ACTY_BASE_RT_STAT_CD |  |
| BEN_ACTY_BASE_RT_F_N21 | Non Unique | Default | NAME, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |  |
| BEN_ACTY_BASE_RT_F_N22 | Non Unique | Default | MAPPING_ID |  |
| BEN_ACTY_BASE_RT_F_N3 | Non Unique | Default | PL_ID |  |
| BEN_ACTY_BASE_RT_F_N4 | Non Unique | Default | OIPL_ID | Obsolete |
| BEN_ACTY_BASE_RT_F_N5 | Non Unique | Default | PLIP_ID |  |
| BEN_ACTY_BASE_RT_F_N6 | Non Unique | Default | PTIP_ID |  |
| BEN_ACTY_BASE_RT_F_N7 | Non Unique | Default | CMBN_PTIP_ID |  |
| BEN_ACTY_BASE_RT_F_N8 | Non Unique | Default | CMBN_PTIP_OPT_ID |  |
| BEN_ACTY_BASE_RT_F_N9 | Non Unique | Default | VSTG_FOR_ACTY_RT_ID |  |
| BEN_ACTY_BASE_RT_F_PK | Unique | Default | ACTY_BASE_RT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |  |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
