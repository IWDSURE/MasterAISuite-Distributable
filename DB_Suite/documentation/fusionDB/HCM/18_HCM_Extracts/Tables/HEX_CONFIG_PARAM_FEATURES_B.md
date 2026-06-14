# HEX_CONFIG_PARAM_FEATURES_B

The base table stores the details of the features/parameters used in the extract configuration groups.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexconfigparamfeaturesb-23522.html#hexconfigparamfeaturesb-23522](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexconfigparamfeaturesb-23522.html#hexconfigparamfeaturesb-23522)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_CONFIG_PARAM_FEATURE_B_PK | PARAM_FEATURE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARAM_FEATURE_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| MAX_VALUE | NUMBER |  | 18 |  | This column contains the Maximum Value of the Feature/Parameter |
| PARAM_FEATURE_RECOMMENDED_VAL | VARCHAR2 | 2000 |  |  | This column contains the recommended value for parameters and features |
| MIN_VALUE | NUMBER |  | 18 |  | This column contains the Minimum Value of the feature/Parameter |
| BASE_PARAM_FEATURE_CODE | VARCHAR2 | 80 |  |  | The column indicates the name for the feature/parameter. Used for migrating the seed data and for storing the custom code. |
| PARAM_FEATURE_DEFAULT_VALUE | VARCHAR2 | 2000 |  |  | The column indicates the value for the feature/parameter. |
| PARAM_FEATURE_TYPE | VARCHAR2 | 10 |  |  | The column indicates the type. Valid values are FEATURE, PARAMETER. |
| LEGACY_PARAM_FEATURE_CODE | VARCHAR2 | 80 |  |  | The column indicates the reference lookup code for deriving the value for the specific feature/parameter. |
| LEGACY_COMPATIBLE | VARCHAR2 | 10 |  |  | The column indicates the parameter compatibility with the values LEGACY/NEW/BOTH. |
| MANDATORY_FLAG | VARCHAR2 | 1 |  |  | The column indicates if the parameter/feature is mandatory. Valid values are Y and N. |
| ENABLED_FLAG | VARCHAR2 | 15 |  |  | ENABLED/HIDE/DEPRECATED/DISABLED (Default :ENABLED) |
| PARAM_FEAT_LOOKUP_TYPE | VARCHAR2 | 30 |  |  | The column indicates the lookup associated with the parameter/feature. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HEX_CONFIG_PARAM_FEATURE_B_N1 | Non Unique | Default | BASE_PARAM_FEATURE_CODE |
| HEX_CONFIG_PARAM_FEATURE_B_PK | Unique | Default | PARAM_FEATURE_ID, ORA_SEED_SET1 |
| HEX_CONFIG_PARAM_FEATURE_B_PK1 | Unique | Default | PARAM_FEATURE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
