# BEN_OPT_F

BEN_OPT_F  identifies compensation alternatives, typically in coverage and investment choices,  which are provided by one or more plans.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benoptf-17635.html#benoptf-17635](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benoptf-17635.html#benoptf-17635)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_OPT_F_PK | OPT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| OPT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the option. |  |
| CMBN_PTIP_OPT_ID | NUMBER |  | 18 |  | Foreign key to BEN_CMBN_PTIP_OPT_F. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| OPT_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| OPT_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Option Attributes (BEN_OPT_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| INVK_WV_OPT_FLAG | VARCHAR2 | 30 |  | Yes | Invoke Waive Option Y or N. |  |
| RQD_PERD_ENRT_NENRT_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |  |
| RQD_PERD_ENRT_NENRT_UOM | VARCHAR2 | 30 |  |  | Required period of enrollment unit of measure. |  |
| RQD_PERD_ENRT_NENRT_VAL | NUMBER |  | 18 |  | Required period of enrollment value. |  |
| SHORT_CODE | VARCHAR2 | 30 |  |  | Short Code |  |
| SHORT_NAME | VARCHAR2 | 30 |  |  | short Name |  |
| MAPPING_TABLE_PK_ID | NUMBER |  | 18 |  | Primary key of mapping table row to which option row is mapped to |  |
| MAPPING_TABLE_NAME | VARCHAR2 | 60 |  |  | Name of the table to which option is mapped to |  |
| COMPONENT_REASON | VARCHAR2 | 30 |  |  | Component Reason |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| LEGISLATION_SUBGROUP | VARCHAR2 | 30 |  |  | Further identifies the legislation of startup data. |  |
| GROUP_OPT_ID | NUMBER |  | 18 |  | Group Option id. |  |
| GLOBAL_FLAG | VARCHAR2 | 30 |  |  | Indicates exposure to legal entities. |  |
| CARRIER_OPT_NAME | VARCHAR2 | 240 |  |  | Carrier option name. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_OPT_F_FK3 | Non Unique | Default | GROUP_OPT_ID |
| BEN_OPT_F_N1 | Non Unique | Default | CMBN_PTIP_OPT_ID |
| BEN_OPT_F_N2 | Non Unique | Default | MAPPING_TABLE_NAME |
| BEN_OPT_F_N3 | Non Unique | Default | NAME |
| BEN_OPT_F_PK | Unique | Default | OPT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
