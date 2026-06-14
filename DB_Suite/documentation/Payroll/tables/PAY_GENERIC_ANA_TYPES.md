# PAY_GENERIC_ANA_TYPES

This table contains pay generic ANALYTICS type.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygenericanatypes-25414.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygenericanatypes-25414.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_GENERIC_ANA_TYPES_PK | PAY_GEN_ANA_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_GEN_ANA_TYPE_ID | NUMBER |  | 18 | Yes | PAY_GEN_ANA_TYPE_ID, Unique Id for pay generic analytics type |
| BASE_GEN_ANA_TYPE | VARCHAR2 | 128 |  | Yes | Base Generic Analytics Type. Unique Code |
| ANALYTICS_CATEGORY | VARCHAR2 | 128 |  | Yes | ANALYTICS_CATEGORY, default is Data Collection. Can be Validation |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Legislative Data Group Id. Foreign key to PER_LEGISLATIVE_DATA_GROUPS_vl table. |
| LEGISLATION_CODE | VARCHAR2 | 10 |  |  | Legislation Code. Identify legislation code. |
| METHOD_TYPE | VARCHAR2 | 64 |  |  | METHOD_TYPE: JAVA or PLSQL. Execution Method. |
| METHOD | VARCHAR2 | 128 |  |  | Method name. Java or PLSQL name will be used at runtime. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  | Yes | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_GENERIC_ANA_TYPES_N1 | Non Unique | Default | BASE_GEN_ANA_TYPE, LEGISLATION_CODE |
| PAY_GENERIC_ANA_TYPES_U1 | Unique | Default | PAY_GEN_ANA_TYPE_ID, ORA_SEED_SET1 |
| PAY_GENERIC_ANA_TYPES_U2 | Unique | Default | PAY_GEN_ANA_TYPE_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
