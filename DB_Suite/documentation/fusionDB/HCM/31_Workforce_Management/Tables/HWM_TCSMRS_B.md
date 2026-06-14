# HWM_TCSMRS_B

Each row contains information about a Time Consumer

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcsmrsb-7437.html#hwmtcsmrsb-7437](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcsmrsb-7437.html#hwmtcsmrsb-7437)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCSMRS_B_PK | TCSMRS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCSMRS_ID | NUMBER |  | 18 | Yes | TCSMRS_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| TCSMRS_CODE | VARCHAR2 | 255 |  |  | TCSMRS_CODE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise Id |
| GRP_TYPE_ID | NUMBER |  | 18 |  | GRP_TYPE_ID |
| TM_ATRB_STRUCTURE_ID | NUMBER |  | 18 |  | FK reference to Time Attribute Structures. This is a list of Time Attributes that 'belong' to the application |
| FUSION_APPLICATION | VARCHAR2 | 3 |  | Yes | Used to determine if the Module Name should be used (Fusion Application) |
| UPDATE_RAW_TM_SVC | VARCHAR2 | 240 |  |  | Service OTL should call when it needs raw time to be updated by this Time Consumer |
| VALIDATE_RAW_TM_SVC | VARCHAR2 | 240 |  |  | Service OTL should call when it needs raw time to be validated by this Time Consumer |
| UPDATE_CALC_TM_SVC | VARCHAR2 | 240 |  |  | Service OTL should call when it needs calculated time to be updated by this Time Consumer |
| VALIDATE_CALC_TM_SVC | VARCHAR2 | 240 |  |  | Service OTL should call when it needs calculated time to be validated by this Time Consumer |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TCSMRS_B_N20 | Non Unique | Default | SGUID |
| HWM_TCSMRS_B_U1 | Unique | FUSION_TS_TX_DATA | TCSMRS_ID, ORA_SEED_SET1 |
| HWM_TCSMRS_B_U11 | Unique | FUSION_TS_TX_DATA | TCSMRS_ID, ORA_SEED_SET2 |
| HWM_TCSMRS_B_U2 | Unique | Default | TCSMRS_CODE, ENTERPRISE_ID, TCSMRS_ID, ORA_SEED_SET1 |
| HWM_TCSMRS_B_U21 | Unique | Default | TCSMRS_CODE, ENTERPRISE_ID, TCSMRS_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
