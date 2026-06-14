# HWM_TCSMR_IN_SETS

Each row in this table is a Time Consumer belonging to a Time Consumer Set.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcsmrinsets-22125.html#hwmtcsmrinsets-22125](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcsmrinsets-22125.html#hwmtcsmrinsets-22125)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCSMR_IN_SETS_PK | TCSMR_SET_TCSMRS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCSMR_SET_TCSMRS_ID | NUMBER |  | 18 | Yes | Surrogate Key (generated) |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TCSMRS_ID | NUMBER |  | 18 | Yes | Time Consumer that is a member of a Time Consumer Set |
| TCSMR_SET_ID | NUMBER |  | 18 | Yes | Time Consumer Set that the member belongs to |
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
| HWM_TCSMR_IN_SETS_U1 | Unique | FUSION_TS_TX_DATA | TCSMR_SET_TCSMRS_ID, ORA_SEED_SET1 |
| HWM_TCSMR_IN_SETS_U11 | Unique | FUSION_TS_TX_DATA | TCSMR_SET_TCSMRS_ID, ORA_SEED_SET2 |
| HWM_TCSMR_IN_SETS_U2 | Unique | Default | TCSMRS_ID, ENTERPRISE_ID, TCSMR_SET_ID, ORA_SEED_SET1 |
| HWM_TCSMR_IN_SETS_U21 | Unique | Default | TCSMRS_ID, ENTERPRISE_ID, TCSMR_SET_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
