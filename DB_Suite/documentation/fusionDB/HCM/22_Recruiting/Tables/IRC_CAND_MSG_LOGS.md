# IRC_CAND_MSG_LOGS

This table stores a dump of the email and SMS content  as it is used to process newly received emails and SMS.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandmsglogs-30156.html#irccandmsglogs-30156](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandmsglogs-30156.html#irccandmsglogs-30156)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_MSG_LOGS_PK | CAND_MSG_LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_MSG_LOG_ID | NUMBER |  | 18 | Yes | Primary key for the IRC_CAND_MSG_LOGS table. |
| MSG_TYPE | VARCHAR2 | 20 |  | Yes | This is a discriminator column .possible values will be ORA_EMAIL/ORA_SMS |
| PROCESSING_STATUS | VARCHAR2 | 30 |  | Yes | Processing status of the record.'ORA_NEW' when the message dump row is created (default value).
'ORA_PROCESSED' when the processing is successful.'ORA_FAILED' if the processing fails even after retries. |
| REFERENCE_ID | NUMBER |  | 18 |  | Store INTERACTION_ID in case of SMS.
CAND_MSG_ID in case of Email (Optional). |
| RETRY_COUNT | NUMBER |  | 2 |  | How many times the batch job has tried to process the record. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| MESSAGE_IDENTIFIER | VARCHAR2 | 400 |  |  | Contains the message identifier for both email and SMS. For email stores the UMS SMTP message id and for SMS stores the id sent by the provider. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MESSAGE_DUMP | CLOB |  |  |  | Email or SMS raw content from the Email Provider or SMS Provider |
| PROCESSING_ERROR_MESSAGE | CLOB |  |  |  | Error message while processing the row |
| ATTACHMENT_COUNT | NUMBER |  | 2 |  | Total number of attachments available in the email |
| ATTACHMENT_INFO | CLOB |  |  |  | Information about attachments uploaded in UMC or errored out in the form of json |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_MSG_LOGS_N1 | Non Unique | Default | MSG_TYPE, PROCESSING_STATUS |
| IRC_CAND_MSG_LOGS_PK | Unique | Default | CAND_MSG_LOG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
