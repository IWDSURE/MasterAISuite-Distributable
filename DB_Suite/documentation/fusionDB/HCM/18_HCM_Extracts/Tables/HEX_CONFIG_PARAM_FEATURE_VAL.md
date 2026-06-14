# HEX_CONFIG_PARAM_FEATURE_VAL

The table stores the values for the features/parameters used in the extract configuration groups.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexconfigparamfeatureval-8904.html#hexconfigparamfeatureval-8904](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexconfigparamfeatureval-8904.html#hexconfigparamfeatureval-8904)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_CONFIG_PARAM_FEAT_VAL_PK | PARAM_FEATURE_VALUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARAM_FEATURE_VALUE_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| BASE_PARAM_FEATURE_CODE | VARCHAR2 | 80 |  | Yes | The column indicates the name of the feature/parameter used in the current configuration group. |
| PARAM_FEATURE_VALUE | VARCHAR2 | 2000 |  | Yes | The column indicates the default/overridden value of the feature/parameter used in the current configuration group. |
| CONFIGURATION_GROUP_ID | NUMBER |  | 18 | Yes | The column is a reference to the hex_configuration_groups_b to point to the configuration group. |
| PROCESS_SYNC_FLAG | VARCHAR2 | 1 |  |  | The column indicates if the parameter/feature is synched with process data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HEX_CONFIG_PARAM_FEAT_VAL_N1 | Non Unique | Default | CONFIGURATION_GROUP_ID, BASE_PARAM_FEATURE_CODE |
| HEX_CONFIG_PARAM_FEAT_VAL_PK | Unique | Default | PARAM_FEATURE_VALUE_ID, ORA_SEED_SET1 |
| HEX_CONFIG_PARAM_FEAT_VAL_PK1 | Unique | Default | PARAM_FEATURE_VALUE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
