# IRC_MP_IGNORED_CANDIDATES

This table consists of the ignored candidates information from the recommendations for the Gig

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpignoredcandidates-24618.html#ircmpignoredcandidates-24618](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpignoredcandidates-24618.html#ircmpignoredcandidates-24618)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MP_IGNORED_CANDIDATES_PK | IGNORED_CANDIDATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| IGNORED_CANDIDATE_ID | NUMBER |  | 18 | Yes | This column represents the primary key for the table IRC_MP_IGNORED_CANDIDATES |
| GIG_ID | NUMBER |  | 18 | Yes | This column represents the Gig Id for which the candidate is ignored.Foreign Key to irc_mp_gigs_b table. |
| PERSON_ID | NUMBER |  | 18 | Yes | This column represents the Person Id of the candidate ignored for the given Gig.Foreign Key to PER_PERSONS table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MP_IGNORED_CANDIDATES_FK2 | Non Unique | Default | PERSON_ID |
| IRC_MP_IGNORED_CANDIDATES_PK | Unique | Default | IGNORED_CANDIDATE_ID |
| IRC_MP_IGNORED_CANDIDATES_U1 | Unique | Default | GIG_ID, PERSON_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
