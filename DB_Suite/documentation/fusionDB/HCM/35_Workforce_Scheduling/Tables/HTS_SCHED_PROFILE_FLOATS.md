# HTS_SCHED_PROFILE_FLOATS

Table containing list of Float Pool Departments as part of the schedule generation.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofilefloats-25571.html#htsschedprofilefloats-25571](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofilefloats-25571.html#htsschedprofilefloats-25571)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_PROFILE_FLOATS_PK | SCHED_PROFILE_FLOAT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_PROFILE_FLOAT_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a schedule profile Units |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SCHED_PROFILE_FLOAT_CODE | VARCHAR2 | 30 |  | Yes | Schedule Profile Float Pool Department Code |
| SCHED_GEN_PROFILE_ID | NUMBER |  | 18 | Yes | foreign key to Schedule Generation Profile table |
| SCHED_UNIT_ID | NUMBER |  | 18 | Yes | foreign key to Schedule Unit table |
| DEPARTMENT_ID | NUMBER |  | 18 |  | Department defined as staffing department for the schedule generation profile. |
| LOCATION_ID | NUMBER |  | 18 |  | Location added to department to define a staffing department for the schedule generation profile. |
| TIMEZONE_CODE | VARCHAR2 | 100 |  |  | Time Zone Code |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_PROFILE_FLOATS_N1 | Non Unique | Default | SCHED_UNIT_ID |
| HTS_SCHED_PROFILE_FLOATS_PK | Unique | Default | SCHED_PROFILE_FLOAT_ID |
| HTS_SCHED_PROFILE_FLOATS_U1 | Unique | Default | SCHED_PROFILE_FLOAT_CODE |
| HTS_SCHED_PROFILE_FLOATS_U2 | Unique | Default | SCHED_GEN_PROFILE_ID, DEPARTMENT_ID, LOCATION_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
