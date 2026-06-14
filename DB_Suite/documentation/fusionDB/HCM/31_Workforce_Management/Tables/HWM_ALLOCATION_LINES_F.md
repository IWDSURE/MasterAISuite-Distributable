# HWM_ALLOCATION_LINES_F

Time Allocations lines table contains detail allocation values per each Allocation Rule row.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmallocationlinesf-10246.html#hwmallocationlinesf-10246](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmallocationlinesf-10246.html#hwmallocationlinesf-10246)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_ALLOCATION_LINES_F_PK | ALLOCATION_LINE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALLOCATION_LINE_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| ALLOCATION_RULE_ID | NUMBER |  | 18 | Yes | Foreign Key to the allocation Rule table. |
| ALLOCATION_LINE_PRIORITY | NUMBER |  |  | Yes | ALLOCATION_LINE_PRIORITY |
| ALLOCATION_VALUE | NUMBER |  |  | Yes | ALLOCATION_VALUE |
| DATA_LEVEL | NUMBER |  | 9 | Yes | DATA_LEVEL |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_ALLOCATION_LINES_F_N1 | Non Unique | Default | ALLOCATION_RULE_ID |
| HWM_ALLOCATION_LINES_F_PK | Unique | FUSION_TS_TX_DATA | ALLOCATION_LINE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
