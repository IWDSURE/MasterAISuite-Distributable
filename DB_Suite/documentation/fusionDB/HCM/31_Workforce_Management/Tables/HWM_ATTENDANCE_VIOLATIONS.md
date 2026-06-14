# HWM_ATTENDANCE_VIOLATIONS

table to store attendance violations

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmattendanceviolations-30619.html#hwmattendanceviolations-30619](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmattendanceviolations-30619.html#hwmattendanceviolations-30619)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_ATTENDANCE_VIOLATIONS_PK | ATTENDANCE_VIOLATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTENDANCE_VIOLATION_ID | NUMBER |  | 18 | Yes | Primary Key to uniquely identify Attendance Violations |
| ATTENDANCE_VIOLATION_DATE | DATE |  |  | Yes | Date on which violation has been raised |
| STATUS | VARCHAR2 | 30 |  | Yes | Status of the violation which can have values NEW/FIXED/ACKNOWLEDGED/EXCUSED/PENDING_APPROVAL |
| PERSON_ID | NUMBER |  | 18 | Yes | Person identifier for which violation is raised |
| EXCUSED_BY | NUMBER |  | 18 |  | Identifier of the manager who has excused the violation |
| EXCUSED_TIME | TIMESTAMP |  |  |  | DateTime on which manager has excused the violation |
| COMMENTS | VARCHAR2 | 2000 |  |  | Remarks added for violation |
| POINTS | NUMBER |  |  |  | Penalty point for the violation when threshold is achieved |
| THRESHOLD_VIOLATED_FLAG | VARCHAR2 | 1 |  |  | Flag to check if threshold is violated. Can have values Y/N |
| THRESHOLD_PERIOD_START_DATE | DATE |  |  |  | Start Date since when we will begin evaluating the threshold |
| THRESHOLD_PERIOD_STOP_DATE | DATE |  |  |  | Stop Date since when we will begin evaluating the threshold |
| TIME_ENTRY_ID | NUMBER |  | 18 |  | ID to uniquely identify the time entry |
| TIME_ENTRY_VERSION | NUMBER |  | 9 |  | Version of the time entry record |
| ENTRY_START_TIME | TIMESTAMP |  |  |  | Start time of time entry or absence |
| ENTRY_STOP_TIME | TIMESTAMP |  |  |  | Stop time of time entry or absence |
| TIME_EVENT_ID | NUMBER |  | 18 |  | ID to uniquely identify the time event |
| ABSENCE_ID | NUMBER |  | 18 |  | ID to uniquely identify the absence |
| ABSENCE_REPORTING_TIME | TIMESTAMP |  |  |  | DateTime on which the absence is created |
| SHIFT_ID | NUMBER |  | 18 |  | ID to uniquely identify a shift |
| SHIFT_START_TIME | TIMESTAMP |  |  |  | Start Time of Shift |
| SHIFT_STOP_TIME | TIMESTAMP |  |  |  | Stop Time of Shift |
| RULE_SET_ID | NUMBER |  | 18 | Yes | Rule Set Identifier |
| RULE_ID | NUMBER |  | 18 | Yes | Rule Identifier |
| RULE_TYPE | VARCHAR2 | 64 |  | Yes | The type of rule against which the violation has been raised e.g. Tardy. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_ATTENDANCE_VIOLATIONS_PK | Unique | Default | ATTENDANCE_VIOLATION_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
