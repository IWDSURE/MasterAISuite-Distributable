# IRC_MP_GIG_APPLICATIONS

This table list out all the gig submissions of the seeker and also it will list out all the applications submitted by the seekers for a given opportunity.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpgigapplications-19123.html#ircmpgigapplications-19123](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpgigapplications-19123.html#ircmpgigapplications-19123)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MP_GIG_APPLICATIONS_PK | APPLICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| APPLICATION_ID | NUMBER |  | 18 | Yes | This column indicates the primary key column for IRC_MP_GIG_APPLICATIONS table |
| PERSON_ID | NUMBER |  | 18 |  | This column indicates the person who submiited application for a gig, Foreign Key to PER_PERSONS table |
| GIG_ID | NUMBER |  | 18 |  | This column indicates the gig to which this application has submitted, Foreign Key to IRC_MP_GIGS_B table |
| STATUS_CODE | VARCHAR2 | 30 |  |  | This column indicates state of the application in phases |
| OBJECT_STATUS | VARCHAR2 | 30 |  |  | This column indicates object status like ORA_ACTIVE/ORA_DELETED |
| WRITE_UP | CLOB |  |  |  | This column indicates the write up for this application |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MP_GIG_APPLICATIONS_FK1 | Non Unique | Default | GIG_ID |
| IRC_MP_GIG_APPLICATIONS_FK2 | Non Unique | Default | PERSON_ID |
| IRC_MP_GIG_APPLICATIONS_PK | Unique | Default | APPLICATION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
