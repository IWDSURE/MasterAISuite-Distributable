# HTS_SHIFTS_B_

Table holding templates for a library shift, shifts can be used to build work patterns.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsshiftsb-20941.html#htsshiftsb-20941](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsshiftsb-20941.html#htsshiftsb-20941)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SHIFTS_B_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, SHIFT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SHIFT_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a Shift |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| SHIFT_CODE | VARCHAR2 | 30 |  |  | Unique code entered when creating a shift, in order to help user identify the shift. |
| START_TIME_OFFSET | NUMBER |  | 9 |  | Offset from midnight saved in minutes defining the start time of the shift |
| END_TIME_OFFSET | NUMBER |  | 9 |  | Offset from midnight saved in minutes defining the end time of the shift |
| WORK_DURATION | NUMBER |  | 9 |  | Work duration in minutes of the shift |
| BREAK_DURATION | NUMBER |  | 9 |  | Break duration in minutes of the shift |
| END_PLUS_DAYS | NUMBER |  | 9 |  | Identifies whether the end time offset comes one day after the start time offset (1) or the same day (0) |
| SHIFT_CATEGORY | VARCHAR2 | 30 |  |  | A category such as Day or Night that helps classify the Shifts. |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | ACTIVE_FLAG |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SHIFTS_B_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, SHIFT_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
