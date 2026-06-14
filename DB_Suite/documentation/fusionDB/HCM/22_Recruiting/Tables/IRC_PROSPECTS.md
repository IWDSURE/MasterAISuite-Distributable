# IRC_PROSPECTS

This table stores all prospects related to a Requisition.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircprospects-8730.html#ircprospects-8730](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircprospects-8730.html#ircprospects-8730)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_PROSPECTS_PK | PROSPECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROSPECT_ID | NUMBER |  | 18 | Yes | Primary key of the table. Populated by global sequence. |
| OBJECT_STATUS | VARCHAR2 | 40 |  | Yes | Stores whether the record is active or soft deleted. Used in soft delete functionality |
| CANDIDATE_PERSON_ID | NUMBER |  | 18 | Yes | Stores the PersonId of the candidate who is added as a prospect. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Reference to the Requisition against which this prospect is created. Foreign key to IRC_REQUISITIONS_B table. |
| PROSPECT_TYPE_CODE | VARCHAR2 | 40 |  | Yes | Stores the type of the prospect i.e Match or Referral etc. |
| PROSPECT_STATUS_CODE | VARCHAR2 | 40 |  |  | Stores the status of the prospect i.e active or not interested etc. |
| SUBMISSION_ID | NUMBER |  | 18 |  | Stores the Submission created against this prospect. Foreign key to IRC_SUBMISSIONS table. |
| REFERRAL_ID | NUMBER |  | 18 |  | Stores the Referral from which the prospect was created. Foreign key to IRC_REFERRALS table. |
| ADDED_BY_PERSON_ID | NUMBER |  | 18 |  | Stores the PersonId who added this prospect. Foreign key to PER_PERSONS table. |
| CONTEXT_TYPE_CODE | VARCHAR2 | 40 |  |  | Stores the context from where this prospect was added i.e Requsition or Candidate Pool or Candidate Search |
| CONTEXT_ID | NUMBER |  | 18 |  | Stores the ID of the reference object from where this Prospect was added i.e REQUISITION_ID or CANDIDATE_POOL_ID. Will be null incase of Candidate Search. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_PROSPECTS_FK1 | Non Unique | Default | CANDIDATE_PERSON_ID |
| IRC_PROSPECTS_FK2 | Non Unique | Default | REQUISITION_ID |
| IRC_PROSPECTS_FK3 | Non Unique | Default | SUBMISSION_ID |
| IRC_PROSPECTS_FK4 | Non Unique | Default | REFERRAL_ID |
| IRC_PROSPECTS_PK | Unique | Default | PROSPECT_ID |
| IRC_PROSPECTS_N1 | Non Unique | Default | LAST_UPDATE_DATE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
