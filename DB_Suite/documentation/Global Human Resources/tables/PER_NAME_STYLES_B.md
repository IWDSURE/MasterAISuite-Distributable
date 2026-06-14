# PER_NAME_STYLES_B

This table is used to associate name style with legislation. It holds one row for the universal name style plus additional rows for legislations that wish to define their own name style.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernamestylesb-15740.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernamestylesb-15740.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_NAME_STYLES_B_PK | NAME_STYLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NAME_STYLE_ID | NUMBER |  | 18 | Yes | System generated primary key. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  | Yes | Alternate Key. Can be valid legislation code or ???WW??? for the universal style |
| ALTERNATE_NAME_REQUIRED | VARCHAR2 | 30 |  | Yes | Y/N flag to indicate whether an alternate-language name (i.e. different language from corporate language) must be entered for this style. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
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
|-------|------------|------------|----------|
| PER_NAME_STYLES_B_PK | Unique | Default | NAME_STYLE_ID, ORA_SEED_SET1 |
| PER_NAME_STYLES_B_PK1 | Unique | Default | NAME_STYLE_ID, ORA_SEED_SET2 |
| PER_NAME_STYLES_B_U1 | Unique | Default | LEGISLATION_CODE, ORA_SEED_SET1 |
| PER_NAME_STYLES_B_U11 | Unique | Default | LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
