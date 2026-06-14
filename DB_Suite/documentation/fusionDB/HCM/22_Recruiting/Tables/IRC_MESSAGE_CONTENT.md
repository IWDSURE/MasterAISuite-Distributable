# IRC_MESSAGE_CONTENT

This table stores the message sent  for a person as a reference to support view in browser.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmessagecontent-9941.html#ircmessagecontent-9941](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmessagecontent-9941.html#ircmessagecontent-9941)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MESSAGE_CONTENT_PK | MESSAGE_REFERENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MESSAGE_REFERENCE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CHANNEL_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Lookup codes of type 'ORA_IRC_INTERACTION_TYPE'. |
| MESSAGE_SUBJECT | CLOB |  |  |  | Stores the message subject which has been sent to the person. |
| MESSAGE_CONTENT | CLOB |  |  |  | Stores Message content which has been sent to the person. |
| REQUEST | CLOB |  |  |  | Request details of the message sent. |
| RESPONSE | CLOB |  |  |  | Response data of the message sent. |
| PERSON_ID | NUMBER |  | 18 |  | Stores ID of the person for whom the message content is saved. |
| PHONE_NUMBER | VARCHAR2 | 60 |  |  | Stores Phone number of the person for whom the REQUEST/RESPONSE is saved. |
| MESSAGE_LANGUAGE | VARCHAR2 | 32 |  |  | Stores the candidate preferred language for the message. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| UMS_MSG_ID | VARCHAR2 | 256 |  |  | Stores UMS Message ID |
| STATUS | VARCHAR2 | 256 |  |  | Status of the notification |
| ERROR | CLOB |  |  |  | Error during the process |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MESSAGE_CONTENT_FK1 | Non Unique | Default | PERSON_ID |
| IRC_MESSAGE_CONTENT_N1 | Non Unique | Default | CREATION_DATE |
| IRC_MESSAGE_CONTENT_PK | Unique | Default | MESSAGE_REFERENCE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
