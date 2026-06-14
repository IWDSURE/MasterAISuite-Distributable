# IRC_TP_EVENTS

This table logs inbound and outbound REST calls between thrid party partner integrations and Oracle Recruiting Cloud.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctpevents-27985.html#irctpevents-27985](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctpevents-27985.html#irctpevents-27985)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TP_EVENTS_PK | EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| DIRECTION_TYPE | VARCHAR2 | 30 |  | Yes | Stores the direction of request. (INBOUND or OUTBOUND) |
| RESOURCE_TYPE | VARCHAR2 | 30 |  |  | Stores the type of REST invocation. |
| RESOURCE_NAME | VARCHAR2 | 240 |  |  | Stores the name of REST resource. |
| RESOURCE_URL | CLOB |  |  |  | Stores the path of REST resource. |
| REQUEST_HEADERS | CLOB |  |  |  | Stores all request headers from the request. |
| PAYLOAD_IN | CLOB |  |  |  | Stores input payload from the request. |
| PAYLOAD_OUT | CLOB |  |  |  | Stores output  payload from the response. |
| METHOD | VARCHAR2 | 30 |  |  | Stores HTTP method of the request. |
| STATUS_CODE | NUMBER |  |  |  | Stores HTTP status of the response. |
| STATUS_MESSAGE | CLOB |  |  |  | Stores HTTP status message of the response. |
| PHASE_CODE | VARCHAR2 | 30 |  |  | Stores code identifying the category phase to which the service belongs. |
| CATEGORY_CODE | VARCHAR2 | 30 |  |  | Stores the code for thrid party category. |
| PROVISIONING_ID | NUMBER |  | 18 |  | Identifies partner provisioning. Foreign Key to IRC_TP_PARTNER_PROVISNGS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TP_EVENTS_FK1 | Non Unique | Default | PROVISIONING_ID |
| IRC_TP_EVENTS_N1 | Non Unique | Default | CATEGORY_CODE, CREATION_DATE |
| IRC_TP_EVENTS_PK | Unique | Default | EVENT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
