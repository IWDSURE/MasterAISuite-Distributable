# BEN_PGM_F

BEN_PGM_F identifies the processing characteristics for a compensation program.  A program is a way to group plans together which are typically offered as a package of benefits to a group of people.  Attributes of the program which control  participation eligibility are logically inherited down to the plans which are defined to it,  this allows plan sponsors to establish plan definitions more easily and is a primary means of determining what plans should be put into a program.  Additionally, this table defines the standard unit of measure and reference period  for activity rates used by  the plans in the program.  
For example, Acme Flex Program, Acme Assigned Benefits for New Hires, Acme COBRA Program, Acme Executive Benefits Program.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpgmf-14790.html#benpgmf-14790](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpgmf-14790.html#benpgmf-14790)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PGM_F_PK | PGM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PGM_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| NAME | VARCHAR2 | 240 |  | Yes | This column holds Name of the program. |  |
| PGM_PRVDS_NO_AUTO_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | Program Provides No Automatic Enrollment Y or N. |  |
| PGM_PRVDS_NO_DFLT_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | Program Provides No Default Enrollment Y or N. |  |
| DPNT_DSGN_LVL_CD | VARCHAR2 | 30 |  |  | This column is used to store Dependent designation level. |  |
| PGM_STAT_CD | VARCHAR2 | 30 |  |  | This column is used to store Program status. |  |
| IVR_IDENT | VARCHAR2 | 90 |  |  | This column is used to store Interactive Voice Response identifier. |  |
| PGM_TYP_CD | VARCHAR2 | 30 |  |  | This column is used to store Program type. |  |
| ELIG_APLS_FLAG | VARCHAR2 | 30 |  | Yes | This column is used to store Eligibility applies Y or N. |  |
| PRTT_CHC_UNCRS_TRTMT_FLAG | VARCHAR2 | 30 |  |  | This column is used to store PRTT_CHC_UNCRS_TRTMT_FLAG |  |
| PGM_PRVDS_CR_FLAG | VARCHAR2 | 30 |  |  | This column is used to store PGM_PRVDS_CR_FLAG |  |
| PGM_DESC | VARCHAR2 | 2000 |  |  | This column is used to store Program description. |  |
| PRTN_ELIG_OVRID_ALWD_FLAG | VARCHAR2 | 30 |  | Yes | This column is used to store Participation Eligible Override Allowed Y or N. |  |
| PGM_USE_ALL_ASNTS_ELIG_FLAG | VARCHAR2 | 30 |  | Yes | This column is used to store Program uses all assignments for eligibility Y or N. |  |
| MX_DPNT_PCT_PRTT_LF_AMT | NUMBER |  |  |  | Maximum dependent percent of participant life insurance coverage amount. |  |
| MX_SPS_PCT_PRTT_LF_AMT | NUMBER |  |  |  | Maximum spouse percent of the  participant life insurance coverage amount. |  |
| ACTY_REF_PERD_CD | VARCHAR2 | 30 |  |  | This column is used to store Activity reference period. |  |
| COORD_CVG_FOR_ALL_PLS_FLG | VARCHAR2 | 30 |  | Yes | This column is used to store Coordinate coverage for all plans Y or N. |  |
| ENRT_CVG_END_DT_CD | VARCHAR2 | 30 |  |  | This column is used to store Enrollment coverage end date code. |  |
| ENRT_CVG_END_DT_RL | NUMBER |  | 18 |  | This column is used to store Foreign key to FF_FORMULAS_F. |  |
| DPNT_CVG_END_DT_CD | VARCHAR2 | 30 |  |  | This column is used to store Dependent coverage end date code. |  |
| DPNT_CVG_END_DT_RL | NUMBER |  | 18 |  | This column is used to store Foreign key to FF_FORMULAS_F. |  |
| DPNT_CVG_STRT_DT_CD | VARCHAR2 | 30 |  |  | This column is used to store Dependent coverage start date code. |  |
| DPNT_CVG_STRT_DT_RL | NUMBER |  | 18 |  | This column is used to store Foreign key to FF_FORMULAS_F. |  |
| DPNT_DSGN_NO_CTFN_RQD_FLAG | VARCHAR2 | 30 |  | Yes | This column is used to store Dependent designation certification required Y or N. |  |
| DRVBL_FCTR_DPNT_ELIG_FLAG | VARCHAR2 | 30 |  | Yes | This column is used to store Derivable factors for dependent eligibility Y or N. |  |
| DRVBL_FCTR_PRTN_ELIG_FLAG | VARCHAR2 | 30 |  | Yes | This column is used to store Derivable factors for participation eligibility Y or N. |  |
| ENRT_CVG_STRT_DT_CD | VARCHAR2 | 30 |  |  | This column is used to store Enrollment coverage start date code. |  |
| ENRT_CVG_STRT_DT_RL | NUMBER |  | 18 |  | This column is used to store Foreign key to FF_FORMULAS_F. |  |
| ENRT_INFO_RT_FREQ_CD | VARCHAR2 | 30 |  |  | This column is used to store Enrollment information rate frequency. |  |
| RT_STRT_DT_CD | VARCHAR2 | 30 |  |  | This column is used to store Rate start date code. |  |
| RT_STRT_DT_RL | NUMBER |  | 18 |  | This column is used to store Foreign key to FF_FORMULAS_F. |  |
| RT_END_DT_CD | VARCHAR2 | 30 |  |  | This column is used to store Rate end date code. |  |
| RT_END_DT_RL | NUMBER |  | 18 |  | This column is used to store Foreign key to FF_FORMULAS_F. |  |
| PGM_GRP_CD | VARCHAR2 | 30 |  |  | This column is used to store Program group. |  |
| PGM_UOM | VARCHAR2 | 30 |  |  | This column is used to store Program unit of measure. |  |
| DRVBL_FCTR_APLS_RTS_FLAG | VARCHAR2 | 30 |  | Yes | This column is used to store Derivable factors apply to rates Y or N. |  |
| TRK_INELIG_PER_FLAG | VARCHAR2 | 30 |  | Yes | This column is used to store Track Ineligible Person Y or N. |  |
| ENRT_CD | VARCHAR2 | 30 |  |  | This column is used to store Enrollment code. |  |
| ENRT_MTHD_CD | VARCHAR2 | 30 |  |  | This column is used to store Enrollment method. |  |
| AUTO_ENRT_MTHD_RL | NUMBER |  | 18 |  | This column is used to store Foreign key to FF_FORMULAS_F. |  |
| ENRT_RL | NUMBER |  | 18 |  | This column is used to store Foreign key to FF_FORMULAS_F. |  |
| ALWS_UNRSTRCTD_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | This column is used to store Allows Unrestricted Enrollment Y or N. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | This column is used to store Foreign Key to HR_ORGANIZATION_UNITS |  |
| PGM_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| PGM_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Program Attributes (BEN_PGM_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| USES_ALL_ASMTS_FOR_RTS_FLAG | VARCHAR2 | 30 |  | Yes | Uses All Assignments For Rates Y or N. |  |
| URL_REF_NAME | VARCHAR2 | 240 |  |  | This column is used to store URL reference name. |  |
| POE_LVL_CD | VARCHAR2 | 30 |  |  | This column is used to store Period of enrollment level. |  |
| VRFY_FMLY_MMBR_CD | VARCHAR2 | 30 |  |  | This column is used to store Verify family member code |  |
| VRFY_FMLY_MMBR_RL | NUMBER |  | 18 |  | This column is used to store Foreign key to FF_FORMULAS_F. |  |
| PER_CVRD_CD | VARCHAR2 | 30 |  |  | This column is used to store Person covered code. |  |
| SHORT_CODE | VARCHAR2 | 30 |  |  | This column is used to store Short Code |  |
| SHORT_NAME | VARCHAR2 | 30 |  |  | This column is used to store short Name |  |
| DFLT_ELEMENT_TYPE_ID | NUMBER |  | 18 |  | This column is used to store Default Salary Element |  |
| DFLT_INPUT_VALUE_ID | NUMBER |  | 18 |  | This column is used to store Default input value of salary element |  |
| DFLT_PGM_FLAG | VARCHAR2 | 30 |  | Yes | This column is used to store Default Grade Ladder Flag |  |
| DFLT_STEP_CD | VARCHAR2 | 30 |  |  | This column is used to store Default Step a Employee is placed |  |
| DFLT_STEP_RL | NUMBER |  | 18 |  | This column is used to store Default Step Rule |  |
| SCORES_CALC_MTHD_CD | VARCHAR2 | 30 |  |  | This column is used to store Employee score calculation method |  |
| SCORES_CALC_RL | NUMBER |  | 18 |  | This column is used to store Employee score calculation rule |  |
| UPDATE_SALARY_CD | VARCHAR2 | 30 |  |  | This column is used to store Salary Updation method code |  |
| USE_MULTI_PAY_RATES_FLAG | VARCHAR2 | 30 |  | Yes | Allow multiple rates for grades and steps |  |
| USE_PROG_POINTS_FLAG | VARCHAR2 | 30 |  | Yes | This column is used to store Use Progression Points Flag |  |
| USE_SCORES_CD | VARCHAR2 | 30 |  |  | This column is used to store Use Scores to rank employees |  |
| SALARY_CALC_MTHD_CD | VARCHAR2 | 30 |  |  | This column is used to store Salary Calculation Method Code |  |
| SALARY_CALC_MTHD_RL | NUMBER |  | 18 |  | This column is used to store Salary Calculation Method Rule |  |
| GSP_ALLOW_OVERRIDE_FLAG | VARCHAR2 | 30 |  | Yes | This column is used to store Grade Step Override Flag Y or N |  |
| USE_VARIABLE_RATES_FLAG | VARCHAR2 | 30 |  | Yes | This column is used to store Grade Step Use Variable Rates Flag |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | This column is used to store Foreign key to FND_TERRITORIES. |  |
| LEGISLATION_SUBGROUP | VARCHAR2 | 30 |  |  | Further identifies the legislation of startup data. |  |
| GLOBAL_FLAG | VARCHAR2 | 30 |  |  | This column indicates exposure to legal entities. |  |
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
| PGM_INFO | BLOB |  |  |  | This column holds additional information of the program. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PGM_F_N5 | Non Unique | Default | UPPER("NAME") |
| BEN_PGM_F_PK | Unique | Default | PGM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
