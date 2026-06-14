# HRY_VALUE_MAP_RULESET_B

Stores information related to value map rule set.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryvaluemaprulesetb-16132.html#hryvaluemaprulesetb-16132](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryvaluemaprulesetb-16132.html#hryvaluemaprulesetb-16132)

## Primary Key

| Name | Columns |
|------|----------|
| hry_value_map_ruleset_PK | RULE_SET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RULE_SET_ID | NUMBER |  | 18 | Yes | Primary key for HRY_VALUE_MAP_RULESET |
| BASE_RULE_SET_NAME | VARCHAR2 | 150 |  |  | For storing base rule set name. |
| EXT_DEFINITION_ID | NUMBER |  | 18 |  | Foreign key to PER_EXT_DEFINITIONS_B |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |
| VENDOR_NAME | VARCHAR2 | 150 |  |  | This column is used for storing the vendor name. |
| PAYROLL_ID | NUMBER |  | 18 |  | Foreign Key to the PAY_PAYROLL_ACTION Table. |
| XSL_TEMPLATE | CLOB |  |  |  | For storing the generated XSLT for each data element. |
| XSLT_GENERATED_DATE | DATE |  |  |  | For storing the generated XSLT date. |
| STATUS | VARCHAR2 | 30 |  |  | This flag shows whether the ruleset is valid or not. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hry_value_map_ruleset_b_N20 | Non Unique | Default | SGUID |
| hry_value_map_ruleset_b_PK | Unique | Default | RULE_SET_ID, ORA_SEED_SET1 |
| hry_value_map_ruleset_b_PK1 | Unique | Default | RULE_SET_ID, ORA_SEED_SET2 |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
