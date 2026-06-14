# IRC_MP_FAVOURITES

This table consist of all the other favorite opportunities of the OpSeeker except permanent jobs as favorite jobs of the candidate will be retrieved from the existing irc_favorite_jobs table.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpfavourites-18207.html#ircmpfavourites-18207](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpfavourites-18207.html#ircmpfavourites-18207)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MP_FAVOURITES_PK | FAVOURITE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FAVOURITE_ID | NUMBER |  | 18 | Yes | this column indicates primary key of the table IRC_MP_FAVORITES |
| PERSON_ID | NUMBER |  | 18 | Yes | This column indicates person who choose this favourite, Foreign Key to PER_PERSONS table |
| CONTEXT_ID | NUMBER |  | 18 |  | This column indicates context id of this favorite |
| CONTEXT_TYPE | VARCHAR2 | 240 |  |  | This column indicates Context Type of this favorite |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MP_FAVOURITES_FK1 | Non Unique | Default | PERSON_ID |
| IRC_MP_FAVOURITES_PK | Unique | Default | FAVOURITE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
