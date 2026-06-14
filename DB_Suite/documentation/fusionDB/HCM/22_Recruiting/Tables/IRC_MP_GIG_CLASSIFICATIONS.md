# IRC_MP_GIG_CLASSIFICATIONS

The table to store the classifications associated with a gig

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpgigclassifications-21301.html#ircmpgigclassifications-21301](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpgigclassifications-21301.html#ircmpgigclassifications-21301)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MP_GIG_CLASSIFICATIONS_PK | CLASSIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CLASSIFICATION_ID | NUMBER |  | 18 | Yes | The primary key of the table which uniquely identifies the gig classification |
| GIG_ID | NUMBER |  | 18 |  | Foreign key to the table IRC_MP_GIGS_B |
| JOB_ID | NUMBER |  | 18 |  | Foreign key to the table PER_JOBS_F |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MP_GIG_CLASSIFICATIONS_FK1 | Non Unique | Default | GIG_ID |
| IRC_MP_GIG_CLASSIFICATIONS_FK2 | Non Unique | Default | JOB_ID |
| IRC_MP_GIG_CLASSIFICATIONS_PK | Unique | Default | CLASSIFICATION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
