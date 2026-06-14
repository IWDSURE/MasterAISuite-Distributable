# HWM_RP_TM_PERIODS_B

Repeating Time Periods Base table

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrptmperiodsb-21266.html#hwmrptmperiodsb-21266](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrptmperiodsb-21266.html#hwmrptmperiodsb-21266)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RP_TM_PERIODS_B_PK | REPEATING_TM_PERIOD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REPEATING_TM_PERIOD_ID | NUMBER |  | 18 | Yes | REPEATING_TM_PERIOD_ID |
| ATTENDANCE_TRACKING_USAGE | VARCHAR2 | 30 |  |  | Used for Attendance Tracking |
| ACCRUAL_USAGE | VARCHAR2 | 30 |  |  | ACCRUAL_USAGE |
| OVERTIME_USAGE | VARCHAR2 | 30 |  |  | OVERTIME_USAGE |
| BALANCE_USAGE | VARCHAR2 | 30 |  |  | BALANCE_USAGE |
| PERIOD_CD | VARCHAR2 | 80 |  |  | PERIOD_CD |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| PERIOD_CLASS | VARCHAR2 | 32 |  | Yes | PERIOD_CLASS |
| PERIOD_TYPE | VARCHAR2 | 32 |  | Yes | PERIOD_TYPE |
| PERIOD_START_DATE | DATE |  |  |  | PERIOD_START_DATE |
| MULTIPLE | NUMBER |  | 3 |  | MULTIPLE |
| MONTH_TYPE | VARCHAR2 | 32 |  |  | MONTH_TYPE |
| ONE_OR_MANY | VARCHAR2 | 32 |  |  | ONE_OR_MANY |
| WEEK_TYPE | VARCHAR2 | 32 |  |  | WEEK_TYPE |
| PERIOD_LENGTH | NUMBER |  | 2 |  | PERIOD_LENGTH |
| REFERENCE_DATE | DATE |  |  |  | DAY_REFERENCE_DATE |
| RULE_USAGE | VARCHAR2 | 30 |  |  | RULE_USAGE |
| TIME_ENTRY_USAGE | VARCHAR2 | 30 |  |  | TIME_ENTRY_USAGE |
| APPROVAL_USAGE | VARCHAR2 | 30 |  |  | APPROVAL_USAGE |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RP_TM_PERIODS_B_N1 | Non Unique | Default | PERIOD_CLASS |
| HWM_RP_TM_PERIODS_B_N20 | Non Unique | Default | SGUID |
| HWM_RP_TM_PERIODS_B_U1 | Unique | Default | REPEATING_TM_PERIOD_ID, ORA_SEED_SET1 |
| HWM_RP_TM_PERIODS_B_U11 | Unique | Default | REPEATING_TM_PERIOD_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
