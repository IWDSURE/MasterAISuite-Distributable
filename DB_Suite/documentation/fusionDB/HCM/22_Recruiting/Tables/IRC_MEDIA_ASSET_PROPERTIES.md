# IRC_MEDIA_ASSET_PROPERTIES

This table will hold the properties of media assets

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmediaassetproperties-15223.html#ircmediaassetproperties-15223](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmediaassetproperties-15223.html#ircmediaassetproperties-15223)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MEDIA_ASSETS_PROPERTIES_PK | MEDIA_PROPERTY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MEDIA_PROPERTY_ID | NUMBER |  | 18 | Yes | The primary key for this table. System-generated |
| MEDIA_ASSET_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_MEDIA_ASSETS_B table. |
| KEY | VARCHAR2 | 20 |  | Yes | Store the media property key |
| VALUE | VARCHAR2 | 20 |  | Yes | Store the media property value |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MEDIA_ASSET_PROPERTIES_FK1 | Non Unique | Default | MEDIA_ASSET_ID |
| IRC_MEDIA_ASSET_PROPERTIES_N1 | Non Unique | Default | KEY, VALUE |
| IRC_MEDIA_ASSET_PROPERTIES_PK | Unique | Default | MEDIA_PROPERTY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
