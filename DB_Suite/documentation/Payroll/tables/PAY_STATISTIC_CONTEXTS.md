# PAY_STATISTIC_CONTEXTS

It stores the all possible context, against which statistics can be stored.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paystatisticcontexts-20778.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paystatisticcontexts-20778.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_STATISTIC_CONTEXTS_PK | STATISTIC_CONTEXT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STATISTIC_CONTEXT_ID | NUMBER |  | 18 | Yes | STATISTIC_CONTEXT_ID |
| BASE_STATISTIC_CONTEXT_ID | NUMBER |  | 18 |  | BASE_STATISTIC_CONTEXT_ID |
| DISPLAY_FLAG | VARCHAR2 | 30 |  |  | DISPLAY_FLAG |
| STATISTIC_CONTEXT_NAME | VARCHAR2 | 200 |  |  | STATISTIC_CONTEXT_NAME |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_STATISTIC_CONTEXTS_N20 | Non Unique | Default | SGUID |
| PAY_STATISTIC_CONTEXTS_PK | Unique | Default | STATISTIC_CONTEXT_ID, ORA_SEED_SET1 |
| PAY_STATISTIC_CONTEXTS_PK1 | Unique | Default | STATISTIC_CONTEXT_ID, ORA_SEED_SET2 |
| PAY_STATISTIC_CONTEXTS_UK1 | Unique | Default | STATISTIC_CONTEXT_ID, STATISTIC_CONTEXT_NAME, ORA_SEED_SET1 |
| PAY_STATISTIC_CONTEXTS_UK11 | Unique | Default | STATISTIC_CONTEXT_ID, STATISTIC_CONTEXT_NAME, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
