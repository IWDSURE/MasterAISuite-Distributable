# HWM_RP_TM_RESOLVED

This table holds the generated repeating period.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrptmresolved-19330.html#hwmrptmresolved-19330](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrptmresolved-19330.html#hwmrptmresolved-19330)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RP_TM_RESOLVED_PK | RESOLVED_TM_PERIOD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RESOLVED_TM_PERIOD_ID | NUMBER |  | 18 | Yes | RESOLVED_TM_PERIOD_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REPEATING_TM_PERIOD_ID | NUMBER |  | 18 |  | REPEATING_TM_PERIOD_ID |
| START_DATE | TIMESTAMP |  |  |  | START_DATE |
| END_DATE | TIMESTAMP |  |  |  | END_DATE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RP_TM_RESOLVED_N1 | Non Unique | FUSION_TS_TX_DATA | REPEATING_TM_PERIOD_ID, START_DATE, END_DATE |
| HWM_RP_TM_RESOLVED_PK | Unique | Default | RESOLVED_TM_PERIOD_ID, ORA_SEED_SET1 |
| HWM_RP_TM_RESOLVED_PK1 | Unique | Default | RESOLVED_TM_PERIOD_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
