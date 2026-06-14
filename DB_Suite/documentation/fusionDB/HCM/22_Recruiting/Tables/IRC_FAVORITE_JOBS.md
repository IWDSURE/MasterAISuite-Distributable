# IRC_FAVORITE_JOBS

This table stores all the favourite jobs for a person.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircfavoritejobs-5022.html#ircfavoritejobs-5022](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircfavoritejobs-5022.html#ircfavoritejobs-5022)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_FAVORITE_JOBS_PK | FAVORITE_JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FAVORITE_JOB_ID | NUMBER |  | 18 | Yes | Primary key for the table. Populated based on global sequence. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITIONS_B table. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_PERSONS table. PersonId of the person for whom the Favorite Job is stored. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_FAVORITE_JOBS_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_FAVORITE_JOBS_FK2 | Non Unique | Default | PERSON_ID |
| IRC_FAVORITE_JOBS_PK | Unique | Default | FAVORITE_JOB_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
