# HRY_SETUP_CONFIG_PROP_DTLS

All the Detailed properties of all the base properties.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrysetupconfigpropdtls-4766.html#hrysetupconfigpropdtls-4766](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrysetupconfigpropdtls-4766.html#hrysetupconfigpropdtls-4766)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_SETUP_CNFG_PROP_DTL_PK | PROPERTY_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROPERTY_ID | NUMBER |  | 18 |  | Foreign key to the table hry_setup_config_properties |
| BASE_PROPERTY_DETAILS_NAME | VARCHAR2 | 256 |  |  | Name of the Base Property Detail |
| PROPERTY_DETAIL_VALUE | VARCHAR2 | 256 |  |  | It represents Value of the Property |
| EDITABLE | VARCHAR2 | 8 |  |  | It represents property is editable or not |
| ENABLE | VARCHAR2 | 8 |  |  | It represents property will be visible in UI or not |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PROPERTY_DETAIL_ID | NUMBER |  | 18 | Yes | Primary key to the table hry_pi_configuration_details |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | It represents SGUID which is unique identifier |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_SETUP_CNFG_PROP_DTL_N20 | Non Unique | Default | SGUID |
| HRY_SETUP_CNFG_PROP_DTL_PK1 | Unique | Default | PROPERTY_DETAIL_ID, ORA_SEED_SET1 |
| HRY_SETUP_CNFG_PROP_DTL_PK11 | Unique | Default | PROPERTY_DETAIL_ID, ORA_SEED_SET2 |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
