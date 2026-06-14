# IRC_MESSAGE_DETAIL_LOGS

This table logs all message details data for all communication channels that will help in debugging any issues in HCM Communicate and Recruiting.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmessagedetaillogs-13378.html#ircmessagedetaillogs-13378](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmessagedetaillogs-13378.html#ircmessagedetaillogs-13378)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MESSAGE_DETAIL_LOGS_PK | MESSAGE_DETAIL_LOGS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MESSAGE_DETAIL_LOGS_ID | NUMBER |  | 18 | Yes | Primary Key for the table. System generated. |
| MESSAGE_TRACKING_ID | NUMBER |  | 18 | Yes | Foreign key to the table IRC_MESSAGE_TRACKING. |
| MESSAGE_IDENTIFIER | VARCHAR2 | 400 |  |  | UMS SMTP message ID for email, Id sent by the provider for SMS, etc. Foreign key to the table IRC_INTERACTIONS. |
| MESSAGE_SUBJECT | CLOB |  |  |  | The subject for the message that was sent to the person. |
| MESSAGE_CONTENT | CLOB |  |  | Yes | The content of the message that was sent to the person. |
| MESSAGE_API_REQUEST | CLOB |  |  |  | Message API request details of the message sent. |
| MESSAGE_API_RESPONSE | CLOB |  |  |  | Message API response data of the message sent. |
| ERROR | CLOB |  |  |  | Details of any error that was encountered in sending out the message. |
| ADDITIONAL_DETAILS | VARCHAR2 | 4000 |  |  | Stores the request details, including headers. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MESSAGE_DETAIL_LOGS_FK1 | Non Unique | Default | MESSAGE_TRACKING_ID |
| IRC_MESSAGE_DETAIL_LOGS_PK | Unique | Default | MESSAGE_DETAIL_LOGS_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
