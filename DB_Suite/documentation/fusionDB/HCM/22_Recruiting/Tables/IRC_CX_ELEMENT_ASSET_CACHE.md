# IRC_CX_ELEMENT_ASSET_CACHE

This table contains data for media asset to use for a given site, element and entity for a period of 24hrs.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxelementassetcache-29994.html#irccxelementassetcache-29994](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxelementassetcache-29994.html#irccxelementassetcache-29994)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_ELEMENT_ASSET_CACHE_PK | ELEMENT_ASSET_CACHE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELEMENT_ASSET_CACHE_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| INTELLIGENT_ASSET_ELEMENT_ID | NUMBER |  | 18 | Yes | Indicates the ElementID that uses the asset. |
| REF_ENTITY_TYPE | VARCHAR2 | 240 |  | Yes | Indicates the usage element type. |
| REF_ENTITY_ID | NUMBER |  | 18 | Yes | Primary Key of entity the element is used for. |
| SITE_NUMBER | VARCHAR2 | 240 |  | Yes | Indicates the site number the element belongs to. |
| SUGGESTED_MEDIA_ASSET_ID | NUMBER |  | 18 | Yes | Indicates the media asset id suggested by GenAI. |
| SUGGESTED_MEDIA_ASSET_URL | VARCHAR2 | 1000 |  | Yes | Stores the URL of the suggested media asset. |
| EXPIRY_DATE | TIMESTAMP |  |  | Yes | Indicates the dateTime the record is considered expired. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_ELEMENT_ASSET_CACHE_N1 | Non Unique | Default | EXPIRY_DATE |
| IRC_CX_ELEMENT_ASSET_CACHE_PK | Unique | Default | ELEMENT_ASSET_CACHE_ID |
| IRC_CX_ELEMENT_ASSET_CACHE_U1 | Unique | Default | INTELLIGENT_ASSET_ELEMENT_ID, REF_ENTITY_TYPE, REF_ENTITY_ID, SITE_NUMBER |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
