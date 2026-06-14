# BEN_PTIP_F

BEN_PTIP_F  identifies processing requirements for a plan type that is supported within a program.  For example, the ABC Corporation Flexible Benefits Program is composed of Medical, Dental, Vision, Employee Group Term Life Insurance, Health Care Flexible Spending Account, and Dependent Care Flexible Spending Account types of plans.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benptipf-18004.html#benptipf-18004](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benptipf-18004.html#benptipf-18004)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PTIP_F_PK | PTIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PTIP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| COORD_CVG_FOR_ALL_PLS_FLAG | VARCHAR2 | 30 |  | Yes | Coordinate coverage for all plans Y or N. |
| DPNT_CVG_NO_CTFN_RQD_FLAG | VARCHAR2 | 30 |  | Yes | Dependent coverage requires no certification Y or N. |
| DPNT_CVG_STRT_DT_CD | VARCHAR2 | 30 |  |  | Dependent coverage start date code. |
| DPNT_CVG_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| DPNT_CVG_END_DT_CD | VARCHAR2 | 30 |  |  | Dependent coverage end date code. |
| DPNT_CVG_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| POSTELCN_EDIT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| CRS_THIS_PL_TYP_ONLY_FLAG | VARCHAR2 | 30 |  | Yes | Credits this plan type only Y or N. |
| PTIP_STAT_CD | VARCHAR2 | 30 |  | Yes | Plan type in program status. |
| MX_CVG_ALWD_AMT | NUMBER |  |  |  | Maximum coverage allowed amount. |
| MX_ENRD_ALWD_OVRID_NUM | NUMBER |  | 18 |  | Maximum enrollment allowed to override the value defined for the plan type. |
| MN_ENRD_RQD_OVRID_NUM | NUMBER |  | 18 |  | Minimum required enrollment to override the value defined for the plan type. |
| NO_MX_PL_TYP_OVRID_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Plan Type Override Y or N. |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |
| PRVDS_CR_FLAG | VARCHAR2 | 30 |  | Yes | Provides Credit Y or N. |
| RQD_PERD_ENRT_NENRT_VAL | NUMBER |  | 15 |  | Required period of enrollment value. |
| RQD_PERD_ENRT_NENRT_TM_UOM | VARCHAR2 | 30 |  |  | Required period of enrollment unit of measure. |
| WVBL_FLAG | VARCHAR2 | 30 |  | Yes | Waivable Y or N. |
| DRVD_FCTR_DPNT_CVG_FLAG | VARCHAR2 | 30 |  | Yes | Derived factor for dependent coverage Y or N. |
| NO_MN_PL_TYP_OVERID_FLAG | VARCHAR2 | 30 |  | Yes | No Minimum Plan Type Override Y or N. |
| SBJ_TO_SPS_LF_INS_MX_FLAG | VARCHAR2 | 30 |  | Yes | Subject To Spouse Life Insurance Maximum Y or N. |
| SBJ_TO_DPNT_LF_INS_MX_FLAG | VARCHAR2 | 30 |  | Yes | Subject To Dependent Life Insurance Maximum Y or N. |
| USE_TO_SUM_EE_LF_INS_FLAG | VARCHAR2 | 30 |  | Yes | Use To Sum Employee Life Insurance Y or N. |
| IVR_IDENT | VARCHAR2 | 90 |  |  | Interactive Voice Response identifier. |
| RQD_ENRT_PERD_TCO_CD | VARCHAR2 | 30 |  |  | Required enrollment period total compensation object code. |
| RQD_PERD_ENRT_NENRT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| PGM_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PGM_F. |
| PL_TYP_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PL_TYP_F. |
| CMBN_PTIP_ID | NUMBER |  | 18 |  | Foreign key to BEN_CMBN_PTIP_F. |
| CMBN_PTIP_OPT_ID | NUMBER |  | 18 |  | Foreign key to BEN_CMBN_PTIP_OPT_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENRT_CVG_STRT_DT_CD | VARCHAR2 | 30 |  |  | Enrollment coverage start date code. |
| ENRT_CVG_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ENRT_CVG_END_DT_CD | VARCHAR2 | 30 |  |  | Enrollment coverage end date code. |
| ENRT_CVG_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| RT_STRT_DT_CD | VARCHAR2 | 30 |  |  | Rate start date code. |
| RT_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| RT_END_DT_CD | VARCHAR2 | 30 |  |  | Rate end date code. |
| RT_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| URL_REF_NAME | VARCHAR2 | 240 |  |  | URL reference name. |
| ACRS_PTIP_CVG_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACRS_PTIP_CVG_F. |
| AUTO_ENRT_MTHD_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| ENRT_MTHD_CD | VARCHAR2 | 30 |  |  | Enrollment method |
| ENRT_CD | VARCHAR2 | 30 |  |  | Enrollment code. |
| ENRT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| DFLT_ENRT_CD | VARCHAR2 | 30 |  |  | Default enrollment code. |
| DFLT_ENRT_DET_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| DRVBL_FCTR_APLS_RTS_FLAG | VARCHAR2 | 30 |  | Yes | Derivable factors apply to rates Y or N. |
| DRVBL_FCTR_PRTN_ELIG_FLAG | VARCHAR2 | 30 |  | Yes | Derivable factors for participation eligibility Y or N. |
| ELIG_APLS_FLAG | VARCHAR2 | 30 |  | Yes | Eligibility applies Y or N. |
| PRTN_ELIG_OVRID_ALWD_FLAG | VARCHAR2 | 30 |  | Yes | Participation Eligible Override Allowed Y or N. |
| TRK_INELIG_PER_FLAG | VARCHAR2 | 30 |  | Yes | Track Ineligible Person Y or N. |
| VRFY_FMLY_MMBR_CD | VARCHAR2 | 30 |  |  | Verify family member code |
| VRFY_FMLY_MMBR_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| PER_CVRD_CD | VARCHAR2 | 30 |  |  | Person covered code. |
| SHORT_CODE | VARCHAR2 | 30 |  |  | Short Code |
| SHORT_NAME | VARCHAR2 | 30 |  |  | short Name |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATION_SUBGROUP | VARCHAR2 | 30 |  |  | Further identifies the legislation of startup data. |
| DFLT_TO_ASN_PNDG_CTFN_CD | VARCHAR2 | 30 |  |  | DFLT_TO_ASN_PNDG_CTFN_CD |
| DFLT_TO_ASN_PNDG_CTFN_RL | NUMBER |  |  |  | DFLT_TO_ASN_PNDG_CTFN_RL |
| UNSSPND_ENRT_CD | VARCHAR2 | 30 |  |  | UNSSPND_ENRT_CD |
| UNSSPND_ENRT_RL | NUMBER |  |  |  | UNSSPND_ENRT_RL |
| UNSSPND_RT_CD | VARCHAR2 | 30 |  |  | UNSSPND_RT_CD |
| UNSSPND_RT_RL | NUMBER |  |  |  | UNSSPND_RT_RL |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PTIP_F_N1 | Non Unique | Default | PL_TYP_ID |
| BEN_PTIP_F_N2 | Non Unique | Default | PGM_ID |
| BEN_PTIP_F_N3 | Non Unique | Default | CMBN_PTIP_ID |
| BEN_PTIP_F_N4 | Non Unique | Default | CMBN_PTIP_OPT_ID |
| BEN_PTIP_F_N5 | Non Unique | Default | ACRS_PTIP_CVG_ID |
| BEN_PTIP_F_PK | Unique | Default | PTIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
