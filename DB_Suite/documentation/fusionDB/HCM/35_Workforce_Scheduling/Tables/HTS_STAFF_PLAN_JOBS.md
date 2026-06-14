# HTS_STAFF_PLAN_JOBS

Table holding the Schedule Staffing Plan Jobs used in the Staffing grids

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffplanjobs-28200.html#htsstaffplanjobs-28200](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffplanjobs-28200.html#htsstaffplanjobs-28200)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_STAFF_PLAN_JOBS_PK | STAFF_PLAN_JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STAFF_PLAN_JOB_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a Staffing Plan Skills |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| STAFF_PLAN_ID | NUMBER |  | 18 | Yes | Foreign key to Staffing Plan table |
| JOB_PROFILE_TYPE | VARCHAR2 | 30 |  |  | Job Profile Type |
| JOB_PROFILE_ID | NUMBER |  | 18 |  | Job Profile Id |
| JOB_PROFILE_CODE | VARCHAR2 | 30 |  |  | Job Profile Code |
| STAFF_PLAN_SKILL_ID | NUMBER |  | 18 |  | Filtered Skill Without Qualifications |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_STAFF_PLAN_JOBS_PK | Unique | Default | STAFF_PLAN_JOB_ID |
| HTS_STAFF_PLAN_JOBS_U1 | Unique | Default | STAFF_PLAN_ID, JOB_PROFILE_TYPE, JOB_PROFILE_ID, JOB_PROFILE_CODE |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
