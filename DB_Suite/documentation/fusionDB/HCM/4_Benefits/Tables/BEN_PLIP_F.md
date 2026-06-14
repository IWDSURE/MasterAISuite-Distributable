# BEN_PLIP_F

BEN_PLIP_F identifies and specifies processing characteristics of a plan assigned to a program.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplipf-11514.html#benplipf-11514](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplipf-11514.html#benplipf-11514)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PLIP_F_PK | PLIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PLIP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| DFLT_FLAG | VARCHAR2 | 30 |  | Yes | Default Y or N. |  |
| PLIP_STAT_CD | VARCHAR2 | 30 |  | Yes | Plan in program status. |  |
| DFLT_ENRT_CD | VARCHAR2 | 30 |  |  | Default enrollment code. |  |
| DFLT_ENRT_DET_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |  |
| IVR_IDENT | VARCHAR2 | 90 |  |  | Interactive Voice Response identifier. |  |
| ENRT_CD | VARCHAR2 | 30 |  |  | Enrollment code. |  |
| ENRT_MTHD_CD | VARCHAR2 | 30 |  |  | Enrollment method. |  |
| ENRT_CVG_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| ENRT_CVG_END_DT_CD | VARCHAR2 | 30 |  |  | Enrollment coverage end date code. |  |
| ENRT_CVG_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| RT_STRT_DT_CD | VARCHAR2 | 30 |  |  | Rate start date code. |  |
| RT_STRT_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| RT_END_DT_CD | VARCHAR2 | 30 |  |  | Rate end date code. |  |
| RT_END_DT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| AUTO_ENRT_MTHD_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| ENRT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| ENRT_CVG_STRT_DT_CD | VARCHAR2 | 30 |  |  | Enrollment coverage start date code. |  |
| ALWS_UNRSTRCTD_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | Allows Unrestricted Enrollment Y or N. |  |
| PGM_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PGM_F. |  |
| PL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_PL_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| CPP_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| CPP_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Plan In Program Attributes (BEN_PLIP_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| URL_REF_NAME | VARCHAR2 | 240 |  |  | URL reference name. |  |
| CVG_INCR_R_DECR_ONLY_CD | VARCHAR2 | 30 |  |  | Coverage increment or decrement only. |  |
| DFLT_TO_ASN_PNDG_CTFN_CD | VARCHAR2 | 30 |  |  | Default to assign pending notification code. |  |
| DFLT_TO_ASN_PNDG_CTFN_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| MN_CVG_AMT | NUMBER |  |  |  | Minimum coverage amount. |  |
| MN_CVG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| MX_CVG_ALWD_AMT | NUMBER |  |  |  | Maximum coverage allowed amount. |  |
| MX_CVG_INCR_ALWD_AMT | NUMBER |  |  |  | Maximum coverage increase allowed amount. |  |
| MX_CVG_INCR_WCF_ALWD_AMT | NUMBER |  |  |  | Maximum coverage increase with certification allowed amount. |  |
| MX_CVG_MLT_INCR_NUM | NUMBER |  | 18 |  | Maximum coverage multiple increase number. |  |
| MX_CVG_MLT_INCR_WCF_NUM | NUMBER |  | 18 |  | Maximum coverage multiple increase with certification number. |  |
| MX_CVG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| MX_CVG_WCFN_AMT | NUMBER |  |  |  | Maximum coverage with certification amount. |  |
| MX_CVG_WCFN_MLT_NUM | NUMBER |  | 18 |  | Maximum coverage with certification multiple number. |  |
| NO_MN_CVG_AMT_APLS_FLAG | VARCHAR2 | 30 |  |  | No Minimum Coverage Amount Applies Y or N. |  |
| NO_MN_CVG_INCR_APLS_FLAG | VARCHAR2 | 30 |  |  | No Minimum Coverage Increase Applies Y or N. |  |
| NO_MX_CVG_AMT_APLS_FLAG | VARCHAR2 | 30 |  |  | No Maximum Coverage Amount Applies Y or N. |  |
| NO_MX_CVG_INCR_APLS_FLAG | VARCHAR2 | 30 |  |  | No Maximum Coverage Increase Applies Y or N. |  |
| UNSSPND_ENRT_CD | VARCHAR2 | 30 |  |  | Unsuspended enrollment code. |  |
| PRORT_PRTL_YR_CVG_RSTRN_CD | VARCHAR2 | 30 |  |  | Prorate partial year coverage restriction code. |  |
| PRORT_PRTL_YR_CVG_RSTRN_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| CMBN_PLIP_ID | NUMBER |  | 18 |  | Foreign key to BEN_CMBN_PLIP_F. |  |
| DRVBL_FCTR_APLS_RTS_FLAG | VARCHAR2 | 30 |  | Yes | Derivable factors apply to rates Y or N. |  |
| DRVBL_FCTR_PRTN_ELIG_FLAG | VARCHAR2 | 30 |  | Yes | Derivable factors for participation eligibility Y or N. |  |
| ELIG_APLS_FLAG | VARCHAR2 | 30 |  | Yes | Eligibility applies Y or N. |  |
| PRTN_ELIG_OVRID_ALWD_FLAG | VARCHAR2 | 30 |  | Yes | Participation Eligible Override Allowed Y or N. |  |
| TRK_INELIG_PER_FLAG | VARCHAR2 | 30 |  | Yes | Track Ineligible Person Y or N. |  |
| POSTELCN_EDIT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| BNFT_OR_OPTION_RSTRCTN_CD | VARCHAR2 | 30 |  |  | Benefit or option restriction. |  |
| VRFY_FMLY_MMBR_CD | VARCHAR2 | 30 |  |  | Verify family member code |  |
| VRFY_FMLY_MMBR_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| PER_CVRD_CD | VARCHAR2 | 30 |  |  | Person covered code. |  |
| SHORT_CODE | VARCHAR2 | 30 |  |  | Short Code |  |
| SHORT_NAME | VARCHAR2 | 30 |  |  | short Name |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| LEGISLATION_SUBGROUP | VARCHAR2 | 30 |  |  | Further Identifies the legislation startup data |  |
| USE_CSD_RSD_PRCCNG_CD | VARCHAR2 | 30 |  |  | User Coverage and/or Rate Start Date for Processing |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PLIP_F_N1 | Non Unique | Default | PGM_ID |
| BEN_PLIP_F_N2 | Non Unique | Default | PL_ID |
| BEN_PLIP_F_N4 | Non Unique | Default | CMBN_PLIP_ID |
| BEN_PLIP_F_PK | Unique | Default | PLIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
