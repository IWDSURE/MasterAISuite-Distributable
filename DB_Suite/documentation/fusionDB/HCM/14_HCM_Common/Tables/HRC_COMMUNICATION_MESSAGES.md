# HRC_COMMUNICATION_MESSAGES

Table to Store Communication messages

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** hrc_communication_messages

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccommunicationmessages-31603.html#hrccommunicationmessages-31603](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccommunicationmessages-31603.html#hrccommunicationmessages-31603)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_COMMUNICATION_MESSAGES_PK | COMMUNICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMMUNICATION_ID | NUMBER |  | 24 | Yes | Unique Id for identifying the communication message |
| TRANSACTION_ID | NUMBER |  | 18 |  | Id of transaction for which the communication is for |
| COMMUNICATION_DATA | CLOB |  |  |  | Communication data in Json format |
| USER_GUID | VARCHAR2 | 64 |  |  | Guid of the user to whom the communication is intented. |
| MODULEIDENTIFIER | VARCHAR2 | 60 |  |  | Module Identifier of the process related to what communication is sent |
| PROCESS_ID | NUMBER |  | 18 |  | Process Id of the process related to what the communication is intented to. |
| SUBJECT_CODE | VARCHAR2 | 200 |  |  | Subject code related to message being sent. |
| OBJECT_CODE | VARCHAR2 | 200 |  |  | Object code related to the message being sent. |
| SUBJECT | VARCHAR2 | 100 |  |  | Name of the component which triggered the notification |
| SUBJECT_ID | NUMBER |  | 18 |  | Identifier of the component which triggered the notification. |
| MESSAGE_INSTANCE_ID | VARCHAR2 | 200 |  |  | Correlation id sent by the triggering component to identify the message record. |
| MESSAGE_EXPIRATION_TIME | NUMBER |  | 10 |  | Message Expiration time which will determine the life time of the message. |
| OBJECT | VARCHAR2 | 100 |  |  | Name of the object which is getting modified and related to what communication is sent |
| OBJECT_ID | NUMBER |  | 18 |  | Id of the primary key of the object row related to which the communication is sent out |
| STATUS | VARCHAR2 | 20 |  |  | Status of the communication. It will have values like pending completed failed etc |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Identifier of the enterprise for filtering the records. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| IS_MSG_GETTING_PURGED | VARCHAR2 | 20 |  |  | Flag to indicate if communication message is a candidate for getting purged. |
| MESSAGE_HEADER | VARCHAR2 | 260 |  |  | Indicates the header of the message to be shown in the auditing ui. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_COMMUNICATION_MESSAGES_PK | Unique | HRC_COMMUNICATION_MESSAGES_PK | COMMUNICATION_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
