# IRC_CAND_EMAIL_MESSAGE_DUMP

This table stores a dump of the email content as it is used to process newly received emails from the mailbox.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandemailmessagedump-4217.html#irccandemailmessagedump-4217](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandemailmessagedump-4217.html#irccandemailmessagedump-4217)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_EMAIL_MESSAGE_DUMP_PK | CAND_EMAIL_MESSAGE_DUMP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_EMAIL_MESSAGE_DUMP_ID | NUMBER |  | 18 | Yes | Primary key for the IRC_CAND_EMAIL_MESSAGE_DUMP table. |
| PROCESSING_STATUS | VARCHAR2 | 64 |  | Yes | The processing status for the inbound message. 'ORA_NEW' when the message dump row is created, 'ORA_PROCESSING' when the processing is ongoing and 'ORA_PROCESSED' when the processing is successful, 'ORA_FAILED' if the processing fails even after retries. |
| EMAIL_MESSAGE_DUMP | CLOB |  |  | Yes | Stores all of the content that needs to be saved for an inbound email message. |
| PROCESSING_ERROR_MESSAGE | CLOB |  |  |  | Stores the error in processing the inbound message,, in case there is one. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_EMAIL_MESSAGE_DUMP_PK | Unique | Default | CAND_EMAIL_MESSAGE_DUMP_ID |
| IRC_CAND_EMAIL_MESSAGE_DUMP_U1 | Unique | Default | PROCESSING_STATUS, CAND_EMAIL_MESSAGE_DUMP_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
