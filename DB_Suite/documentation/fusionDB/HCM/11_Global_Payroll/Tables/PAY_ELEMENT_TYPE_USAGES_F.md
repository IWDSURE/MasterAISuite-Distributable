# PAY_ELEMENT_TYPE_USAGES_F

Used to identify how  the Element is used with the Run Type

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelementtypeusagesf-5562.html#payelementtypeusagesf-5562](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelementtypeusagesf-5562.html#payelementtypeusagesf-5562)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELEMENT_TYPE_USAGES_PK | ELEMENT_TYPE_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELEMENT_TYPE_USAGE_ID | NUMBER |  | 18 | Yes | Primary Surrogate Key ELEMENT_TYPE_USAGE_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| RUN_TYPE_ID | NUMBER |  | 18 | Yes | Used to identify the Run Type being refered to RUN_TYPE_ID |
| ELEMENT_TYPE_ID | NUMBER |  | 18 | Yes | Used to identify the Element that is being refered to ELEMENT_TYPE_ID |
| USAGE_TYPE | VARCHAR2 | 30 |  | Yes | Used to identify the type of row in this table USAGE_TYPE |
| INCLUSION_FLAG | VARCHAR2 | 20 |  |  | Used to work out id the Element is included INCLUSION_FLAG |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ELEMENT_TYPE_USAGES_PK | Unique | Default | ELEMENT_TYPE_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_ELEMENT_TYPE_USAGES_PK1 | Unique | Default | ELEMENT_TYPE_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |
| PAY_ELE_TYPE_USAGES_F_N1 | Non Unique | Default | ELEMENT_TYPE_ID |
| PAY_ELE_TYPE_USAGES_F_N2 | Non Unique | Default | RUN_TYPE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
