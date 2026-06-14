# HTS_SKILLS_B

This table holds the skill information for scheduling, that enables to match a worker with a task.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsskillsb-23926.html#htsskillsb-23926](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsskillsb-23926.html#htsskillsb-23926)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SKILLS_B_PK | SCHED_SKILL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_SKILL_ID | NUMBER |  | 18 | Yes | System generated identifier to uniquely identify a skill |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SCHED_SKILL_CODE | VARCHAR2 | 255 |  | Yes | Code entered when creating a skill, to uniquely identify the skill. |
| JOB_PROFILE_TYPE | VARCHAR2 | 30 |  | Yes | The type of job profile used to define the skill, may be job, job family or position. |
| JOB_PROFILE_ID | NUMBER |  | 18 | Yes | Identifier of the job profile. |
| SCHEDULING_GROUP_CODE | VARCHAR2 | 30 |  |  | Scheduling Group to group jobs. |
| COMPETENCY_ID | NUMBER |  | 18 |  | Identifier of a competency. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SKILLS_B_PK | Unique | Default | SCHED_SKILL_ID |
| HTS_SKILLS_B_U1 | Unique | Default | JOB_PROFILE_ID, SCHEDULING_GROUP_CODE, COMPETENCY_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
