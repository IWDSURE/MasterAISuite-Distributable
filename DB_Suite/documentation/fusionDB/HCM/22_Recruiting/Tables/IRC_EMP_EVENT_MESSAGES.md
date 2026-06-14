# IRC_EMP_EVENT_MESSAGES

This table stores the details of the employee event messages

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircempeventmessages-28333.html#ircempeventmessages-28333](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircempeventmessages-28333.html#ircempeventmessages-28333)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_EMP_EVENT_MESSAGES_PK | MESSAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MESSAGE_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |
| ACTION_TRACKING_ID | NUMBER |  | 18 | Yes | Stores ACTION_TRACKING_ID. Foreign key to irc_emp_event_action_trk table. |
| ACTION_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores action types supported values are ORA_MSG and ORA_NOTIFICATION. |
| RECIPIENT_PERSON_ID | NUMBER |  | 18 | Yes | Stores RECIPIENT_PERSON_ID. Foreign Key to per_persons table. |
| ADDRESS | VARCHAR2 | 240 |  |  | Stores recipient (Email) Address of the recipient. |
| MESSAGE_DIRECTION | VARCHAR2 | 30 |  |  | Stores the message direction values are ORA_INBOUND and ORA_OUTBOUND. |
| SUBJECT | VARCHAR2 | 4000 |  |  | Stores subject part for the message. |
| BODY | CLOB |  |  |  | Stores body part for the message. |
| MSG_IDENTIFIER | VARCHAR2 | 128 |  |  | Stores Unified Message Service (UMS) message Id. |
| MSG_STATUS_CODE | VARCHAR2 | 30 |  |  | Stores the message status as a lookup code. The corresponding lookup type is ORA_IRC_CMT_MSG_STATUS_TYPE. |
| MSG_SENT_TS | TIMESTAMP |  |  |  | Stores message sent time  for this message. |
| DELIVERY_ERROR_MESSAGE | VARCHAR2 | 1000 |  |  | Stores the reason for error status of the execution. |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | Stores the ESS Job Request ID of the current recipient row. |
| MSG_RETRY_COUNT | NUMBER |  |  |  | stores current message retry count. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_EMP_EVENT_MESSAGES_FK1 | Non Unique | Default | ACTION_TRACKING_ID |
| IRC_EMP_EVENT_MESSAGES_FK2 | Non Unique | Default | RECIPIENT_PERSON_ID |
| IRC_EMP_EVENT_MESSAGES_PK | Unique | Default | MESSAGE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
