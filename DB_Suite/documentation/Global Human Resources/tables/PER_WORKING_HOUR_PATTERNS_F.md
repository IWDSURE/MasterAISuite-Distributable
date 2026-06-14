# PER_WORKING_HOUR_PATTERNS_F

This table contains Work Hour Patterns data.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perworkinghourpatternsf-24357.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perworkinghourpatternsf-24357.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_WORKING_HOUR_PATTERNS_PK | WORKING_HOUR_PATTERN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORKING_HOUR_PATTERN_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PERSON_ID | NUMBER |  | 18 |  | Identifies person holding the Working Hour Patterns. |
| OBJECT | VARCHAR2 | 30 |  | Yes | The module, with which the Working Hour Patterns functionality is integrated. |
| OBJECT_ID | NUMBER |  | 18 | Yes | Foreign key to the module, with which the Working Hour Patterns functionality is integrated. |
| WORKING_HOURS_TYPE | VARCHAR2 | 30 |  |  | The Working Hours type  None, Frequency, Work Week. |
| MON_START_TIME | VARCHAR2 | 30 |  |  | Monday's Starting Time in 24 hrs format HH:mm |
| TUE_START_TIME | VARCHAR2 | 30 |  |  | Tueday's Starting Time in 24 hrs format HH:mm |
| WED_START_TIME | VARCHAR2 | 30 |  |  | Wednesday's Starting Time in 24 hrs format HH:mm |
| THU_START_TIME | VARCHAR2 | 30 |  |  | Thursday's Starting Time in 24 hrs format HH:mm |
| FRI_START_TIME | VARCHAR2 | 30 |  |  | Friday's Starting Time in 24 hrs format HH:mm |
| SAT_START_TIME | VARCHAR2 | 30 |  |  | Saturday's Starting Time in 24 hrs format HH:mm |
| SUN_START_TIME | VARCHAR2 | 30 |  |  | Sunday's Starting Time in 24 hrs format HH:mm |
| MON_END_TIME | VARCHAR2 | 30 |  |  | Monday's Ending Time in 24 hrs format HH:mm |
| TUE_END_TIME | VARCHAR2 | 30 |  |  | Tuesday's Ending Time in 24 hrs format HH:mm |
| WED_END_TIME | VARCHAR2 | 30 |  |  | Wednesday's Ending Time in 24 hrs format HH:mm |
| THU_END_TIME | VARCHAR2 | 30 |  |  | Thursday's Ending Time in 24 hrs format HH:mm |
| FRI_END_TIME | VARCHAR2 | 30 |  |  | Friday's Ending Time in 24 hrs format HH:mm |
| SAT_END_TIME | VARCHAR2 | 30 |  |  | Saturday's Ending Time in 24 hrs format HH:mm |
| SUN_END_TIME | VARCHAR2 | 30 |  |  | Sunday's Ending Time in 24 hrs format HH:mm |
| MON_HOURS | NUMBER |  | 22 |  | Total hours worked on Monday. |
| TUE_HOURS | NUMBER |  | 22 |  | Total hours worked on Tuesday. |
| WED_HOURS | NUMBER |  | 22 |  | Total hours worked on Wednesday. |
| THU_HOURS | NUMBER |  | 22 |  | Total hours worked on Thursday. |
| FRI_HOURS | NUMBER |  | 22 |  | Total hours worked on Friday. |
| SAT_HOURS | NUMBER |  | 22 |  | Total hours worked on Saturday. |
| SUN_HOURS | NUMBER |  | 22 |  | Total hours worked on Sunday. |
| TOTAL_HOURS | NUMBER |  | 22 |  | Total hours worked in one week,month,etc. |
| DEFAULT_START_DAY | VARCHAR2 | 30 |  |  | Default Start Day for a week,month,etc. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| WHP_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| WHP_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_NUMBER1 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_NUMBER2 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_NUMBER3 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_NUMBER4 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_NUMBER5 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_NUMBER6 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_NUMBER7 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_NUMBER8 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_NUMBER9 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_NUMBER10 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WHP_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| WORK_SHIFT_TYPE | VARCHAR2 | 30 |  |  | The work shift type can be Time or Elapsed. For the work week, if the shift type is Time, the user must enter a start time and end time. If the shift type is Elapsed, the user must enter the number of hours. |
| WORK_DAY_DEF_ID | NUMBER |  | 18 |  | Work day definition identifier. This column is the foreign key for table HWM_WORK_DAY_DEF_B. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | To store action occurrence id from assignment in child entity |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_WORKING_HOUR_PATTERNS_F_N1 | Non Unique | Default | OBJECT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_WORKING_HOUR_PATTERNS_F_N2 | Non Unique | Default | NVL("WORK_DAY_DEF_ID",-1) |
| PWHPF_U1 | Unique | Default | WORKING_HOUR_PATTERN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
