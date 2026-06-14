# PER_MASS_ACTION_HEADER

Stores status and other general information related to a Mass Action.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permassactionheader-25736.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permassactionheader-25736.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_MASS_ACTION_HEADER_PK | MASS_ACTION_HEADER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MASS_ACTION_HEADER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| MODULE_IDENTIFIER | VARCHAR2 | 60 |  |  | The Module that set up the business data. |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| ACTION_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ACTIONS_B table. |
| ACTION_REASON_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_REASONS_B table. |
| NAME | VARCHAR2 | 80 |  | Yes | Denotes name for Mass Action Header. |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description for the Mass Action Header. |
| STATUS | VARCHAR2 | 30 |  | Yes | Identifies whether a mass update transaction is in progress or complete. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| NUMBER_OF_LINES | NUMBER |  | 18 |  | Represents the number of changes (population getting updated). |
| LOADER_BATCH_ID | NUMBER |  | 18 |  | Identifies the batch processed by batch loader. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_MASS_ACTION_HEADER_PK | Unique | FUSION_TS_TX_IDX | MASS_ACTION_HEADER_ID |
| PER_MASS_ACTION_HEADER_U1 | Unique | Default | NAME |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
