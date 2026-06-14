# PAY_OBJECT_GROUPS

This table contains groups of elements, people, or deduction card data, used for reporting, processing, data entry, and costing distributions.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobjectgroups-18338.html#payobjectgroups-18338](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobjectgroups-18338.html#payobjectgroups-18338)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_OBJECT_GROUPS_PK | OBJECT_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_GROUP_ID | NUMBER |  | 18 | Yes | OBJECT_GROUP_ID |
| OBJECT_GROUP_TYPE_ID | NUMBER |  | 18 | Yes | OBJECT_GROUP_TYPE_ID |
| BASE_OBJECT_GROUP_NAME | VARCHAR2 | 80 |  | Yes | BASE_OBJECT_GROUP_NAME |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| START_DATE | DATE |  |  | Yes | START_DATE |
| END_DATE | DATE |  |  | Yes | END_DATE |
| FORMULA_ID | NUMBER |  | 18 |  | FORMULA_ID |
| STATIC_DYNAMIC_FLAG | VARCHAR2 | 30 |  |  | STATIC_DYNAMIC_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | SOURCE_TYPE |
| SOURCE_ID | NUMBER |  | 18 |  | SOURCE_ID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_OBJECT_GROUPS_N2 | Non Unique | Default | LEGISLATIVE_DATA_GROUP_ID, ENTERPRISE_ID, OBJECT_GROUP_ID |
| PAY_OBJECT_GROUPS_N3 | Non Unique | Default | BASE_OBJECT_GROUP_NAME |
| PAY_OBJECT_GROUPS_PK | Unique | Default | OBJECT_GROUP_ID, ORA_SEED_SET1 |
| PAY_OBJECT_GROUPS_PK1 | Unique | Default | OBJECT_GROUP_ID, ORA_SEED_SET2 |
| PAY_OBJECT_GROUPS_U1 | Unique | Default | OBJECT_GROUP_ID, OBJECT_GROUP_TYPE_ID, ORA_SEED_SET1 |
| PAY_OBJECT_GROUPS_U11 | Unique | Default | OBJECT_GROUP_ID, OBJECT_GROUP_TYPE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
