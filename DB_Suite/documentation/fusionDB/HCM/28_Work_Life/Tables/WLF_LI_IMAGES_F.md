# WLF_LI_IMAGES_F

This table is used to store images for Thumbnails,Cover Arts.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliimagesf-27178.html#wlfliimagesf-27178](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliimagesf-27178.html#wlfliimagesf-27178)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_IMAGES_F_PK | IMAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| IMAGE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | This is column represents the parent table reference. |
| CONTENT_ID | NUMBER |  | 18 |  | This column represents CONTENT_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| CREATED_BY_ID | NUMBER |  | 18 | Yes | Indicates the person identifier who created the content object. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| IMAGE_TYPE | VARCHAR2 | 64 |  |  | This column represents different image types can be stored in  different Storage Providers |
| HEIGHT | VARCHAR2 | 64 |  |  | This column represent height of image |
| POINT_IN_TIME | NUMBER |  | 18 |  | This column represents position of video in time. Example : 6 second of time frame of video is thumbnail captured |
| STORAGE_PROVIDER | VARCHAR2 | 64 |  |  | This column represents storage servers sources used for images to store binary content. Example : Akamai , UCM. |
| STORAGE_LOCATION | VARCHAR2 | 4000 |  |  | This column represents storage server location used for images to store the binary content. Example : Akamai , UCM. |
| IS_PRIMARY | VARCHAR2 | 1 |  |  | This column represents Is this thumbnail or image used in Learning Items. This will allow values "Y" or "N" |
| STATUS | VARCHAR2 | 64 |  |  | This column represents current status of content image |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_IMAGES_F_N1 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_LI_IMAGES_F_N2 | Non Unique | WLF_LI_IMAGES_F_N2 | CONTENT_ID |
| WLF_LI_IMAGES_F_U1 | Unique | Default | IMAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
