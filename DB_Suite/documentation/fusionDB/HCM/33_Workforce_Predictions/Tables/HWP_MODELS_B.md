# HWP_MODELS_B

This table contains models used for data mining for predictives.

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpmodelsb-5829.html#hwpmodelsb-5829](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpmodelsb-5829.html#hwpmodelsb-5829)

## Primary Key

| Name | Columns |
|------|----------|
| HWP_MODELS_B_PK | MODEL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| MODEL_ID | NUMBER |  | 18 | Yes | Predictive Data mining model ID. |
| MODEL_CODE | VARCHAR2 | 200 |  |  | Data mining model code. |
| MINING_FUNCTION | VARCHAR2 | 200 |  |  | Data mining mining function. |
| TABLE_NAME | VARCHAR2 | 200 |  |  | Data mining table name. |
| CASE_ID_COLUMN | VARCHAR2 | 200 |  |  | Data mining case ID column. |
| TARGET_ID_COLUMN | VARCHAR2 | 200 |  |  | Data mining Target ID column. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CORRECTION_VALUE | NUMBER |  | 6 |  | Correction value used as multiplier for showing mining results. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWP_MODELS_B_N20 | Non Unique | Default | SGUID |  |
| HWP_MODELS_B_PK | Unique | Default | MODEL_ID, ORA_SEED_SET1 |  |
| HWP_MODELS_B_PK1 | Unique | Default | MODEL_ID, ORA_SEED_SET2 |  |
| HWP_MODELS_B_U1 | Unique | Default | MODEL_CODE | Obsolete |

---

[← Back to Index](../33_Workforce_Predictions_Tables_Index.md)
