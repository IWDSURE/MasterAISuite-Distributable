# HRY_PI_CONFIG_PROPERTIES

Stores additional configuration option values of extract definitions for GPI Configurator.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypiconfigproperties-4239.html#hrypiconfigproperties-4239](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypiconfigproperties-4239.html#hrypiconfigproperties-4239)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_PI_CONFIG_PROPERTIES_PK | CONFIG_PROPERTY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIG_PROPERTY_ID | NUMBER |  | 18 | Yes | Primary Key for GPI Configurator Property |
| EXT_DEFINITION_ID | NUMBER |  | 18 | Yes | Foreign key to PER_EXT_DEFINITIONS_B. |
| REPORT_BLOCK_ID | NUMBER |  | 18 |  | Foreign key to PAY_REPORT_BLOCKS. |
| REPORT_RECORD_ID | NUMBER |  | 18 |  | Foreign key to PAY_REPORT_RECORDS_F. |
| EXT_DATA_ELEMENT_ID | NUMBER |  | 18 |  | Foreign key to PER_EXT_DATA_ELEMENTS_B. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES_B. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| PROPERTY_NAME | VARCHAR2 | 30 |  | Yes | Property Name |
| PROPERTY_VALUE | VARCHAR2 | 4000 |  | Yes | Property Value |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | SGUID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_PI_CONFIG_PROPERTIES_N20 | Non Unique | Default | SGUID |
| HRY_PI_CONFIG_PROPERTIES_PK | Unique | Default | CONFIG_PROPERTY_ID, ORA_SEED_SET1 |
| HRY_PI_CONFIG_PROPERTIES_PK1 | Unique | Default | CONFIG_PROPERTY_ID, ORA_SEED_SET2 |
| HRY_PI_CONFIG_PROPERTIES_U1 | Unique | Default | EXT_DEFINITION_ID, REPORT_BLOCK_ID, REPORT_RECORD_ID, EXT_DATA_ELEMENT_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, PROPERTY_NAME, ORA_SEED_SET1 |
| HRY_PI_CONFIG_PROPERTIES_U11 | Unique | Default | EXT_DEFINITION_ID, REPORT_BLOCK_ID, REPORT_RECORD_ID, EXT_DATA_ELEMENT_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, PROPERTY_NAME, ORA_SEED_SET2 |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
