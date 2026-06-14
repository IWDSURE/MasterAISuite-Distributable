# BEN_BNFT_VRBL_RT_F

BEN_BNFT_VRBL_RT_F specifies the variable rate profiles used to calculate a rate for a benefit. . For example,  life insurance coverage benefits may be calculated based on whether the person uses tobacco.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbnftvrblrtf-20052.html#benbnftvrblrtf-20052](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbnftvrblrtf-20052.html#benbnftvrblrtf-20052)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BNFT_VRBL_RT_F_PK | BNFT_VRBL_RT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| BNFT_VRBL_RT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |  |
| CVG_AMT_CALC_MTHD_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_CVG_AMT_CALC_MTHD_F. |  |
| VRBL_RT_PRFL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_VRBL_RT_PRFL_F |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| BVR_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| BVR_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Variable Rate Attributes (BEN_BNFT_VRBL_RT_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Columns |
|---|---|---|
| BEN_BNFT_VRBL_RT_F_N1 | Non Unique | CVG_AMT_CALC_MTHD_ID |
| BEN_BNFT_VRBL_RT_F_N2 | Non Unique | VRBL_RT_PRFL_ID |
| BEN_BNFT_VRBL_RT_F_PK | Unique | BNFT_VRBL_RT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
