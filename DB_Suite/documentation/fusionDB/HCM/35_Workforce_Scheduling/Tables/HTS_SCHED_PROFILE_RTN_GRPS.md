# HTS_SCHED_PROFILE_RTN_GRPS

Table holding self-scheduling rotation groups which are used self-scheduling

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofilertngrps-21085.html#htsschedprofilertngrps-21085](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofilertngrps-21085.html#htsschedprofilertngrps-21085)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_PROFILE_RTN_GRPS_PK | SCHED_PROFILE_RTN_GRP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_PROFILE_RTN_GRP_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a schedule profile rotation list. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SCHED_PROFILE_RTN_GRP_CODE | VARCHAR2 | 30 |  | Yes | Schedule Profile Rotation List Code |
| SCHED_GEN_PROFILE_ID | NUMBER |  |  | Yes | foreign key to Schedule Generation Profile table |
| SCHED_PROFILE_ROTATION_ID | NUMBER |  | 18 | Yes | foreign key to Schedule Generation Profile Rotations table |
| LIST_ID | NUMBER |  | 18 | Yes | Foreign key to Condition builder for rotation groups |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_PROFILE_RTN_GRPS_PK | Unique | Default | SCHED_PROFILE_RTN_GRP_ID |
| HTS_SCHED_PROFILE_RTN_GRPS_U1 | Unique | Default | SCHED_GEN_PROFILE_ID, SCHED_PROFILE_RTN_GRP_CODE |
| HTS_SCHED_PROFILE_RTN_GRPS_U2 | Unique | Default | SCHED_GEN_PROFILE_ID, LIST_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
