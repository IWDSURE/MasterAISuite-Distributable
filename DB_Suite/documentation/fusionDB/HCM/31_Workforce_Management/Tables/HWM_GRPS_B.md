# HWM_GRPS_B

This table contains details for HCM groups

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpsb-31532.html#hwmgrpsb-31532](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpsb-31532.html#hwmgrpsb-31532)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_GRPS_B_PK | GRP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GRP_ID | NUMBER |  | 18 | Yes | GRP_ID |
| LIST_ID | NUMBER |  | 18 |  | FK to hr_vbcs_lists |
| EVAL_SOURCE_CD | VARCHAR2 | 30 |  |  | Source of Evaluation for Group, either Criteria or Rules. |
| ONLINE_EVAL_FLAG | VARCHAR2 | 30 |  |  | ONLINE_EVAL_FLAG |
| MASS_EVAL_FLAG | VARCHAR2 | 30 |  |  | MASS_EVAL_FLAG |
| GRP_CODE | VARCHAR2 | 960 |  |  | GRP_CODE |
| APPL_USG_CD | VARCHAR2 | 30 |  |  | APPL_USG_CD |
| APPLIES_TO_CD | VARCHAR2 | 30 |  |  | APPLIES_TO_CD |
| FREEZE_FLAG | VARCHAR2 | 30 |  |  | FREEZE_FLAG |
| RUN_TYPE | VARCHAR2 | 30 |  |  | RUN_TYPE |
| EVAL_STATUS_CD | VARCHAR2 | 30 |  |  | EVAL_STATUS_CD |
| NUM_DAYS_PREV | NUMBER |  | 9 |  | NUM_DAYS_PREV |
| NUM_DAYS_NEXT | NUMBER |  | 9 |  | NUM_DAYS_NEXT |
| LAST_REFRESH_DT | TIMESTAMP |  |  |  | LAST_REFRESH_DT |
| NEXT_REFRESH_DT | TIMESTAMP |  |  |  | NEXT_REFRESH_DT |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ASSIGNMENT_TO_USE_CD | VARCHAR2 | 20 |  |  | ASSIGNMENT_TO_USE_CD |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| MEM_TYPE_CD | VARCHAR2 | 30 |  |  | MEM_TYPE_CD |
| INCLUDE_SUSPENDED | VARCHAR2 | 30 |  |  | INCLUDE_SUSPENDED |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_GRPS_B_N10 | Non Unique | Default | NVL2("MODULE_ID",'Y','N'), ENTERPRISE_ID, GRP_ID |
| HWM_GRPS_B_N20 | Non Unique | Default | SGUID |
| HWM_GRPS_B_U1 | Unique | FUSION_TS_TX_DATA | GRP_ID, ORA_SEED_SET1 |
| HWM_GRPS_B_U11 | Unique | FUSION_TS_TX_DATA | GRP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
