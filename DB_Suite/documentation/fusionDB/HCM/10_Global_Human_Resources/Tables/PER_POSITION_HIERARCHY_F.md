# PER_POSITION_HIERARCHY_F

This table will be used to store position hierarchy information.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpositionhierarchyf-28209.html#perpositionhierarchyf-28209](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpositionhierarchyf-28209.html#perpositionhierarchyf-28209)

## Primary Key

| Name | Columns |
|------|----------|
| PER_POSITION_HIERARCHY_F_PK | POSITION_HIERARCHY_ID, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POSITION_HIERARCHY_ID | NUMBER |  | 18 | Yes | POSITIONHIERARCHYID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| POSITION_ID | NUMBER |  | 18 | Yes | PositionId of the record. |
| PARENT_POSITION_ID | NUMBER |  | 18 |  | PositionId of Parent position record. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ACTION_OCCURRENCES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_POSITION_HIERARCHY_F_N1 | Non Unique | Default | PARENT_POSITION_ID, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE |
| PER_POSITION_HIERARCHY_F_U1 | Unique | Default | POSITION_HIERARCHY_ID, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE |
| PER_POSITION_HIERARCHY_F_U2 | Unique | Default | POSITION_ID, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE, PARENT_POSITION_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
