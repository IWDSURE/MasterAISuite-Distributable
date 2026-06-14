# BEN_COMP_LVL_FCTR

BEN_COMP_LVL_FCTR  identifies how to calculate a person's compensation level,for example, base pay, for such purposes as determining eligibility and calculating rates, in those cases when compensation level is a factor. In addition it identifies a range of compensation  levels, again for eligibility and rate purposes.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencomplvlfctr-26028.html#bencomplvlfctr-26028](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencomplvlfctr-26028.html#bencomplvlfctr-26028)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_COMP_LVL_FCTR_PK | COMP_LVL_FCTR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| COMP_LVL_FCTR_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the compensation level factor. |  |
| COMP_LVL_DET_CD | VARCHAR2 | 30 |  |  | Compensation determination type. |  |
| COMP_LVL_DET_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| COMP_LVL_UOM | VARCHAR2 | 30 |  |  | Compensation level unit of measure. |  |
| COMP_SRC_CD | VARCHAR2 | 30 |  |  | Compensation source. |  |
| NO_MN_COMP_FLAG | VARCHAR2 | 30 |  | Yes | No Minimum Compensation Y or N. |  |
| NO_MX_COMP_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Compensation Y or N. |  |
| MX_COMP_VAL | NUMBER |  |  |  | Maximum compensation value. |  |
| MN_COMP_VAL | NUMBER |  |  |  | Minimum compensation value. |  |
| RNDG_CD | VARCHAR2 | 30 |  |  | Rounding code. |  |
| RNDG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| BALANCE_TYPE_ID | NUMBER |  | 18 |  | System-generated primary key column from PAY_BALANCE_TYPES. |  |
| BNFTS_BAL_ID | NUMBER |  | 18 |  | Foreign key to BEN_BNFTS_BAL_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| CLF_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| CLF_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Compensation Factor Attributes (BEN_COMP_LVL_FCTR_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| COMP_ALT_VAL_TO_USE_CD | VARCHAR2 | 30 |  |  | Compensation alternative value to use code. |  |
| STTD_SAL_PRDCTY_CD | VARCHAR2 | 30 |  |  | Stated salary periodicity. |  |
| COMP_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| DEFINED_BALANCE_ID | NUMBER |  | 18 |  | Foreign key to PAY_DEFINED_BALANCE. |  |
| PRORATION_FLAG | VARCHAR2 | 30 |  |  | Flag to determine prorated amount |  |
| START_DAY_MO | VARCHAR2 | 4 |  |  | Start Day and month |  |
| END_DAY_MO | VARCHAR2 | 4 |  |  | End Day and month |  |
| START_YEAR | VARCHAR2 | 4 |  |  | Start Year |  |
| END_YEAR | VARCHAR2 | 4 |  |  | End Year |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_COMP_LVL_FCTR_N1 | Non Unique | Default | COMP_LVL_DET_RL |
| BEN_COMP_LVL_FCTR_N2 | Non Unique | Default | RNDG_RL |
| BEN_COMP_LVL_FCTR_N3 | Non Unique | Default | BNFTS_BAL_ID |
| BEN_COMP_LVL_FCTR_N4 | Non Unique | Default | NAME |
| BEN_COMP_LVL_FCTR_PK | Unique | Default | COMP_LVL_FCTR_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
