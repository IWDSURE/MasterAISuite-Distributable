# HRC_LOADER_PARAMETERS

The table is used for defining configuration parameters for the ESS processing of HR2HR ESS Jobs.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloaderparameters-6465.html#hrcloaderparameters-6465](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloaderparameters-6465.html#hrcloaderparameters-6465)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_LOADER_PARAMETERS_PK | PARAMETER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PARAMETER_ID | NUMBER |  | 18 | Yes | Surrogate Primary key populated by sequence |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| PARAM_NAME | VARCHAR2 | 30 |  | Yes | The internal Parameter Name (e.g. ODI_CONTEXT). The parameter display name is derived from the corresponding LOOKUP where LOOKUP_TYPE='HRC_LOADER_PARAMETERS' |  |
| PARAM_VALUE | VARCHAR2 | 400 |  |  | The parameter value. This value is validated by taking into account the PARAM_REQUIRED and PARAM_DATATYPE columns. |  |
| PARAM_REQUIRED | VARCHAR2 | 30 |  | Yes | Defines if the parameter is required (i.e can not be null ) and has value of Y or N. Default value is Y |  |
| PARAM_DATATYPE | VARCHAR2 | 30 |  | Yes | Defines the data type for the parameter. The only values supported are; S(String and I(Integer) |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_LOADER_PARAMETERS_PK | Unique | Default | PARAMETER_ID |
| HRC_LOADER_PARAMETERS_U1 | Unique | Default | ENTERPRISE_ID, PARAM_NAME |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
