# CEL_FEED_LIKES

Table to hold likes recieved by a person.

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celfeedlikes-28398.html#celfeedlikes-28398](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celfeedlikes-28398.html#celfeedlikes-28398)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_FEED_LIKES_PK | LIKE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LIKE_ID | NUMBER |  | 18 | Yes | Unique identifer for a like |
| PROGRAM_ID | NUMBER |  | 18 | Yes | Program identifier |
| MAIN_OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Main Object type |
| MAIN_OBJECT_KEY | NUMBER |  | 18 | Yes | Main Object key |
| PARENT_OBJECT_TYPE | VARCHAR2 | 30 |  |  | Parent object type |
| PARENT_OBJECT_KEY | NUMBER |  | 18 |  | Parent object key |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Type of object liked |
| OBJECT_KEY | NUMBER |  | 18 | Yes | Key of the object liked |
| PERSON_ID | NUMBER |  | 18 | Yes | Identifer of the person who liked |
| LIKE_TYPE | VARCHAR2 | 30 |  |  | Type of like |
| LIKE_DATE | TIMESTAMP |  |  |  | Date and Time when liked |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_FEED_LIKES_N1 | Non Unique | Default | OBJECT_TYPE, OBJECT_KEY, LIKE_TYPE |
| CEL_FEED_LIKES_N2 | Non Unique | Default | PROGRAM_ID, MAIN_OBJECT_TYPE, MAIN_OBJECT_KEY |
| CEL_FEED_LIKES_PK | Unique | Default | LIKE_ID |
| CEL_FEED_LIKES_UK1 | Unique | Default | PERSON_ID, OBJECT_TYPE, OBJECT_KEY |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
