# HTS_SCHED_SHIFT_EVENTS

Table to store schedule shift events

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_INTERFACE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedshiftevents-16853.html#htsschedshiftevents-16853](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedshiftevents-16853.html#htsschedshiftevents-16853)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_SHIFT_EVENTS_PK | SCHED_SHIFT_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_SHIFT_EVENT_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| SCHED_REQUEST_NUMBER | VARCHAR2 | 120 |  |  | Identifier of the request as specified by the exporter |
| SCHED_EVENT_NUMBER | VARCHAR2 | 120 |  |  | Identifier of the schedule event as specified by the exporter |
| SCHED_SHIFT_EVENT_NUMBER | VARCHAR2 | 120 |  |  | Identifier of the schedule shift event as specified by the exporter |
| SCHED_EVENT_ID | NUMBER |  | 18 |  | SCHED_EVENT_ID |
| SHIFT_NUMBER | VARCHAR2 | 120 |  |  | Shift identifier provided by the exporter |
| SHIFT_ACTION | VARCHAR2 | 30 |  |  | Action to perform on the shift. Values are CREATE, UPDATE, or DELETE.
When the import mode is FULL, only CREATE actions are accepted |
| REF_DAY | DATE |  |  |  | Date for the day of reference for the shift |
| START_TIME_STR | VARCHAR2 | 80 |  |  | The start time of shifts of type Time, entered in a format with time zone offset. |
| START_TIME_OFFSET | NUMBER |  | 22 |  | START_TIME_OFFSET |
| START_TIME | TIMESTAMP |  |  |  | START_TIME |
| END_TIME_STR | VARCHAR2 | 80 |  |  | The end time of shifts of type Time, entered in a format with time zone offset. |
| END_TIME_OFFSET | NUMBER |  | 22 |  | END_TIME_OFFSET |
| END_TIME | TIMESTAMP |  |  |  | END_TIME |
| DURATION | NUMBER |  | 18 |  | Duration of the shift in minutes.
Mandatory if the shift type is Elapsed. For other shift types, you must supply start and end times. |
| TIME_NOT_WORKED | NUMBER |  | 18 |  | Unpaid time at the shift level in minutes.
The shift value in the library provides the default value, which you can override. |
| SHIFT_CODE | VARCHAR2 | 120 |  |  | Reference to a shift in the library. Code is language-independent and is required only when you create or update shifts |
| SHIFT_TYPE | VARCHAR2 | 30 |  |  | Type of shift. Values are ELAPSED or TIME |
| SHIFT_CATEGORY | VARCHAR2 | 30 |  |  | Category of the shift. Values are (WORK or ABSENCE). In R13, the value WORK is the only accepted value. |
| STATUS_IMP | NUMBER |  | 2 |  | Status for the import phase |
| STATUS_INT | NUMBER |  | 2 |  | Status for the internalization phase |
| SHIFT_TYPE_CODE | VARCHAR2 | 30 |  |  | Code of the shift type for the workforce schedule shift. Default REGULAR. |
| ENTERPRISE_SHIFT_NAME | VARCHAR2 | 240 |  |  | Name of the enterprise shift. Nothing if custom shift, not from enterprise shift. |
| ENTERPRISE_SHIFT_DATE | DATE |  |  |  | Calendar date of the workforce schedule shift; if shifts coming from enterprise shifts only. |
| UNPAID_BREAK_DURATION | NUMBER |  | 9 |  | Unpaid break duration in minutes, if custom shift only. |
| PAID_BREAK_DURATION | NUMBER |  | 9 |  | Paid break duration in minutes. |
| SHIFT_NOTES | VARCHAR2 | 4000 |  |  | Notes added to the workforce schedule shift. |
| PREMIUM_SHIFT_CODE | VARCHAR2 | 30 |  |  | Premium code for the workforce schedule shift |
| ALLOW_OVERTIME_FLAG | VARCHAR2 | 1 |  |  | Indicated if workers assigned to the workforce schedule shift can go over their assignment weekly hours |
| SHIFT_INCENTIVE | NUMBER |  | 9 |  | Monetary amount a worker will get when assigned the workforce schedule shift. |
| ADV_SHIFT_CATEGORY | VARCHAR2 | 30 |  |  | Category for the workforce schedule shift, if custom shift only. |
| JOB_PROFILE_TYPE | VARCHAR2 | 30 |  |  | Job profile type used to define the skill: Job, Job family, Position, or Scheduling Group. |
| JOB_PROFILE_NAME | VARCHAR2 | 255 |  |  | Name of the job profile type value used to describe the skill for the coverage. |
| JOB_SET_CODE | VARCHAR2 | 255 |  |  | Code that uniquely identifies the HCM job set used to identify which job type is represented on the workload value for the import record. |
| QUALIFICATION_TYPE | VARCHAR2 | 30 |  |  | Type of criteria to including in the corresponding Qualification drop-down list. |
| QUALIFICATION | VARCHAR2 | 150 |  |  | Competency, license or certification, or language value for the selected qualification type. |
| BUSINESS_UNIT_NAME | VARCHAR2 | 240 |  |  | Name of the business unit. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ALLOW_EDITS | VARCHAR2 | 1 |  |  | Specify whether the shift that is imported can be edited by the scheduler in the application, on the Manage Planned Schedule page. Values are Y or N.
If the value is Y or null, shift edition is allowed only if the value of the option AllowEdits is Y on the schedule event or on the Worker Time Setup profile when it is not overriden on the schedule event. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_SHIFT_EVENTS_N1 | Non Unique | FUSION_TS_INTERFACE | SCHED_EVENT_ID |
| HTS_SCHED_SHIFT_EVENTS_N2 | Non Unique | FUSION_TS_INTERFACE | SCHED_SHIFT_EVENT_NUMBER, SCHED_EVENT_NUMBER, SCHED_REQUEST_NUMBER |
| HTS_SCHED_SHIFT_EVENTS_PK | Unique | FUSION_TS_INTERFACE | SCHED_SHIFT_EVENT_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
