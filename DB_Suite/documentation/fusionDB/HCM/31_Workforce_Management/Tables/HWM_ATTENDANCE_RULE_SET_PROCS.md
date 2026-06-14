# HWM_ATTENDANCE_RULE_SET_PROCS

table to maintain ruleset processing information for attendace tracking

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmattendancerulesetprocs-28339.html#hwmattendancerulesetprocs-28339](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmattendancerulesetprocs-28339.html#hwmattendancerulesetprocs-28339)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_ATTENDANCE_RULE_SET_PK | ATTENDANCE_RULE_SET_PROC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTENDANCE_RULE_SET_PROC_ID | NUMBER |  | 18 | Yes | Primary key to uniquely identify each row |
| RULE_SET_ID | NUMBER |  | 18 | Yes | ID to uniquely identify ruleset |
| START_TIME | TIMESTAMP |  |  | Yes | Start datetime of the records picked up by ESS job |
| END_TIME | TIMESTAMP |  |  |  | End datetime of the records picked up by ESS job |
| ESS_REQUEST_ID | NUMBER |  |  | Yes | ID to uniquely identify ESS Request |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_ATTENDANCE_RULE_SET_PK | Unique | Default | ATTENDANCE_RULE_SET_PROC_ID |
| HWM_ATTENDANCE_RULE_SET_U1 | Unique | Default | RULE_SET_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
