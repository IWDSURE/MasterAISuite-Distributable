# IRC_MP_PROSPECTS

This table consists of the invited candidates information for the Gig

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpprospects-17332.html#ircmpprospects-17332](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpprospects-17332.html#ircmpprospects-17332)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MP_PROSPECTS_PK | PROSPECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROSPECT_ID | NUMBER |  | 18 | Yes | This column represents the primary key for the table IRC_MP_PROSPECTS |
| GIG_ID | NUMBER |  | 18 | Yes | This column represents the Gig Id for which the candidate is invited.Foreign Key to irc_mp_gigs_b table. |
| PERSON_ID | NUMBER |  | 18 | Yes | This column represents the Person Id of the candidate invited for the given Gig.Foreign Key to PER_PERSONS table. |
| PROSPECT_STATUS | VARCHAR2 | 32 |  | Yes | This column represents the prospect status |
| PROSPECT_TYPE | VARCHAR2 | 32 |  | Yes | This column represents the prospect type |
| APPLICATION_ID | NUMBER |  | 18 |  | This column represents the Gig Application Id. Foreign Key to irc_mp_gig_applications table |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MP_PROSPECTS_FK2 | Non Unique | Default | APPLICATION_ID |
| IRC_MP_PROSPECTS_FK3 | Non Unique | Default | PERSON_ID |
| IRC_MP_PROSPECTS_PK | Unique | Default | PROSPECT_ID |
| IRC_MP_PROSPECTS_U1 | Unique | Default | GIG_ID, PERSON_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
