# IRC_MP_GIG_MEDIA_LINKS

Stores all the media links for a Gig.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpgigmedialinks-13126.html#ircmpgigmedialinks-13126](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpgigmedialinks-13126.html#ircmpgigmedialinks-13126)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MP_GIG_MEDIA_LINKS_PK | GIG_MEDIA_LINK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GIG_MEDIA_LINK_ID | NUMBER |  | 18 | Yes | This column is the Primary Key column of the IRC_MP_GIG_MEDIA_LINKS which is unique and not null. |
| MEDIA_LINK_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_MEDIA_LINKS_B. |
| GIG_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_MP_GIGS_B table |
| SEQUENCE_NUMBER | NUMBER |  | 9 |  | Indicates the sequence of the media link. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MP_GIG_MEDIA_LINKS_FK1 | Non Unique | Default | MEDIA_LINK_ID |
| IRC_MP_GIG_MEDIA_LINKS_FK2 | Non Unique | Default | GIG_ID |
| IRC_MP_GIG_MEDIA_LINKS_PK | Unique | Default | GIG_MEDIA_LINK_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
