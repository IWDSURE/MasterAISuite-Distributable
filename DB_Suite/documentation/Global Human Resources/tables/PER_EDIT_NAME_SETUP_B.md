# PER_EDIT_NAME_SETUP_B

This table is used to hold the configuration of the fields for entering person names on the user interface.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pereditnamesetupb-17665.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pereditnamesetupb-17665.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EDIT_NAME_SETUP_B_PK | EDIT_NAME_SETUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EDIT_NAME_SETUP_ID | NUMBER |  | 18 | Yes | System generated primary key. |
| ACTIVE_FLAG | VARCHAR2 | 30 |  |  | Y/N flag to indicate whether this field is active or not. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| NAME_STYLE_ID | NUMBER |  | 18 | Yes | Part of Alternate Key (also foreign key to PER_NAME_STYLES_B/_TL) |
| DISPLAY_SEQUENCE | NUMBER |  | 3 | Yes | Part of Alternate Key. Refers to the order that the columns will be presented |
| COLUMN_NAME | VARCHAR2 | 30 |  | Yes | Refers to a column name from PER_PERSON_NAMES_F |
| REQUIRED_FLAG | VARCHAR2 | 30 |  | Yes | Y/N flag to indicate whether field is mandatory or not |
| COLUMN_LOOKUP | VARCHAR2 | 30 |  |  | COLUMN_LOOKUP |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEEDED_REQUIRED_FLAG | VARCHAR2 | 30 |  | Yes | Y/N flag to indicate whether this Seeded field is mandatory or not. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EDIT_NAME_SETUP_B_N20 | Non Unique | Default | SGUID |
| PER_EDIT_NAME_SETUP_B_PK | Unique | Default | EDIT_NAME_SETUP_ID, ORA_SEED_SET1 |
| PER_EDIT_NAME_SETUP_B_PK1 | Unique | Default | EDIT_NAME_SETUP_ID, ORA_SEED_SET2 |
| PER_EDIT_NAME_SETUP_B_U2 | Unique | Default | NAME_STYLE_ID, COLUMN_NAME, ORA_SEED_SET1 |
| PER_EDIT_NAME_SETUP_B_U21 | Unique | Default | NAME_STYLE_ID, COLUMN_NAME, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
