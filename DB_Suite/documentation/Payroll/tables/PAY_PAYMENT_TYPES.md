# PAY_PAYMENT_TYPES

PAY_PAYMENT_TYPES holds the definitions of payment type.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypaymenttypes-30939.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypaymenttypes-30939.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PAYMENT_TYPES_PK | PAYMENT_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYMENT_TYPE_ID | NUMBER |  | 18 | Yes | PAYMENT_TYPE_ID |
| BASE_PAYMENT_TYPE_NAME | VARCHAR2 | 80 |  | Yes | BASE_PAYMENT_TYPE_NAME |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CATEGORY | VARCHAR2 | 2 |  | Yes | CATEGORY |
| ALLOW_AS_DEFAULT | VARCHAR2 | 30 |  |  | ALLOW_AS_DEFAULT |
| BASE_PAYMENT_TYPE_ID | NUMBER |  | 18 |  | BASE_PAYMENT_TYPE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_PAYMENT_TYPES_N1 | Non Unique | Default | BASE_PAYMENT_TYPE_ID, LEGISLATION_CODE |
| PAY_PAYMENT_TYPES_PK | Unique | Default | PAYMENT_TYPE_ID, ORA_SEED_SET1 |
| PAY_PAYMENT_TYPES_PK1 | Unique | Default | PAYMENT_TYPE_ID, ORA_SEED_SET2 |
| PAY_PAYMENT_TYPES_U1 | Unique | Default | BASE_PAYMENT_TYPE_NAME, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_PAYMENT_TYPES_U11 | Unique | Default | BASE_PAYMENT_TYPE_NAME, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
