# HTS_SCHEDULE_GEN_PROFILES_B

Base table containing schedule generation profile information used to generate schedules.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedulegenprofilesb-24802.html#htsschedulegenprofilesb-24802](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedulegenprofilesb-24802.html#htsschedulegenprofilesb-24802)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHEDULE_GEN_PROFILES_PK | SCHED_GEN_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SCHED_GEN_PROFILE_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a schedule generation profile |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support | Active |
| SCHED_PROFILE_CODE | VARCHAR2 | 30 |  | Yes | Schedule Generation Profile Code |  |
| ACTIVE_START_DATE | DATE |  |  | Yes | Schedule Generation Profile Active Start Date |  |
| ACTIVE_END_DATE | DATE |  |  |  | Schedule Generation Profile Active End Date |  |
| SCHEDULE_PERIOD_WEEKS | NUMBER |  | 9 |  | Schedule Period Cycle in Weeks |  |
| SCHEDULE_PERIOD_START_DATE | DATE |  |  |  | Schedule Period Start Date |  |
| GEN_WINDOW_START | NUMBER |  | 9 |  | Number of days before the schedule period starts to open the schedule generation window. |  |
| GEN_WINDOW_END | NUMBER |  | 9 |  | Number of days before the schedule period starts to close the schedule generation window. |  |
| SELF_SCHED_START_OFFSET | NUMBER |  | 9 |  | Number of days before the schedule period starts to open the self scheduling window. |  |
| SELF_SCHED_END_OFFSET | NUMBER |  | 9 |  | Number of days before the schedule period starts to close the self scheduling window. |  |
| START_OF_WORK_WEEK | VARCHAR2 | 30 |  |  | First Day of the Schedule Period Week |  |
| MON_IS_WEEKEND_FLAG | VARCHAR2 | 1 |  |  | MON_IS_WEEKEND_FLAG |  |
| TUE_IS_WEEKEND_FLAG | VARCHAR2 | 1 |  |  | TUE_IS_WEEKEND_FLAG |  |
| WED_IS_WEEKEND_FLAG | VARCHAR2 | 1 |  |  | WED_IS_WEEKEND_FLAG |  |
| THU_IS_WEEKEND_FLAG | VARCHAR2 | 1 |  |  | THU_IS_WEEKEND_FLAG |  |
| FRI_IS_WEEKEND_FLAG | VARCHAR2 | 1 |  |  | FRI_IS_WEEKEND_FLAG |  |
| SAT_IS_WEEKEND_FLAG | VARCHAR2 | 1 |  |  | SAT_IS_WEEKEND_FLAG |  |
| SUN_IS_WEEKEND_FLAG | VARCHAR2 | 1 |  |  | SUN_IS_WEEKEND_FLAG |  |
| AUTO_GENERATE_SCHED_FLAG | VARCHAR2 | 1 |  |  | Specify if the schedule is automatically generated when the schedule generation window opens. |  |
| AUTO_GENERATE_TYPE | VARCHAR2 | 30 |  |  | When the schedule is automatically generated, specify the generation method type, such as open shift or automatic assignment. |  |
| AUTO_PUBLISH_SCHED_FLAG | VARCHAR2 | 1 |  |  | Specify if the schedule is automatically published 1 day after the schedule generation window closes. |  |
| ALERT_FINALIZE_FLAG | VARCHAR2 | 1 |  |  | Specify whether to send schedulers notifications to finalize their schedules. |  |
| ALERT_FINALIZE_DAYS_OFFSET | NUMBER |  | 9 |  | ALERT_FINALIZE_DAYS_OFFSET |  |
| JOB_POS_INCL_EXCL_RULE | VARCHAR2 | 30 |  |  | JOB_POS_INCL_EXCL_RULE |  |
| IS_DRAFT | VARCHAR2 | 1 |  |  | Indicates whether a profile is still in draft mode and has not been fully validated. |  |
| RULE_SET_ID | NUMBER |  | 18 |  | RULE_SET_ID |  |
| DAY_START_TIME_OFFSET | NUMBER |  | 9 |  | Day Start Time offset |  |
| FLOAT_BETWEEN_DEPTS_FLAG | VARCHAR2 | 1 |  |  | Indicator to define if workers can float between departments of the schedule generation profile |  |
| FLOAT_POOL_DEPTS_FLAG | VARCHAR2 | 1 |  |  | Indicator to define if self scheduling allowed for float pool department workers |  |
| GRACE_PERIOD | NUMBER |  | 9 |  | Clock integration Threshold to ignore violation |  |
| START_EARLY_PERIOD | NUMBER |  | 9 |  | Clock integration start early grace period for violation |  |
| START_LATE_PERIOD | NUMBER |  | 9 |  | Clock integration Start late grace period for violation |  |
| END_EARLY_PERIOD | NUMBER |  | 9 |  | Clock integration end early grace period for violation |  |
| END_LATE_PERIOD | NUMBER |  | 9 |  | Clock integration end late grace period for violation |  |
| START_EARLY_VIOLATION_TYPE | VARCHAR2 | 30 |  |  | Clock integration start early violation message |  |
| START_LATE_VIOLATION_TYPE | VARCHAR2 | 30 |  |  | Clock integration start late violation message |  |
| END_EARLY_VIOLATION_TYPE | VARCHAR2 | 30 |  |  | Clock integration end early violation message |  |
| END_LATE_VIOLATION_TYPE | VARCHAR2 | 30 |  |  | Clock integration end late violation message |  |
| SELF_SCHED_RTN_ENABLED_FLAG | VARCHAR2 | 1 |  |  | Specifies if the rotation is enabled for Self-scheduling. |  |
| SELF_SCHED_ROTATION_TYPE | VARCHAR2 | 30 |  |  | Rotation Type used for Self-scheduling |  |
| SELF_SCHED_RTN_LAST_UPD_DATE | TIMESTAMP |  |  |  | Specifies the date when self-scheduling rotation is last updated. |  |
| DEVIATION_ALLOW_TIME_FLAG | VARCHAR2 | 1 |  |  | Indicates whether time deviation is allowed for operating shifts. |  |
| DEVIATION_ALLOW_START_MINUTES | NUMBER |  | 9 |  | Indicates the default deviation allowance in minutes for operating shift start time. |  |
| DEVIATION_ALLOW_END_MINUTES | NUMBER |  | 9 |  | Indicates the default deviation allowance in minutes for operating shift end time. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HTS_SCHEDULE_GEN_PROFILES_PK | Unique | Default | SCHED_GEN_PROFILE_ID | Active |
| HTS_SCHEDULE_GEN_PROFILES_U1 | Unique | Default | SCHED_PROFILE_CODE |  |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
