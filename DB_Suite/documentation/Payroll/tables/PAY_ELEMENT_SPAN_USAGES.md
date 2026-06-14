# PAY_ELEMENT_SPAN_USAGES

This table contains information to determine which retropay element to use depending on the age of the retrospective change. For example, if a correction is processed from the previous tax year, there may be legislative rules concerning different taxation that needs to be applied.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelementspanusages-30969.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelementspanusages-30969.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELEMENT_SPAN_USAGES_PK | ELEMENT_SPAN_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELEMENT_SPAN_USAGE_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| RETRO_COMPONENT_USAGE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_RETRO_COMPONENT_USAGES |
| TIME_SPAN_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_TIME_SPANS |
| RETRO_ELEMENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_ELEMENT_TYPES_F |
| ADJUSTMENT_TYPE | VARCHAR2 | 30 |  |  | Type of adjustment (Credit, Debit) |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign Key to FND_TERRITORIES |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ELEMENT_SPAN_USAGES_N1 | Non Unique | Default | RETRO_ELEMENT_TYPE_ID |
| PAY_ELEMENT_SPAN_USAGES_N20 | Non Unique | Default | SGUID |
| PAY_ELEMENT_SPAN_USAGES_PK | Unique | Default | ELEMENT_SPAN_USAGE_ID, ORA_SEED_SET1 |
| PAY_ELEMENT_SPAN_USAGES_PK1 | Unique | Default | ELEMENT_SPAN_USAGE_ID, ORA_SEED_SET2 |
| PAY_ELEMENT_SPAN_USAGES_U1 | Unique | Default | RETRO_COMPONENT_USAGE_ID, TIME_SPAN_ID, ADJUSTMENT_TYPE, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_ELEMENT_SPAN_USAGES_U11 | Unique | Default | RETRO_COMPONENT_USAGE_ID, TIME_SPAN_ID, ADJUSTMENT_TYPE, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |
| PAY_ELEMENT_SPAN_USAGES_U2 | Unique | Default | RETRO_COMPONENT_USAGE_ID, TIME_SPAN_ID, ADJUSTMENT_TYPE, ORA_SEED_SET1 |
| PAY_ELEMENT_SPAN_USAGES_U21 | Unique | Default | RETRO_COMPONENT_USAGE_ID, TIME_SPAN_ID, ADJUSTMENT_TYPE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
