# PAY_COST_ALLOCATIONS_F

This table contains the definition of the cost allocation to various objects such as job, payroll, and payroll relationship. This table is the parent of payroll cost allocation accounts that defines how costs are proportioned to different accounts.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycostallocationsf-12114.html#paycostallocationsf-12114](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycostallocationsf-12114.html#paycostallocationsf-12114)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_COST_ALLOCATIONS_F_PK | COST_ALLOCATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COST_ALLOCATION_ID | NUMBER |  | 18 | Yes | COST_ALLOCATION_ID |
| SOURCE_TYPE | VARCHAR2 | 30 |  | Yes | SOURCE_TYPE |
| SOURCE_ID | NUMBER |  | 18 |  | SOURCE_ID |
| HISTORY_COMMENTS | VARCHAR2 | 80 |  |  | HISTORY_COMMENTS |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATOR_ID | NUMBER |  | 18 |  | CREATOR_ID |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | PAYROLL_RELATIONSHIP_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| PROGRAM_ID | NUMBER |  | 18 |  | PROGRAM_ID |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | PROGRAM_UPDATE_DATE |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| COST_ALLOCATION_RECORD_ID | NUMBER |  | 18 | Yes | COST_ALLOCATION_RECORD_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_COST_ALLOCATIONS_F_N1 | Non Unique | Default | SOURCE_TYPE, SOURCE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_COST_ALLOCATIONS_F_N2 | Non Unique | Default | CREATOR_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_COST_ALLOCATIONS_F_N3 | Non Unique | Default | COST_ALLOCATION_RECORD_ID |
| PAY_COST_ALLOCATIONS_F_PK | Unique | Default | COST_ALLOCATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
