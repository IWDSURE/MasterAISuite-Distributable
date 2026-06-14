# BEN_RPTG_GRP

BEN_RPTG_GRP identifies a way in which plans and/or programs may be grouped for reporting and administration purposes.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benrptggrp-24381.html#benrptggrp-24381](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benrptggrp-24381.html#benrptggrp-24381)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_RPTG_GRP_PK | RPTG_GRP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| RPTG_GRP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| NAME | VARCHAR2 | 240 |  |  | Name of the reporting group. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| RPTG_PRPS_CD | VARCHAR2 | 30 |  |  | Reporting purpose. |  |
| RPG_DESC | VARCHAR2 | 240 |  |  | Reporting group description. |  |
| BNR_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| BNR_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Reporting Group Attributes (BEN_RPTG_GRP_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| FUNCTION_CODE | VARCHAR2 | 30 |  |  | Function Code |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation Code |  |
| ORDR_NUM | NUMBER |  | 18 |  | Order Number |  |
| GLOBAL_FLAG | VARCHAR2 | 30 |  |  | Indicates exposure to legal entities. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_RPTG_GRP_N1 | Non Unique |  | NAME |
| BEN_RPTG_GRP_PK | Unique | Default | RPTG_GRP_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
