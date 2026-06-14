# HEX_CONFIG_PARAM_FEATURES_TL

The transactional table stores the details of the features/parameters used in the extract configuration groups.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexconfigparamfeaturestl-23962.html#hexconfigparamfeaturestl-23962](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexconfigparamfeaturestl-23962.html#hexconfigparamfeaturestl-23962)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_CONFIG_PARAM_FEAT_TL_PK | PARAM_FEATURE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARAM_FEATURE_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| PARAM_FEATURE_NAME | VARCHAR2 | 240 |  | Yes | The column indicates the name for the feature/parameter. |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | The column indicates the purpose of the parameter/feature. |
| DESCRIPTION_DTLS | VARCHAR2 | 4000 |  |  | The column indicates the detailed purpose of the parameter/feature. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HEX_CONFIG_PARAM_FEAT_TL_N1 | Non Unique | Default | PARAM_FEATURE_NAME, LANGUAGE |
| HEX_CONFIG_PARAM_FEAT_TL_PK | Unique | Default | PARAM_FEATURE_ID, LANGUAGE, ORA_SEED_SET1 |
| HEX_CONFIG_PARAM_FEAT_TL_PK1 | Unique | Default | PARAM_FEATURE_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
