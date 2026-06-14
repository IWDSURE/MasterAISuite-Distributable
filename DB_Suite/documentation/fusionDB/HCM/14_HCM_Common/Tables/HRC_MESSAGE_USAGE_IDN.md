# HRC_MESSAGE_USAGE_IDN

This is the table used for storing the consumer identificaiton data for communications.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** hrc_comm_consumer_idn_data

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessageusageidn-6086.html#hrcmessageusageidn-6086](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessageusageidn-6086.html#hrcmessageusageidn-6086)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_MESSAGE_USAGE_IDN_PK | MESSAGE_IDENTIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MESSAGE_IDENTIFICATION_ID | NUMBER |  | 18 | Yes | Unique key to represent the identificaition record |
| INCOMING_MESSAGE_ID | NUMBER |  | 18 |  | Identificaiton key of the message which is being used. |
| SUBJECT_CODE | VARCHAR2 | 200 |  |  | Represents the primary or source entity involved in the callback. |
| OBJECT_CODE | VARCHAR2 | 200 |  |  | Represents the target or related entity linked to the subject |
| CONVERSATION_ID | VARCHAR2 | 200 |  |  | Id which represents the conversation |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_MESSAGE_USAGE_IDN_PK | Unique | HRC_COMM_CONSUMER_IDN_PK | MESSAGE_IDENTIFICATION_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
