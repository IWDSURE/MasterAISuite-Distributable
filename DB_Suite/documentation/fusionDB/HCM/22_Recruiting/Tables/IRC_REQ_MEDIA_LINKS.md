# IRC_REQ_MEDIA_LINKS

Stores all links for a Requisition.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreqmedialinks-10673.html#ircreqmedialinks-10673](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreqmedialinks-10673.html#ircreqmedialinks-10673)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REQ_MEDIA_LINKS_PK | REQ_MEDIA_LINK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQ_MEDIA_LINK_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| MEDIA_LINK_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_MEDIA_LINKS_B. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITIONS_B. |
| SEQUENCE_NUMBER | NUMBER |  | 9 |  | Indicates the sequence of the media link. |
| SHOW_ON_OFFERS_FLAG | VARCHAR2 | 1 |  |  | Indicates if this requisition media link should be available to show on offers or not. |
| VISIBILITY_CODE | VARCHAR2 | 30 |  |  | Indicates where this media should be visible (external, internal or both) as a lookup code. The corresponding lookup type is ORA_IRC_MEDIA_VISIBILITY. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REQ_MEDIA_LINKS_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_REQ_MEDIA_LINKS_FK2 | Non Unique | Default | MEDIA_LINK_ID |
| IRC_REQ_MEDIA_LINKS_PK | Unique | Default | REQ_MEDIA_LINK_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
