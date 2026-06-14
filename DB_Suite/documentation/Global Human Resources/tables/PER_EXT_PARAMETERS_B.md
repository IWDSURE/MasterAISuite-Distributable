# PER_EXT_PARAMETERS_B

Parameters used in extracts definitions.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextparametersb-31365.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextparametersb-31365.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_PARAMETERS_B_PK | EXT_PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXT_PARAM_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| BASE_PARAM_NAME | VARCHAR2 | 80 |  |  | Base Name of the Parameter |
| EXT_DEFINITION_ID | NUMBER |  | 18 |  | Identifier for the Extract definition. |
| XML_TAG_NAME | VARCHAR2 | 80 |  |  | XML Tag Name of Parameter |
| DATA_TYPE | VARCHAR2 | 80 |  |  | Data Type of the Parameter |
| ESS_PARAM_NAME | VARCHAR2 | 80 |  |  | ESS Parameter Name |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ALLOWED_IN_EXPRESSION | VARCHAR2 | 1 |  |  | ALLOWED_IN_EXPRESSION - To distinguish parameters, which are auto generated for some extract types, if they are allowed in expressions. |
| GENERATED | VARCHAR2 | 1 |  |  | GENERATED - Some parameters are auto generated for some extract types. They should not be deleted by user. This flag is added to ensure that. |
| PARAM_SEQUENCE | NUMBER |  | 18 |  | Sequence of the Parameter |
| DEFAULT_TYPE | VARCHAR2 | 30 |  |  | Default Parameter Type |
| DEFAULT_VAL | VARCHAR2 | 2000 |  |  | Defaulted Parameter Value |
| DISPLAY_FLAG | VARCHAR2 | 1 |  |  | Flag that determines Parameter display |
| PARAM_LOOKUP | VARCHAR2 | 200 |  |  | Look up for the parameter |
| PARAM_USAGE_TYPE | VARCHAR2 | 30 |  |  | Determines whether it is input parameter or ouput parameter |
| PARAM_DISP_TYPE | VARCHAR2 | 30 |  |  | Display Type of the Parameter |
| PARAM_VALUE_SET | VARCHAR2 | 200 |  |  | Value set associated with the parameter |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EXT_PARAMETERS_B_N20 | Non Unique | Default | SGUID |
| PER_EXT_PARAMETERS_B_PK | Unique | Default | EXT_PARAM_ID, ORA_SEED_SET1 |
| PER_EXT_PARAMETERS_B_PK1 | Unique | Default | EXT_PARAM_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
