# HRC_MESSAGE_HISTORY

This is the table to store historical data of the messages entry in hrc_communication_messages table. This will capture each action performed on messages.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** hrc_message_history

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessagehistory-12199.html#hrcmessagehistory-12199](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessagehistory-12199.html#hrcmessagehistory-12199)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_MESSAGE_HISTORY_PK | HISTORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HISTORY_ID | NUMBER |  | 18 | Yes | Unique identifier of the message history table. |
| COMMUNICATION_ID | NUMBER |  | 18 |  | Indicates the type of the communication through which the message is being sent. |
| MESSAGE_ID | NUMBER |  | 18 |  | Identifier of the delivery message given. |
| ACTION_PERFORMED | VARCHAR2 | 120 |  |  | Indicates of what action performed for the particular message. |
| HISTORY_OBJECT | VARCHAR2 | 240 |  |  | Records the details of the history activity which has taken place for the communication message. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_MESSAGE_HISTORY_FK1 | Non Unique | HRC_MESSAGE_HISTORY_FK1 | COMMUNICATION_ID |
| HRC_MESSAGE_HISTORY_PK | Unique | HRC_MESSAGE_HISTORY_PK | HISTORY_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
