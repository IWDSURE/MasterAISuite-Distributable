# PAY_DEDUCTION_GROUPS

This table contains logical groupings of deductions, such as an income tax group that includes the value definitions for calculating income tax.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydeductiongroups-26141.html#paydeductiongroups-26141](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydeductiongroups-26141.html#paydeductiongroups-26141)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DEDUCTION_GRUOUPS_PK | DEDUCTION_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DEDUCTION_GROUP_ID | NUMBER |  | 18 | Yes | DEDUCTION_GROUP_ID |
| BASE_NAME | VARCHAR2 | 240 |  | Yes | BASE_NAME |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| BASE_DEDUCTION_GROUP_ID | NUMBER |  | 18 |  | BASE_DEDUCTION_GROUP_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_STATUS | VARCHAR2 | 1 |  |  | SEED_STATUS |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_DEDUCTION_GROUPS_N1 | Non Unique | Default | BASE_DEDUCTION_GROUP_ID, LEGISLATION_CODE |
| PAY_DEDUCTION_GRUOUPS_PK | Unique | Default | DEDUCTION_GROUP_ID, ORA_SEED_SET1 |
| PAY_DEDUCTION_GRUOUPS_PK1 | Unique | Default | DEDUCTION_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
