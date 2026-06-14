# PAY_CONTEXT_USAGES

This table contains the context details used by each localization.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycontextusages-15436.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycontextusages-15436.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_CONTEXT_USAGES_PK | CONTEXT_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTEXT_USAGE_ID | NUMBER |  | 18 | Yes | CONTEXT_USAGE_ID |
| CONTEXT_ID | NUMBER |  | 18 | Yes | Identifier for the context. Foreign key to FF_CONTEXTS. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CONTEXT_ABBR | VARCHAR2 | 30 |  |  | CONTEXT_ABBR |
| USED_IN_BALANCE_FLAG | VARCHAR2 | 30 |  |  | USED_IN_BALANCE_FLAG |
| USED_IN_DIST_COSTING_FLAG | VARCHAR2 | 30 |  |  | USED_IN_DIST_COSTING_FLAG |
| INPUT_VALUE_CONTEXT_FLAG | VARCHAR2 | 30 |  |  | INPUT_VALUE_CONTEXT_FLAG |
| LOOKUP_TYPE | VARCHAR2 | 30 |  |  | LOOKUP_TYPE |
| VO_NAME | VARCHAR2 | 100 |  |  | VO_NAME |
| DEFAULT_VALUE_DBI_ID | NUMBER |  | 18 |  | DEFAULT_VALUE_DBI_ID |
| MEANING_DBI_ID | NUMBER |  | 18 |  | Database item that returns the meaning of the context value. Foreign key to FF_DATABASE_ITEMS_B. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_CONTEXT_USAGES_N20 | Non Unique | Default | SGUID |
| PAY_CONTEXT_USAGES_PK | Unique | Default | CONTEXT_USAGE_ID, ORA_SEED_SET1 |
| PAY_CONTEXT_USAGES_PK1 | Unique | Default | CONTEXT_USAGE_ID, ORA_SEED_SET2 |
| PAY_CONTEXT_USAGES_U1 | Unique | Default | CONTEXT_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_CONTEXT_USAGES_U11 | Unique | Default | CONTEXT_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
