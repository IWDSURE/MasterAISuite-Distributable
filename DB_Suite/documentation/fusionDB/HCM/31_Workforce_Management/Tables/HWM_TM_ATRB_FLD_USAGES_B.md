# HWM_TM_ATRB_FLD_USAGES_B

A Table to identify the usages of attributes for the corresponding contexts.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmatrbfldusagesb-21947.html#hwmtmatrbfldusagesb-21947](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmatrbfldusagesb-21947.html#hwmtmatrbfldusagesb-21947)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_ATRB_FLD_USAGES_B_PK | TM_ATRB_FLD_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_ATRB_FLD_USAGE_ID | NUMBER |  | 18 | Yes | Primary key of the Time Attribute Field Usages |
| TM_ATRB_FLD_CODE | VARCHAR2 | 240 |  |  | TM_ATRB_FLD_CODE |
| CXT_CODE | VARCHAR2 | 64 |  |  | Name of application that uses attributes (like TimeCardFields, TimeCategory etc) |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| TM_ATRB_FLD_CONTEXT_ID | NUMBER |  | 18 | Yes | Foreign Key to HWM_TM_ATRB_FLD_CONTEXTS |
| TM_ATRB_FLD_ID | NUMBER |  | 18 | Yes | Foreign key to HWM_TM_ATRB_FLDS_B |
| USER_DATA_SOURCE_USAGE_ID | NUMBER |  | 18 |  | Seeded attribute usages: use the seeded USER data source usage ID from hxt_tclayfld_defns_b table |
| ADMIN_DATA_SOURCE_USAGE_ID | NUMBER |  | 18 |  | Seeded attribute usages: use the seeded ADMIN data source usage ID from hxt_tclayfld_defns_b table |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| NAME | VARCHAR2 | 240 |  |  | Overridden Name (optional) |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_ATRB_FLD_USAGES_B_N1 | Non Unique | Default | TM_ATRB_FLD_CODE, CXT_CODE |
| HWM_TM_ATRB_FLD_USAGES_B_N20 | Non Unique | Default | SGUID |
| HWM_TM_ATRB_FLD_USAGES_B_U1 | Unique | Default | TM_ATRB_FLD_USAGE_ID, ORA_SEED_SET1 |
| HWM_TM_ATRB_FLD_USAGES_B_U11 | Unique | Default | TM_ATRB_FLD_USAGE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
