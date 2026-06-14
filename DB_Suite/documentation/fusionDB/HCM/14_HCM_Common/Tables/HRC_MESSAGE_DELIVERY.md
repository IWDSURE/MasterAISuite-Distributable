# HRC_MESSAGE_DELIVERY

Table to track the messages delivery

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** hrc_message_delivery

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessagedelivery-17341.html#hrcmessagedelivery-17341](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessagedelivery-17341.html#hrcmessagedelivery-17341)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_MESSAGE_DELIVERY_PK | MESSAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MESSAGE_ID | NUMBER |  |  | Yes | Unique Identifier for the message which is being sent out to through different media. |
| RESPONSE_REQUIRED | VARCHAR2 | 1 |  |  | This field indicates whether response is required for the specific message delivery or not. |
| RESPONSE_STATUS | VARCHAR2 | 50 |  |  | The response status which is sent as part of user response. Will have values like ACKNOWLEDGED APPROVED REJECT |
| COMMUNICATION_ID | NUMBER |  | 24 |  | Unique identifier of the communication table row related to which this individual message is. |
| DELIVERY_STATUS | VARCHAR2 | 20 |  |  | Status of the message delivery. This field indicates whether a message is sucessfully delivered or not. |
| COMMUNICATION_TYPE | VARCHAR2 | 100 |  |  | Indicates the type of the communication through which the message is being sent. |
| COMMUNICATION_ADDRESS | VARCHAR2 | 1000 |  |  | Communication Address phone number, device id etc |
| USER_GUID | VARCHAR2 | 64 |  |  | GUID of the user to whom the message is intented to. |
| DELIVERY_TRACKER_ID | VARCHAR2 | 1000 |  |  | The tracker identification key which is obtained while sending the email. |
| DELIVERY_TYPE | VARCHAR2 | 20 |  |  | The field indicates the type of the message delivery. |
| RULE_NODE_ID | VARCHAR2 | 20 |  |  | Identifier of the rule node for which message is sent. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| RECIPIENT_TYPE | VARCHAR2 | 60 |  |  | The field indicates whether the recipient is of cc or bcc or to type. |
| GROUP_ID | NUMBER |  | 2 |  | The field indicate the identifier used of grouping the data. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_MESSAGE_DELIVERY_FK1 | Non Unique | HRC_MESSAGE_DELIVERY_FK1 | COMMUNICATION_ID |
| HRC_MESSAGE_DELIVERY_PK | Unique | HRC_MESSAGE_DELIVERY_PK | MESSAGE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
