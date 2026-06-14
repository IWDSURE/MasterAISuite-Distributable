# HEX_PARAM_FEATURE_OVERRIDE_VAL

The table stores the details of override values of parameters and features.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexparamfeatureoverrideval-13330.html#hexparamfeatureoverrideval-13330](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexparamfeatureoverrideval-13330.html#hexparamfeatureoverrideval-13330)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_OVERRIDE_VAL_PK | PARAM_FEATURE_OVERRIDE_VAL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARAM_FEATURE_OVERRIDE_VAL_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| CONFIGURATION_GROUP_ID | NUMBER |  | 18 | Yes | This column contains the configuration group id as the foreign key. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| BASE_PARAM_FEATURE_CODE | VARCHAR2 | 80 |  |  | The column indicates the code for the feature/parameter. |
| PARAM_FEATURE_OVERRIDE_VALUE | VARCHAR2 | 2000 |  |  | The column indicates the value for the feature/parameter. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HEX_OVERRIDE_VAL_N1 | Non Unique | FUSION_TS_SEED | CONFIGURATION_GROUP_ID, BASE_PARAM_FEATURE_CODE |
| HEX_OVERRIDE_VAL_PK | Unique | FUSION_TS_SEED | PARAM_FEATURE_OVERRIDE_VAL_ID |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
