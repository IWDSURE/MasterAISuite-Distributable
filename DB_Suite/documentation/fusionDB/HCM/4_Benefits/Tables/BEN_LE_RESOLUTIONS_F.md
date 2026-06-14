# BEN_LE_RESOLUTIONS_F

BEN_LE_RESOLUTIONS_F identifies the legal entities that are striped against life event reasons or programs or plans.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benleresolutionsf-12524.html#benleresolutionsf-12524](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benleresolutionsf-12524.html#benleresolutionsf-12524)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LE_RESOLUTIONS_F_PK | LE_RESOLUTION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LE_RESOLUTION_ID | NUMBER |  | 18 | Yes | LE_RESOLUTION_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEGAL_ENTITY_ID | NUMBER |  | 18 | Yes | LEGAL_ENTITY_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| MAPPING_TABLE_NAME | VARCHAR2 | 30 |  | Yes | MAPPING_TABLE_NAME |
| MAPPING_COLUMN_NAME | VARCHAR2 | 30 |  | Yes | MAPPING_COLUMN_NAME |
| MAPPING_TABLE_PK_ID | NUMBER |  | 18 | Yes | MAPPING_TABLE_PK_ID |
| LRS_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | LRS_ATTRIBUTE_CATEGORY |
| LRS_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE1 |
| LRS_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE2 |
| LRS_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE3 |
| LRS_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE4 |
| LRS_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE5 |
| LRS_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE6 |
| LRS_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE7 |
| LRS_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE8 |
| LRS_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE9 |
| LRS_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE10 |
| LRS_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE11 |
| LRS_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE12 |
| LRS_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE13 |
| LRS_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE14 |
| LRS_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE15 |
| LRS_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE16 |
| LRS_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE17 |
| LRS_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE18 |
| LRS_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE19 |
| LRS_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE20 |
| LRS_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE21 |
| LRS_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE22 |
| LRS_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE23 |
| LRS_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE24 |
| LRS_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE25 |
| LRS_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE26 |
| LRS_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE27 |
| LRS_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE28 |
| LRS_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE29 |
| LRS_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | LRS_ATTRIBUTE30 |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LE_RESOLUTIONS_F_FK1 | Non Unique | Default | LEGAL_ENTITY_ID |
| BEN_LE_RESOLUTIONS_F_N1 | Non Unique | Default | MAPPING_TABLE_NAME, MAPPING_COLUMN_NAME |
| BEN_LE_RESOLUTIONS_F_PK | Unique | Default | LE_RESOLUTION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
