# ANC_PROCESS_MESSAGES

Table Stores Absence Process Messages

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancprocessmessages-11105.html#ancprocessmessages-11105](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancprocessmessages-11105.html#ancprocessmessages-11105)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PROCESS_MESSAGES_PK | MESSAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MESSAGE_ID | NUMBER |  | 18 | Yes | Process Message Id |
| MESSAGE_TYPE | VARCHAR2 | 30 |  |  | Process Message Type |
| SOURCE_FLOW | VARCHAR2 | 30 |  |  | Process Message Source Flow |
| PROCESS_NAME | VARCHAR2 | 30 |  |  | Process Name |
| PROCESS_KEY_ATTRIBUTE | VARCHAR2 | 30 |  |  | Process Identification Key Attribute |
| PROCESS_KEY_ATTRIBUTE_VALUE | NUMBER |  | 18 |  | Process Identification Key Attribute Value |
| PROCESS_CONTEXT | CLOB |  |  |  | Process Message Context Map |
| MSG_TEXT | VARCHAR2 | 2000 |  |  | Process Message Text |
| MSG_VALIDITY | VARCHAR2 | 20 |  |  | Process Message Validity |
| STACK_TRACE | CLOB |  |  |  | Process Message Stack Trace |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ANC_CATEGORY | VARCHAR2 | 2000 |  |  | ANC_CATEGORY |
| ANC_CHAR1 | VARCHAR2 | 2000 |  |  | ANC_CHAR1 |
| ANC_CHAR2 | VARCHAR2 | 2000 |  |  | ANC_CHAR2 |
| ANC_CHAR3 | VARCHAR2 | 2000 |  |  | ANC_CHAR3 |
| ANC_CHAR4 | VARCHAR2 | 2000 |  |  | ANC_CHAR4 |
| ANC_CHAR5 | VARCHAR2 | 2000 |  |  | ANC_CHAR5 |
| ANC_NUMBER1 | NUMBER |  |  |  | ANC_NUMBER1 |
| ANC_NUMBER2 | NUMBER |  |  |  | ANC_NUMBER2 |
| ANC_NUMBER3 | NUMBER |  |  |  | ANC_NUMBER3 |
| ANC_NUMBER4 | NUMBER |  |  |  | ANC_NUMBER4 |
| ANC_NUMBER5 | NUMBER |  |  |  | ANC_NUMBER5 |
| ANC_DATE1 | DATE |  |  |  | ANC_DATE1 |
| ANC_DATE2 | DATE |  |  |  | ANC_DATE2 |
| ANC_DATE3 | DATE |  |  |  | ANC_DATE3 |
| ANC_DATE4 | DATE |  |  |  | ANC_DATE4 |
| ANC_DATE5 | DATE |  |  |  | ANC_DATE5 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PROCESS_MESSAGES_N1 | Non Unique | Default | PROCESS_NAME, PROCESS_KEY_ATTRIBUTE_VALUE |
| ANC_PROCESS_MESSAGES_U1 | Unique | Default | MESSAGE_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
