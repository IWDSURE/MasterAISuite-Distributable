# PAY_GI_MAPPINGS

This table contains the general interface mapping information.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygimappings-25569.html#paygimappings-25569](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygimappings-25569.html#paygimappings-25569)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_GI_MAPPINGS_PK | MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MAPPING_ID | NUMBER |  | 18 | Yes | COLUMN1 |
| PRIMARY_ENTITY_ID | NUMBER |  | 18 | Yes | PRIMARY_ENTITY_ID |
| SECONDARY_ENTITY_ID | NUMBER |  | 18 |  | SECONDARY_ENTITY_ID |
| TERTIARY_ID | NUMBER |  | 18 |  | TERTIARY_ID |
| ENTITY_TYPE | VARCHAR2 | 30 |  | Yes | ENTITY_TYPE |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_GI_MAPPINGS_PK | Unique | Default | MAPPING_ID, ORA_SEED_SET1 |
| PAY_GI_MAPPINGS_PK1 | Unique | Default | MAPPING_ID, ORA_SEED_SET2 |
| PAY_GI_MAPPINGS_U1 | Unique | Default | ENTITY_TYPE, PRIMARY_ENTITY_ID, SECONDARY_ENTITY_ID, TERTIARY_ID, ENTERPRISE_ID, ORA_SEED_SET1 |
| PAY_GI_MAPPINGS_U11 | Unique | Default | ENTITY_TYPE, PRIMARY_ENTITY_ID, SECONDARY_ENTITY_ID, TERTIARY_ID, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
