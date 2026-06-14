# IRC_REC_EVENT_SITES

This table stores all the published sites of an event.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventsites-17660.html#ircreceventsites-17660](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventsites-17660.html#ircreceventsites-17660)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REC_EVENT_SITES_PK | EVENT_SITE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_SITE_ID | NUMBER |  | 18 | Yes | Primary key for this table. Auto-generated. |
| EVENT_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REC_EVENTS_B |
| SITE_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CX_SITES_B table. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REC_EVENT_SITES_FK1 | Non Unique | Default | EVENT_ID |
| IRC_REC_EVENT_SITES_FK2 | Non Unique | Default | SITE_ID |
| IRC_REC_EVENT_SITES_PK | Unique | Default | EVENT_SITE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
