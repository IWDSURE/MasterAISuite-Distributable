# PAY_TIME_SPANS

This table contains details of time spans used to create time definitions.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytimespans-12811.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytimespans-12811.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TIME_SPANS_PK | TIME_SPAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TIME_SPAN_ID | NUMBER |  | 18 | Yes | TIME_SPAN_ID |
| CREATOR_ID | NUMBER |  | 18 | Yes | CREATOR_ID |
| CREATOR_TYPE | VARCHAR2 | 30 |  | Yes | CREATOR_TYPE |
| START_TIME_DEF_ID | NUMBER |  | 18 | Yes | START_TIME_DEF_ID |
| END_TIME_DEF_ID | NUMBER |  | 18 | Yes | END_TIME_DEF_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_TIME_SPANS_N20 | Non Unique | Default | SGUID |
| PAY_TIME_SPANS_PK | Unique | Default | TIME_SPAN_ID, ORA_SEED_SET1 |
| PAY_TIME_SPANS_PK1 | Unique | Default | TIME_SPAN_ID, ORA_SEED_SET2 |
| PAY_TIME_SPANS_UK1 | Unique | Default | CREATOR_ID, CREATOR_TYPE, START_TIME_DEF_ID, END_TIME_DEF_ID, ORA_SEED_SET1 |
| PAY_TIME_SPANS_UK11 | Unique | Default | CREATOR_ID, CREATOR_TYPE, START_TIME_DEF_ID, END_TIME_DEF_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
