# PAY_DEFINED_BALANCES

This table contains a complete description of a balance. It is the intersection between balance types and balance dimensions.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydefinedbalances-8785.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydefinedbalances-8785.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DEFINED_BALANCES_PK | DEFINED_BALANCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DEFINED_BALANCE_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| BALANCE_TYPE_ID | NUMBER |  | 18 | Yes | BALANCE_TYPE_ID |
| BALANCE_DIMENSION_ID | NUMBER |  | 18 | Yes | BALANCE_DIMENSION_ID |
| GROSSUP_ALLOWED_FLAG | VARCHAR2 | 30 |  |  | GROSSUP_ALLOWED_FLAG |
| GROSSUP_EXCLUDE_BY_DEFAULT | VARCHAR2 | 30 |  |  | Exclude By Default |
| SAVE_RUN_BALANCE | VARCHAR2 | 30 |  |  | SAVE_RUN_BALANCE |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_DEFINED_BALANCES_N1 | Non Unique | Default | BALANCE_DIMENSION_ID |
| PAY_DEFINED_BALANCES_N2 | Non Unique | Default | LAST_UPDATE_DATE |
| PAY_DEFINED_BALANCES_N20 | Non Unique | Default | SGUID |
| PAY_DEFINED_BALANCES_PK | Unique | Default | DEFINED_BALANCE_ID, ORA_SEED_SET1 |
| PAY_DEFINED_BALANCES_PK1 | Unique | Default | DEFINED_BALANCE_ID, ORA_SEED_SET2 |
| PAY_DEFINED_BALANCES_U1 | Unique | Default | BALANCE_TYPE_ID, BALANCE_DIMENSION_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_DEFINED_BALANCES_U11 | Unique | Default | BALANCE_TYPE_ID, BALANCE_DIMENSION_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
