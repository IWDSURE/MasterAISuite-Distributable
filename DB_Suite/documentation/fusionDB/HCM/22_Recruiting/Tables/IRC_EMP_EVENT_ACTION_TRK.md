# IRC_EMP_EVENT_ACTION_TRK

This table stores the details of the employee event actions tracking details

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircempeventactiontrk-28484.html#ircempeventactiontrk-28484](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircempeventactiontrk-28484.html#ircempeventactiontrk-28484)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_EMP_EVENT_ACTION_TRK_PK | ACTION_TRACKING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_TRACKING_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |
| EMP_EVENT_ID | NUMBER |  | 18 | Yes | Stores EMP_EVENT_ID. Foreign key to irc_emp_events_b table. |
| ACTION_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores action types supported values are ORA_MSG and ORA_NOTIFICATION. |
| STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores the status as a lookup code. The corresponding lookup type are ORA_NEW, ORA_INPROGRESS and ORA_COMPLETED. |
| START_TIME | TIMESTAMP |  |  |  | Stores employee event action start time. |
| END_TIME | TIMESTAMP |  |  |  | Stores employee event action end time. |
| SUCCESS_COUNT | NUMBER |  |  |  | Stores the count of successful event sends. |
| FAILED_COUNT | NUMBER |  |  |  | Stores the count of failed event sends. |
| REQUESTOR_PERSON_ID | NUMBER |  | 18 | Yes | Stores REQUESTOR_PERSON_ID. Foreign Key to per_persons table. |
| SCHEDULE_TIME | TIMESTAMP |  |  |  | Stores scheduled date for the event. |
| ERROR_MESSAGE | VARCHAR2 | 1000 |  |  | Stores error details if any failures to send event. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_EMP_EVENT_ACTION_TRK_FK1 | Non Unique | Default | EMP_EVENT_ID |
| IRC_EMP_EVENT_ACTION_TRK_FK2 | Non Unique | Default | REQUESTOR_PERSON_ID |
| IRC_EMP_EVENT_ACTION_TRK_PK | Unique | Default | ACTION_TRACKING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
