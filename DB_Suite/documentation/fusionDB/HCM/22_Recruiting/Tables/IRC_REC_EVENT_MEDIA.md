# IRC_REC_EVENT_MEDIA

This table stores the event banner related media details

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventmedia-18510.html#ircreceventmedia-18510](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventmedia-18510.html#ircreceventmedia-18510)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REC_EVENT_MEDIA_PK | EVENT_MEDIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_MEDIA_ID | NUMBER |  | 18 | Yes | Primary Key of this table. Auto-generated value. |
| MEDIA_LINK_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_MEDIA_LINKS_B |
| EVENT_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REC_EVENTS_B |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEQUENCE_NUMBER | NUMBER |  | 9 |  | Indicates the sequence number of the media link |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REC_EVENT_MEDIA_FK1 | Non Unique | Default | EVENT_ID |
| IRC_REC_EVENT_MEDIA_FK2 | Non Unique | Default | MEDIA_LINK_ID |
| IRC_REC_EVENT_MEDIA_PK | Unique | Default | EVENT_MEDIA_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
