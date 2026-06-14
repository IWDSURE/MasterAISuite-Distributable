# BEN_ENRT_BNFT

BEN_ENRT_BNFT  identifies the coverage or benefit provided by the electable choices available to an eligible person as a result of a life event or for open enrollment.  This is denormalized data, made available primarily to avoid the need for reporting and enrollment processes to calculate these values on the fly.   For example,  if a specific person chooses group term life insurance at 2 time salary, the coverage provided will be $85,000.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benenrtbnft-9028.html#benenrtbnft-9028](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benenrtbnft-9028.html#benenrtbnft-9028)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ENRT_BNFT_PK | ENRT_BNFT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ENRT_BNFT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| SUSP_IF_CTFN_NOT_PRVD_FLAG | VARCHAR2 | 30 |  |  | This column holds SUSP_IF_CTFN_NOT_PRVD_FLAG |  |
| DFLT_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Default Y or N. |  |
| VAL_HAS_BN_PRORTD_FLAG | VARCHAR2 | 30 |  | Yes | Value Has Been Prorated Y or N. |  |
| BNDRY_PERD_CD | VARCHAR2 | 30 |  |  | This column holds Boundary period. |  |
| VAL | NUMBER |  |  |  | This column indicates rate Value. |  |
| NNMNTRY_UOM | VARCHAR2 | 30 |  |  | This column holds Non-monentary unit of measure. |  |
| BNFT_TYP_CD | VARCHAR2 | 30 |  |  | This column holds Benefit type. |  |
| ENTR_VAL_AT_ENRT_FLAG | VARCHAR2 | 30 |  |  | Enter Value At Enrollment Y or N. |  |
| MN_VAL | NUMBER |  |  |  | This column holds Minimum value. |  |
| MX_VAL | NUMBER |  |  |  | This column holds Maximum value. |  |
| INCRMT_VAL | NUMBER |  |  |  | This column holds Increment value. |  |
| RT_TYP_CD | VARCHAR2 | 30 |  |  | This column holds Rate type code. |  |
| CVG_MLT_CD | VARCHAR2 | 30 |  |  | This column holds Coverage multiply code. |  |
| CTFN_RQD_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Certification required Y or N. |  |
| ORDR_NUM | NUMBER |  | 18 |  | This column holds Order number. |  |
| CRNTLY_ENRLD_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Currently enrolled Y or N. |  |
| ELIG_PER_ELCTBL_CHC_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ELIG_PER_ELCTBL_CHC. |  |
| PRTT_ENRT_RSLT_ID | NUMBER |  | 18 |  | Foreign key to BEN_PRTT_ENRT_RSLT_F. |  |
| COMP_LVL_FCTR_ID | NUMBER |  | 18 |  | Foreign Key to BEN_COMP_LVL_FCTR_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| ENB_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| ENB_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Benefit Attribute (BEN_ENRT_BNFT_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |  |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |  |
| PROGRAM_APP_NAME | VARCHAR2 | 30 |  |  | This column holds PROGRAM_APP_NAME |  |
| PROGRAM_NAME | VARCHAR2 | 30 |  |  | This column holds PROGRAM_NAME value |  |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| DFLT_VAL | NUMBER |  |  |  | This column holds Default value. |  |
| MX_WOUT_CTFN_VAL | NUMBER |  |  |  | Maximum without certification value. |  |
| MX_WO_CTFN_FLAG | VARCHAR2 | 30 |  | Yes | Maximum without certification Y or N. |  |
| ENDED_PRTT_ENRT_RSLT_ID | NUMBER |  | 18 |  | This column holds ENDED_PRTT_ENRT_RSLT_ID |  |
| CVRD_FLAG | VARCHAR2 | 30 |  |  | ???Y??? when the choice is selected. Need to be carried backward from enrollment results, if default is run and elections are made. This always needs to be in sync with enrollment results created for the life event. |  |
| CVRD_BNFT_AMT | NUMBER |  |  |  | This is the field used to capture the benefit amount entered by the user.In case of default enrollments, we need to make sure this amount is also populated. |  |
| INTERIM_FLAG | VARCHAR2 | 30 |  |  | Enrollment Benefit Record associated with the interim enrollment. |  |
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
| TYPE_ID | NUMBER |  | 18 |  | This column is Foreign Key to BEN_TYPES. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ENRT_BNFT_FK3 | Non Unique | Default | ELIG_PER_ELCTBL_CHC_ID |
| BEN_ENRT_BNFT_FK4 | Non Unique | Default | COMP_LVL_FCTR_ID |
| BEN_ENRT_BNFT_FK5 | Non Unique | Default | ENDED_PRTT_ENRT_RSLT_ID |
| BEN_ENRT_BNFT_N1 | Non Unique | Default | PRTT_ENRT_RSLT_ID |
| BEN_ENRT_BNFT_PK1 | Unique | Default | ENRT_BNFT_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
