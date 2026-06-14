# HR_NAME_FORMATS

This table stores the setup data defining name formats, which are the rules for constructing various formatted names from individual name components

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrnameformats-31170.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrnameformats-31170.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_NAME_FORMATS_PK | NAME_FORMAT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NAME_FORMAT_ID | NUMBER |  | 18 | Yes | System generated part of primary key. Surrogate key |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| FORMAT_NAME | VARCHAR2 | 80 |  | Yes | Identifies the type of formatted name this applies to |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Identifies the legislation of the formatted name |
| USER_FORMAT_CHOICE | VARCHAR2 | 1 |  | Yes | Identifies the target audience of the formatted name, whether the name is to be understood in a Global or a Local (legislation specific) context |
| FORMAT_MASK | VARCHAR2 | 250 |  | Yes | Stores coded string that system understands to use in constructing formatted names. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_NAME_FORMATS_N20 | Non Unique | Default | SGUID |
| HR_NAME_FORMATS_PK | Unique | Default | NAME_FORMAT_ID, ORA_SEED_SET1 |
| HR_NAME_FORMATS_PK1 | Unique | Default | NAME_FORMAT_ID, ORA_SEED_SET2 |
| HR_NAME_FORMATS_U1 | Unique | Default | BUSINESS_GROUP_ID, FORMAT_NAME, LEGISLATION_CODE, USER_FORMAT_CHOICE, ORA_SEED_SET1 |
| HR_NAME_FORMATS_U11 | Unique | Default | BUSINESS_GROUP_ID, FORMAT_NAME, LEGISLATION_CODE, USER_FORMAT_CHOICE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
