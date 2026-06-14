# HTS_SCHEDULE_SHIFT_DETAILS

Table holding the detailed information about the shifts scheduled for employees within a department or an unit.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsscheduleshiftdetails-17436.html#htsscheduleshiftdetails-17436](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsscheduleshiftdetails-17436.html#htsscheduleshiftdetails-17436)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHEDULE_SHIFT_DTLS_PK | SCHEDULE_SHIFT_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_SHIFT_DETAIL_ID | NUMBER |  | 18 | Yes | Primary Key. System generated unique identifier for the Schedule Shift Detail. |
| SCHEDULE_SHIFT_ID | NUMBER |  | 18 | Yes | Foreign Key. Identifier for the Schedule Shift, to which this detail belongs to. |
| START_DATE_TIME | TIMESTAMP |  |  |  | Indicates the start date and time of the shift detail. |
| END_DATE_TIME | TIMESTAMP |  |  |  | Indicates the end date and time of the shift detail. |
| SHIFT_DETAIL_TYPE | VARCHAR2 | 30 |  | Yes | Indicates the particular type of shift detail, as defined. |
| SHIFT_DATE | DATE |  |  | Yes | Indicates the calendar date of the scheduled shift. |
| DURATION | NUMBER |  | 9 | Yes | Indicates the duration specified for the element pertaining to the shift detail, in minutes. |
| SOURCE | VARCHAR2 | 30 |  | Yes | Indicates the origin of creation for the shift detail. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHEDULE_SHIFT_DTLS_N1 | Non Unique | Default | SCHEDULE_SHIFT_ID |
| HTS_SCHEDULE_SHIFT_DTLS_PK | Unique | Default | SCHEDULE_SHIFT_DETAIL_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
