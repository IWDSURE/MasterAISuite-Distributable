# FAI_MODEL_CONFIG_PARAMS

This table stores model configuration parameters for generative AI.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faimodelconfigparams-15229.html#faimodelconfigparams-15229](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faimodelconfigparams-15229.html#faimodelconfigparams-15229)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_MODEL_CONFIG_PARAMS_PK | MDL_CONFIG_PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MDL_CONFIG_PARAM_ID | NUMBER |  | 18 | Yes | The unique Identifier of model configuration parameters. |
| MDL_PARAM_CODE | VARCHAR2 | 80 |  |  | This column stores the parameter code. |
| MDL_PARAM_TYPE | VARCHAR2 | 32 |  |  | This column stores the parameter type. |
| MODEL_CONFIG_ID | NUMBER |  | 18 |  | Model configuration this parameter belongs to. Foreign key to FAI_MODEL_CONFIG. |
| NUMBER_VALUE | NUMBER |  | 14 |  | This column stores the value for numeric parameter. |
| VARCHAR2_VALUE | VARCHAR2 | 4000 |  |  | This column stores the value for string parameter. |
| TIMESTAMP_VALUE | TIMESTAMP |  |  |  | This column stores the value for timestamp parameter. |
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
| FAI_MODEL_CONFIG_PARAMS_PK | Unique | Default | MDL_CONFIG_PARAM_ID, ORA_SEED_SET1 |
| FAI_MODEL_CONFIG_PARAMS_PK1 | Unique | Default | MDL_CONFIG_PARAM_ID, ORA_SEED_SET2 |
| FAI_MODEL_CONFIG_PARAMS_U1 | Unique | Default | MODEL_CONFIG_ID, MDL_PARAM_CODE, ORA_SEED_SET1 |
| FAI_MODEL_CONFIG_PARAMS_U11 | Unique | Default | MODEL_CONFIG_ID, MDL_PARAM_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
