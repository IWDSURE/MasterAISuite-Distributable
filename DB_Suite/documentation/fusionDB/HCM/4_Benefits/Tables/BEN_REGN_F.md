# BEN_REGN_F

BEN_REGN_F identifies a discreet rule, policy, or requirement defined by a governmental or policy making body  which may govern the administration of one or more benefits.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benregnf-22808.html#benregnf-22808](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benregnf-22808.html#benregnf-22808)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_REGN_F_PK | REGN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| REGN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| NAME | VARCHAR2 | 240 |  |  | Name of the regulation. |  |
| STTRY_CITN_NAME | VARCHAR2 | 240 |  |  | Statutory citation name. |  |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Foreign key to HR_ORGANIZATION_UNITS. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| REG_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| REG_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Regulation Attributes (BEN_REGN_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_REGN_F_FK1 | Non Unique | Default | ORGANIZATION_ID |
| BEN_REGN_F_N1 | Non Unique |  | NAME |
| BEN_REGN_F_PK | Unique | Default | REGN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
