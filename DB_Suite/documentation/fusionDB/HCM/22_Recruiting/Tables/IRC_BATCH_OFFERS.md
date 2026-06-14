# IRC_BATCH_OFFERS

Stores all the offer batch related details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbatchoffers-18944.html#ircbatchoffers-18944](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbatchoffers-18944.html#ircbatchoffers-18944)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_BATCH_OFFERS_PK | BATCH_OFFER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_OFFER_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 |  | Requisition Id of the Source Offer. |
| SOURCE_OFFER_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_OFFERS table. Refers to the Job submission. |
| BULK_ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_BULK_ACTIONS table. |
| BATCH_NAME | VARCHAR2 | 240 |  |  | Batch name |
| PROPOSED_START_DATE | DATE |  |  |  | Proposed start date of the new offers created in batch |
| SEND_TO_APPROVAL_FLAG | VARCHAR2 | 1 |  |  | Send offers in the batch to approval. |
| SUBMITTED_BY_PERSON_ID | NUMBER |  | 18 |  | Foreign to key to PER_PERSONS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_BATCH_OFFERS_FK1 | Non Unique | Default | SOURCE_OFFER_ID |
| IRC_BATCH_OFFERS_FK2 | Non Unique | Default | BULK_ACTION_ID |
| IRC_BATCH_OFFERS_FK3 | Non Unique | Default | SUBMITTED_BY_PERSON_ID |
| IRC_BATCH_OFFERS_FK4 | Non Unique | Default | REQUISITION_ID |
| IRC_BATCH_OFFERS_PK | Unique | Default | BATCH_OFFER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
