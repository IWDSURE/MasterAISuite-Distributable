# BEN_OIPL_F

BEN_OIPL_F identifies the processing characteristics of an option that is provided by a plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benoiplf-14075.html#benoiplf-14075](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benoiplf-14075.html#benoiplf-14075)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_OIPL_F_PK | OIPL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| OIPL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| IVR_IDENT | VARCHAR2 | 90 |  |  | Interactive Voice Response identifier. |  |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |  |
| MNDTRY_FLAG | VARCHAR2 | 30 |  | Yes | Mandatory Y or N. |  |
| DFLT_FLAG | VARCHAR2 | 30 |  | Yes | Default Y or N. |  |
| OIPL_STAT_CD | VARCHAR2 | 30 |  | Yes | Option in plan status. |  |
| ELIG_APLS_FLAG | VARCHAR2 | 30 |  | Yes | Eligibility applies Y or N. |  |
| DFLT_ENRT_DET_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| TRK_INELIG_PER_FLAG | VARCHAR2 | 30 |  | Yes | Track Ineligible Person Y or N. |  |
| DRVBL_FCTR_PRTN_ELIG_FLAG | VARCHAR2 | 30 |  | Yes | Derivable factors for participation eligibility Y or N. |  |
| MNDTRY_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| DFLT_ENRT_CD | VARCHAR2 | 30 |  |  | Default enrollment code. |  |
| PRTN_ELIG_OVRID_ALWD_FLAG | VARCHAR2 | 30 |  | Yes | Participation Eligible Override Allowed Y or N. |  |
| DRVBL_FCTR_APLS_RTS_FLAG | VARCHAR2 | 30 |  | Yes | Derivable factors apply to rates Y or N. |  |
| PER_CVRD_CD | VARCHAR2 | 30 |  |  | Person covered code. |  |
| POSTELCN_EDIT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| VRFY_FMLY_MMBR_CD | VARCHAR2 | 30 |  |  | Verify family member code |  |
| VRFY_FMLY_MMBR_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| AUTO_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | Automatically Enroll Y or N. |  |
| AUTO_ENRT_MTHD_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| COP_AUTO_ENRT_FLAG | VARCHAR2 | 30 |  |  | COP_AUTO_ENRT_FLAG |  |
| RQD_PERD_ENRT_NENRT_UOM | VARCHAR2 | 30 |  |  | Required period of enrollment unit of measure. |  |
| RQD_PERD_ENRT_NENRT_VAL | NUMBER |  |  |  | Required period of enrollment value. |  |
| RQD_PERD_ENRT_NENRT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| OPT_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_OPT_F. |  |
| PL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_PL_F. |  |
| ACTL_PREM_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTL_PREM_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| COP_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| COP_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option In Plan Attributes (BEN_OIPL_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| URL_REF_NAME | VARCHAR2 | 240 |  |  | URL reference name. |  |
| ENRT_CD | VARCHAR2 | 30 |  |  | Enrollment code. |  |
| ENRT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| PCP_DSGN_CD | VARCHAR2 | 30 |  |  | Primary Care Provider designation code. |  |
| PCP_DPNT_DSGN_CD | VARCHAR2 | 30 |  |  | Primary Care Provider dependent designation code. |  |
| SHORT_CODE | VARCHAR2 | 30 |  |  | Short Code |  |
| SHORT_NAME | VARCHAR2 | 30 |  |  | short Name |  |
| HIDDEN_FLAG | VARCHAR2 | 30 |  | Yes | Hiddent for Self Service Flag |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| LEGISLATION_SUBGROUP | VARCHAR2 | 30 |  |  | Further identifies the legislation of startup data. |  |
| SUSP_IF_CTFN_NOT_PRVD_FLAG | VARCHAR2 | 30 |  | Yes | Suspend Enrollment if Certification not provided |  |
| DFLT_TO_ASN_PNDG_CTFN_CD | VARCHAR2 | 30 |  |  | DFLT_TO_ASN_PNDG_CTFN_CD |  |
| DFLT_TO_ASN_PNDG_CTFN_RL | NUMBER |  |  |  | DFLT_TO_ASN_PNDG_CTFN_RL |  |
| UNSSPND_ENRT_CD | VARCHAR2 | 30 |  |  | UNSSPND_ENRT_CD |  |
| UNSSPND_ENRT_RL | NUMBER |  |  |  | UNSSPND_ENRT_RL |  |
| UNSSPND_RT_CD | VARCHAR2 | 30 |  |  | UNSSPND_RT_CD |  |
| UNSSPND_RT_RL | NUMBER |  |  |  | UNSSPND_RT_RL |  |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number column for future use. |  |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number column for future use. |  |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number column for future use. |  |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number column for future use. |  |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number column for future use. |  |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template string column for future use. |  |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template string column for future use. |  |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template string column for future use. |  |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template string column for future use. |  |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template string column for future use. |  |
| CONFIG_DATE_1 | DATE |  |  |  | Template date column for future use. |  |
| CONFIG_DATE_2 | DATE |  |  |  | Template date column for future use. |  |
| CONFIG_DATE_3 | DATE |  |  |  | Template date column for future use. |  |
| CONFIG_DATE_4 | DATE |  |  |  | Template date column for future use. |  |
| CONFIG_DATE_5 | DATE |  |  |  | Template date column for future use. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_OIPL_F_N1 | Non Unique | Default | ACTL_PREM_ID |
| BEN_OIPL_F_N2 | Non Unique | Default | PL_ID |
| BEN_OIPL_F_N3 | Non Unique | Default | OPT_ID |
| BEN_OIPL_F_PK | Unique | Default | OIPL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
