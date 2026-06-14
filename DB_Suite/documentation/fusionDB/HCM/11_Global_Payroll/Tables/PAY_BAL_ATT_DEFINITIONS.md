# PAY_BAL_ATT_DEFINITIONS

This table contains definitions of balance attributes, with which defined balances can be associated. A balance attribute represents a subset of defined balances.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalattdefinitions-16336.html#paybalattdefinitions-16336](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalattdefinitions-16336.html#paybalattdefinitions-16336)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BAL_ATT_DEFINITIONS_PK | ATTRIBUTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTRIBUTE_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| BASE_ATTRIBUTE_NAME | VARCHAR2 | 80 |  | Yes | Base balance attribute name |
| ALTERABLE | VARCHAR2 | 30 |  | Yes | ALTERABLE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| BALANCE_CATEGORY_ID | NUMBER |  | 18 |  | Foreign key to PAY_BALANCE_CATEGORIES_F. |
| BALANCE_DIMENSION_ID | NUMBER |  | 18 |  | Foreign key to PAY_BALANCE_DIMENSIONS. |
| GROUP_LEVEL_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the balance attribute definition is for group level balances. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_BAL_ATT_DEFINITIONS_PK | Unique | Default | ATTRIBUTE_ID, ORA_SEED_SET1 |
| PAY_BAL_ATT_DEFINITIONS_PK1 | Unique | Default | ATTRIBUTE_ID, ORA_SEED_SET2 |
| PAY_BAL_ATT_DEFINITIONS_U1 | Unique | Default | BASE_ATTRIBUTE_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_BAL_ATT_DEFINITIONS_U11 | Unique | Default | BASE_ATTRIBUTE_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
