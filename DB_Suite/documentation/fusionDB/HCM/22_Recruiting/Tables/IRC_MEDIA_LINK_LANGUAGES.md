# IRC_MEDIA_LINK_LANGUAGES

Association table between a media link and a language.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmedialinklanguages-9838.html#ircmedialinklanguages-9838](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmedialinklanguages-9838.html#ircmedialinklanguages-9838)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MEDIA_LINK_LANGUAGES_PK | MEDIA_LINK_LANGUAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MEDIA_LINK_LANGUAGE_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| MEDIA_LINK_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_MEDIA_LINKS_B table. |
| LANGUAGE_CODE | VARCHAR2 | 4 |  | Yes | Language code for which this media link is applicable. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MEDIA_LINK_LANGUAGES_FK1 | Non Unique | Default | MEDIA_LINK_ID |
| IRC_MEDIA_LINK_LANGUAGES_PK | Unique | Default | MEDIA_LINK_LANGUAGE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
