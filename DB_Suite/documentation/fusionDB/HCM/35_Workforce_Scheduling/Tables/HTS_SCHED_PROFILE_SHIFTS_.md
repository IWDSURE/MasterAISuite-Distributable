# HTS_SCHED_PROFILE_SHIFTS_

Table holding shifts from the shift library which are to be scheduled for the profile

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofileshifts-27543.html#htsschedprofileshifts-27543](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofileshifts-27543.html#htsschedprofileshifts-27543)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_PROFILE_SHIFTS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, SCHED_PROFILE_SHIFT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_PROFILE_SHIFT_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a schedule profile Shifts |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| SCHED_PROFILE_SHIFT_CODE | VARCHAR2 | 30 |  |  | Schedule Profile Shifts Code |
| SCHED_GEN_PROFILE_ID | NUMBER |  | 18 |  | foreign key to Schedule Generation Profile table |
| SHIFT_ID | NUMBER |  | 18 |  | Shift to be used as operating shift. |
| ON_CALL_FLAG | VARCHAR2 | 1 |  |  | On Call Flag |
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
| HTS_SCHED_PROFILE_SHIFTS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, SCHED_PROFILE_SHIFT_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
