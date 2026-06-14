# BEN_LE_CLSN_N_RSTR

BEN_LE_CLSN_N_RSTR  is a processing table and contains the information about persons and life events who have been backed out due to an overriding/winning life eventt, where the backed out information is not maintainable on the originating table.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benleclsnnrstr-12313.html#benleclsnnrstr-12313](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benleclsnnrstr-12313.html#benleclsnnrstr-12313)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LE_CLSN_N_RSTR_PK | BKUP_TBL_ID, BKUP_TBL_TYP_CD, OBJECT_VERSION_NUMBER |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BKUP_TBL_ID | NUMBER |  | 18 | Yes | Foreign key Identifier of Record being backed up. |
| BKUP_TBL_TYP_CD | VARCHAR2 | 30 |  | Yes | Backup table type. |
| PER_IN_LER_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_PER_IN_LER. |
| EFFECTIVE_START_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ENRT_CVG_STRT_DT | DATE |  |  |  | Enrollment coverage start date. |
| ENRT_CVG_THRU_DT | DATE |  |  |  | Enrollment coverage through date. |
| BNFT_AMT | NUMBER |  |  |  | Amount. |
| BNFT_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | Non-monetary unit of measure. |
| BNFT_ORDR_NUM | NUMBER |  | 30 |  | Order number. |
| BNFT_TYP_CD | VARCHAR2 | 30 |  |  | Benefit type. |
| COMP_LVL_CD | VARCHAR2 | 30 |  |  | Compensation level. |
| ENRT_MTHD_CD | VARCHAR2 | 30 |  |  | Enrollment method. |
| ENRT_OVRID_RSN_CD | VARCHAR2 | 30 |  |  | Enrollment override reason. |
| ENRT_OVRID_THRU_DT | DATE |  |  |  | Enrollment override through date. |
| ENRT_OVRIDN_FLAG | VARCHAR2 | 30 |  |  | Enrollment Overriden Y or N. |
| ERLST_DEENRT_DT | DATE |  |  |  | Earliest de-enrollment date. |
| NO_LNGR_ELIG_FLAG | VARCHAR2 | 30 |  |  | No Longer Eligible Y or N. |
| ORGNL_ENRT_DT | DATE |  |  |  | Original enrollment date. |
| PRTT_ENRT_RSLT_STAT_CD | VARCHAR2 | 30 |  |  | Participant enrollment result status. |
| PRTT_IS_CVRD_FLAG | VARCHAR2 | 30 |  |  | Participant Is Covered Y or N. |
| SSPNDD_FLAG | VARCHAR2 | 30 |  |  | Suspended Y or N. |
| UOM | VARCHAR2 | 30 |  |  | Unit of measure. |
| ADDL_INSTRN_TXT | VARCHAR2 | 2000 |  |  | Additional instructions. |
| AMT_DSGD_VAL | NUMBER |  |  |  | Amount designated value. |
| AMT_DSGD_UOM | VARCHAR2 | 30 |  |  | Amount designated unit of measure. |
| DSGN_STRT_DT | DATE |  |  |  | Designation start date. |
| DSGN_THRU_DT | DATE |  |  |  | Designation through date. |
| PCT_DSGD_NUM | NUMBER |  |  |  | Percent designated. |
| PRMRY_CNTNGNT_CD | VARCHAR2 | 30 |  |  | Primary or contingent beneficiary. |
| CVG_PNDG_FLAG | VARCHAR2 | 30 |  |  | Coverage pending Y or N. |
| CVRD_FLAG | VARCHAR2 | 30 |  |  | Covered Y or N. |
| ELIG_FLAG | VARCHAR2 | 30 |  |  | Eligible Y or N. |
| OVRDN_FLAG | VARCHAR2 | 30 |  |  | Overridden Y or N. |
| CVG_STRT_DT | DATE |  |  |  | Coverage start date. |
| CVG_THRU_DT | DATE |  |  |  | Coverage through date. |
| ELIG_STRT_DT | DATE |  |  |  | Eligibility start date. |
| ELIG_THRU_DT | DATE |  |  |  | Eligibility through date. |
| OVRDN_THRU_DT | DATE |  |  |  | Overridden through date. |
| RT_STRT_DT | DATE |  |  |  | Rate start date. |
| RT_END_DT | DATE |  |  |  | Rate end date. |
| DSPLY_ON_ENRT_FLAG | VARCHAR2 | 30 |  |  | Display on Enrollment Y or N. |
| RT_OVRIDN_FLAG | VARCHAR2 | 30 |  |  | Rate Overriden Y or N. |
| ACTY_REF_PERD_CD | VARCHAR2 | 30 |  |  | Activity reference period. |
| ACTY_TYP_CD | VARCHAR2 | 30 |  |  | Activity type. |
| ANN_RT_VAL | NUMBER |  |  |  | Annual rate. |
| BNFT_RT_TYP_CD | VARCHAR2 | 30 |  |  | Benefit rate type. |
| CMCD_REF_PERD_CD | VARCHAR2 | 30 |  |  | Communicated reference period. |
| CMCD_RT_VAL | NUMBER |  |  |  | Communicated rate value. |
| ELCNS_MADE_DT | DATE |  |  |  | Elections made date. |
| MLT_CD | VARCHAR2 | 30 |  |  | Multiply code. |
| PRTT_RT_VAL_STAT_CD | VARCHAR2 | 30 |  |  | Participant rate value status. |
| RT_OVRIDN_THRU_DT | DATE |  |  |  | Rate overriden through date. |
| RT_VAL | NUMBER |  |  |  | Rate value. |
| TX_TYP_CD | VARCHAR2 | 30 |  |  | Tax type. |
| INELG_RSN_CD | VARCHAR2 | 30 |  |  | Ineligible reason. |
| RT_COMP_REF_AMT | NUMBER |  |  |  | Rate compensation reference amount. |
| RT_CMBN_AGE_N_LOS_VAL | NUMBER |  |  |  | Rate combination age and length of service value. |
| RT_COMP_REF_UOM | VARCHAR2 | 30 |  |  | Rate compensation reference unit of measure. |
| RT_AGE_VAL | NUMBER |  |  |  | Rate age value. |
| RT_LOS_VAL | NUMBER |  |  |  | Rate length of service value. |
| RT_HRS_WKD_VAL | NUMBER |  |  |  | Rate hours worked value. |
| RT_HRS_WKD_BNDRY_PERD_CD | VARCHAR2 | 30 |  |  | Rate hours worked boundary period. |
| RT_AGE_UOM | VARCHAR2 | 30 |  |  | Rate age unit of measure. |
| RT_LOS_UOM | VARCHAR2 | 30 |  |  | Rate length of service unit of measure. |
| RT_PCT_FL_TM_VAL | NUMBER |  |  |  | Rate percent full time value. |
| RT_FRZ_LOS_FLAG | VARCHAR2 | 30 |  |  | Rate Freeze Length of Service Y or N. |
| RT_FRZ_AGE_FLAG | VARCHAR2 | 30 |  |  | Rate Freeze Age Y or N. |
| RT_FRZ_CMP_LVL_FLAG | VARCHAR2 | 30 |  |  | Rate Freeze Compensation Level Y or N. |
| RT_FRZ_PCT_FL_TM_FLAG | VARCHAR2 | 30 |  |  | Rate Freeze Percent Full Time Y or N. |
| RT_FRZ_HRS_WKD_FLAG | VARCHAR2 | 30 |  |  | Rate Freeze Hours Worked Y or N. |
| RT_FRZ_COMB_AGE_AND_LOS_FLAG | VARCHAR2 | 30 |  |  | Rate Freeze Combination Age And Length of Service Y or N. |
| AGE_UOM | VARCHAR2 | 30 |  |  | Eligible age unit of measure. |
| AGE_VAL | NUMBER |  |  |  | Eligible age value. |
| CMBN_AGE_N_LOS_VAL | NUMBER |  |  |  | Eligible combined age and length of service value. |
| COMP_REF_AMT | NUMBER |  |  |  | Eligible compensation reference amount. |
| COMP_REF_UOM | VARCHAR2 | 30 |  |  | Eligible compensation reference unit of measure. |
| DPNT_OTHER_PL_CVRD_RL_FLAG | VARCHAR2 | 30 |  |  | Dependent covered in other plan rule Y or N. |
| DSTR_RSTCN_FLAG | VARCHAR2 | 30 |  |  | Distribution restriction Y or N. |
| FRZ_AGE_FLAG | VARCHAR2 | 30 |  |  | Freeze Age Y or N. |
| FRZ_CMP_LVL_FLAG | VARCHAR2 | 30 |  |  | Freeze Compensation Level Y or N. |
| FRZ_COMB_AGE_AND_LOS_FLAG | VARCHAR2 | 30 |  |  | Freeze Combination Age And Length of Service Y or N. |
| FRZ_HRS_WKD_FLAG | VARCHAR2 | 30 |  |  | Freeze Hours Worked Y or N. |
| FRZ_LOS_FLAG | VARCHAR2 | 30 |  |  | Freeze Length of Service Y or N. |
| FRZ_PCT_FL_TM_FLAG | VARCHAR2 | 30 |  |  | Freeze Percent Full Time Y or N. |
| HRS_WKD_BNDRY_PERD_CD | VARCHAR2 | 30 |  |  | Eligible hours worked boundary period. |
| HRS_WKD_VAL | NUMBER |  |  |  | Eligible hours worked. |
| LOS_UOM | VARCHAR2 | 30 |  |  | Eligible length of service unit of measure. |
| LOS_VAL | NUMBER |  |  |  | Eligible length of service value. |
| NO_MX_PRTN_OVRID_THRU_FLAG | VARCHAR2 | 30 |  |  | No Maximum Participation Override Through Y or N. |
| OVRID_SVC_DT | DATE |  |  |  | Override service date. |
| PCT_FL_TM_VAL | NUMBER |  |  |  | Eligible percent full time value. |
| PL_HGHLY_COMPD_FLAG | VARCHAR2 | 30 |  |  | Plan Highly Compensated Y or N. |
| PL_KEY_EE_FLAG | VARCHAR2 | 30 |  |  | Plan Key Employee Y or N. |
| PL_WVD_FLAG | VARCHAR2 | 30 |  |  | Plan Waived Y or N. |
| PRTN_END_DT | DATE |  |  |  | Participation end date. |
| PRTN_OVRIDN_FLAG | VARCHAR2 | 30 |  |  | Participation Overriden Y or N. |
| PRTN_OVRIDN_RSN_CD | VARCHAR2 | 30 |  |  | Participation override reason. |
| PRTN_OVRIDN_THRU_DT | DATE |  |  |  | Participation overriden through date. |
| PRTN_STRT_DT | DATE |  |  |  | Participation start date. |
| WAIT_PERD_CMPLTN_DT | DATE |  |  |  | Waiting period completion date. |
| WV_CTFN_TYP_CD | VARCHAR2 | 30 |  |  | Waive certification type. |
| WV_PRTN_RSN_CD | VARCHAR2 | 30 |  |  | Waive participation reason. |
| PERSON_ID | NUMBER |  | 18 |  | Foreign Key to PER_PEOPLE_F. |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| LER_ID | NUMBER |  | 18 |  | Foreign Key to BEN_LER_F. |
| PTIP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PTIP_F. |
| PLIP_ID | NUMBER |  | 18 |  | Foreign key to BEN_PLIP_F. |
| OTHR_PL_ENRLD_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_F. |
| PGM_ID | NUMBER |  | 18 |  | Foreign key to BEN_PGM_F. |
| ELIG_PER_ID | NUMBER |  | 18 |  | Foreign key to BEN_ELIG_PER. |
| OPT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OPT_F. |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Foreign key to HR_ORGANIZATION_UNITS. |
| PRTT_ENRT_RSLT_ID | NUMBER |  | 18 |  | Foreign key to BEN_PRTT_ENRT_RSLT_F. |
| PERSON_TTEE_ID | NUMBER |  | 18 |  | Foreign key to PER_PEOPLE_F. |
| ELIG_PER_ELCTBL_CHC_ID | NUMBER |  | 18 |  | Foreign key to BEN_ELIG_PER_ELCTBL_CHC. |
| PERSON_DPNT_ID | NUMBER |  | 18 |  | Foreign key to BEN_ELIG_CVRD_DPNT. |
| ELEMENT_ENTRY_VALUE_ID | NUMBER |  | 18 |  | Foreign key to PAY_ELEMENT_ENTRY_VALUES_F. |
| PER_IN_LER_ENDED_ID | NUMBER |  | 18 |  | Foreign key to BEN_PER_IN_LER. |
| CVG_AMT_CALC_MTHD_ID | NUMBER |  | 18 |  | Foreign key to BEN_CVG_AMT_CALC_MTHD_F. |
| ENRT_RT_ID | NUMBER |  | 18 |  | Foreign key to BEN_ENRT_RT_F. |
| ACTY_BASE_RT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTY_BASE_RT_F. |
| OIPL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OIPL_F. |
| COMP_LVL_FCTR_ID | NUMBER |  | 18 |  | Foreign Key to BEN_COMP_LVL_FCTR_F. |
| PL_TYP_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_TYP_F. |
| ACTL_PREM_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTL_PREM_F. |
| PRTT_ENRT_RSLT_SSPNDD_ID | NUMBER |  | 18 |  | Foreign key to BEN_PRTT_ENRT_RSLT_F. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign Key to PER_ALL_ASSIGNMENTS_F. |
| ENRT_BNFT_ID | NUMBER |  | 18 |  | Foreign key to BEN_ENRT_BNFT_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TTEE_PERSON_ID | NUMBER |  | 18 |  | Foreign key to PER_PEOPLE_F. |
| DPNT_PERSON_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_PEOPLE_F. |
| ONCE_R_CNTUG_CD | VARCHAR2 | 30 |  |  | Once or Continuing. |
| DPNT_OTHR_PL_CVRD_RL_FLAG | VARCHAR2 | 30 |  |  | Dependent covered in other plan rule Y or N. |
| MUST_ENRL_ANTHR_PL_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_F. |
| PL_ORDR_NUM | NUMBER |  | 18 |  | Plan order number. |
| PLIP_ORDR_NUM | NUMBER |  | 18 |  | Plan in program order number. |
| PTIP_ORDR_NUM | NUMBER |  | 18 |  | Plan type in program order number. |
| OIPL_ORDR_NUM | NUMBER |  | 18 |  | Option in plan order number. |
| BNF_PERSON_ID | NUMBER |  | 18 |  | Foreign Key to PER_ALL_PEOPLE_F. |
| RPLCS_SSPNDD_RSLT_ID | NUMBER |  | 18 |  | Foreign key to BEN_PRTT_ENRT_RSLT_F. |
| VAL | NUMBER |  |  |  | Value. |
| STD_PREM_VAL | NUMBER |  | 18 |  | Standard premium value. |
| STD_PREM_UOM | VARCHAR2 | 30 |  |  | Standard premium unit of measure. |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | Foreign Key to BEN_BENEFIT_RELATIONS_F |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LE_CLSN_N_RSTR_FK12 | Non Unique | FUSION_TS_TX_DATA | PRTT_ENRT_RSLT_ID |
| BEN_LE_CLSN_N_RSTR_FK14 | Non Unique | FUSION_TS_TX_DATA | ELIG_PER_ELCTBL_CHC_ID |
| BEN_LE_CLSN_N_RSTR_FK21 | Non Unique | FUSION_TS_TX_DATA | BENEFIT_RELATION_ID |
| BEN_LE_CLSN_N_RSTR_FK9 | Non Unique | FUSION_TS_TX_DATA | ELIG_PER_ID |
| BEN_LE_CLSN_N_RSTR_PK1 | Unique | FUSION_TS_TX_IDX | BKUP_TBL_ID, BKUP_TBL_TYP_CD, OBJECT_VERSION_NUMBER |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
