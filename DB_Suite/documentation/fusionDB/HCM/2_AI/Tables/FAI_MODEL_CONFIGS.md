# FAI_MODEL_CONFIGS

This table stores model configurations for generative AI.	.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faimodelconfigs-23806.html#faimodelconfigs-23806](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faimodelconfigs-23806.html#faimodelconfigs-23806)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_MODEL_CONFIGS_PK | MODEL_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MODEL_CONFIG_ID | NUMBER |  | 18 | Yes | The unique Identifier of model configuration. |
| MODEL_CONFIGURATION_CODE | VARCHAR2 | 200 |  | Yes | Alternate Key: Uniquely identifies Model configurations. |
| INTERNAL_NAME | VARCHAR2 | 200 |  |  | This column represents the system name of the Model configuration. |
| INTERNAL_DESCRIPTION | VARCHAR2 | 2000 |  |  | This column represents the system description of the Model configuration. |
| MODEL | VARCHAR2 | 255 |  |  | This column stores the Model identification. |
| VERSION | VARCHAR2 | 80 |  |  | This column stores the Model version. |
| PROVIDER | VARCHAR2 | 80 |  |  | This column stores the Model provider. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_MODEL_CONFIGS_PK | Unique | Default | MODEL_CONFIG_ID, ORA_SEED_SET1 |
| FAI_MODEL_CONFIGS_PK1 | Unique | Default | MODEL_CONFIG_ID, ORA_SEED_SET2 |
| FAI_MODEL_CONFIGS_U1 | Unique | Default | MODEL_CONFIGURATION_CODE, ORA_SEED_SET1 |
| FAI_MODEL_CONFIGS_U11 | Unique | Default | MODEL_CONFIGURATION_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
