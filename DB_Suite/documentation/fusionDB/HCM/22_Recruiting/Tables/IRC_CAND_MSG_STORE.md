# IRC_CAND_MSG_STORE

This table stores a dump of the email and SMS content  as it is used to process newly received emails and SMS.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandmsgstore-22329.html#irccandmsgstore-22329](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandmsgstore-22329.html#irccandmsgstore-22329)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_MSG_STORE_PK | CAND_MSG_STORE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_MSG_STORE_ID | NUMBER |  | 18 | Yes | Primary key for the IRC_CAND_MSG_STORE table. |
| MSG_TYPE | VARCHAR2 | 20 |  | Yes | This is a discriminator column .possible values will be ORA_EMAIL/ORA_SMS |
| PROCESSING_STATUS | VARCHAR2 | 30 |  | Yes | Processing status of the record.'ORA_NEW' when the message dump row is created (default value).
'ORA_PROCESSED' when the processing is successful.'ORA_FAILED' if the processing fails even after retries. |
| REFERENCE_ID | NUMBER |  |  |  | Store INTERACTION_ID in case of SMS.
CAND_MSG_ID in case of Email (Optional). |
| RETRY_COUNT | NUMBER |  | 2 |  | How many times the batch job has tried to process the record. |
| MESSAGE_DUMP | CLOB |  |  |  | Email or SMS raw content |
| PROCESSING_ERROR_MESSAGE | CLOB |  |  |  | Error message while processing the row |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_MSG_STORE_N1 | Non Unique | Default | MSG_TYPE, PROCESSING_STATUS, CAND_MSG_STORE_ID |
| IRC_CAND_MSG_STORE_PK | Unique | Default | CAND_MSG_STORE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
