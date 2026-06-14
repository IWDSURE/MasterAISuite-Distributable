# HWM_TCD_EXP_DATA_SCH_SHFT

This table contains details for Time Clock Device export data for Schedule Shift

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcdexpdataschshft-15025.html#hwmtcdexpdataschshft-15025](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcdexpdataschshft-15025.html#hwmtcdexpdataschshft-15025)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCD_EXP_DATA_SCH_SHFT_PK | SCHEDULE_SHIFT_ID, SCHEDULE_SHIFT_VERSION |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_SHIFT_ID | NUMBER |  | 18 | Yes | Schedule shift identifier |
| SHIFT_ID | NUMBER |  | 18 |  | SHIFT_ID |
| TCD_EXP_DATA_ESS_PROCESS_ID | NUMBER |  | 18 |  | The process which generated the data. |
| SCHEDULE_SHIFT_VERSION | NUMBER |  | 9 | Yes | SCHEDULE_SHIFT_VERSION |
| LATEST_VERSION | VARCHAR2 | 1 |  |  | LATEST_VERSION |
| STATUS | VARCHAR2 | 20 |  |  | Export or Collection Data Status |
| REC_TYPE | VARCHAR2 | 10 |  |  | REC_TYPE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SCHEDULE_SHIFT_NAME | VARCHAR2 | 240 |  |  | Shift Name |
| START_EARLY_GRACE | NUMBER |  | 18 |  | Grace period allowed before start time of the shift |
| START_LATE_GRACE | NUMBER |  | 18 |  | Grace period allowed after start time of the shift |
| END_EARLY_GRACE | NUMBER |  | 18 |  | Grace period allowed before end time of the shift |
| DURATION | NUMBER |  | 18 |  | Duration of work |
| TIME_NOT_WORKED | NUMBER |  | 18 |  | Time not worked |
| END_LATE_GRACE | NUMBER |  | 18 |  | Grace period allowed after end time of the shift |
| TOLERANCE | NUMBER |  | 9 |  | Threshold to ignore violation |
| START_EARLY_VIOLATION | VARCHAR2 | 10 |  |  | Code used to indicate start early violation |
| START_LATE_VIOLATION | VARCHAR2 | 10 |  |  | Code used to indicate start late violation |
| END_EARLY_VIOLATION | VARCHAR2 | 10 |  |  | Code used to indicate end early violation |
| END_LATE_VIOLATION | VARCHAR2 | 10 |  |  | Code used to indicate end late violation |
| DELETE_FLAG | VARCHAR2 | 1 |  |  | Flag to indicate deleted shift |
| SETUP_PROFILE_ID | NUMBER |  | 18 |  | The setup profile id driving the export data collection. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TCD_EXP_DATA_SCH_SHFT_U1 | Unique | Default | SCHEDULE_SHIFT_ID, SCHEDULE_SHIFT_VERSION |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
