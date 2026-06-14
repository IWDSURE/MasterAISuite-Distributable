# BEN_CVG_AMT_CALC_MTHD_F

BEN_CVG_AMT_CALC_MTHD_F  identifies what the coverage amount is or how coverage is calculated for a plan or option in plan.  For example, coverage for the 1 X salary option provided by a group term life insurance plan is calculated by multiplying the participant's plan year annualized salary by 1, with rounding up to the nearest whole 1000's of dollars.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencvgamtcalcmthdf-20977.html#bencvgamtcalcmthdf-20977](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencvgamtcalcmthdf-20977.html#bencvgamtcalcmthdf-20977)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_CVG_AMT_CALC_MTHD_F_PK | CVG_AMT_CALC_MTHD_ID, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| CVG_AMT_CALC_MTHD_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_CVG_AMT_CALC_MTHD_F. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the coverage calculation method. |  |
| INCRMT_VAL | NUMBER |  |  |  | Increment value. |  |
| MX_VAL | NUMBER |  |  |  | Maximum value. |  |
| MN_VAL | NUMBER |  |  |  | Minimum value. |  |
| NO_MX_VAL_DFND_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Value Defined Y or N. |  |
| NO_MN_VAL_DFND_FLAG | VARCHAR2 | 30 |  | Yes | No Minimum Value Defined Y or N. |  |
| RNDG_CD | VARCHAR2 | 30 |  |  | Rounding code. |  |
| RNDG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| VAL | NUMBER |  |  |  | Value. |  |
| VAL_OVRID_ALWD_FLAG | VARCHAR2 | 30 |  | Yes | Value Override Allowed Y or N. |  |
| VAL_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| UOM | VARCHAR2 | 30 |  |  | Unit of measure. |  |
| NNMNTRY_UOM | VARCHAR2 | 30 |  |  | Non-monentary unit of measure. |  |
| BNDRY_PERD_CD | VARCHAR2 | 30 |  |  | Boundary period. |  |
| BNFT_TYP_CD | VARCHAR2 | 30 |  |  | Benefit type. |  |
| CVG_MLT_CD | VARCHAR2 | 30 |  |  | Coverage multiply code. |  |
| RT_TYP_CD | VARCHAR2 | 30 |  |  | Rate type. |  |
| DFLT_VAL | NUMBER |  |  |  | Default value. |  |
| ENTR_VAL_AT_ENRT_FLAG | VARCHAR2 | 30 |  | Yes | Enter Value At Enrollment Y or N. |  |
| DFLT_FLAG | VARCHAR2 | 30 |  | Yes | Default Y or N. |  |
| LWR_LMT_VAL | NUMBER |  |  |  | Lower limit value. |  |
| LWR_LMT_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| UPR_LMT_VAL | NUMBER |  |  |  | Upper limit value. |  |
| UPR_LMT_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| COMP_LVL_FCTR_ID | NUMBER |  | 18 |  | Foreign Key to BEN_COMP_LVL_FCTR_F. |  |
| OIPL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OIPL_F. |  |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| CCM_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| CCM_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Attributes (BEN_CVG_AMT_CALC_MTHD_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| PLIP_ID | NUMBER |  | 18 |  | Foreign key to BEN_PLIP_F. |  |
| CONTEXT_PL_ID | NUMBER |  | 18 |  | CONTEXT_PL_ID |  |
| CONTEXT_OPT_ID | NUMBER |  | 18 |  | CONTEXT_OPT_ID |  |
| COMP_OBJ_TYPE | VARCHAR2 | 30 |  |  | COMP_OBJ_TYPE |  |
| ACTY_BASE_RT_ID | NUMBER |  | 18 |  | ACTY_BASE_RT_ID |  |
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
| BEN_CVG_AMT_CALC_MTHD_F_FK3 | Non Unique | Default | COMP_LVL_FCTR_ID |
| BEN_CVG_AMT_CALC_MTHD_F_N1 | Non Unique | Default | OIPL_ID |
| BEN_CVG_AMT_CALC_MTHD_F_N3 | Non Unique | Default | PL_ID |
| BEN_CVG_AMT_CALC_MTHD_F_N6 | Non Unique | Default | PLIP_ID |
| BEN_CVG_AMT_CALC_MTHD_F_N7 | Non Unique | Default | UPPER("NAME") |
| BEN_CVG_AMT_CALC_MTHD_F_PK | Unique | Default | CVG_AMT_CALC_MTHD_ID, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
