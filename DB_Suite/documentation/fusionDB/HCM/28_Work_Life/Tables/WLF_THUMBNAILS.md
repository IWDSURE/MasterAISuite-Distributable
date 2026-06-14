# WLF_THUMBNAILS

Table to store of learning item object thumbnails.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfthumbnails-6813.html#wlfthumbnails-6813](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfthumbnails-6813.html#wlfthumbnails-6813)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_THUMBNAILS_PK | THUMBNAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| THUMBNAIL_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| URL | VARCHAR2 | 1000 |  |  | Thumbnail URL |
| THUMBNAIL_TYPE | VARCHAR2 | 32 |  |  | Polymorphic discriminator column { IMAGE, THUMBNAIL ... }. |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | LEARNING_ITEM_ID |
| UUID | VARCHAR2 | 64 |  |  | UUID |
| MIME_TYPE | VARCHAR2 | 32 |  |  | File data format  {.jpg, .pnp ...}. |
| LOCATION | VARCHAR2 | 1024 |  |  | Location/URL to external source. |
| POSITION | NUMBER |  | 18 |  | Index position of the thumbnail. |
| ORIGINAL_WIDTH | NUMBER |  |  |  | ORIGINAL_WIDTH |
| ORIGINAL_HEIGHT | NUMBER |  |  |  | ORIGINAL_HEIGHT |
| CENTER_X | NUMBER |  |  |  | CENTER_X |
| CENTER_Y | NUMBER |  |  |  | CENTER_Y |
| SCALE_FACTOR | NUMBER |  |  |  | SCALE_FACTOR |
| EXTRACTION_STATUS | VARCHAR2 | 30 |  |  | This column stores image processing status. Example ORA_MED_NEW, ORA_MED_COMPLETE, ORA_MED_ERROR etc |
| STORAGE_LOCATION | VARCHAR2 | 4000 |  |  | This column stores location of Storage server path where actual content (Thumbnail/Image) is available |
| STORAGE_PROVIDER | VARCHAR2 | 64 |  |  | This column represents Storage server name where  actual content (Thumbnail/Image) is stored. Example Akamai, UCM etc |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_THUMBNAILS_N1 | Non Unique | Default | THUMBNAIL_TYPE |
| WLF_THUMBNAILS_N2 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_THUMBNAILS_U1 | Unique | Default | THUMBNAIL_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
