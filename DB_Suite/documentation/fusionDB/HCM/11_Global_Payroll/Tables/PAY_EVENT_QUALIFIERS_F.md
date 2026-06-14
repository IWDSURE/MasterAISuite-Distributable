# PAY_EVENT_QUALIFIERS_F

This table contains event qualifiers, which define which changes are relevant to track, such as changes to a specific segment of a flexfield.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventqualifiersf-10638.html#payeventqualifiersf-10638](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventqualifiersf-10638.html#payeventqualifiersf-10638)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_EVENT_QUALIFIERS_F_PK | EVENT_QUALIFIER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_QUALIFIER_ID | NUMBER |  | 18 | Yes | EVENT_QUALIFIER_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| DATED_TABLE_ID | NUMBER |  | 18 | Yes | DATED_TABLE_ID |
| COLUMN_NAME | VARCHAR2 | 30 |  |  | COLUMN_NAME |
| QUALIFIER_NAME | VARCHAR2 | 80 |  | Yes | QUALIFIER_NAME |
| QUALIFIER_TYPE | VARCHAR2 | 30 |  |  | The type of qualifier that is defined. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| COMPARISON_COLUMN | VARCHAR2 | 2000 |  |  | COMPARISON_COLUMN |
| QUALIFIER_DEFINITION | VARCHAR2 | 2000 |  |  | QUALIFIER_DEFINITION |
| QUALIFIER_WHERE_CLAUSE | VARCHAR2 | 2000 |  |  | QUALIFIER_WHERE_CLAUSE |
| SEC_QUAL_DEFINITION | VARCHAR2 | 2000 |  |  | SEC_QUAL_DEFINITION |
| SEC_QUAL_WHERE_CLAUSE | VARCHAR2 | 2000 |  |  | SEC_QUAL_WHERE_CLAUSE |
| ENTRY_QUALIFICATION | VARCHAR2 | 2000 |  |  | ENTRY_QUALIFICATION |
| ASSIGNMENT_QUALIFICATION | VARCHAR2 | 2000 |  |  | ASSIGNMENT_QUALIFICATION |
| MULTI_EVENT_SQL | VARCHAR2 | 2000 |  |  | MULTI_EVENT_SQL |
| DESCRIPTION | VARCHAR2 | 240 |  |  | DESCRIPTION |
| FORMULA_ID | NUMBER |  | 18 |  | FORMULA_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_EVENT_QUALIFIERS_F_PK | Unique | Default | EVENT_QUALIFIER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_EVENT_QUALIFIERS_F_PK1 | Unique | Default | EVENT_QUALIFIER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
