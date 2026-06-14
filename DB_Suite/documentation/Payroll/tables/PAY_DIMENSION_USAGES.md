# PAY_DIMENSION_USAGES

This table contains details of how dimensions are used and named within a legislation.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydimensionusages-26816.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydimensionusages-26816.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DIMENSION_USAGES_PK | DIMENSION_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DIMENSION_USAGE_ID | NUMBER |  | 18 | Yes | DIMENSION_USAGE_ID |
| BALANCE_DIMENSION_ID | NUMBER |  | 18 | Yes | BALANCE_DIMENSION_ID |
| DATABASE_ITEM_SUFFIX | VARCHAR2 | 80 |  | Yes | DATABASE_ITEM_SUFFIX |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| USE_IN_EXCEP_REPORTING_FLAG | VARCHAR2 | 1 |  |  | Indicates whether the Balance dimension can be used in balance exception reporting for this Legislation |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
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
| PAY_DIMENSION_USAGES_N20 | Non Unique | Default | SGUID |
| PAY_DIMENSION_USAGES_PK | Unique | Default | DIMENSION_USAGE_ID, ORA_SEED_SET1 |
| PAY_DIMENSION_USAGES_PK1 | Unique | Default | DIMENSION_USAGE_ID, ORA_SEED_SET2 |
| PAY_DIMENSION_USAGES_U1 | Unique | Default | BALANCE_DIMENSION_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_DIMENSION_USAGES_U11 | Unique | Default | BALANCE_DIMENSION_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |
| PAY_DIMENSION_USAGES_U2 | Unique | Default | DATABASE_ITEM_SUFFIX, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_DIMENSION_USAGES_U21 | Unique | Default | DATABASE_ITEM_SUFFIX, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
