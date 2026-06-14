# WLF_PROVIDER_ATTENDANCE

Table to store provider attendance information.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfproviderattendance-16182.html#wlfproviderattendance-16182](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfproviderattendance-16182.html#wlfproviderattendance-16182)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ATTENDANCE_PK | ATTENDANCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTENDANCE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| PROVIDER_ATTENDANCE_NUMBER | VARCHAR2 | 30 |  |  | PROVIDER_ATTENDANCE_NUMBER |
| PROVIDER_BOOKING_ID | NUMBER |  | 18 | Yes | Indicates provider booking id |
| MEETING_ID | VARCHAR2 | 250 |  | Yes | Indicates meeting id |
| ASSIGNMENT_TASK_ID | NUMBER |  | 18 | Yes | Indicates assignment task id |
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | Indicates learning item id |
| LEARNER_ID | NUMBER |  | 18 | Yes | Indicates learner id |
| START_TIME | TIMESTAMP |  |  |  | Indicates start time of the meeting |
| END_TIME | TIMESTAMP |  |  |  | Indicates end time of the meeting |
| DURATION | NUMBER |  |  |  | Indicates the duration of the call attended |
| ATTENDEE_EMAIL | VARCHAR2 | 240 |  |  | Indicates attendee email id |
| DISPLAY_NAME | VARCHAR2 | 240 |  |  | Indicates attendee display name. |
| INSTRUCTOR_FLAG | VARCHAR2 | 1 |  |  | Indicates whether the attendee is an instructor. |
| ADDITIONAL_INFO | VARCHAR2 | 1000 |  |  | Indicates additional information of an attendance. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PROVIDER_ATTENDANCE_N1 | Non Unique | Default | PROVIDER_BOOKING_ID |
| WLF_PROVIDER_ATTENDANCE_N2 | Non Unique | Default | MEETING_ID |
| WLF_PROVIDER_ATTENDANCE_N3 | Non Unique | Default | LEARNING_ITEM_ID, LEARNER_ID |
| WLF_PROVIDER_ATTENDANCE_N4 | Non Unique | Default | PROVIDER_ATTENDANCE_NUMBER |
| WLF_PROVIDER_ATTENDANCE_U1 | Unique | Default | ATTENDANCE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
