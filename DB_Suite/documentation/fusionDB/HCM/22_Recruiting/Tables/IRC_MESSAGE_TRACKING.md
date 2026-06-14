# IRC_MESSAGE_TRACKING

This table tracks message metadata for all communication channels in HCM Communicate and Recruiting.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmessagetracking-3198.html#ircmessagetracking-3198](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmessagetracking-3198.html#ircmessagetracking-3198)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MESSAGE_TRACKING_PK | MESSAGE_TRACKING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MESSAGE_TRACKING_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| ADDED_BY_PERSON_ID | NUMBER |  | 18 |  | Stores the ID of the person triggering the message. |
| ADMIN_ALERT_ID | NUMBER |  | 18 |  | Foreign Key to the table IRC_ADMIN_ALERT_HISTORY. |
| CONTACT_INFORMATION | VARCHAR2 | 240 |  | Yes | The communication contact information such as email, phone number, etc., as per channel type code. |
| CHANNEL_TYPE_CODE | VARCHAR2 | 20 |  | Yes | The code for the channel such as SMS, email etc., that is used to send the message to the person. Lookup codes of type 'ORA_IRC_INTERACTION_TYPE'. |
| CHANNEL_SUB_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores additional details about the channel type, such as whether the message was initiated by the user or the agent/system. |
| PERSON_ID | NUMBER |  | 18 |  | The ID of the person who is receiving the message. Foreign key to PER_PERSONS table. |
| PRODUCT_CONTEXT | VARCHAR2 | 30 |  | Yes | The product such as HCM_COMMUNICATE, HCM_RECRUITING etc., for which the message belongs to. |
| PRODUCT_SUB_CONTEXT | VARCHAR2 | 30 |  |  | The product's sub context such as  ORA_SUBMISSION, ORA_PROSPECT, ORA_EVENT, etc., in which this message was sent for a product. |
| PRODUCT_SUB_CONTEXT_ID | NUMBER |  | 18 |  | Provides the link to the product's sub context through  SUBMISSION_ID, PROSPECT_ID, EVENT_ID, etc. of tables IRC_SUBMISSIONS, IRC_PROSPECTS, IRC_REC_EVENTS_B etc. |
| CONTENT_LIBRARY_ITEM_CODE | VARCHAR2 | 30 |  |  | The Recruiting Content Library's DESCRIPTION_CODE that points to the table IRC_DESCRIPTIONS_B. |
| MESSAGE_API_STATUS | VARCHAR2 | 30 |  |  | Message API availability at the instance of sending a message depending on throttling rules imposed by the admin and if available API's call status. |
| MESSAGE_API_RESPONSE_CODE | VARCHAR2 | 40 |  |  | Message API status based on the unique API response code given by the message provider. |
| MESSAGE_DIRECTION | VARCHAR2 | 30 |  |  | Indicates whether the message is inbound  or outbound based on the flow of communication |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PHONE_COUNTRY_CODE | VARCHAR2 | 30 |  |  | Country prefix for international phone numbers including area code, such as 33 for France |
| REQUEST_SOURCE | VARCHAR2 | 200 |  |  | Identifies the functional area or system component from which the API call to send a message is initiated |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MESSAGE_TRACKING_FK1 | Non Unique | Default | PERSON_ID |
| IRC_MESSAGE_TRACKING_FK2 | Non Unique | Default | ADMIN_ALERT_ID |
| IRC_MESSAGE_TRACKING_N1 | Non Unique | Default | PRODUCT_CONTEXT, CHANNEL_TYPE_CODE, PERSON_ID, CREATION_DATE, CHANNEL_SUB_TYPE_CODE, ADDED_BY_PERSON_ID |
| IRC_MESSAGE_TRACKING_N2 | Non Unique | Default | PRODUCT_CONTEXT, CHANNEL_TYPE_CODE, CREATION_DATE, MESSAGE_API_STATUS, CONTENT_LIBRARY_ITEM_CODE, CHANNEL_SUB_TYPE_CODE, ADDED_BY_PERSON_ID |
| IRC_MESSAGE_TRACKING_N3 | Non Unique | Default | PRODUCT_CONTEXT, CHANNEL_TYPE_CODE, CONTACT_INFORMATION, CREATION_DATE, CHANNEL_SUB_TYPE_CODE, ADDED_BY_PERSON_ID |
| IRC_MESSAGE_TRACKING_N4 | Non Unique | Default | PRODUCT_CONTEXT, CHANNEL_TYPE_CODE, CREATION_DATE, PHONE_COUNTRY_CODE, MESSAGE_API_STATUS, MESSAGE_API_RESPONSE_CODE |
| IRC_MESSAGE_TRACKING_PK | Unique | Default | MESSAGE_TRACKING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
