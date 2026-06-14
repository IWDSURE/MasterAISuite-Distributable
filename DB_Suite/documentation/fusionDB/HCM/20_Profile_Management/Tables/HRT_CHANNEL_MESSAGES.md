# HRT_CHANNEL_MESSAGES

The table stores the email messages for each channel

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtchannelmessages-9835.html#hrtchannelmessages-9835](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtchannelmessages-9835.html#hrtchannelmessages-9835)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_CHANNEL_MESSAGES_PK | MESSAGE_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MESSAGE_ID | NUMBER |  | 18 | Yes | Primary Key of Channel Messages |
| MESSAGE_FROM | VARCHAR2 | 4000 |  |  | Identify the Message Sender Email Address |
| MESSAGE_TO | NUMBER |  | 18 | Yes | Identify the Receipient Channel, Foreign Key to the Channel |
| PERSON_ID | NUMBER |  | 18 |  | Foreign Key to Person |
| EMAIL_FROM | VARCHAR2 | 4000 |  |  | Idenitfy the Original Email Sender's Email Address |
| EMAIL_TO | VARCHAR2 | 4000 |  |  | Idenitfy the Original Email Receipient's Email Addressy |
| EMAIL_CC | VARCHAR2 | 4000 |  |  | Idenitfy the Original Email CC Email Address |
| EMAIL_BCC | VARCHAR2 | 4000 |  |  | Idenitfy the Original Email BCC Email Address |
| EMAIL_DATE | DATE |  |  | Yes | Idenitfy the Original Email Date |
| EMAIL_SUBJECT | VARCHAR2 | 4000 |  |  | Idenitfy the Original Email Subject |
| EMAIL_BODY | CLOB |  |  |  | Idenitfy the Original Email Body |
| TAGS | VARCHAR2 | 4000 |  |  | Idenitfy the Tags Used for the Message |
| STAR | VARCHAR2 | 30 |  |  | Idenitfy the Star Used in the Original Email |
| HASHTAGS | VARCHAR2 | 4000 |  |  | Idenitfy the Hashtags Being Used in the Original Email |
| STATUS | VARCHAR2 | 30 |  |  | Identify the Status of the Message |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| SOURCE | VARCHAR2 | 1000 |  |  | Identify the Source of the Message |
| ATTACHMENT_EXIST_FLAG | VARCHAR2 | 30 |  |  | Indicates if attachment exists for the channel message. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_CHANNEL_MESSAGES_N1 | Non Unique | Default | MESSAGE_TO, PERSON_ID |
| HRT_CHANNEL_MESSAGES_U1 | Unique | Default | MESSAGE_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
