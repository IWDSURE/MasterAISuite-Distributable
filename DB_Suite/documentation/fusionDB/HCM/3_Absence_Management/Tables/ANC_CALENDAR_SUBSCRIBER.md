# ANC_CALENDAR_SUBSCRIBER

Table for subscriptions in Calendars.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/anccalendarsubscriber-29878.html#anccalendarsubscriber-29878](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/anccalendarsubscriber-29878.html#anccalendarsubscriber-29878)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_CALENDAR_SUBSCRIBER_PK | CALENDAR_SUBSCRIBER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CALENDAR_SUBSCRIBER_ID | NUMBER |  | 18 | Yes | Calendar Subscription ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise ID |
| CALENDAR_ID | NUMBER |  | 18 | Yes | Calendar ID |
| GRP_ID | NUMBER |  | 18 | Yes | Group ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_CALENDAR_SUBSCRIBER_FK1 | Non Unique | Default | CALENDAR_ID |
| ANC_CALENDAR_SUBSCRIBER_FK2 | Non Unique | default | GRP_ID |
| ANC_CALENDAR_SUBSCRIBER_PK | Unique | Default | CALENDAR_SUBSCRIBER_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
