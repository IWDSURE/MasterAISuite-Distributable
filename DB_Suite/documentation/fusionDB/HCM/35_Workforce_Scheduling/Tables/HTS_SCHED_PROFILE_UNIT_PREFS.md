# HTS_SCHED_PROFILE_UNIT_PREFS

table to store schedule unit preferences based on schedule generation profile

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofileunitprefs-22218.html#htsschedprofileunitprefs-22218](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofileunitprefs-22218.html#htsschedprofileunitprefs-22218)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_PRF_UNIT_PREFS_PK | PROFILE_UNIT_PREFERENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_UNIT_PREFERENCE_ID | NUMBER |  | 18 | Yes | A unique system-generated identifier for schedule profile unit's preference. |
| SCHEDULE_UNIT_ID | NUMBER |  | 18 | Yes | foreign key to Schedule Unit table |
| SCHED_GEN_PROFILE_ID | NUMBER |  | 18 | Yes | foreign key to Schedule Generation Profile table |
| SETTING_TYPE | VARCHAR2 | 30 |  |  | Preference setting type |
| SETTING_VALUES | VARCHAR2 | 4000 |  |  | Preference setting value |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_PRF_UNIT_PREFS_PK | Unique | Default | PROFILE_UNIT_PREFERENCE_ID |
| HTS_SCHED_PRF_UNIT_PREFS_U1 | Unique | Default | SCHEDULE_UNIT_ID, SCHED_GEN_PROFILE_ID, SETTING_TYPE |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
