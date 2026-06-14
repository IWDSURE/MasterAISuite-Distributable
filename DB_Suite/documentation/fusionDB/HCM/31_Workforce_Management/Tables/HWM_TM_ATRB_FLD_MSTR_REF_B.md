# HWM_TM_ATRB_FLD_MSTR_REF_B

Table to identify the master  references for all detail instance attributes.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmatrbfldmstrrefb-30696.html#hwmtmatrbfldmstrrefb-30696](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmatrbfldmstrrefb-30696.html#hwmtmatrbfldmstrrefb-30696)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_ATRB_FLD_MSTR_REF_B_PK | TM_ATRB_FLD_MSTR_REF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_ATRB_FLD_MSTR_REF_ID | NUMBER |  | 18 | Yes | TM_ATRB_FLD_MSTR_INS_REF_IDFR |
| TM_ATRB_FLD_MSTR_REF_CODE | VARCHAR2 | 150 |  | Yes | TM_ATRB_FLD_MSTR_REF_CODE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| TM_ATRB_FLD_ID | NUMBER |  | 18 | Yes | TM_ATRB_FLD_ID |
| MASTER_INSTANCE_IDENTIFIER | VARCHAR2 | 150 |  | Yes | MASTER_INSTANCE_IDENTIFIER |
| DET_INS_ATTRIBUTE_TYPE | VARCHAR2 | 20 |  | Yes | DET_INS_ATTRIBUTE_TYPE |
| DET_INS_VALUE_LOCATION | VARCHAR2 | 32 |  | Yes | DES_INS_VALUE_LOCATION |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| TM_ATRB_FLD_ESS_PROCESS_ID | NUMBER |  | 18 |  | TM_ATRB_FLD_ESS_PROCESS_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_ATRB_FLD_MSTR_REF_B_N20 | Non Unique | Default | SGUID, START_DATE, END_DATE |
| HXT_TM_ATFLD_MSRF_B_N1 | Non Unique | Default | MASTER_INSTANCE_IDENTIFIER, LEGISLATIVE_DATA_GROUP_ID |
| HXT_TM_ATFLD_MSRF_B_N2 | Non Unique | Default | MASTER_INSTANCE_IDENTIFIER, LEGISLATION_CODE |
| HXT_TM_ATFLD_MSRF_B_U1 | Unique | Default | TM_ATRB_FLD_MSTR_REF_ID, ORA_SEED_SET1 |
| HXT_TM_ATFLD_MSRF_B_U11 | Unique | Default | TM_ATRB_FLD_MSTR_REF_ID, ORA_SEED_SET2 |
| HXT_TM_ATFLD_MSRF_B_U2 | Unique | Default | TM_ATRB_FLD_MSTR_REF_CODE, ENTERPRISE_ID, ORA_SEED_SET1 |
| HXT_TM_ATFLD_MSRF_B_U21 | Unique | Default | TM_ATRB_FLD_MSTR_REF_CODE, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
