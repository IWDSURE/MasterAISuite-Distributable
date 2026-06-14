# HRC_DL_PARAMETERS

The HRC DL LOADER PARAMETER table is used for defining and storing configuration parameters for the ESS processing of DataLoader Jobs.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlparameters-15361.html#hrcdlparameters-15361](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlparameters-15361.html#hrcdlparameters-15361)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_PARAMETERS_PK | PARAMETER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PARAMETER_ID | NUMBER |  | 18 | Yes | PARAMETER_ID |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |  |
| PARAM_NAME | VARCHAR2 | 30 |  | Yes | PARAM_NAME |  |
| PARAM_VALUE | VARCHAR2 | 400 |  |  | PARAM_VALUE |  |
| PARAM_REQUIRED | VARCHAR2 | 30 |  | Yes | PARAM_REQUIRED |  |
| PARAM_DATATYPE | VARCHAR2 | 30 |  | Yes | PARAM_DATATYPE |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_PARAMETERS_U1 | Unique | Default | PARAMETER_ID |
| HRC_DL_PARAMETERS_U2 | Unique | Default | ENTERPRISE_ID, PARAM_NAME |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
