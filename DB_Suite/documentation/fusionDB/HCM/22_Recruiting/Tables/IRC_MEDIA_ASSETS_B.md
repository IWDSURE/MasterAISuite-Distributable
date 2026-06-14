# IRC_MEDIA_ASSETS_B

This table stores the media asset details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmediaassetsb-6616.html#ircmediaassetsb-6616](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmediaassetsb-6616.html#ircmediaassetsb-6616)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MEDIA_ASSETS_B_PK | MEDIA_ASSET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MEDIA_ASSET_ID | NUMBER |  | 18 | Yes | The primary key for this table. System-generated |
| MEDIA_ASSET_GUID | VARCHAR2 | 64 |  | Yes | Stores the GUID of the uploaded image |
| MEDIA_ASSET_STATUS | VARCHAR2 | 20 |  | Yes | Indicates Active/Inactive |
| CONTEXT | VARCHAR2 | 40 |  | Yes | Indicates the context |
| LINKED_ASSET_ID | NUMBER |  | 18 |  | Stores MEDIA_ASSET_ID value of image asset, its self join of the table. And its FK to self table irc_media_assets_b |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MEDIA_ASSETS_B_FK1 | Non Unique | Default | LINKED_ASSET_ID |
| IRC_MEDIA_ASSETS_B_N1 | Non Unique | Default | CREATION_DATE |
| IRC_MEDIA_ASSETS_B_PK | Unique | Default | MEDIA_ASSET_ID |
| IRC_MEDIA_ASSETS_B_U1 | Unique | Default | CONTEXT, MEDIA_ASSET_GUID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
