# HTS_SCHED_PROFILE_FLOATS_

Table containing list of Float Pool Departments as part of the schedule generation.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofilefloats-30015.html#htsschedprofilefloats-30015](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofilefloats-30015.html#htsschedprofilefloats-30015)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_PROFILE_FLOATS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, SCHED_PROFILE_FLOAT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_PROFILE_FLOAT_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a schedule profile Units |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| SCHED_PROFILE_FLOAT_CODE | VARCHAR2 | 30 |  |  | Schedule Profile Float Pool Department Code |
| SCHED_GEN_PROFILE_ID | NUMBER |  | 18 |  | foreign key to Schedule Generation Profile table |
| SCHED_UNIT_ID | NUMBER |  | 18 |  | foreign key to Schedule Unit table |
| DEPARTMENT_ID | NUMBER |  | 18 |  | Department defined as staffing department for the schedule generation profile. |
| LOCATION_ID | NUMBER |  | 18 |  | Location added to department to define a staffing department for the schedule generation profile. |
| TIMEZONE_CODE | VARCHAR2 | 100 |  |  | Time Zone Code |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_PROFILE_FLOATSN1_ | Non Unique | Default | SCHED_PROFILE_FLOAT_ID |
| HTS_SCHED_PROFILE_FLOATSU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, SCHED_PROFILE_FLOAT_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
