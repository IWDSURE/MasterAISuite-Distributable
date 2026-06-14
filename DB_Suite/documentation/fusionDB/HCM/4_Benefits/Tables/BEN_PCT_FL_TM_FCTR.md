# BEN_PCT_FL_TM_FCTR

BEN_PCT_FL_TM_FCTR  identifies a range of percent full time values for such purposes as determining eligibility and calculating rates, in those cases when percent full time is a factor.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpctfltmfctr-19550.html#benpctfltmfctr-19550](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpctfltmfctr-19550.html#benpctfltmfctr-19550)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PCT_FL_TM_FCTR_PK | PCT_FL_TM_FCTR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PCT_FL_TM_FCTR_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| ASMT_TO_USE_CD | VARCHAR2 | 30 |  |  | Assignment to use. |  |
| NAME | VARCHAR2 | 255 |  | Yes | Name of the percent full time factor. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| MX_PCT_VAL | NUMBER |  |  |  | Maximum percent value. |  |
| MN_PCT_VAL | NUMBER |  |  |  | Minimum percent value. |  |
| NO_MN_PCT_VAL_FLAG | VARCHAR2 | 30 |  | Yes | No Minimum Percent Value Y or N. |  |
| NO_MX_PCT_VAL_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Percent Value Y or N. |  |
| USE_PRMRY_ASNT_ONLY_FLAG | VARCHAR2 | 30 |  | Yes | Use Primary Assignment Only Y or N. |  |
| USE_SUM_OF_ALL_ASNTS_FLAG | VARCHAR2 | 30 |  | Yes | Use Sum Of All Assignments Y or N. |  |
| RNDG_CD | VARCHAR2 | 30 |  |  | Rounding code. |  |
| RNDG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| PFF_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| PFF_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Part Time Full Time Factor Attributes (BEN_PCT_FL_TM_FCTR_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PCT_FL_TM_FCTR_N1 | Non Unique | Default | RNDG_RL |
| BEN_PCT_FL_TM_FCTR_N2 | Non Unique | Default | NAME |
| BEN_PCT_FL_TM_FCTR_PK | Unique | Default | PCT_FL_TM_FCTR_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
