# HTS_SCHED_PROFILE_COV_INTVLS

Table containing coverage day intervals that are part of the schedule generation.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofilecovintvls-29094.html#htsschedprofilecovintvls-29094](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofilecovintvls-29094.html#htsschedprofilecovintvls-29094)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_PROFILE_INTVLS_PK | SCHED_PROFILE_INTVL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_PROFILE_INTVL_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a schedule profile Shifts |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SCHED_PROFILE_INTVL_CODE | VARCHAR2 | 30 |  | Yes | Schedule Profile Coverage Interval Code. This Column used is an alternate key. |
| SCHED_GEN_PROFILE_ID | NUMBER |  | 18 | Yes | foreign key to Schedule Generation Profile table |
| INTERVAL_IN_MINUTES | NUMBER |  | 9 | Yes | Interval length in minutes |
| NUMBER_OF_INTERVALS | NUMBER |  | 9 | Yes | Number of intervals |
| START_TIME_OFFSET | NUMBER |  | 9 | Yes | Coverage interval start time offset in minutes from midnight |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_PROFILE_INTVLS_PK | Unique | Default | SCHED_PROFILE_INTVL_ID |
| HTS_SCHED_PROFILE_INTVLS_U1 | Unique | Default | SCHED_PROFILE_INTVL_CODE |
| HTS_SCHED_PROFILE_INTVLS_U2 | Unique | Default | SCHED_GEN_PROFILE_ID, START_TIME_OFFSET |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
