# BEN_AGE_FCTR

BEN_AGE_FCTR  identifies how to calculate a person's age for such purposes as determining eligibility and calculating rates, in those cases when  age is a factor.  It may also identify a range of ages, again for  eligibility and rate purposes.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benagefctr-12823.html#benagefctr-12823](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benagefctr-12823.html#benagefctr-12823)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_AGE_FCTR_PK | AGE_FCTR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| AGE_FCTR_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the age factor. |  |
| MX_AGE_NUM | NUMBER |  |  |  | Maximum age. |  |
| MN_AGE_NUM | NUMBER |  |  |  | Minimum age. |  |
| AGE_UOM | VARCHAR2 | 30 |  |  | Age unit of measure. |  |
| NO_MN_AGE_FLAG | VARCHAR2 | 30 |  | Yes | No Minimum Age Y or N. |  |
| NO_MX_AGE_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Age Y or N. |  |
| AGE_DET_CD | VARCHAR2 | 30 |  |  | Age determination code. |  |
| AGE_DET_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| RNDG_CD | VARCHAR2 | 30 |  |  | Rounding code. |  |
| RNDG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| USE_PRTT_SPS_INFO_FLAG | VARCHAR2 | 30 |  |  | Use participant spouse info. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| AGF_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| AGF_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Age Factor Attributes (BEN_AGE_FCTR_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| AGE_TO_USE_CD | VARCHAR2 | 30 |  |  | Person age to use. |  |
| AGE_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_AGE_FCTR_N1 | Non Unique | Default | AGE_DET_RL |
| BEN_AGE_FCTR_N2 | Non Unique | Default | RNDG_RL |
| BEN_AGE_FCTR_N3 | Non Unique | Default | NAME |
| BEN_AGE_FCTR_PK1 | Unique | Default | AGE_FCTR_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
