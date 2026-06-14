# BEN_PRTT_RT_VAL

BEN_PRTT_RT_VAL identifies the values, tax consequence and other information about standard rates, total flex credits and imputed income calculated for a person enrolled in a plan or option in plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprttrtval-4219.html#benprttrtval-4219](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprttrtval-4219.html#benprttrtval-4219)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PRTT_RT_VAL_PK | PRTT_RT_VAL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PRTT_RT_VAL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| MAPPING_ID | NUMBER |  | 18 |  | Payroll Mapping Id- Foreign key to PAY_GI_MAPPINGS |  |
| DIR_CARD_DEFINITION_ID | NUMBER |  | 18 |  | Payroll Card Definition Id- Foreign key to  pay_dir_card_definitions |  |
| DIR_CARD_COMP_DEF_ID | NUMBER |  | 18 |  | Payroll Component Definition Id- Foreign key to pay_dir_card_comp_defs_f |  |
| VALUE_DEFINITION_BASE_NAME | VARCHAR2 | 128 |  |  | Base name of the Value Definition |  |
| VDEFN_DIR_CARD_COMP_DEF_ID | NUMBER |  | 18 |  | Payroll Component Definition Id Corresponding to Value Definitions |  |
| VDEFN_ELEMENT_TYPE_ID | NUMBER |  | 18 |  | Element Type Id Corresponding to CIR |  |
| CONFIG_CHAR_6 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_7 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_8 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_9 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_CHAR_10 | VARCHAR2 | 240 |  |  | Template character field for future use. |  |
| CONFIG_NUM_6 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_7 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_8 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_9 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_NUM_10 | NUMBER |  |  |  | Template number field for future use. |  |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template ID field for future use. |  |
| RT_STRT_DT | DATE |  |  | Yes | This column holds Rate start date. |  |
| RT_END_DT | DATE |  |  | Yes | This column holds Rate end date. |  |
| ENDED_RATE_THRU_DT | DATE |  |  |  | This column holds ENDED_RATE_THRU_DT |  |
| PRVS_RATE_STRT_DT | DATE |  |  |  | This column holds PRVS_RATE_STRT_DT |  |
| PRVS_RATE_THRU_DT | DATE |  |  |  | This column holds PRVS_RATE_THRU_DT |  |
| RCRRG_FLAG | VARCHAR2 | 30 |  |  | This column holds RCRRG_FLAG value |  |
| RT_TYP_CD | VARCHAR2 | 30 |  |  | This column holds Rate type value. |  |
| TX_TYP_CD | VARCHAR2 | 30 |  |  | This column holds Tax type value. |  |
| ACTY_TYP_CD | VARCHAR2 | 30 |  |  | This column holds Activity type. |  |
| MLT_CD | VARCHAR2 | 30 |  |  | This column holds Multiply code. |  |
| ACTY_REF_PERD_CD | VARCHAR2 | 30 |  |  | This column holds Activity reference period. |  |
| RT_VAL | NUMBER |  |  |  | This  column  holds Rate value. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| ANN_RT_VAL | NUMBER |  | 15 |  | This column holds Annual rate value. |  |
| CMCD_RT_VAL | NUMBER |  | 15 |  | This column holds Communicated rate value. |  |
| CMCD_REF_PERD_CD | VARCHAR2 | 30 |  |  | This column holds Communicated reference period. |  |
| BNFT_RT_TYP_CD | VARCHAR2 | 30 |  |  | This column holds Benefit rate type. |  |
| PRTT_ENRT_RSLT_ID | NUMBER |  | 18 | Yes | This column holds Foreign key to BEN_PRTT_ENRT_RSLT_F. |  |
| DSPLY_ON_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Display on Enrollment Y or N. |  |
| RT_OVRIDN_FLAG | VARCHAR2 | 30 |  | Yes | This column holds Rate Overriden Y or N. |  |
| RT_OVRIDN_THRU_DT | DATE |  |  |  | This column holds Rate overriden through date. |  |
| ELCTNS_MADE_DT | DATE |  |  |  | This column holds Elections made date. |  |
| ELEMENT_ENTRY_VALUE_ID | NUMBER |  | 18 |  | Foreign key to PAY_ELEMENT_ENTRY_VALUES_F. |  |
| PRTT_RT_VAL_STAT_CD | VARCHAR2 | 30 |  |  | This column holds Participant rate value status. |  |
| CVG_AMT_CALC_MTHD_ID | NUMBER |  | 18 |  | Foreign key to BEN_CVG_AMT_CALC_MTHD_F. |  |
| ACTL_PREM_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTL_PREM_F. |  |
| COMP_LVL_FCTR_ID | NUMBER |  | 18 |  | Foreign Key to BEN_COMP_LVL_FCTR_F. |  |
| ACTY_BASE_RT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTY_BASE_RT_F. |  |
| PER_IN_LER_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_PER_IN_LER. |  |
| ENDED_PER_IN_LER_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_PER_IN_LER. |  |
| PRV_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| PRV_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Participant Rate Attributes (BEN_PRTT_RT_VAL_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| PRTT_REIMBMT_RQST_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_PRTT_REIMBMT_RQST_F. |  |
| PRTT_RMT_APRVD_FR_PYMT_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_PRTT_RMT_APRVD_FR_PYMT_F. |  |
| PP_IN_YR_USED_NUM | NUMBER |  | 18 |  | This column holds Pay Periods in the year used. |  |
| PK_ID | NUMBER |  | 18 |  | Primary Key of the table to which rate row is linked to |  |
| PK_ID_TABLE_NAME | VARCHAR2 | 100 |  |  | Name of the table whose primary key is linked to rate row. |  |
| ORDR_NUM | NUMBER |  | 18 |  | This column holds Order Number value |  |
| RATE_DISPLAY_CD | VARCHAR2 | 30 |  |  | This column holds ‘P’ –Primary, ‘S’ –Secondary and ‘O’ -Others |  |
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
| BEN_PRTT_RT_VAL_FK3 | Non Unique | Default | PER_IN_LER_ID |
| BEN_PRTT_RT_VAL_FK4 | Non Unique | Default | ENDED_PER_IN_LER_ID |
| BEN_PRTT_RT_VAL_N1 | Non Unique | Default | PRTT_ENRT_RSLT_ID |
| BEN_PRTT_RT_VAL_N2 | Non Unique | Default | ELEMENT_ENTRY_VALUE_ID |
| BEN_PRTT_RT_VAL_N3 | Non Unique | Default | PRTT_REIMBMT_RQST_ID |
| BEN_PRTT_RT_VAL_N5 | Non Unique | Default | ACTY_BASE_RT_ID |
| BEN_PRTT_RT_VAL_PK1 | Unique | Default | PRTT_RT_VAL_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
