# HRC_DL_ALL_PARAMETERS

The HRC DL LOADER PARAMETER table is used for defining and storing configuration parameters for the ESS processing of DataLoader Jobs.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlallparameters-20583.html#hrcdlallparameters-20583](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlallparameters-20583.html#hrcdlallparameters-20583)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_ALL_PARAMETERS_PK | PARAMETER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARAMETER_ID | NUMBER |  | 18 | Yes | PARAMETER_ID |
| PARAM_NAME | VARCHAR2 | 30 |  | Yes | PARAM_NAME |
| PARAM_CATEGORY | VARCHAR2 | 30 |  | Yes | PARAM_CATEGORY |
| PARAM_SET_TYPE | VARCHAR2 | 30 |  |  | PARAM_SET_TYPE |
| DEFAULT_VALUE | VARCHAR2 | 240 |  |  | DEFAULT_VALUE |
| HSDL_DEFAULT_VALUE | VARCHAR2 | 240 |  |  | HSDL_DEFAULT_VALUE |
| HDL_ENABLED | VARCHAR2 | 1 |  | Yes | HDL_ENABLED |
| HDL_OVERRIDE_ENABLED | VARCHAR2 | 1 |  | Yes | HDL_OVERRIDE_ENABLED |
| HSDL_ENABLED | VARCHAR2 | 1 |  | Yes | HSDL_ENABLED |
| HSDL_OVERRIDE_ENABLED | VARCHAR2 | 1 |  | Yes | HSDL_OVERRIDE_ENABLED |
| HSDL_TEMPLATE_ENABLED | VARCHAR2 | 1 |  | Yes | HSDL_TEMPLATE_ENABLED |
| VALUE_DATA_TYPE | VARCHAR2 | 1 |  | Yes | VALUE_DATA_TYPE |
| VALUE_MINIMUM | NUMBER |  | 9 |  | VALUE_MINIMUM |
| VALUE_MAXIMUM | NUMBER |  | 9 |  | VALUE_MAXIMUM |
| VALUE_SUGGESTED_MAX | NUMBER |  | 9 |  | VALUE_SUGGESTED_MAX |
| VALUE_MAX_LENGTH | NUMBER |  | 9 |  | VALUE_MAX_LENGTH |
| VALUE_LOOKUP_TYPE | VARCHAR2 | 30 |  |  | VALUE_LOOKUP_TYPE |
| SET_COMMAND | VARCHAR2 | 240 |  |  | SET_COMMAND |
| BUS_OBJ_TOP_DISCRIMINATOR | VARCHAR2 | 100 |  |  | BUS_OBJ_TOP_DISCRIMINATOR |
| DISPLAY_CONDITION | VARCHAR2 | 1000 |  |  | DISPLAY_CONDITION |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| RETENTION_METHOD | VARCHAR2 | 20 |  |  | Column which indiates the retention method for the parameter. Based on this value parameter values will be maintained in the summary table for each data set business object. |
| ORIGINATING_PROCESS | VARCHAR2 | 30 |  |  | Column which indicates the phase of the data loader during which this parameter is useful. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_ALL_PARAMETERS_U1 | Unique | Default | PARAMETER_ID, ORA_SEED_SET1 |
| HRC_DL_ALL_PARAMETERS_U11 | Unique | Default | PARAMETER_ID, ORA_SEED_SET2 |
| HRC_DL_ALL_PARAMETERS_U2 | Unique | Default | ENTERPRISE_ID, PARAM_NAME, ORA_SEED_SET1 |
| HRC_DL_ALL_PARAMETERS_U21 | Unique | Default | ENTERPRISE_ID, PARAM_NAME, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
