# HTS_SCHED_PROFILE_PRSN_FLTRS_

Table containing include or excluded list of jobs and positions that are part of the schedule generation.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofileprsnfltrs-29183.html#htsschedprofileprsnfltrs-29183](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofileprsnfltrs-29183.html#htsschedprofileprsnfltrs-29183)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_PROFILE_PRSN_FL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, SCHED_PROFILE_FLTR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_PROFILE_FLTR_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a schedule profile filter |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| SCHED_PROFILE_FLTR_CODE | VARCHAR2 | 30 |  |  | Schedule Profile Filter Code |
| SCHED_GEN_PROFILE_ID | NUMBER |  | 18 |  | foreign key to Schedule Generation Profile table |
| JOB_POSITION_MEMBER_TYPE | VARCHAR2 | 30 |  |  | Specify if a rule is about a job or a position. |
| JOB_ID | NUMBER |  | 18 |  | In case the rule is about a job, job defined as filter for the rule. |
| POSITION_ID | NUMBER |  | 18 |  | In case the rule is about a position, position defined as filter for the rule. |
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
| HTS_SCHED_PROFILE_PRSN_FLT_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, SCHED_PROFILE_FLTR_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
