# PAY_TASK_PARAMETERS

pay_task_parameters captures the parameters  required to execute a task

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskparameters-20198.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskparameters-20198.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TASK_PARAMETERS_PK | TASK_PARAMETER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_PARAMETER_ID | NUMBER |  | 18 | Yes | This column is the primary key of the table pay_task_parameters. |
| BASE_CONTEXT_NAME | VARCHAR2 | 100 |  |  | This column contains the base context name value of the task parameter. |
| PARAMETER_CODE | VARCHAR2 | 20 |  |  | This column contains the parameter code value of the task parameter. |
| BASE_TASK_PARAMETER_NAME | VARCHAR2 | 100 |  | Yes | This column contains the base task parameter name value of the task parameter. |
| UI_EXPRESSION | CLOB |  |  |  | This column contains the ui expression value of the task parameter. |
| BASE_TASK_PARAMETER_ID | NUMBER |  | 18 | Yes | This column contains the base task parameter id value of the task parameter. |
| BASE_TASK_ACTION_ID | NUMBER |  | 18 | Yes | This column contains the base task action id value of the task parameter. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| PARENT_TASK_PARAM_ID | NUMBER |  | 18 |  | This column contains the parent task param id value of the task parameter. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| DISPLAY_FLAG | VARCHAR2 | 1 |  | Yes | This column contains the display flag value of the task parameter. |
| PARAM_DISP_TYPE | VARCHAR2 | 30 |  | Yes | This column contains the param display type value of the task parameter. |
| PARAM_USAGE_TYPE | VARCHAR2 | 30 |  | Yes | This column contains the param usage type value of the task parameter. |
| PARAM_SEQUENCE | NUMBER |  | 18 | Yes | This column contains the param sequence value of the task parameter. |
| PARAM_LOOKUP | VARCHAR2 | 200 |  |  | This column contains the param lookup value of the task parameter. |
| PARAM_VALUE_SET | VARCHAR2 | 200 |  |  | This column contains the param value set value of the task parameter. |
| PARAM_LEVEL | VARCHAR2 | 30 |  |  | This column contains the param level value of the task parameter. |
| DEFAULT_TYPE | VARCHAR2 | 30 |  |  | This column contains the default type value of the task parameter. |
| DEFAULT_VAL | VARCHAR2 | 2000 |  |  | This column contains the default val value of the task parameter. |
| DATA_TYPE | VARCHAR2 | 50 |  |  | This column contains the data type value of the task parameter. |
| DATA_DOMAIN | VARCHAR2 | 50 |  |  | This column contains the data domain value of the task parameter. |
| NAMESPACE | VARCHAR2 | 4000 |  |  | This column contains the namespace value of the task parameter. |
| REPETITIVE_FLAG | VARCHAR2 | 1 |  |  | This column contains the repetitive flag value of the task parameter. |
| DRIVING_LABEL_METHOD | VARCHAR2 | 200 |  |  | Column contains VO/SQL defination that will drive the dynamic label for the parameter. NULL values implies there is no dynamic label generation. |
| PARAMETER_TYPE | VARCHAR2 | 20 |  |  | This column contains the parameter type value of the task parameter. |
| ELEMENT_NAME | VARCHAR2 | 50 |  |  | This column contains the element name value of the task parameter. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| REF_TASK_ACTION_ID | NUMBER |  | 18 |  | This column contains the ref task action id value of the task parameter. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| HDL_ATTRIBUTE | VARCHAR2 | 100 |  |  | This column contains the HDL attribute value of the task parameter. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| MULTI_VALUED_FLAG | VARCHAR2 | 2 |  |  | This column contains the multi valued flag value of the task parameter. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_TASK_PARAMETERS_N1 | Non Unique | Default | BASE_TASK_ACTION_ID |
| PAY_TASK_PARAMETERS_N2 | Non Unique | Default | BASE_TASK_PARAMETER_ID |
| PAY_TASK_PARAMETERS_N20 | Non Unique | Default | SGUID |
| PAY_TASK_PARAMETERS_N3 | Non Unique | Default | TO_CHAR("BASE_TASK_PARAMETER_ID") |
| PAY_TASK_PARAMETERS_PK | Unique | Default | TASK_PARAMETER_ID, ORA_SEED_SET1 |
| PAY_TASK_PARAMETERS_PK1 | Unique | Default | TASK_PARAMETER_ID, ORA_SEED_SET2 |
| PAY_TASK_PARAMETERS_U1 | Unique | Default | BASE_TASK_PARAMETER_NAME, BASE_TASK_ACTION_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_TASK_PARAMETERS_U11 | Unique | Default | BASE_TASK_PARAMETER_NAME, BASE_TASK_ACTION_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
