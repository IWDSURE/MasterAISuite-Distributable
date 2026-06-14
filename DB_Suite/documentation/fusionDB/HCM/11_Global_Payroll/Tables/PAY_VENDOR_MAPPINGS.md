# PAY_VENDOR_MAPPINGS

This table contains internal values mapped to values in third-party applications that the Payroll application directly interfaces with.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvendormappings-14583.html#payvendormappings-14583](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvendormappings-14583.html#payvendormappings-14583)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_VENDOR_MAPPINGS_PK | VENDOR_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VENDOR_MAPPING_ID | NUMBER |  | 18 | Yes | VENDOR_MAPPING_ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| MAPPING_TYPE | VARCHAR2 | 30 |  | Yes | MAPPING_TYPE |
| INTERNAL_NAME | VARCHAR2 | 30 |  | Yes | INTERNAL_NAME |
| INTERNAL_VALUE | NUMBER |  | 18 | Yes | INTERNAL_VALUE |
| VENDOR_VALUE | VARCHAR2 | 30 |  |  | VENDOR_VALUE |
| CONTEXT_VALUE1 | VARCHAR2 | 30 |  |  | CONTEXT_VALUE1 |
| CONTEXT_VALUE2 | VARCHAR2 | 30 |  |  | CONTEXT_VALUE2 |
| CONTEXT_VALUE3 | VARCHAR2 | 30 |  |  | CONTEXT_VALUE3 |
| CONTEXT_VALUE4 | VARCHAR2 | 30 |  |  | CONTEXT_VALUE4 |
| CONTEXT_VALUE5 | VARCHAR2 | 30 |  |  | CONTEXT_VALUE5 |
| CONTEXT_VALUE6 | VARCHAR2 | 60 |  |  | CONTEXT_VALUE6 |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_VENDOR_MAPPINGS_N1 | Non Unique | Default | MAPPING_TYPE, INTERNAL_NAME |
| PAY_VENDOR_MAPPINGS_N2 | Non Unique | Default | MAPPING_TYPE, INTERNAL_VALUE |
| PAY_VENDOR_MAPPINGS_N20 | Non Unique | Default | SGUID |
| PAY_VENDOR_MAPPINGS_PK | Unique | Default | VENDOR_MAPPING_ID, ORA_SEED_SET1 |
| PAY_VENDOR_MAPPINGS_PK1 | Unique | Default | VENDOR_MAPPING_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
