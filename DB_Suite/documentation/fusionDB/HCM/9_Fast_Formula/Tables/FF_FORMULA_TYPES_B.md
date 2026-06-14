# FF_FORMULA_TYPES_B

This table contains formula types, which define groups of formulas to associate with formula contexts and used for specific purposes.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffformulatypesb-25754.html#ffformulatypesb-25754](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffformulatypesb-25754.html#ffformulatypesb-25754)

## Primary Key

| Name | Columns |
|------|----------|
| FF_FORMULA_TYPES_PK | FORMULA_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FORMULA_TYPE_ID | NUMBER |  | 18 | Yes | Unique identifier of the formula type. |
| BASE_FORMULA_TYPE_NAME | VARCHAR2 | 80 |  | Yes | Unique name for the formula type. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| EDIT_TYPE | VARCHAR2 | 30 |  |  | Indicates whether Formula can be edited as Text,Expression or Both |
| PARTITION_TYPE | VARCHAR2 | 30 |  |  | This column is utilized to distinguish whether formula  is for Ldg or Enterprise or both |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FF_FORMULA_TYPES_B_PK | Unique | Default | FORMULA_TYPE_ID, ORA_SEED_SET1 |
| FF_FORMULA_TYPES_B_PK1 | Unique | Default | FORMULA_TYPE_ID, ORA_SEED_SET2 |
| FF_FORMULA_TYPES_B_U1 | Unique | Default | UPPER("BASE_FORMULA_TYPE_NAME"), ORA_SEED_SET1 |
| FF_FORMULA_TYPES_B_U11 | Unique | Default | UPPER("BASE_FORMULA_TYPE_NAME"), ORA_SEED_SET2 |
| FF_FORMULA_TYPES_B_U2 | Unique | Default | BASE_FORMULA_TYPE_NAME, ORA_SEED_SET1 |
| FF_FORMULA_TYPES_B_U21 | Unique | Default | BASE_FORMULA_TYPE_NAME, ORA_SEED_SET2 |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
