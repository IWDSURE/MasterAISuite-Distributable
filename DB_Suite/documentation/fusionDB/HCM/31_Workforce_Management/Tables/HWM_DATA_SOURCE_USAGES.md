# HWM_DATA_SOURCE_USAGES

Table storing the mapping between the Data Source and the Time Attribute Field. It also contains the mapping for the default data source for a time attribute field.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmdatasourceusages-20246.html#hwmdatasourceusages-20246](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmdatasourceusages-20246.html#hwmdatasourceusages-20246)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_DATA_SOURCE_USAGES_PK | DATA_SOURCE_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DATA_SOURCE_USAGE_ID | NUMBER |  | 18 | Yes | DATA_SOURCE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DATA_SOURCE_USAGE_CODE | VARCHAR2 | 120 |  | Yes | DATA_SOURCE_USAGE_CODE |
| TM_ATRB_FLD_ID | NUMBER |  | 18 | Yes | TM_ATRB_FLD_ID |
| DATA_SOURCE_ID | NUMBER |  | 18 | Yes | DATA_SOURCE_ID |
| USAGE_TYPE | VARCHAR2 | 20 |  | Yes | USAGE_TYPE |
| LINKED_USAGE_ID | NUMBER |  | 18 |  | LINKED_USAGE_ID |
| DEFAULT_FLAG | VARCHAR2 | 1 |  | Yes | DEFAULT_FLAG |
| TM_ATRB_FLD_MSTR_REF_ID | NUMBER |  | 18 |  | TM_ATRB_FLD_MSTR_REF_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
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
| HWM_DATA_SOURCE_USAGES_N1 | Non Unique | Default | TM_ATRB_FLD_ID, DATA_SOURCE_ID |
| HWM_DATA_SOURCE_USAGES_N20 | Non Unique | Default | SGUID |
| HWM_DATA_SOURCE_USAGES_U1 | Unique | Default | DATA_SOURCE_USAGE_ID, ORA_SEED_SET1 |
| HWM_DATA_SOURCE_USAGES_U11 | Unique | Default | DATA_SOURCE_USAGE_ID, ORA_SEED_SET2 |
| HWM_DATA_SOURCE_USAGES_U2 | Unique | Default | DATA_SOURCE_USAGE_CODE, ENTERPRISE_ID, ORA_SEED_SET1 |
| HWM_DATA_SOURCE_USAGES_U21 | Unique | Default | DATA_SOURCE_USAGE_CODE, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
