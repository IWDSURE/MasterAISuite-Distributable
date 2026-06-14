# IRC_MEDIA_LINKS_B

Stores links to media contents.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmedialinksb-30936.html#ircmedialinksb-30936](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmedialinksb-30936.html#ircmedialinksb-30936)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MEDIA_LINKS_B_PK | MEDIA_LINK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MEDIA_LINK_ID | NUMBER |  | 18 | Yes | System generated primary key for this entity. |
| MEDIA_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Specifies the type of media (typically video or image) as a lookup code. The corresponding lookup type is ORA_IRC_MEDIA_TYPE. |
| URL | VARCHAR2 | 1000 |  |  | Stores the URL that this link points to. |
| THUMBNAIL_URL | VARCHAR2 | 1000 |  |  | Stores the Thumbnail url for this link |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MEDIA_LINKS_B_PK | Unique | Default | MEDIA_LINK_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
