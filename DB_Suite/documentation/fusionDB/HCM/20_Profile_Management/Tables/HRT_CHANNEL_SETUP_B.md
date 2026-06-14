# HRT_CHANNEL_SETUP_B

The table stores the channel definition

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtchannelsetupb-22589.html#hrtchannelsetupb-22589](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtchannelsetupb-22589.html#hrtchannelsetupb-22589)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_CHANNEL_SETUP_B_PK | CHANNEL_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHANNEL_ID | NUMBER |  | 18 | Yes | Primary key of Channel Setup |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| EMAIL_ID | VARCHAR2 | 240 |  | Yes | Email Associated to the Channel |
| CODE | VARCHAR2 | 240 |  | Yes | Unique User Defined Code to Identify the Channel |
| TYPE | VARCHAR2 | 240 |  | Yes | Identify the Type of the Channel.  Possible Values Are Private, Public, Directs and Organization |
| DEPENDENT_CHANNEL_ID | NUMBER |  | 18 |  | Corresponding Channel Associated for Directs and Organization Channel |
| ENABLED | VARCHAR2 | 30 |  | Yes | Indicates if tthe Channel is Enabled or Not |
| PAGENAME | VARCHAR2 | 1000 |  |  | Indicate the page using the channel |
| INCOMING_SERVER_PROTOCOL | VARCHAR2 | 30 |  |  | Incoming Server Protocol |
| INCOMING_SERVER_HOST | VARCHAR2 | 4000 |  |  | Incoming Server Host Name |
| INCOMING_SERVER_PORT | NUMBER |  | 18 |  | Incoming Server Port Number |
| INCOMING_SERVER_AUTH_TYPE | VARCHAR2 | 30 |  |  | Incoming Server Authorization Type |
| INCOMING_SERVER_AUTH_KEY | VARCHAR2 | 1000 |  |  | Incoming Server Authorization Key |
| INCOMING_SERVER_AUTH_VALUE | CLOB |  |  |  | Incoming Server Authorization Value |
| INCOMING_SERVER_BEARER_TOKEN | CLOB |  |  |  | Incoming Server Authorization Bearer Token |
| INCOMING_SERVER_SSL | VARCHAR2 | 30 |  |  | Whether or Not to Enable SSL When Connecting to the Incoming Server. |
| OUTGOING_SERVER_PROTOCOL | VARCHAR2 | 30 |  |  | Outgoing Server Protocol |
| OUTGOING_SERVER_HOST | VARCHAR2 | 4000 |  |  | Outgoing Server Host Name |
| OUTGOING_SERVER_PORT | NUMBER |  | 18 |  | Outgoing Server Port Number |
| OUTGOING_SERVER_AUTH_TYPE | VARCHAR2 | 30 |  |  | Outgoing Server Authorization Type |
| OUTGOING_SERVER_AUTH_KEY | VARCHAR2 | 1000 |  |  | Outgoing Server Authorization Key |
| OUTGOING_SERVER_AUTH_VALUE | CLOB |  |  |  | Outgoing Server Authorization Value |
| OUTGOING_SERVER_BEARER_TOKEN | CLOB |  |  |  | Outgoing Server Authorization Bearer Token |
| RECEIVE_FOLDER | VARCHAR2 | 1000 |  |  | The name of the email folder the driver is polling messages from. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_CHANNEL_SETUP_B_U1 | Unique | Default | CHANNEL_ID, BUSINESS_GROUP_ID |
| HRT_CHANNEL_SETUP_B_U2 | Unique | Default | BUSINESS_GROUP_ID, CODE |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
