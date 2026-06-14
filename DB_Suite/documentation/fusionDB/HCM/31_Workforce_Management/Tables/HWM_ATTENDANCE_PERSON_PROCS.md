# HWM_ATTENDANCE_PERSON_PROCS

table to maintain person processing information for attendance tracking

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmattendancepersonprocs-30080.html#hwmattendancepersonprocs-30080](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmattendancepersonprocs-30080.html#hwmattendancepersonprocs-30080)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_ATTENDANCE_PERSON_PROC_PK | ATTENDANCE_PERSON_PROC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTENDANCE_PERSON_PROC_ID | NUMBER |  | 18 | Yes | Primary Key to uniquely identify each row. |
| PERSON_ID | NUMBER |  | 18 | Yes | ID to uniquely identify the person for whom violation has been processsed |
| RULE_SET_ID | NUMBER |  | 18 | Yes | ID to uniquely identify ruleset |
| RULE_EXEC_STATUS | VARCHAR2 | 100 |  | Yes | Status of the ruleset execution for the person |
| RETRY_COUNT | NUMBER |  |  |  | Total number of retry counts by ESS jobs |
| OVERRIDE_TIME | TIMESTAMP |  |  |  | Datetime of failed records, which will override the ruleSet default datetime |
| LAST_RUN_ERROR | VARCHAR2 | 2000 |  |  | Error description from last ESS job execution |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_ATTENDANCE_PERSON_PROCS_PK | Unique | Default | ATTENDANCE_PERSON_PROC_ID |
| HWM_ATTENDANCE_PERSON_PROCS_U1 | Unique | Default | RULE_SET_ID, PERSON_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
