# IRC_CX_CONV_TRACKING_DETAILS

Stores user conversation request and response tracking information details in the career coach orchestration layers

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxconvtrackingdetails-5676.html#irccxconvtrackingdetails-5676](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxconvtrackingdetails-5676.html#irccxconvtrackingdetails-5676)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_CONV_TRACK_DETAILS_PK | CONVERSATION_LOG_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONVERSATION_LOG_DETAIL_ID | NUMBER |  | 18 | Yes | System generated unique identifier for the converstaion tracking details. |
| CONVERSATION_LOG_ID | NUMBER |  | 18 | Yes | Foreign key to irc_cx_conv_tracking. |
| LOG_SOURCE | VARCHAR2 | 240 |  |  | Classname where the api is invoked |
| SOURCE_REQUEST | CLOB |  |  |  | Request payload depending on the LOG_SOURCE. |
| SOURCE_RESPONSE | CLOB |  |  |  | Response payload depending on the LOG_SOURCE. |
| RESPONSE_STATUS | VARCHAR2 | 30 |  |  | Allowed values are ERROR/COMPLETE |
| SERVICE_URL | VARCHAR2 | 240 |  |  | CE endpoint Url invoked by agent to get requested conversation response. |
| ADDITIONAL_INFO_01 | VARCHAR2 | 1000 |  |  | Additional column for any other data that may be need tracking in the future |
| ADDITIONAL_INFO_02 | VARCHAR2 | 1000 |  |  | Additional column for any other data that may be need tracking in the future |
| ADDITIONAL_INFO_03 | VARCHAR2 | 1000 |  |  | Additional column for any other data that may be need tracking in the future |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_CONV_TRACK_DETAILS_N1 | Non Unique | Default | CONVERSATION_LOG_ID, LOG_SOURCE |
| IRC_CX_CONV_TRACK_DETAILS_N2 | Non Unique | Default | LOG_SOURCE |
| IRC_CX_CONV_TRACK_DETAILS_PK | Unique | Default | CONVERSATION_LOG_DETAIL_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
