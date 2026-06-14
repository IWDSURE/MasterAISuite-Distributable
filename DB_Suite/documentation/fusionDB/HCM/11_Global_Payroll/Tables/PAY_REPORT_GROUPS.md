# PAY_REPORT_GROUPS

Used to identify a Group of report definitions and categories that are related.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payreportgroups-21187.html#payreportgroups-21187](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payreportgroups-21187.html#payreportgroups-21187)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REPORT_GROUPS_PK | REPORT_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REPORT_GROUP_ID | NUMBER |  | 18 | Yes | REPORT_GROUP_ID |
| REPORT_FORMAT_MAPPING_ID | NUMBER |  | 18 |  | REPORT_FORMAT_MAPPING_ID |
| REPORT_GROUP_NAME | VARCHAR2 | 80 |  | Yes | REPORT_GROUP_NAME |
| SHORT_NAME | VARCHAR2 | 30 |  | Yes | SHORT_NAME |
| REL_REPORT_BLOCK_ID | NUMBER |  | 18 |  | REL_REPORT_BLOCK_ID |
| EXT_DEFINITION_ID | NUMBER |  | 18 |  | EXT_DEFINITION_ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_REPORT_GROUPS_PK | Unique | Default | REPORT_GROUP_ID, ORA_SEED_SET1 |
| PAY_REPORT_GROUPS_PK1 | Unique | Default | REPORT_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
