# HTS_SCHED_PROFILE_ROTATIONS_

Table holding self-scheduling rotations which are used self-scheduling

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofilerotations-23686.html#htsschedprofilerotations-23686](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofilerotations-23686.html#htsschedprofilerotations-23686)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_PROFILE_ROTATIN_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, SCHED_PROFILE_ROTATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_PROFILE_ROTATION_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a schedule profile rotations |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| SCHED_PROFILE_ROTATION_CODE | VARCHAR2 | 30 |  |  | Schedule Profile Rotation Code |
| SCHED_GEN_PROFILE_ID | NUMBER |  | 18 |  | foreign key to Schedule Generation Profile table |
| ROTATION_WINDOW_OPENS | NUMBER |  | 9 |  | Specifies when the rotation window opens for the rotation group |
| ROTATION_WINDOW_CLOSES | NUMBER |  | 9 |  | Specifies when the rotation window closes for the rotation group |
| IS_LAST_ROTATION_FLAG | VARCHAR2 | 1 |  |  | Specifies if the current row is for the last rotation for remaining eligible employees. |
| ROTATION_SEQUENCE | NUMBER |  | 9 |  | Specifies the rotation sequence |
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
| HTS_SCHED_PROFILE_ROTATIN_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, SCHED_PROFILE_ROTATION_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
