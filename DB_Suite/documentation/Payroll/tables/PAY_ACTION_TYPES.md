# PAY_ACTION_TYPES

This table contains types of payroll action, such as payroll run and prepayments.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactiontypes-31255.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactiontypes-31255.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ACTION_TYPES_PK | ACTION_TYPE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_TYPE | VARCHAR2 | 20 |  | Yes | ACTION_TYPE |
| PROCESS_MASTER_ACTION | VARCHAR2 | 260 |  | Yes | PROCESS_MASTER_ACTION |
| PROCESS_WORK_UNIT | VARCHAR2 | 260 |  | Yes | PROCESS_WORK_UNIT |
| DYNAMIC_WORK_UNIT | VARCHAR2 | 1 |  |  | DYNAMIC_WORK_UNIT |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ACTION_TYPES_PK | Unique | Default | ACTION_TYPE, ORA_SEED_SET1 |
| PAY_ACTION_TYPES_PK1 | Unique | Default | ACTION_TYPE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
