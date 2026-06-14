# PAY_FLOW_TASK_PARAMETERS

This Table captures the parameters to execute the flow task parameters

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowtaskparameters-3023.html#payflowtaskparameters-3023](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowtaskparameters-3023.html#payflowtaskparameters-3023)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_FLOW_TASK_PARAMETERS_PK | FLOW_TASK_PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FLOW_TASK_PARAM_ID | NUMBER |  | 18 | Yes | FLOW_TASK_PARAM_ID |
| BASE_PARAMETER_NAME | VARCHAR2 | 100 |  | Yes | BASE_PARAMETER_NAME |
| BASE_FLOW_TASK_PARAM_ID | NUMBER |  | 18 | Yes | BASE_FLOW_TASK_PARAM_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BASE_FLOW_TASK_ID | NUMBER |  | 18 | Yes | BASE_FLOW_TASK_ID |
| BASE_TASK_PARAMETER_ID | NUMBER |  | 18 |  | BASE_TASK_PARAMETER_ID |
| BASE_FLOW_PARAMETER_ID | NUMBER |  | 18 |  | BASE_FLOW_PARAMETER_ID |
| DISPLAY_FLAG | VARCHAR2 | 1 |  | Yes | DISPLAY_FLAG |
| PARAM_DISP_TYPE | VARCHAR2 | 30 |  |  | PARAM_DISP_TYPE |
| PARAM_USAGE_TYPE | VARCHAR2 | 30 |  |  | PARAM_USAGE_TYPE |
| PARAM_VALUE_SET | VARCHAR2 | 200 |  |  | PARAM_VALUE_SET |
| PARAM_LOOKUP | VARCHAR2 | 200 |  |  | PARAM_LOOKUP |
| PARAM_SEQUENCE | NUMBER |  | 18 |  | PARAM_SEQUENCE |
| DEFAULT_TYPE | VARCHAR2 | 30 |  |  | DEFAULT_TYPE |
| DEFAULT_VAL | VARCHAR2 | 2000 |  |  | DEFAULT_VAL |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_FLOW_TASK_PARAMETERS_N1 | Non Unique | Default | BASE_FLOW_TASK_PARAM_ID, BASE_TASK_PARAMETER_ID |
| PAY_FLOW_TASK_PARAMETERS_N20 | Non Unique | Default | SGUID |
| PAY_FLOW_TASK_PARAMETERS_PK | Unique | Default | FLOW_TASK_PARAM_ID, ORA_SEED_SET1 |
| PAY_FLOW_TASK_PARAMETERS_PK1 | Unique | Default | FLOW_TASK_PARAM_ID, ORA_SEED_SET2 |
| PAY_FLOW_TASK_PARAMETERS_U1 | Unique | Default | BASE_PARAMETER_NAME, BASE_FLOW_TASK_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_FLOW_TASK_PARAMETERS_U11 | Unique | Default | BASE_PARAMETER_NAME, BASE_FLOW_TASK_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
