# PAY_GI_MAPPING_USAGES

This table contains the general interface mapping usage information.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygimappingusages-25237.html#paygimappingusages-25237](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygimappingusages-25237.html#paygimappingusages-25237)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_GI_MAPPING_USAGES_PK | MAPPING_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MAPPING_USAGE_ID | NUMBER |  | 18 | Yes | MAPPING_USAGE_ID |
| MAPPING_ID | NUMBER |  | 18 |  | MAPPING_ID |
| INTERFACE_TYPE_ID | NUMBER |  | 18 |  | INTERFACE_TYPE_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_GI_MAPPING_USAGES_N1 | Non Unique | Default | MAPPING_ID |
| PAY_GI_MAPPING_USAGES_N2 | Non Unique | Default | INTERFACE_TYPE_ID |
| PAY_GI_MAPPING_USAGES_PK | Unique | Default | MAPPING_USAGE_ID, ORA_SEED_SET1 |
| PAY_GI_MAPPING_USAGES_PK1 | Unique | Default | MAPPING_USAGE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
