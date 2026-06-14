# WLF_CM_THUMBNAILS

Table to store of content object thumbnails.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcmthumbnails-15829.html#wlfcmthumbnails-15829](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcmthumbnails-15829.html#wlfcmthumbnails-15829)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CM_THUMBNAILS_PK | THUMBNAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| THUMBNAIL_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| THUMBNAIL_TYPE | VARCHAR2 | 32 |  |  | Polymorphic discriminator column { IMAGE, THUMBNAIL ... }. |
| TYPE | VARCHAR2 | 32 |  |  | File data format  {.jpg, .pnp ...}. |
| DATA | BLOB |  |  |  | Binary data in local storage. |
| LOCATION | VARCHAR2 | 1024 |  |  | Location/URL to external source. |
| CONTENT_ID | NUMBER |  | 18 |  | Content object the thumbnail belongs to. Foreign key to WLF_CM_CONTENTS_B. |
| POSITION | NUMBER |  | 18 |  | Index position of the thumbnail. |
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
| WLF_CM_THUMBNAILS_N1 | Non Unique | Default | THUMBNAIL_TYPE |
| WLF_CM_THUMBNAILS_N2 | Non Unique | Default | CONTENT_ID |
| WLF_CM_THUMBNAILS_U1 | Unique | Default | THUMBNAIL_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
