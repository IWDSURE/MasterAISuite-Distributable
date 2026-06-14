# BEN_ENRT_RT

BEN_ENRT_RT identifies the rates calculated for a person for a plan or option in plan.  It also identifies the values of flexible credits and imputed income values.  This is denormalized data, made available primarily to avoid the need for reporting and enrollment processes to calculate these values on the fly.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benenrtrt-31192.html#benenrtrt-31192](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benenrtrt-31192.html#benenrtrt-31192)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ENRT_RT_PK | ENRT_RT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ENRT_RT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| MAPPING_ID | NUMBER |  | 18 |  | Payroll Mapping Id- Foreign key to PAY_GI_MAPPINGS |  |
| DIR_CARD_COMP_DEF_ID | NUMBER |  | 18 |  | Payroll Component Definition Id- Foreign key to pay_dir_card_comp_defs_f |  |
| VALUE_DEFINITION_BASE_NAME | VARCHAR2 | 128 |  |  | Base name of the Value Definition |  |
| DIR_CARD_DEFINITION_ID | NUMBER |  | 18 |  | Payroll Card Definition Id- Foreign key to  pay_dir_card_definitions |  |
| VDEFN_DIR_CARD_COMP_DEF_ID | NUMBER |  | 18 |  | Payroll Component Definition Id Corresponding to Value Definitions |  |
| VDEFN_ELEMENT_TYPE_ID | NUMBER |  | 18 |  | Element Type Id Corresponding to CIR |  |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_6 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_7 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_8 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_9 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_10 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_CHAR_6 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_7 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_8 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_9 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_10 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| ACTY_TYP_CD | VARCHAR2 | 30 |  | Yes | This column holds Activity type. |  |
| TX_TYP_CD | VARCHAR2 | 30 |  | Yes | This column holds Tax type value. |  |
| CTFN_RQD_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Certification required Y or N. |  |
| DFLT_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Default Y or N. |  |
| DFLT_PNDG_CTFN_FLAG | VARCHAR2 | 30 |  | Yes | Default pending certifications Y or N. |  |
| DSPLY_ON_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Display on Enrollment Y or N. |  |
| USE_TO_CALC_NET_FLX_CR_FLAG | VARCHAR2 | 30 |  | Yes | Use to calculate net flexible credit Y or N. |  |
| ENTR_VAL_AT_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | Enter Value At Enrollment Y or N. |  |
| ASN_ON_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Assign on Enrollment Y or N. |  |
| RL_CRS_ONLY_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Rule Credits Only Y or N. |  |
| DFLT_VAL | NUMBER |  |  |  | This column holds Default value. |  |
| ANN_VAL | NUMBER |  |  |  | This column holds Annual value. |  |
| ANN_MN_ELCN_VAL | NUMBER |  |  |  | This column holds Annual maximum election value. |  |
| ANN_MX_ELCN_VAL | NUMBER |  |  |  | This column holds Annual minimum election value. |  |
| VAL | NUMBER |  |  |  | This column holds rate amount Value. |  |
| NNMNTRY_UOM | VARCHAR2 | 30 |  |  | This column holds Non-monentary unit of measure. |  |
| MX_ELCN_VAL | NUMBER |  |  |  | This column holds Maximum election value. |  |
| MN_ELCN_VAL | NUMBER |  |  |  | This column holds Minimum election value. |  |
| INCRMT_ELCN_VAL | NUMBER |  |  |  | This column holds Increment election value. |  |
| CMCD_ACTY_REF_PERD_CD | VARCHAR2 | 30 |  |  | Communicated activity reference period. |  |
| CMCD_MN_ELCN_VAL | NUMBER |  |  |  | Communicated minimum election value. |  |
| CMCD_MX_ELCN_VAL | NUMBER |  |  |  | Communicated maximum election value. |  |
| CMCD_VAL | NUMBER |  |  |  | This column holds Communicated value. |  |
| CMCD_DFLT_VAL | NUMBER |  |  |  | This column holds Communicated default value. |  |
| RT_USG_CD | VARCHAR2 | 30 |  |  | This column holds Rate usage value. |  |
| ANN_DFLT_VAL | NUMBER |  | 15 |  | This column holds Annual default value. |  |
| BNFT_RT_TYP_CD | VARCHAR2 | 30 |  |  | This column holds Benefit rate type. |  |
| RT_MLT_CD | VARCHAR2 | 30 |  |  | This column holds Rate multiply code. |  |
| DSPLY_MN_ELCN_VAL | NUMBER |  | 15 |  | Display minimum election value. |  |
| DSPLY_MX_ELCN_VAL | NUMBER |  | 15 |  | Display maximum election value. |  |
| ENTR_ANN_VAL_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Enter Annual Value Y or N. |  |
| RT_STRT_DT | DATE |  |  |  | This column holds Rate start date. |  |
| RT_STRT_DT_CD | VARCHAR2 | 30 |  |  | This column holds Rate start date code. |  |
| RT_STRT_DT_RL | NUMBER |  | 18 |  | This column holds Foreign key to FF_FORMULAS_F. |  |
| RT_TYP_CD | VARCHAR2 | 30 |  |  | This column holds Rate type value. |  |
| ELIG_PER_ELCTBL_CHC_ID | NUMBER |  | 18 |  | Foreign key to BEN_ELIG_PER_ELCTBL_CHC. |  |
| ACTY_BASE_RT_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_ACTY_BASE_RT_F. |  |
| SPCL_RT_ENRT_RT_ID | NUMBER |  | 18 |  | This column holds Foreign kry to BEN_ENRT_RT. |  |
| ENRT_BNFT_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_ENRT_BNF_F. |  |
| PRTT_RT_VAL_ID | NUMBER |  | 18 |  | Foreign key to BEN_PRTT_RT_VAL_F. |  |
| DECR_BNFT_PRVDR_POOL_ID | NUMBER |  | 18 |  | Foreign Key to DECR_BNFT_PRVDR_POOL_F. |  |
| CVG_AMT_CALC_MTHD_ID | NUMBER |  | 18 |  | Foreign key to BEN_CVG_AMT_CALC_MTHD_F. |  |
| ACTL_PREM_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTL_PREM_F. |  |
| COMP_LVL_FCTR_ID | NUMBER |  | 18 |  | Foreign Key to BEN_COMP_LVL_FCTR_F. |  |
| PTD_COMP_LVL_FCTR_ID | NUMBER |  | 18 |  | Foreign key to BEN_PTD_COMP_LVL_FCTR_F. |  |
| CLM_COMP_LVL_FCTR_ID | NUMBER |  | 18 |  | Foreign Key to BEN_CLM_COMP_LVL_FCTR_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| ECR_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| ECR_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Enrollment Rate Attribute (BEN_ENRT_RT_DFF) |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |  |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |  |
| PROGRAM_APP_NAME | VARCHAR2 | 30 |  |  | This column holds PROGRAM_APP_NAME |  |
| PROGRAM_NAME | VARCHAR2 | 30 |  |  | This column holds PROGRAM_NAME value |  |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ISS_VAL | NUMBER |  |  |  | This column holds value iss_val. |  |
| VAL_LAST_UPD_DATE | DATE |  |  |  | This column holds val_last_upd_date. |  |
| VAL_LAST_UPD_PERSON_ID | NUMBER |  | 18 |  | This column holds val_last_upd_person_id. |  |
| PP_IN_YR_USED_NUM | NUMBER |  | 18 |  | This column holds Pay Periods in the year used. |  |
| ORDR_NUM | NUMBER |  | 18 |  | This column holds Order Number value |  |
| ENDED_PRTT_RT_VAL_ID | NUMBER |  | 18 |  | This column holds ENDED_PRTT_RT_VAL_ID |  |
| RCRRG_FLAG | VARCHAR2 | 30 |  |  | This column holds RCRRG_FLAG value |  |
| CVRD_RT_AMT | NUMBER |  |  |  | This column holds CVRD_RT_AMT value |  |
| CVRD_ANN_RT_AMT | NUMBER |  |  |  | This column holds CVRD_ANN_RT_AMT |  |
| RATE_DISPLAY_CD | VARCHAR2 | 30 |  |  | P’ –Primary, ‘S’ –Secondary and ‘O’ -Others |  |
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
| BEN_ENRT_RT_FK4 | Non Unique | Default | ELIG_PER_ELCTBL_CHC_ID |
| BEN_ENRT_RT_FK5 | Non Unique | Default | ENRT_BNFT_ID |
| BEN_ENRT_RT_FK7 | Non Unique | Default | SPCL_RT_ENRT_RT_ID |
| BEN_ENRT_RT_N1 | Non Unique | Default | ACTY_BASE_RT_ID |
| BEN_ENRT_RT_N2 | Non Unique | Default | DECR_BNFT_PRVDR_POOL_ID |
| BEN_ENRT_RT_N3 | Non Unique | Default | PRTT_RT_VAL_ID |
| BEN_ENRT_RT_PK1 | Unique | Default | ENRT_RT_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
