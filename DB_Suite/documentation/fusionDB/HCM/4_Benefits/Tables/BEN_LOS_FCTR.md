# BEN_LOS_FCTR

BEN_LOS_FCTR  identifies how to calculate a person's length of service for such purposes as determining eligibility and calculating rates, in those cases when length of service is a factor. In  addition, it identifies a range of lengths of service, again for eligibility and rate purposes.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlosfctr-7188.html#benlosfctr-7188](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlosfctr-7188.html#benlosfctr-7188)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LOS_FCTR_PK | LOS_FCTR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| LOS_FCTR_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the length of service factor. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| LOS_DET_CD | VARCHAR2 | 30 |  |  | Length of service determination code. |  |
| LOS_DET_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| MN_LOS_NUM | NUMBER |  |  |  | Minimum length of service. |  |
| MX_LOS_NUM | NUMBER |  |  |  | Maximum length of service. |  |
| NO_MX_LOS_NUM_APLS_FLAG | VARCHAR2 | 30 |  | Yes | No Maximum Length of Service Number Applies Y or N. |  |
| NO_MN_LOS_NUM_APLS_FLAG | VARCHAR2 | 30 |  | Yes | No Minimum Length of Service Number Applies Y or N. |  |
| RNDG_CD | VARCHAR2 | 30 |  |  | Rounding code. |  |
| RNDG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| LOS_DT_TO_USE_CD | VARCHAR2 | 30 |  |  | Length of service date to use code. |  |
| LOS_DT_TO_USE_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| LOS_UOM | VARCHAR2 | 30 |  |  | Length of service unit of measure. |  |
| LSF_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LSF_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Length Of Service Factor Attributes (BEN_LOS_FCTR_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| USE_OVERID_SVC_DT_FLAG | VARCHAR2 | 30 |  | Yes | Use Override Service Date Y or N. |  |
| HRS_ALT_VAL_TO_USE_CD | VARCHAR2 | 30 |  |  | Hours worked alternative value to use code. |  |
| LOS_CALC_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| LOS_ALT_VAL_TO_USE_CD | VARCHAR2 | 30 |  |  | Length of service alternative value to use code. |  |
| CONFIG_ID_1 | NUMBER |  | 18 |  | New Generic Column |  |
| CONFIG_ID_2 | NUMBER |  | 18 |  | New Generic Column |  |
| CONFIG_NUM_1 | NUMBER |  |  |  | New Genric Number Column |  |
| CONFIG_NUM_2 | NUMBER |  |  |  | New Genric Number Column |  |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | New Genric Character Column |  |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | New Genric Character Column |  |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | New Genric Character Column |  |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | New Genric Character Column |  |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | New Genric Character Column |  |
| CONFIG_DATE_1 | DATE |  |  |  | New Genric Date Column |  |
| CONFIG_DATE_2 | DATE |  |  |  | New Genric Date Colum |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LOS_FCTR_N1 | Non Unique | Default | LOS_DET_RL |
| BEN_LOS_FCTR_N2 | Non Unique | Default | LOS_DT_TO_USE_RL |
| BEN_LOS_FCTR_N3 | Non Unique | Default | RNDG_RL |
| BEN_LOS_FCTR_N4 | Non Unique | Default | NAME |
| BEN_LOS_FCTR_PK | Unique | Default | LOS_FCTR_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
