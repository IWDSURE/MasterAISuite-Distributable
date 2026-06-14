# HWR_MSG_MESSAGE_B

The message table stores information about message that needs to be sent to an user in one or more sources.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmsgmessageb-17051.html#hwrmsgmessageb-17051](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmsgmessageb-17051.html#hwrmsgmessageb-17051)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_MSG_MESSAGE_B_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This is the primary key for this table. The number should be generated from the sequence. |
| MESSAGE_TYPE | VARCHAR2 | 30 |  | Yes | This is the type of message that is sent to profiles. |
| MESSAGE_SUBJECT | VARCHAR2 | 50 |  | Yes | This is the subject line of the message. |
| MESSAGE_TEXT | CLOB |  |  |  | This is the body of the message. |
| IMAGE_FILE | BLOB |  |  |  | This column is used to store the image file |
| MESSAGE_PROPS | VARCHAR2 | 4000 |  |  | This is a set of message properties, serialized as XML. |
| POST_DATE | TIMESTAMP |  |  | Yes | This is the date when the message needs to be posted |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_MSG_MESSAGE_B_U1 | Unique | FUSION_TS_TX_DATA | ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
