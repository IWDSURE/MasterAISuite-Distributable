# HTS_SCHED_PROFILE_MANAGERS

Table containing schedule managers or individuals who have access to schedule generation profile for the schedule generation.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofilemanagers-18328.html#htsschedprofilemanagers-18328](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofilemanagers-18328.html#htsschedprofilemanagers-18328)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_PROFILE_MANAGERS_PK | SCHED_PROFILE_MGR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_PROFILE_MGR_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a schedule profile Managers |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SCHED_PROFILE_MGR_CODE | VARCHAR2 | 30 |  | Yes | Schedule Profile Managers Code |
| SCHED_GEN_PROFILE_ID | NUMBER |  | 18 | Yes | foreign key to Schedule Generation Profile table |
| PERSON_ID | NUMBER |  | 18 | Yes | Person defined as schedule manager for the schedule generation profile. |
| START_DATE | DATE |  |  |  | Date when the manager can start generating and publishing schedules for the schedule generation profile. |
| END_DATE | DATE |  |  |  | Date when the manager can no longer generating and publishing schedules for the schedule generation profile. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_PROFILE_MANAGERS_N1 | Non Unique | Default | SCHED_GEN_PROFILE_ID |
| HTS_SCHED_PROFILE_MANAGERS_PK | Unique | Default | SCHED_PROFILE_MGR_ID |
| HTS_SCHED_PROFILE_MANAGERS_U1 | Unique | Default | SCHED_PROFILE_MGR_CODE |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
