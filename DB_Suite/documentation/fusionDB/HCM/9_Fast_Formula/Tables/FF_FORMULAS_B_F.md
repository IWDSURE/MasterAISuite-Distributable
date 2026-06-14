# FF_FORMULAS_B_F

This table contains formula definitions and text.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffformulasbf-22763.html#ffformulasbf-22763](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffformulasbf-22763.html#ffformulasbf-22763)

## Primary Key

| Name | Columns |
|------|----------|
| FF_FORMULAS_F_PK | FORMULA_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FORMULA_ID | NUMBER |  | 18 | Yes | Unique identifier of the formula. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| FORMULA_TYPE_ID | NUMBER |  | 18 | Yes | Identifier for the formula type. Foreign key to FF_FORMULA_TYPES. |
| BASE_FORMULA_NAME | VARCHAR2 | 80 |  | Yes | Unique name for the formula. |
| EDIT_STATUS | VARCHAR2 | 30 |  |  | Edit status to indicate whether formula can be edited in Text mode. |
| FORMULA_TEXT | CLOB |  |  |  | User text of the formula. |
| COMPILE_FLAG | VARCHAR2 | 1 |  |  | Should the formula be compiled. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ORGANIZATION_UNITS. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FF_FORMULAS_B_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| FF_FORMULAS_B_F_N3 | Non Unique | Default | BASE_FORMULA_NAME |
| FF_FORMULAS_B_F_PK | Unique | Default | FORMULA_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| FF_FORMULAS_B_F_PK1 | Unique | Default | FORMULA_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |
| FF_FORMULAS_F_FK1 | Non Unique | Default | FORMULA_TYPE_ID |
| FF_FORMULAS_F_N1 | Non Unique | Default | UPPER("BASE_FORMULA_NAME") |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
