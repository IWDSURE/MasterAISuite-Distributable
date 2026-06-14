# PAY_REPORT_FORMAT_MAPS_F

Table for Report Format Mappings

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payreportformatmapsf-15922.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payreportformatmapsf-15922.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REPORT_FORMAT_MAPS_PK | REPORT_TYPE, REPORT_QUALIFIER, REPORT_CATEGORY, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REPORT_FORMAT_MAPPING_ID | NUMBER |  | 18 | Yes | REPORT_FORMAT_MAPPING_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| REPORT_TYPE | VARCHAR2 | 30 |  | Yes | REPORT_TYPE |
| REPORT_QUALIFIER | VARCHAR2 | 30 |  | Yes | REPORT_QUALIFIER |
| REPORT_CATEGORY | VARCHAR2 | 30 |  | Yes | REPORT_CATEGORY |
| JAVA_CODE | VARCHAR2 | 250 |  |  | JAVA_CODE |
| TEMPORARY_ACTION_FLAG | VARCHAR2 | 1 |  |  | TEMPORARY_ACTION_FLAG |
| UPDATABLE_FLAG | VARCHAR2 | 1 |  |  | UPDATABLE_FLAG |
| RANGE_CODE | VARCHAR2 | 60 |  |  | RANGE_CODE |
| ASSIGNMENT_ACTION_CODE | VARCHAR2 | 60 |  |  | ASSIGNMENT_ACTION_CODE |
| RERUN_MODE | VARCHAR2 | 5 |  |  | RERUN_MODE |
| RETRY_MODE | VARCHAR2 | 5 |  |  | RETRY_MODE |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_REPORT_FORMAT_MAPS_F_N1 | Non Unique | Default | REPORT_FORMAT_MAPPING_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_REPORT_FORMAT_MAPS_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_REPORT_FORMAT_MAPS_PK | Unique | Default | REPORT_TYPE, REPORT_QUALIFIER, REPORT_CATEGORY, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_REPORT_FORMAT_MAPS_PK1 | Unique | Default | REPORT_TYPE, REPORT_QUALIFIER, REPORT_CATEGORY, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
