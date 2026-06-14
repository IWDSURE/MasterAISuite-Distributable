# PAY_REPORT_BLOCKS

BLock description of extract blocks.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payreportblocks-26865.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payreportblocks-26865.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REPORT_BLOCKS_PK | REPORT_BLOCK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REPORT_BLOCK_ID | NUMBER |  | 18 | Yes | REPORT_BLOCK_ID |
| BASE_BLOCK_NAME | VARCHAR2 | 80 |  | Yes | BASE_BLOCK_NAME |
| MAIN_BLOCK_FLAG | VARCHAR2 | 30 |  |  | MAIN_BLOCK_FLAG |
| REPORT_FORMAT | VARCHAR2 | 20 |  |  | REPORT_FORMAT |
| CURSOR_NAME | VARCHAR2 | 80 |  |  | CURSOR_NAME |
| NO_COLUMN_RETURNED | NUMBER |  | 5 |  | NO_COLUMN_RETURNED |
| USER_ENTITY_ID | NUMBER |  | 18 |  | USER_ENTITY_ID |
| EXT_DEFINITION_ID | NUMBER |  | 18 |  | EXT_DEFINITION_ID |
| MULTI_THREAD_ACT_TYPE | VARCHAR2 | 5 |  |  | MULTI_THREAD_ACT_TYPE |
| MULTI_DBI_ID | NUMBER |  | 18 |  | MULTI_DBI_ID |
| INTERLOCK_DBI_ID | NUMBER |  | 18 |  | INTERLOCK_DBI_ID |
| XML_TAG_NAME | VARCHAR2 | 80 |  |  | XML_TAG_NAME |
| REQUIRED_FLAG | VARCHAR2 | 1 |  |  | REQUIRED_FLAG |
| TEMPLATE_BLOCK_ID | NUMBER |  | 18 |  | foreign Key to pay_report_blocks |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| CREATOR_TYPE | VARCHAR2 | 30 |  |  | Creator type for generated template blocks |
| CREATOR_ID | NUMBER |  | 18 |  | Creator ID for generated template blocks |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_REPORT_BLOCKS_N1 | Non Unique | Default | EXT_DEFINITION_ID, BASE_BLOCK_NAME |
| PAY_REPORT_BLOCKS_N2 | Non Unique | Default | TEMPLATE_BLOCK_ID |
| PAY_REPORT_BLOCKS_N20 | Non Unique | Default | SGUID |
| PAY_REPORT_BLOCKS_N3 | Non Unique | Default | CREATOR_ID, CREATOR_TYPE |
| PAY_REPORT_BLOCKS_PK | Unique | Default | REPORT_BLOCK_ID, ORA_SEED_SET1 |
| PAY_REPORT_BLOCKS_PK1 | Unique | Default | REPORT_BLOCK_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
