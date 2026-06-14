# HWM_ALLOCATION_RULES_F

Time Allocations Rules table contains Rules based on Time Category and Allocation type. This table is parent to Time Allocation Lines and child of Time allocation header.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmallocationrulesf-24803.html#hwmallocationrulesf-24803](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmallocationrulesf-24803.html#hwmallocationrulesf-24803)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_ALLOCATION_RULES_F_PK | ALLOCATION_RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALLOCATION_RULE_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| ALLOCATION_ID | NUMBER |  | 18 | Yes | Foreign Key to the Time allocation table |
| ALLOCATION_RULE_PRIORITY | NUMBER |  | 9 | Yes | ALLOCATION_RULE_PRIORITY |
| TCAT_ID | NUMBER |  | 18 |  | Foreign Key to the Time category  table |
| ALLOCATION_TYPE | VARCHAR2 | 30 |  | Yes | ALLOCATION_TYPE |
| RUN_SUMMATION_LEVEL | VARCHAR2 | 30 |  | Yes | RUN_SUMMATION_LEVEL |
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
| HWM_ALLOCATION_RULES_F_N1 | Non Unique | Default | ALLOCATION_ID |
| HWM_ALLOCATION_RULES_F_PK | Unique | FUSION_TS_TX_DATA | ALLOCATION_RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
