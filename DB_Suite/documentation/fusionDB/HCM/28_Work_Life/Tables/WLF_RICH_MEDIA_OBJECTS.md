# WLF_RICH_MEDIA_OBJECTS

Table to store rich-media objects details

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** WLF_RICH_MEDIA_OBJECTS

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrichmediaobjects-22656.html#wlfrichmediaobjects-22656](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrichmediaobjects-22656.html#wlfrichmediaobjects-22656)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_RICH_MEDIA_OBJECTS_PK | RICH_MEDIA_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RICH_MEDIA_OBJECT_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| SOURCE_ID | NUMBER |  | 18 | Yes | Source Id of the Object consuming rich media. eg: learning_item_id, content_id |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | Source Type of object like Content, Asset etc |
| CONTENT_FORMAT | VARCHAR2 | 30 |  | Yes | Content format. Denormalized values from wlf_li_content_f.content_format or tracking_type |
| UUID | VARCHAR2 | 64 |  |  | UUID |
| LOCATION | VARCHAR2 | 4000 |  |  | delivery location details of the content |
| STATUS | VARCHAR2 | 30 |  |  | Current status of the richmedia content object |
| UPLOAD_SOURCE | VARCHAR2 | 30 |  |  | Indicates whether the content is uploaded via UI or a bulk process |
| DELIVERY_PROVIDER_ID | NUMBER |  | 18 |  | Delivery Provider account ID of content |
| STORAGE_PROVIDER_ID | NUMBER |  | 18 |  | Storage Provider account ID of content |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_RICH_MEDIA_OBJECTS_N1 | Non Unique | Default | SOURCE_ID |
| WLF_RICH_MEDIA_OBJECTS_N2 | Non Unique | Default | STATUS |
| WLF_RICH_MEDIA_OBJECTS_N3 | Non Unique | Default | CONTENT_FORMAT |
| WLF_RICH_MEDIA_OBJECTS_N4 | Non Unique | Default | DELIVERY_PROVIDER_ID |
| WLF_RICH_MEDIA_OBJECTS_N5 | Non Unique | Default | STORAGE_PROVIDER_ID |
| WLF_RICH_MEDIA_OBJECTS_U1 | Unique | Default | RICH_MEDIA_OBJECT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
