# HRC_DL_LAYOUT_PARAMS

Table to store template parameters for ESS and HDL process.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdllayoutparams-13202.html#hrcdllayoutparams-13202](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdllayoutparams-13202.html#hrcdllayoutparams-13202)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_LAYOUT_PARAMS_PK | LAYOUT_PARAM_ID, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LAYOUT_PARAM_ID | NUMBER |  | 18 | Yes | LAYOUT_PARAM_ID |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| LAYOUT_ID | NUMBER |  | 18 | Yes | LAYOUT_ID |
| PARAM_NAME | VARCHAR2 | 240 |  | Yes | PARAM_NAME |
| PARAM_VALUE | VARCHAR2 | 400 |  |  | PARAM_VALUE |
| PARAM_MANDATORY | VARCHAR2 | 30 |  | Yes | PARAM_MANDATORY |
| PARAM_TYPE | VARCHAR2 | 30 |  | Yes | PARAM_TYPE |
| PARAM_DATA_TYPE | VARCHAR2 | 30 |  |  | PARAM_DATA_TYPE |
| PARAMETER_ID | NUMBER |  | 18 |  | PARAMETER_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_LAYOUT_PARAMS_N1 | Non Unique | Default | LAYOUT_ID |
| HRC_DL_LAYOUT_PARAMS_N20 | Non Unique | Default | SGUID |
| HRC_DL_LAYOUT_PARAMS_U1 | Unique | Default | LAYOUT_PARAM_ID, ORA_SEED_SET1 |
| HRC_DL_LAYOUT_PARAMS_U11 | Unique | Default | LAYOUT_PARAM_ID, ORA_SEED_SET2 |
| HRC_DL_LAYOUT_PARAMS_U2 | Unique | Default | LAYOUT_PARAM_ID, ENTERPRISE_ID, ORA_SEED_SET1 |
| HRC_DL_LAYOUT_PARAMS_U21 | Unique | Default | LAYOUT_PARAM_ID, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
