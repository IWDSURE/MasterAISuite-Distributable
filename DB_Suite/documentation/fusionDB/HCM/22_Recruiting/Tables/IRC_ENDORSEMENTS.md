# IRC_ENDORSEMENTS

This table stores endorsement data for requisitions in IRC_REQUISITIONS_B table.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircendorsements-4214.html#ircendorsements-4214](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircendorsements-4214.html#ircendorsements-4214)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_ENDORSEMENTS_PK | ENDORSEMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENDORSEMENT_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |
| OBJECT_STATUS | VARCHAR2 | 40 |  | Yes | Stores whether the record is active or soft deleted. Used in soft delete functionality |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Stores REQUISITION_ID. Foreign Key to IRC_REQUISITIONS_B table. |
| CANDIDATE_PERSON_ID | NUMBER |  | 18 | Yes | Stores PERSON_ID of the candidate. Foreign Key to PER_PERSONS table. |
| ENDORSER_PERSON_ID | NUMBER |  | 18 | Yes | Stores PERSON_ID of the endorser. Foreign Key to PER_PERSONS table. |
| NOTES | VARCHAR2 | 1000 |  |  | Endorsement notes for Hiring Team. |
| RATING | NUMBER |  | 2 |  | Endorsement rating for the candidate. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_ENDORSEMENTS_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_ENDORSEMENTS_FK2 | Non Unique | Default | CANDIDATE_PERSON_ID |
| IRC_ENDORSEMENTS_FK3 | Non Unique | Default | ENDORSER_PERSON_ID |
| IRC_ENDORSEMENTS_PK | Unique | Default | ENDORSEMENT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
