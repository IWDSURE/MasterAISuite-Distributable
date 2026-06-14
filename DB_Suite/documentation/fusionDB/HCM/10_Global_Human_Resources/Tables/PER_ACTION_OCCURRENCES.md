# PER_ACTION_OCCURRENCES

This table defines the action occurrences for an action.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractionoccurrences-21291.html#peractionoccurrences-21291](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractionoccurrences-21291.html#peractionoccurrences-21291)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ACTION_OCCURRENCES_PK | ACTION_OCCURRENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Primary key. Uniquely identifies a document of record. |
| ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ACTIONS_B table. |
| ACTION_REASON_ID | NUMBER |  | 18 |  | Foreign key to PER_ACTION_REASONS_B table. |
| ACTION_DATE | DATE |  |  | Yes | Date of occurance of action. |
| SUBMITTED_BY | NUMBER |  | 18 | Yes | Indicates the user who submitted the action. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| FREEZE_START_DATE | DATE |  |  | Yes | Represents the Deferred data freeze start date (defaulted to End of time). |
| FREEZE_UNTIL_DATE | DATE |  |  | Yes | Represents the Deferred data freeze until date (defaulted to Start of Time). |
| ENTITY_TYPE | VARCHAR2 | 32 |  |  | Entity Type stores the parent object of a transactional entity. |
| ENTITY_ID | NUMBER |  | 18 |  | Stores Surrogate key of the entity type |
| PARENT_ENTITY_TYPE | VARCHAR2 | 32 |  |  | Entity Type stores the parent object of a transactional entity. |
| PARENT_ENTITY_KEY_ID | NUMBER |  | 18 |  | Stores Surrogate key of the entity type |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ACTION_TYPE_CODE | VARCHAR2 | 30 |  |  | Denormalized information. Stores the Action Type used in creation of this row |
| PROPOSED_ACTION_ID | NUMBER |  | 18 |  | PROPOSED_ACTION_ID |
| PROPOSED_REASON_ID | NUMBER |  | 18 |  | PROPOSED_REASON_ID |
| PROPOSED_ACTION_TYPE | VARCHAR2 | 150 |  |  | PROPOSED_ACTION_TYPE |
| PROPOSED_WORKER_TYPE | VARCHAR2 | 30 |  |  | PROPOSED_WORKER_TYPE |
| PROPOSED_START_DATE | DATE |  |  |  | PROPOSED_START_DATE |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| CATEGORY_CODE | VARCHAR2 | 80 |  |  | Data with different category |
| REF_ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Reference action Occurrence Id |
| POSITION_ID | NUMBER |  | 18 |  | Position ID for Combined Employment and Position Change action |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Business Unit ID for Combined Employment and Position Change action |
| HOW_TO_PROCESS | VARCHAR2 | 30 |  |  | Choice of position action for Combined Employment and Position Change action |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ACTION_OCCURRENCES_N1 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_ACTION_OCCURRENCES_N2 | Non Unique | Default | PARENT_ENTITY_KEY_ID |
| PER_ACTION_OCCURRENCES_N3 | Non Unique | Default | ACTION_TYPE_CODE, PARENT_ENTITY_KEY_ID |
| PER_ACTION_OCCURRENCES_N4 | Non Unique | Default | ACTION_DATE |
| PER_ACTION_OCCURRENCES_PK | Unique | Default | ACTION_OCCURRENCE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
