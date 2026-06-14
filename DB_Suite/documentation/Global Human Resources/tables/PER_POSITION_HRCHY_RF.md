# PER_POSITION_HRCHY_RF

This table stores Position Hierarchy Row Flattened Data

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpositionhrchyrf-31324.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpositionhrchyrf-31324.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_POSITION_HRCHY_RF_PK | POSITION_ID, NODE_LEVEL, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE, ANCESTOR_POSITION_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POSITION_ID | NUMBER |  | 18 | Yes | Position ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |
| ANCESTOR_POSITION_ID | NUMBER |  | 18 | Yes | Position ID of the Ancestor |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| NODE_LEVEL | NUMBER |  | 3 | Yes | Node Level or the Distance (as Number of Levels) from the current Position to the Ancestor |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_POSITION_HRCHY_RF_N1 | Non Unique | Default | ANCESTOR_POSITION_ID, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE, BUSINESS_GROUP_ID, NODE_LEVEL, POSITION_ID |
| PER_POSITION_HRCHY_RF_U1 | Unique | Default | POSITION_ID, NODE_LEVEL, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE, ANCESTOR_POSITION_ID, BUSINESS_GROUP_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
