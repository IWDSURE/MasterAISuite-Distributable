# HWM_TM_ATRB_FLD_SET_CMPS

Members of a set of time attribute fields

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmatrbfldsetcmps-18191.html#hwmtmatrbfldsetcmps-18191](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmatrbfldsetcmps-18191.html#hwmtmatrbfldsetcmps-18191)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_ATRB_FLD_SET_CMPS_PK | TM_ATRB_FLD_SET_CMP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_ATRB_FLD_SET_CMP_ID | NUMBER |  | 18 | Yes | primary key |
| DATA_SOURCE | VARCHAR2 | 20 |  |  | DATA_SOURCE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TM_ATRB_FLD_ID | NUMBER |  | 18 |  | foreign key to hxt_tm_atrb_flds_b |
| TM_ATRB_FLD_SET_ID | NUMBER |  | 18 |  | foreign key to hxt_tm_atrb_fld_sets |
| TE_ALT_NAME_VAL_ID | NUMBER |  | 18 |  | foreign key to hxt_te_alt_name_vals_b |
| SEQUENCE | NUMBER |  | 3 |  | a helper for UI input |
| VALUE_SET_ID | NUMBER |  | 18 |  | foreign key to fnd_vs_value_sets |
| VALUE_SET_CODE | VARCHAR2 | 120 |  |  | VALUE_SET_CODE |
| PVO_VALUE_ID | VARCHAR2 | 80 |  |  | PVO_VALUE_ID |
| PVO_VALUE_CODE | VARCHAR2 | 80 |  |  | PVO_VALUE_CODE |
| VALUE_SET_DEPEND_ON_FLD | VARCHAR2 | 32 |  |  | VALUE_SET_DEPEND_ON_FLD |
| VALUE_SET_WHERE_CLAUSE | VARCHAR2 | 2000 |  |  | VALUE_SET_WHERE_CLAUSE |
| DATA_SOURCE_USAGE_ID | NUMBER |  | 18 |  | Foreign Key to Data Source Usages |
| USER_DATA_SOURCE_USAGE_ID | NUMBER |  | 18 |  | Foreign key to Data source Usages |
| REQUIRED_FLAG | VARCHAR2 | 20 |  |  | REQUIRED_FLAG |
| LITERAL_VALUE | VARCHAR2 | 64 |  |  | LITERAL_VALUE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
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

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWM_TM_ATRB_FLD_SET_CMPS_FK1 | Non Unique | Default | TM_ATRB_FLD_SET_ID | Obsolete |
| HWM_TM_ATRB_FLD_SET_CMPS_N20 | Non Unique | Default | SGUID |  |
| HWM_TM_ATRB_FLD_SET_CMPS_U1 | Unique | Default | TM_ATRB_FLD_SET_CMP_ID, ORA_SEED_SET1 |  |
| HWM_TM_ATRB_FLD_SET_CMPS_U11 | Unique | Default | TM_ATRB_FLD_SET_CMP_ID, ORA_SEED_SET2 |  |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
