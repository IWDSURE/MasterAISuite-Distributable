# HWM_WORK_DAY_DEF_B

It contains workday definition information.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmworkdaydefb-27467.html#hwmworkdaydefb-27467](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmworkdaydefb-27467.html#hwmworkdaydefb-27467)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_WORK_DAY_DEF_B_PK | WORK_DAY_DEF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORK_DAY_DEF_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| WORK_DAY_DEF_CD | VARCHAR2 | 80 |  |  | This column would be used as alternate key |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| DAY_START_TIME | TIMESTAMP |  |  |  | DAY_START_TIME |
| DAY_BREAKER_RULE | VARCHAR2 | 30 |  |  | DAY_BREAKER_RULE |
| EARNED_DAY_BREAK_RULE | VARCHAR2 | 30 |  |  | EARNED_DAY_BREAK_RULE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. oracle internal use only |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| BREAK_THRESHOLD | NUMBER |  | 4 |  | BREAK_THRESHOLD |
| EARNED_BREAK_THRESHOLD | NUMBER |  | 4 |  | EARNED_BREAK_THRESHOLD |
| TIE_BREAK_CRITERIA | VARCHAR2 | 80 |  |  | Tie Break Rule |
| EARNED_TIE_BREAK_CRITERIA | VARCHAR2 | 80 |  |  | EARNED_TIE_BREAK_CRITERIA |
| IS_OVERTIME_NEXT_DAY | VARCHAR2 | 1 |  |  | IS_OVERTIME_NEXT_DAY |
| EARNED_DAY_START_TIME | TIMESTAMP |  |  |  | Start time of the earned day |
| IS_EARNED_NEXT_DAY | VARCHAR2 | 1 |  |  | 'Y' indicates that the earned day start time is the start of the next day. 'N' indicates that earned day start time is the start of the current day |
| IS_SAME_DEFINITION | VARCHAR2 | 1 |  |  | 'Y' indicates that the earned day and the overtime day have the same start time and spanning days rule |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_WORK_DAY_DEF_B_N20 | Non Unique | Default | SGUID |
| HWM_WORK_DAY_DEF_B_U1 | Unique | Default | WORK_DAY_DEF_ID, ORA_SEED_SET1 |
| HWM_WORK_DAY_DEF_B_U11 | Unique | Default | WORK_DAY_DEF_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
