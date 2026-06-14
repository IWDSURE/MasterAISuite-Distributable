# PAY_FLOW_PARAMETER_PROPERTIES

this will be utilized to store flow parameter properties

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowparameterproperties-23397.html#payflowparameterproperties-23397](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowparameterproperties-23397.html#payflowparameterproperties-23397)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_FLOW_PARAMETER_PROP_PK | PARAM_PROPERTY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARAM_PROPERTY_ID | NUMBER |  | 18 | Yes | PARAM_PROPERTY_ID |
| BASE_FLOW_PARAMETER_ID | NUMBER |  | 18 |  | BASE_FLOW_PARAMETER_ID |
| EXPRESSION_TYPE | VARCHAR2 | 30 |  |  | EXPRESSION_TYPE |
| PROPERTY_NAME | VARCHAR2 | 200 |  |  | PROPERTY_NAME |
| PROPERTY_VALUE | VARCHAR2 | 4000 |  |  | PROPERTY_VALUE |
| PROPERTY_VALUE_EXPRESSION | CLOB |  |  |  | PROPERTY_VALUE_EXPRESSION |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier.Oracle internal use only. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_FLOW_PARAMETER_PROP_PK | Unique | Default | PARAM_PROPERTY_ID, ORA_SEED_SET1 |
| PAY_FLOW_PARAMETER_PROP_PK1 | Unique | Default | PARAM_PROPERTY_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
