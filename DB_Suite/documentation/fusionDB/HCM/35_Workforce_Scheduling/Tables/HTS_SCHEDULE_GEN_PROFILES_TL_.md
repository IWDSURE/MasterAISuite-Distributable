# HTS_SCHEDULE_GEN_PROFILES_TL_

Table containing  translatable name and description of Schedule Generation Profiles.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedulegenprofilestl-16782.html#htsschedulegenprofilestl-16782](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedulegenprofilestl-16782.html#htsschedulegenprofilestl-16782)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHEDULE_GEN_PROF_TL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, SCHED_GEN_PROFILE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_GEN_PROFILE_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a schedule generation profile |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Standard Enterprise Identifier column for multi tenancy support |
| SOURCE_LANG | VARCHAR2 | 4 |  |  | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| PROFILE_NAME | VARCHAR2 | 240 |  |  | Name of the schedule generation profile. |
| PROFILE_DESCRIPTION | VARCHAR2 | 2000 |  |  | Description of the schedule generation profile. |
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
| HTS_SCHEDULE_GEN_PROF_TL_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, SCHED_GEN_PROFILE_ID, LANGUAGE |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
