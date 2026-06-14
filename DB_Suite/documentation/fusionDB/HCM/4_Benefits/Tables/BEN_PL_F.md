# BEN_PL_F

BEN_PL_F identifies a discrete and formally defined compensation offering which is categorized by only one plan type, has one or more activity base rates, shares a known set of eligibility criteria and when applicable, has a fixed set of provided option. For health and welfare benefits, a plan is provided by a  third-party administrator or carrier.   Plan has a number of columns which are prefixed with "NIP," indicating not in program, such columns are used only when the plan is not incorporated into a program,all the remaining attributes apply to the characteristics of the plan either independent of any program affinity or in the context of the program. Examples are  Acme Be Well HMO,Acme Stock Purchase Plan, Acme HQ Employee Savings Plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplf-19719.html#benplf-19719](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplf-19719.html#benplf-19719)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_F_PK | PL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| PAYROLL_MAPPING_LEVEL | VARCHAR2 | 30 |  |  | Will determine if Payroll Component Info should be captured at Plan Level or OIPL Level. |  |
| USES_CIR | VARCHAR2 | 30 |  |  | Flag to determine whether the rate information will be passed to elements or CIR |  |
| CONFIG_ID_10 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_9 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_8 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_7 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_6 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_CHAR_10 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_9 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_7 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_8 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_6 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_NUM_10 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_9 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_8 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_7 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_6 | NUMBER |  |  |  | Template number field for future use. |  |
| PL_CAT | VARCHAR2 | 100 |  |  | Plan Category |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the plan. |  |
| ALWS_QDRO_FLAG | VARCHAR2 | 30 |  | Yes | Allows QDRO Y or N. |  |
| ALWS_QMCSO_FLAG | VARCHAR2 | 30 |  | Yes | Allows QMSCO Y or N. |  |
| ALWS_REIMBMTS_FLAG | VARCHAR2 | 30 |  | Yes | Allows reimbursements Y or N. |  |
| ASNT_RQD_FOR_ENRT_FLAG | VARCHAR2 | 30 |  |  | ASNT_RQD_FOR_ENRT_FLAG |  |
| BNF_ADDL_INSTN_ALWD_FLAG | VARCHAR2 | 30 |  | Yes | Beneficiary additional instruction text allowed Y or N. |  |
| BNF_ADRS_RQD_FLAG | VARCHAR2 | 30 |  | Yes | Benficiary Address Required Y or N. |  |
| BNF_CNTNGT_BNFS_ALWD_FLAG | VARCHAR2 | 30 |  | Yes | Beneficiary continuing benefits Allowed Y or N. |  |
| BNF_CTFN_RQD_FLAG | VARCHAR2 | 30 |  | Yes | Beneficiary certification required Y or N. |  |
| BNF_DOB_RQD_FLAG | VARCHAR2 | 30 |  | Yes | Beneficiary date of birth required Y or N. |  |
| BNF_DSGE_MNR_TTEE_RQD_FLAG | VARCHAR2 | 30 |  | Yes | Beneficiary designee minor,trustee required Y or N. |  |
| BNF_INCRMT_AMT | NUMBER |  |  |  | Beneficiary increment amount. |  |
| BNF_DFLT_BNF_CD | VARCHAR2 | 30 |  |  | Default beneficiary. |  |
| BNF_LEGV_ID_RQD_FLAG | VARCHAR2 | 30 |  | Yes | Beneficiary legislative identifier required Y or N. |  |
| BNF_MAY_DSGT_ORG_FLAG | VARCHAR2 | 30 |  | Yes | Beneficiary may designate organization Y or N. |  |
| BNF_MN_DSGNTBL_AMT | NUMBER |  |  |  | Beneficiary minimum designatable amount. |  |
| BNF_MN_DSGNTBL_PCT_VAL | NUMBER |  | 15 |  | Beneficiary minimum designatable percentage. |  |
| BNF_PCT_INCRMT_VAL | NUMBER |  | 15 |  | Beneficiary increment percent. |  |
| BNF_PCT_AMT_ALWD_CD | VARCHAR2 | 30 |  |  | Beneficiary percentage amount allowed. |  |
| BNF_QDRO_RL_APLS_FLAG | VARCHAR2 | 30 |  | Yes | Benficiary QDRO rule applies Y or N. |  |
| DFLT_TO_ASN_PNDG_CTFN_CD | VARCHAR2 | 30 |  |  | Default to assign pending notification code. |  |
| DFLT_TO_ASN_PNDG_CTFN_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| DRVBL_FCTR_APLS_RTS_FLAG | VARCHAR2 | 30 |  | Yes | Derivable factors apply to rates Y or N. |  |
| DRVBL_FCTR_PRTN_ELIG_FLAG | VARCHAR2 | 30 |  | Yes | Derivable factors for participation eligibility Y or N. |  |
| ELIG_APLS_FLAG | VARCHAR2 | 30 |  | Yes | Eligibility applies Y or N. |  |
| INVK_DCLN_PRTN_PL_FLAG | VARCHAR2 | 30 |  | Yes | Invoke Decline Participation Plan Y or N. |  |
| INVK_FLX_CR_PL_FLAG | VARCHAR2 | 30 |  | Yes | Invoke Flexible Credit Plan Y or N. |  |
| INVK_IMPTD_INCM_PL_FLAG | VARCHAR2 | 30 |  |  | INVK_IMPTD_INCM_PL_FLAG |  |
| DRVBL_DPNT_ELIG_FLAG | VARCHAR2 | 30 |  | Yes | Derivable dependant eligiblility flag Y or N. |  |
| TRK_INELIG_PER_FLAG | VARCHAR2 | 30 |  | Yes | Track Ineligible Person Y or N. |  |
| PL_CD | VARCHAR2 | 30 |  | Yes | Plan usage. |  |
| AUTO_ENRT_MTHD_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| IVR_IDENT | VARCHAR2 | 90 |  |  | Interactive Voice Response identifier. |  |
| CMPR_CLMS_TO_CVG_OR_BAL_CD | VARCHAR2 | 30 |  |  | Compare claims to coverage or balance. |  |
| COBRA_PYMT_DUE_DY_NUM_CD | VARCHAR2 | 30 |  |  | COBRA_PYMT_DUE_DY_NUM_CD |  |
| DMSTC_PRTR_RT_TRTMT_FLAG | VARCHAR2 | 30 |  |  | DMSTC_PRTR_RT_TRTMT_FLAG |  |
| DPNT_CVD_BY_OTHR_APLS_FLAG | VARCHAR2 | 30 |  | Yes | Dependent covered by other plan Y or N. |  |
| ENRT_MTHD_CD | VARCHAR2 | 30 |  |  | Enrollment method. |  |
| ENRT_CD | VARCHAR2 | 30 |  |  | Enrollment code. |  |
| ENRT_CVG_STRT_DT_CD | VARCHAR2 | 30 |  |  | Enrollment coverage start date code. |  |
| ENRT_CVG_END_DT_CD | VARCHAR2 | 30 |  |  | Enrollment coverage end date code. |  |
| FRFS_APLY_FLAG | VARCHAR2 | 30 |  | Yes | Payment to meet minimum standards under the Affordable Care Act in the US Y or N. |  |
| HC_PL_SUBJ_HCFA_APRVL_FLAG | VARCHAR2 | 30 |  | Yes | Health care plan subject to health care finance administration approval Y or N. |  |
| HGHLY_CMPD_RL_APLS_FLAG | VARCHAR2 | 30 |  | Yes | Highly Compensated Rule Applies Y or N. |  |
| INCPTN_DT | DATE |  |  |  | Inception date. |  |
| MN_CVG_RQD_AMT | NUMBER |  |  |  | Minimum required coverage amount. |  |
| MN_OPTS_RQD_NUM | NUMBER |  | 18 |  | Minimum number of required options. |  |
| MX_CVG_ALWD_AMT | NUMBER |  |  |  | Maximum coverage allowed amount. |  |
| MX_OPTS_ALWD_NUM | NUMBER |  | 18 |  | Maximum number of options allowed. |  |
| MX_CVG_WCFN_MLT_NUM | NUMBER |  | 18 |  | Maximum coverage with certification multiple number. |  |
| MX_CVG_WCFN_AMT | NUMBER |  |  |  | Maximum coverage with certification amount. |  |
| MX_CVG_INCR_ALWD_AMT | NUMBER |  |  |  | Maximum coverage increase allowed amount. |  |
| MX_CVG_INCR_WCF_ALWD_AMT | NUMBER |  |  |  | Maximum coverage increase with certification allowed amount. |  |
| MX_CVG_MLT_INCR_NUM | NUMBER |  | 18 |  | Maximum coverage multiple increase number. |  |
| MX_CVG_MLT_INCR_WCF_NUM | NUMBER |  | 18 |  | Maximum coverage multiple increase with certification number. |  |
| MX_WTG_DT_TO_USE_CD | VARCHAR2 | 30 |  |  | Maximum waiting period date to use code. |  |
| MX_WTG_DT_TO_USE_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| MX_WTG_PERD_PRTE_APLS_FLAG | VARCHAR2 | 30 |  |  | MX_WTG_PERD_PRTE_APLS_FLAG |  |
| MX_WTG_PERD_PRTE_DET_CD | VARCHAR2 | 30 |  |  | MX_WTG_PERD_PRTE_DET_CD |  |
| MX_WTG_PERD_PRTE_DET_RL | NUMBER |  | 18 |  | MX_WTG_PERD_PRTE_DET_RL |  |
| MX_WTG_PERD_PRTE_UOM | VARCHAR2 | 30 |  |  | Maximum waiting period to participate unit of measure. |  |
| MX_WTG_PERD_PRTE_VAL | NUMBER |  | 15 |  | Maximum waiting period to participate value. |  |
| NIP_DFLT_ENRT_CD | VARCHAR2 | 30 |  |  | Not in program default enrollment code. |  |
| NIP_DFLT_ENRT_DET_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| DPNT_CVG_END_DT_CD | VARCHAR2 | 30 |  |  | Dependent coverage end date code. |  |
| DPNT_CVG_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| DPNT_CVG_STRT_DT_CD | VARCHAR2 | 30 |  |  | Dependent coverage start date code. |  |
| DPNT_CVG_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| DPNT_LEG_ID_RQD_FLAG | VARCHAR2 | 30 |  | Yes | Dependent Legislative Identifier required Y or N. |  |
| DPNT_NO_CTFN_RQD_FLAG | VARCHAR2 | 30 |  | Yes | Dependent no certification required Y or N. |  |
| NO_MN_OPTS_NUM_APLS_FLAG | VARCHAR2 | 30 |  | Yes | No Minimum Options Number Applies Y or N. |  |
| NO_MX_OPTS_NUM_APLS_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Options Number Applies Y or N. |  |
| NIP_PL_UOM | VARCHAR2 | 30 |  |  | Not in program plan unit of measure. |  |
| NIP_ACTY_REF_PERD_CD | VARCHAR2 | 30 |  |  | Not in program activity reference period. |  |
| NIP_RQD_ENRL_PERD_TCO_CD | VARCHAR2 | 30 |  |  | NIP_RQD_ENRL_PERD_TCO_CD |  |
| NIP_ENRT_INFO_RT_FREQ_CD | VARCHAR2 | 30 |  |  | Not in program enrollment information rate frequency. |  |
| PER_CVRD_CD | VARCHAR2 | 30 |  |  | Person covered code. |  |
| ENRT_CVG_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| POSTELCN_EDIT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| ENRT_CVG_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| PRORT_PRTL_YR_CVG_RSTRN_CD | VARCHAR2 | 30 |  |  | Prorate partial year coverage restriction code. |  |
| PRORT_PRTL_YR_CVG_RSTRN_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| PRTN_ELIG_OVRID_ALWD_FLAG | VARCHAR2 | 30 |  | Yes | Participation Eligible Override Allowed Y or N. |  |
| SVGS_PL_FLAG | VARCHAR2 | 30 |  | Yes | Savings Plan Y or N. |  |
| SUBJ_TO_IMPUT_INC_FLAG | VARCHAR2 | 30 |  |  | SUBJ_TO_IMPUT_INC_FLAG |  |
| USE_ALL_ASNTS_ELIG_FLAG | VARCHAR2 | 30 |  | Yes | Use All Assignments Eligible Y or N. |  |
| USE_ALL_ASNTS_FOR_RT_FLAG | VARCHAR2 | 30 |  | Yes | Use All Assignments For Rate Y or N. |  |
| VSTG_APLS_FLAG | VARCHAR2 | 30 |  | Yes | Vesting Applies Y or N. |  |
| WVBL_FLAG | VARCHAR2 | 30 |  | Yes | Waivable Y or N. |  |
| HC_SVC_TYP_CD | VARCHAR2 | 30 |  |  | Healthcare service type. |  |
| PL_STAT_CD | VARCHAR2 | 30 |  |  | Plan status. |  |
| PRMRY_FNDG_MTHD_CD | VARCHAR2 | 30 |  |  | Primary funding method. |  |
| RT_END_DT_CD | VARCHAR2 | 30 |  |  | Rate end date code. |  |
| RT_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| RT_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| RT_STRT_DT_CD | VARCHAR2 | 30 |  |  | Rate start date code. |  |
| ENRL_PL_OPT_FLAG | VARCHAR2 | 30 |  |  | ENRL_PL_OPT_FLAG |  |
| ENRT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| MAY_ENRL_PL_N_OIPL_FLAG | VARCHAR2 | 30 |  | Yes | May Enroll Plan And Option in Plan Y or N. |  |
| RQD_PERD_ENRT_NENRT_UOM | VARCHAR2 | 30 |  |  | Required period of enrollment unit of measure. |  |
| RQD_PERD_ENRT_NENRT_VAL | NUMBER |  |  |  | Required period of enrollment value. |  |
| RQD_PERD_ENRT_NENRT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |  |
| ALWS_UNRSTRCTD_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | Allows Unrestricted Enrollment Y or N. |  |
| BNFT_R_OPT_RSTRN_CD | VARCHAR2 | 30 |  |  | BNFT_R_OPT_RSTRN_CD |  |
| CVG_INCR_R_DECR_ONLY_CD | VARCHAR2 | 30 |  |  | Coverage increment or decrement only. |  |
| PL_TYP_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PL_TYP_F. |  |
| ACTL_PREM_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTL_PREM_F. |  |
| BNFT_PRVDR_POOL_ID | NUMBER |  | 18 |  | Foreign key to BEN_BNFT_PRVDR_POOL_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| PLN_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| PLN_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan Attributes (BEN_PL_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ENRT_PL_OPT_FLAG | VARCHAR2 | 30 |  | Yes | Enrollment Plan Option Y or N. |  |
| BNFT_OR_OPTION_RSTRCTN_CD | VARCHAR2 | 30 |  |  | Benefit or option restriction. |  |
| MN_CVG_ALWD_AMT | NUMBER |  |  |  | Minimum coverage allowed amount. |  |
| SUBJ_TO_IMPTD_INCM_CD | VARCHAR2 | 30 |  |  | Minimum coverage to avoid the fee for not having insurance under the Affordable Care Act in the US Y or N. |  |
| SUBJ_TO_IMPTD_INCM_TYP_CD | VARCHAR2 | 30 |  |  | Subject to imputed income type. |  |
| URL_REF_NAME | VARCHAR2 | 240 |  |  | URL reference name. |  |
| UNSSPND_ENRT_CD | VARCHAR2 | 30 |  |  | Unsuspended enrollment code. |  |
| IMPTD_INCM_CALC_CD | VARCHAR2 | 30 |  |  | No longer used. |  |
| PLN_MN_CVG_ALWD_AMT | NUMBER |  |  |  | Plan minimum coverage allowed amount. |  |
| PCP_CD | VARCHAR2 | 30 |  |  | No longer used. |  |
| MX_WTG_PERD_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| COBRA_PYMT_DUE_DY_NUM | NUMBER |  | 18 |  | Cobra payment due day. |  |
| CR_DSTR_BNFT_PRVDR_POOL_ID | NUMBER |  | 18 |  | Foreign key to BEN_CR_DSTR_BNFT_PRVDR_POOL_F. |  |
| NIP_DFLT_FLAG | VARCHAR2 | 30 |  | Yes | Not in Plan Default Flag Y or N. |  |
| VRFY_FMLY_MMBR_CD | VARCHAR2 | 30 |  |  | Verify family member code |  |
| VRFY_FMLY_MMBR_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| ALWS_TMPRY_ID_CRD_FLAG | VARCHAR2 | 30 |  | Yes | Allows Temporary ID Card Y or N. |  |
| FRFS_DISTR_MTHD_CD | VARCHAR2 | 30 |  |  | Forfeiture distribution method code |  |
| FRFS_DISTR_MTHD_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| FRFS_CNTR_DET_CD | VARCHAR2 | 30 |  |  | Forfeitures contribution determination code. |  |
| FRFS_DISTR_DET_CD | VARCHAR2 | 30 |  |  | Forfeitures distribution determination code. |  |
| COST_ALLOC_KEYFLEX_1_ID | NUMBER |  | 18 |  | Foreign Key to PAY_COST_ALLOCATION_KEYFLEX. |  |
| COST_ALLOC_KEYFLEX_2_ID | NUMBER |  | 18 |  | Foreign Key to PAY_COST_ALLOCATION_KEYFLEX. |  |
| POST_TO_GL_FLAG | VARCHAR2 | 30 |  | Yes | Post to General Ledger Flag. |  |
| FRFS_VAL_DET_CD | VARCHAR2 | 30 |  |  | Forfeiure value detemination code. |  |
| FRFS_MX_CRYFWD_VAL | NUMBER |  |  |  | Maximum forfeiture carry-forward value. |  |
| FRFS_PORTION_DET_CD | VARCHAR2 | 30 |  |  | Forfeiture portion deteermination code. |  |
| BNDRY_PERD_CD | VARCHAR2 | 30 |  |  | Boundary period code. |  |
| SHORT_CODE | VARCHAR2 | 30 |  |  | Short Code |  |
| SHORT_NAME | VARCHAR2 | 30 |  |  | short Name |  |
| FUNCTION_CODE | VARCHAR2 | 30 |  |  | Function Code |  |
| MAPPING_TABLE_NAME | VARCHAR2 | 60 |  |  | Mapping table Name |  |
| MAPPING_TABLE_PK_ID | NUMBER |  |  |  | Mapping table primary key id |  |
| PL_YR_NOT_APPLCBL_FLAG | VARCHAR2 | 30 |  | Yes | Plan year periods not applicable flag |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| LEGISLATION_SUBGROUP | VARCHAR2 | 30 |  |  | Further identifies the legislation of startup data. |  |
| GROUP_PL_ID | NUMBER |  | 18 |  | Group plan id. |  |
| USE_CSD_RSD_PRCCNG_CD | VARCHAR2 | 30 |  |  | User Coverage and/or Rate Start Date for Processing |  |
| SUSP_IF_CTFN_NOT_PRVD_FLAG | VARCHAR2 | 30 |  | Yes | Suspend Enrollment if Certification not provided |  |
| SUSP_IF_CTFN_NOT_BNF_FLAG | VARCHAR2 | 30 |  | Yes | Suspend Enrollment if Certification for Dependent |  |
| BNF_CTFN_DETERMINE_CD | VARCHAR2 | 30 |  |  | Dependent Certification Determination code |  |
| GLOBAL_FLAG | VARCHAR2 | 30 |  |  | Indicates exposure to legal entities. |  |
| CVG_AMT_LMT_RL | NUMBER |  |  |  | CVG_AMT_LMT_RL |  |
| CVG_MLT_LMT_RL | NUMBER |  |  |  | CVG_MLT_LMT_RL |  |
| MN_CVG_RQD_MLT_NUM | NUMBER |  |  |  | MN_CVG_RQD_MLT_NUM |  |
| MX_CVG_ALWD_MLT_NUM | NUMBER |  |  |  | MX_CVG_ALWD_MLT_NUM |  |
| UNSSPND_ENRT_RL | NUMBER |  |  |  | UNSSPND_ENRT_RL |  |
| UNSSPND_RT_CD | VARCHAR2 | 30 |  |  | UNSSPND_RT_CD |  |
| UNSSPND_RT_RL | NUMBER |  |  |  | UNSSPND_RT_RL |  |
| DSGN_SELF_AS_BNF_FLAG | VARCHAR2 | 30 |  |  | Allow creation of Self Beneficiaries from benmngle only when the above flag is set to Yes. |  |
| CARRIER_ID | NUMBER |  | 18 |  | Identifies plan carrier |  |
| CARRIER_PL_NAME | VARCHAR2 | 240 |  |  | Carrier plan name. |  |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |  |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |  |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use. |  |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use. |  |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use. |  |
| SNRTY_CONFIG_ID | NUMBER |  | 18 |  | Worker Seniority Date |  |
| PL_INFO | BLOB |  |  |  | This column holds additional information of the plan. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_F_FK4 | Non Unique | Default | GROUP_PL_ID |
| BEN_PL_F_N1 | Non Unique | Default | UPPER("NAME") |
| BEN_PL_F_N2 | Non Unique | Default | BNFT_PRVDR_POOL_ID |
| BEN_PL_F_N3 | Non Unique | Default | CR_DSTR_BNFT_PRVDR_POOL_ID |
| BEN_PL_F_N4 | Non Unique | Default | ACTL_PREM_ID |
| BEN_PL_F_N5 | Non Unique | Default | MAPPING_TABLE_NAME |
| BEN_PL_F_N6 | Non Unique | Default | PL_TYP_ID |
| BEN_PL_F_PK | Unique | Default | PL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
