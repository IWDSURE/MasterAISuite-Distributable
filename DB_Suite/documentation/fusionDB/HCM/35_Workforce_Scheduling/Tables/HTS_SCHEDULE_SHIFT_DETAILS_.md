# HTS_SCHEDULE_SHIFT_DETAILS_

Table holding the detailed information about the shifts scheduled for employees within a department or an unit.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsscheduleshiftdetails-7311.html#htsscheduleshiftdetails-7311](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsscheduleshiftdetails-7311.html#htsscheduleshiftdetails-7311)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHEDULE_SHIFT_DTLS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, SCHEDULE_SHIFT_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_SHIFT_DETAIL_ID | NUMBER |  | 18 | Yes | Primary Key. System generated unique identifier for the Schedule Shift Detail. |
| SCHEDULE_SHIFT_ID | NUMBER |  | 18 |  | Foreign Key. Identifier for the Schedule Shift, to which this detail belongs to. |
| START_DATE_TIME | TIMESTAMP |  |  |  | Indicates the start date and time of the shift detail. |
| END_DATE_TIME | TIMESTAMP |  |  |  | Indicates the end date and time of the shift detail. |
| SHIFT_DETAIL_TYPE | VARCHAR2 | 30 |  |  | Indicates the particular type of shift detail, as defined. |
| SHIFT_DATE | DATE |  |  |  | Indicates the calendar date of the scheduled shift. |
| DURATION | NUMBER |  | 9 |  | Indicates the duration specified for the element pertaining to the shift detail, in minutes. |
| SOURCE | VARCHAR2 | 30 |  |  | Indicates the origin of creation for the shift detail. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_SHIFT_DTLSN1_ | Non Unique | Default | SCHEDULE_SHIFT_DETAIL_ID |
| HTS_SCHED_SHIFT_DTLSU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, SCHEDULE_SHIFT_DETAIL_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
