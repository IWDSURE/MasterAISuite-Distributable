# HRC_MESSAGE_INCOMING

This table is used to store the incoming messages. The messages can be email, SMS or any other form of communication.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** hrc_message_inbound

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessageincoming-15966.html#hrcmessageincoming-15966](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessageincoming-15966.html#hrcmessageincoming-15966)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_MESSAGE_INCOMING_PK | MESSAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MESSAGE_ID | NUMBER |  | 18 | Yes | Primary key too represent incoming message |
| SUBJECT | VARCHAR2 | 2000 |  |  | Subject of the message or Message itself in case of short message like SMS |
| WORKFLOW_NAME | VARCHAR2 | 50 |  |  | Name of the workflow which read the email |
| WORKFLOW_CODE | VARCHAR2 | 50 |  |  | Workflow code which have processed this message |
| SERVER_MESSAGE_ID | VARCHAR2 | 20 |  |  | Message Id of the email in the Server. |
| FROM_ADDRESS | VARCHAR2 | 200 |  |  | Address from which message is recieved |
| ACCOUNT_ID | NUMBER |  | 18 |  | List of comma seperated address to which message is intented to |
| MESSAGE_DATA | CLOB |  |  |  | Large message Data like content and Headers |
| MESSAGE_TYPE | VARCHAR2 | 20 |  |  | Type of the message like EMAIL , SMS |
| IS_MESSAGE_READ | VARCHAR2 | 1 |  |  | Will take value Y or N to indicate whether message is read and processed |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| MESSAGE_PROCESSING_STATUS | VARCHAR2 | 20 |  |  | Status of the message processing |
| ATTACHMENT_COUNT | NUMBER |  | 3 |  | Number of attachments present |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_MESSAGE_INCOMING_PK | Unique | HRC_MESSAGE_INCOMING_PK | MESSAGE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
