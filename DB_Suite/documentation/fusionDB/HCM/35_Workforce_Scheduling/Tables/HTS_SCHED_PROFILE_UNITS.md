# HTS_SCHED_PROFILE_UNITS

Table containing list of departments and locations that defines the group to be staffed as part of the schedule generation.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofileunits-11580.html#htsschedprofileunits-11580](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofileunits-11580.html#htsschedprofileunits-11580)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_PROFILE_UNITS_PK | SCHED_PROFILE_UNIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_PROFILE_UNIT_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a schedule profile Units |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SCHED_PROFILE_UNIT_CODE | VARCHAR2 | 30 |  | Yes | Schedule Profile Units Code |
| SCHED_GEN_PROFILE_ID | NUMBER |  | 18 | Yes | foreign key to Schedule Generation Profile table |
| ACTIVE_END_DATE | DATE |  |  |  | This field is also set to the same Active end date when a Schedule Generation Profile becomes inactive in order to eliminate duplicate key restrictions based on department or location for other Schedule Generation Profiles. |
| SCHED_UNIT_ID | NUMBER |  | 18 | Yes | foreign key to Schedule Unit table |
| DEPARTMENT_ID | NUMBER |  | 18 |  | Department defined as staffing department for the schedule generation profile. |
| LOCATION_ID | NUMBER |  | 18 |  | Location added to department to define a staffing department for the schedule generation profile. |
| TIMEZONE_CODE | VARCHAR2 | 100 |  |  | Time Zone Code |
| FLOAT_POOL_DEPARTMENT_FLAG | VARCHAR2 | 1 |  |  | Float pool department flag |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_PROFILE_UNITS_N1 | Non Unique | Default | SCHED_GEN_PROFILE_ID |
| HTS_SCHED_PROFILE_UNITS_N2 | Non Unique | Default | SCHED_UNIT_ID |
| HTS_SCHED_PROFILE_UNITS_PK | Unique | Default | SCHED_PROFILE_UNIT_ID |
| HTS_SCHED_PROFILE_UNITS_U1 | Unique | Default | SCHED_PROFILE_UNIT_CODE |
| HTS_SCHED_PROFILE_UNITS_U2 | Unique | Default | DEPARTMENT_ID, LOCATION_ID, ACTIVE_END_DATE |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
