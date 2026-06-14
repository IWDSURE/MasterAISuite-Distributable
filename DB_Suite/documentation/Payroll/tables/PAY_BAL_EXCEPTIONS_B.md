# PAY_BAL_EXCEPTIONS_B

This table contains balance exception information.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalexceptionsb-14208.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalexceptionsb-14208.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BAL_EXCEPTIONS_B_PK | BAL_EXCEPTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BAL_EXCEPTION_ID | NUMBER |  | 18 | Yes | BAL_EXCEPTION_ID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| REPORT_DEFINITION_ID | NUMBER |  | 18 |  | REPORT_DEFINITION_ID |
| BASE_BAL_EXCEPTION_NAME | VARCHAR2 | 80 |  | Yes | BASE_BAL_EXCEPTION_NAME |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| CURRENCY_CODE | VARCHAR2 | 15 |  |  | CURRENCY_CODE |
| DEFINED_BALANCE_ID | NUMBER |  | 18 |  | DEFINED_BALANCE_ID |
| VARIANCE_TYPE | VARCHAR2 | 30 |  | Yes | VARIANCE_TYPE |
| VARIANCE_VALUE | NUMBER |  | 11 | Yes | VARIANCE_VALUE |
| COMPARISON_TYPE | VARCHAR2 | 30 |  | Yes | COMPARISON_TYPE |
| COMPARISON_VALUE | NUMBER |  | 9 | Yes | COMPARISON_VALUE |
| VARIANCE_OPERATOR | VARCHAR2 | 30 |  | Yes | VARIANCE_OPERATOR |
| OUTPUT_FORMAT | VARCHAR2 | 30 |  |  | OUTPUT_FORMAT |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEVERITY_LEVEL | NUMBER |  | 1 |  | SEVERITY_LEVEL |
| FORMULA_ID | NUMBER |  | 18 |  | FORMULA_ID |
| TARGET_DEFINED_BALANCE_ID | NUMBER |  | 18 |  | TARGET_DEFINED_BALANCE_ID |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| BALANCE_GROUP_ID | NUMBER |  | 18 |  | BALANCE_GROUP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_BAL_EXCEPTIONS_B_PK | Unique | Default | BAL_EXCEPTION_ID, ORA_SEED_SET1 |
| PAY_BAL_EXCEPTIONS_B_PK1 | Unique | Default | BAL_EXCEPTION_ID, ORA_SEED_SET2 |
| PAY_BAL_EXCEPTIONS_B_UK1 | Unique | Default | BASE_BAL_EXCEPTION_NAME, LEGISLATION_CODE, LEGISLATIVE_DATA_GROUP_ID, ORA_SEED_SET1 |
| PAY_BAL_EXCEPTIONS_B_UK11 | Unique | Default | BASE_BAL_EXCEPTION_NAME, LEGISLATION_CODE, LEGISLATIVE_DATA_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
