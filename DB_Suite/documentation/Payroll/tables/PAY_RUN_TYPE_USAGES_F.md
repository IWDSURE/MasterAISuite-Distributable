# PAY_RUN_TYPE_USAGES_F

Holds child run types where the run type parent is of type Cumulative.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payruntypeusagesf-10588.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payruntypeusagesf-10588.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_RUN_TYPE_USAGES_PK | RUN_TYPE_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_TYPE_USAGE_ID | NUMBER |  | 18 | Yes | Primary key. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PARENT_RUN_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key for the parent run type |
| CHILD_RUN_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key for the child run type |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEQUENCE | NUMBER |  | 9 | Yes | The order in which run type will be processed. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
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
| PAY_RUN_TYPE_USAGES_F_N2 | Non Unique | Default | CHILD_RUN_TYPE_ID |
| PAY_RUN_TYPE_USAGES_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_RUN_TYPE_USAGES_F_U1 | Unique | Default | PARENT_RUN_TYPE_ID, CHILD_RUN_TYPE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LEGISLATIVE_DATA_GROUP_ID, ORA_SEED_SET1 |
| PAY_RUN_TYPE_USAGES_F_U11 | Unique | Default | PARENT_RUN_TYPE_ID, CHILD_RUN_TYPE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LEGISLATIVE_DATA_GROUP_ID, ORA_SEED_SET2 |
| PAY_RUN_TYPE_USAGES_PK | Unique | Default | RUN_TYPE_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_RUN_TYPE_USAGES_PK1 | Unique | Default | RUN_TYPE_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
