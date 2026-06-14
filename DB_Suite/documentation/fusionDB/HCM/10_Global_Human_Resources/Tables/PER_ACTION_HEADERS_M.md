# PER_ACTION_HEADERS_M

MCPD supports Action Headers table

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractionheadersm-23766.html#peractionheadersm-23766](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractionheadersm-23766.html#peractionheadersm-23766)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ACTION_HEADERS_M_PK | ACTION_HEADER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, EFFECTIVE_SEQUENCE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_HEADER_ID | NUMBER |  | 18 | Yes | System generated primary key. Surrogate Key. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EFFECTIVE_SEQUENCE | NUMBER |  | 4 | Yes | Date Effective Entity: indicates the order of different changes made during a day. The lowest value represents the earliest change in the day. |
| EFFECTIVE_LATEST_CHANGE | VARCHAR2 | 30 |  | Yes | Date Effective Entity: 'Y' indicates that this row represents the latest change in the day. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ENTITY_TYPE | VARCHAR2 | 30 |  | Yes | Entity getting modified. |
| ENTITY_KEY_ID | NUMBER |  | 18 | Yes | Surrogate key ID of the entity getting modified |
| ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ACTIONS_B table. |
| ACTION_REASON_ID | NUMBER |  | 18 |  | Foreign key to PER_ACTION_REASONS_B table. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ACTION_HEADERS_M_PK | Unique | FUSION_TS_TX_DATA | ACTION_HEADER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, EFFECTIVE_SEQUENCE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
