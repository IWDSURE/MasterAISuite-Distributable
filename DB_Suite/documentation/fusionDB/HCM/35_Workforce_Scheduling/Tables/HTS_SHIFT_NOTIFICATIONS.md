# HTS_SHIFT_NOTIFICATIONS

Table holding information about shift notification flow and status.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsshiftnotifications-31034.html#htsshiftnotifications-31034](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsshiftnotifications-31034.html#htsshiftnotifications-31034)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SHIFT_NOTIFICATIONS_PK | SHIFT_NOTIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SHIFT_NOTIFICATION_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a Shift |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SCHEDULE_ID | NUMBER |  | 18 | Yes | Schedule ID |
| SCHEDULE_GROUP_ID | NUMBER |  | 18 |  | This refers to the primary key on the self-scheduling group row of the relevant schedule. |
| NOTIFICATION_TYPE | VARCHAR2 | 30 |  |  | Types of notification |
| SCHEDULE_SHIFT_ID | NUMBER |  | 18 |  | Contain the schedule shift id involved in the notification. Can be null. |
| SCHEDULE_SHIFT_GROUP_ID | NUMBER |  | 18 |  | The field contains the unique id to group identical shifts |
| NOTIFY_HOME_DEPT_FLAG | VARCHAR2 | 1 |  |  | For publish, If set to ye, don't need to send separate notification to home department workers |
| NOTIFY_OTHER_DEPT_FLAG | VARCHAR2 | 1 |  |  | Applicable to Schedule level notification or Shift level notification |
| TARGET_NOTIFICATION_DATE | DATE |  |  |  | Future dated notification |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Status Code |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SHIFT_NOTIFICATIONS_N1 | Non Unique | Default | SCHEDULE_ID |
| HTS_SHIFT_NOTIFICATIONS_PK | Unique | Default | SHIFT_NOTIFICATION_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
