# HWP_MODEL_ATTRIBUTE_MAPPING

Attribute or Indicators mapping with Model

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpmodelattributemapping-30727.html#hwpmodelattributemapping-30727](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpmodelattributemapping-30727.html#hwpmodelattributemapping-30727)

## Primary Key

| Name | Columns |
|------|----------|
| HWP_MODEL_ATTR_MAPPING_PK | MODEL_ATTR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MODEL_ATTR_ID | NUMBER |  | 18 | Yes | Model Attribute Mapping ID. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| MODEL_ID | NUMBER |  | 18 | Yes | Data Mining model ID. |
| ATTRIBUTE_ID | NUMBER |  | 18 | Yes | Data Mining attribute ID. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWP_MODEL_ATTR_MAPPING_FK1 | Non Unique | Default | MODEL_ID |
| HWP_MODEL_ATTR_MAPPING_FK2 | Non Unique | Default | ATTRIBUTE_ID |
| HWP_MODEL_ATTR_MAPPING_PK | Unique | Default | MODEL_ATTR_ID, ORA_SEED_SET1 |
| HWP_MODEL_ATTR_MAPPING_PK1 | Unique | Default | MODEL_ATTR_ID, ORA_SEED_SET2 |

---

[← Back to Index](../33_Workforce_Predictions_Tables_Index.md)
