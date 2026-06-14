# BEN_ACRS_PTIP_CVG_F

BEN_ACRS_PTIP_CVG_F holds the maximum coverage or benefit value for multiple plan types in the same program.  For example, if you have plan types of Basic Employee Life Insurance and Supplemental Life Insurance, you could define here that if a person enrolls in  plans of both of these plan types,  the total coverage a person is allowed to elect is 1,000,000.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benacrsptipcvgf-18552.html#benacrsptipcvgf-18552](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benacrsptipcvgf-18552.html#benacrsptipcvgf-18552)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ACRS_PTIP_CVG_PK | ACRS_PTIP_CVG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ACRS_PTIP_CVG_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| MX_CVG_ALWD_AMT | NUMBER |  |  |  | Maximum coverage allowed amount. |  |
| MN_CVG_ALWD_AMT | NUMBER |  |  |  | Minimum coverage allowed amount. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| NAME | VARCHAR2 | 240 |  |  | Name of the across plan type in program coverage. |  |
| PGM_ID | NUMBER |  | 18 |  | Foreign key to BEN_PGM_F. |  |
| APC_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| APC_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Coverage Across Plan Types Attributes (BEN_ACRS_PTIP_CVG_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ACRS_PTIP_CVG_F_N1 | Non Unique | Default | NAME |
| BEN_ACRS_PTIP_CVG_F_N2 | Non Unique | Default | PGM_ID |
| BEN_ACRS_PTIP_CVG_PK | Unique | Default | ACRS_PTIP_CVG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
