# IRC_TRACK_USER_VIEWS

This table is used to track which recruiting objects (Job Applications, Prospects etc) user has viewed.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctrackuserviews-12012.html#irctrackuserviews-12012](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctrackuserviews-12012.html#irctrackuserviews-12012)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TRACK_USER_VIEWS_PK | TRACK_USER_VIEW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TRACK_USER_VIEW_ID | NUMBER |  | 18 | Yes | Primary key for the table. System generated. |
| USER_ID | NUMBER |  | 18 | Yes | Foreign key to PER_USERS table. |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Type of Recruiting object user has accessed. |
| OBJECT_ID | NUMBER |  | 18 | Yes | Froeign key of the Object which user has accessed. |
| LAST_VIEWED_TIME | TIMESTAMP |  |  |  | Stores the time when the object was last accessed. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TRACK_USER_VIEWS_FK1 | Non Unique | Default | USER_ID |
| IRC_TRACK_USER_VIEWS_N1 | Non Unique | Default | OBJECT_TYPE, OBJECT_ID, USER_ID |
| IRC_TRACK_USER_VIEWS_PK | Unique | Default | TRACK_USER_VIEW_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
