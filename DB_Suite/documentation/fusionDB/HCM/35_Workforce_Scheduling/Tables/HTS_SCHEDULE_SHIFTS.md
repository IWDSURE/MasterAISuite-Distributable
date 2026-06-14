# HTS_SCHEDULE_SHIFTS

Table holding the shifts scheduled for employees.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsscheduleshifts-18105.html#htsscheduleshifts-18105](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsscheduleshifts-18105.html#htsscheduleshifts-18105)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHEDULE_SHIFTS_PK | SCHEDULE_SHIFT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_SHIFT_ID | NUMBER |  | 18 | Yes | Primary Key. System generated unique identifier for a Schedule Shift. |
| SCHEDULE_ID | NUMBER |  | 18 | Yes | Identifier of the Schedule to which the shift belongs. |
| SCHEDULE_UNIT_ID | NUMBER |  | 18 | Yes | Identifier of the Schedule Unit to which the shift belongs. |
| APPROVAL_REQ_TO_CLAIM_FLAG | VARCHAR2 | 1 |  |  | Indicates if an approval is needed when the shift is claimed |
| SKILL_ID | NUMBER |  | 18 | Yes | Identifier of the Skill for which the shift is created. |
| PERSON_ID | NUMBER |  | 18 | Yes | PersonId to which shift is assigned to. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | AssignmentId of the person to which shift is assigned to. |
| SHIFT_TYPE | VARCHAR2 | 30 |  |  | Indicates whether the shift is Regular or On-Call or any custom shift type |
| SHIFT_TYPE_ID | NUMBER |  | 18 |  | Id of the shift type (defined as an extend lookup for the lookup type ORA_HTS_SHIFT_TYPE) |
| SHIFT_ID | NUMBER |  | 18 |  | Identifier of the shift from Shift library associated to the Schedule Shift. |
| START_DATE_TIME | TIMESTAMP |  |  | Yes | Start date time of the shift |
| END_DATE_TIME | TIMESTAMP |  |  | Yes | End date time of the shift. |
| START_TIME_TZ_OFFSET | NUMBER |  | 3 |  | Timezone offset of shift's start time. Unit of time is minute |
| END_TIME_TZ_OFFSET | NUMBER |  | 3 |  | Timezone offset of shift's end time. Unit of time is minute |
| REF_DATE | DATE |  |  | Yes | Reference or Actual date of the shift. |
| WORK_DURATION | NUMBER |  | 9 |  | Duration of the Work in minutes |
| BREAK_DURATION | NUMBER |  | 9 |  | Break time in minutes |
| SOURCE | VARCHAR2 | 30 |  |  | Origin of the shift, indicating if it was imported, edited in the UI or computed. |
| LOCKED_FLAG | VARCHAR2 | 1 |  |  | Flag indicating if the shift is locked for further updates. |
| ASSIGNMENT_MODE | VARCHAR2 | 30 |  |  | Indicating how the resource was assigned to the shift or null for open shift |
| SHIFT_CATEGORY | VARCHAR2 | 30 |  |  | Indicating shift's category |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| COMMENTS | VARCHAR2 | 4000 |  |  | Comment that may be provided as information at creation or when updating the shift. |
| ASSIGNED_BY | NUMBER |  | 18 |  | Person ID of the user who assigned the scheduled shift to a worker |
| ASSIGNMENT_DATE | TIMESTAMP |  |  |  | Indicates the date and time the shift was assigned to a person. |
| PREMIUM_SHIFT_CODE | VARCHAR2 | 30 |  |  | A code added to the shift that qualifies the type of scheduled hours as premium |
| OPPORTUNITY_TYPE | VARCHAR2 | 30 |  |  | Type of the opportunity available to the worker. |
| AVAIL_TO_OTHER_DEPT_FLAG | VARCHAR2 | 1 |  |  | For a opportunity shift, indicates if it is available to assignments from the departments not in the current schedule. |
| SHIFT_GROUP_ID | NUMBER |  | 18 |  | The field contains the unique id to group for any open shifts.Identical shifts will have the same unique id value. |
| SHIFT_INCENTIVE | NUMBER |  | 9 |  | Incentive provided if shift is assigned. |
| ALLOW_OVERTIME_FLAG | VARCHAR2 | 1 |  |  | Flag denoting whether worker can exceed FTE with this shift. |
| PAID_BREAK_DURATION | NUMBER |  | 9 |  | Current paid break duration in minutes |
| MANUAL_PAID_BREAK_DURATION | NUMBER |  | 9 |  | Paid break duration in minutes from manual input |
| EXTERNAL_SYSTEM_REFERENCE | VARCHAR2 | 120 |  |  | Stores the external, original application reference identifier |
| ORIGINAL_SOURCE | VARCHAR2 | 60 |  |  | Stores the creation source, such as Workforce Scheduling app or HCM Data Loader, until the shift is deleted |
| IMPORT_PROVIDER | VARCHAR2 | 30 |  |  | Contains the Request Source value (exporter code or requestor's name) of the schedule event request that caused the shift to be created. |
| ALLOW_CLAIM_PARTIAL_SHIFT_FLAG | VARCHAR2 | 1 |  |  | Flag indicating whether the shift can be partially claimed |
| OPPORTUNITY_ROTATION_FLAG | VARCHAR2 | 1 |  |  | Flag indicating if the oportunity shift is available for rotation |
| MOCK_DISCRIMINATOR | VARCHAR2 | 1 |  |  | MOCK_DISCRIMINATOR |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 80 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHEDULE_SHIFTS_N1 | Non Unique | Default | START_DATE_TIME, ASSIGNMENT_ID, END_DATE_TIME |
| HTS_SCHEDULE_SHIFTS_N2 | Non Unique | Default | START_DATE_TIME, PERSON_ID, SCHEDULE_ID |
| HTS_SCHEDULE_SHIFTS_N3 | Non Unique | Default | START_DATE_TIME, SCHEDULE_UNIT_ID, SCHEDULE_ID |
| HTS_SCHEDULE_SHIFTS_N4 | Non Unique | Default | SCHEDULE_ID |
| HTS_SCHEDULE_SHIFTS_N5 | Non Unique | Default | SHIFT_ID |
| HTS_SCHEDULE_SHIFTS_N6 | Non Unique | Default | EXTERNAL_SYSTEM_REFERENCE |
| HTS_SCHEDULE_SHIFTS_PK | Unique | Default | SCHEDULE_SHIFT_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
