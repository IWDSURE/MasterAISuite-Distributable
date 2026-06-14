# IRC_CMT_LAUNCHES

This table stores Message Launch request Information.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccmtlaunches-29538.html#irccmtlaunches-29538](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccmtlaunches-29538.html#irccmtlaunches-29538)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CMT_LAUNCHES_PK | LAUNCH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LAUNCH_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PARENT_LAUNCH_ID | NUMBER |  | 18 |  | Foreign key to IRC_CMT_LAUNCHES table. Stores the LAUNCH_ID of the parent asset. |
| LAUNCH_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Specifies the type of message launch. Stores the type as a lookup code. |
| SUBJECT_ID | NUMBER |  | 18 |  | Stores primary key of the launch type requesting message launch. |
| SUBJECT_CODE | VARCHAR2 | 240 |  |  | Stores primary key (String) of the launch type requesting message launch. |
| SCHEDULE_DATE | TIMESTAMP |  |  |  | Stores scheduled date for the launch. |
| SEND_BY_DATE | TIMESTAMP |  |  |  | Maximum send date for the launch. |
| LAUNCH_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores status of the launch. Stores launch status as a lookup code. |
| LAUNCH_START_TS | TIMESTAMP |  |  |  | Stores launch processing start time. |
| LAUNCH_COMPLETE_TS | TIMESTAMP |  |  |  | Stores launch processing completion time. |
| RECIPIENT_COUNT | NUMBER |  |  |  | Aggregate column. Stores total recipients targeted. |
| UNSENT_COUNT | NUMBER |  |  |  | Aggregate column. Stores total number of messages which did not get sent. |
| PENDING_COUNT | NUMBER |  |  |  | Aggregate column. Stores total number of messages which are due to be sent. |
| BOUNCE_COUNT | NUMBER |  |  |  | Aggregate column. Stores the total count of bounced messages. |
| OPEN_COUNT | NUMBER |  |  |  | Aggregate column. Stores the total count of Opened messages. |
| ERROR_REASON | VARCHAR2 | 1000 |  |  | Stores the reason for error status of the launch. |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | Stores the ESS Job Request ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| IRC_CMT_LAUNCHES_FK1 | Non Unique | Default | PARENT_LAUNCH_ID |  |
| IRC_CMT_LAUNCHES_N1 | Non Unique | Default | LAUNCH_TYPE_CODE |  |
| IRC_CMT_LAUNCHES_N2 | Non Unique | Default | SUBJECT_ID |  |
| IRC_CMT_LAUNCHES_N3 | Non Unique | Default | LAUNCH_STATUS_CODE | Obsolete |
| IRC_CMT_LAUNCHES_PK | Unique | Default | LAUNCH_ID |  |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
