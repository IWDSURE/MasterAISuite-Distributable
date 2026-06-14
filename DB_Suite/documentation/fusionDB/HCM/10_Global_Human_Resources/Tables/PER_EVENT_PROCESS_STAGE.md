# PER_EVENT_PROCESS_STAGE

This table is used to store the event process details of Person synchronization.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pereventprocessstage-4313.html#pereventprocessstage-4313](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pereventprocessstage-4313.html#pereventprocessstage-4313)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EVENT_PROCESS_STAGE_PK | EVENT_PROCESS_STAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_PROCESS_STAGE_ID | NUMBER |  | 18 | Yes | Surrogate Key for this table |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| EVENT_PROCESS_FROM_DATE | DATE |  |  | Yes | From date of the event processing range. |
| EVENT_PROCESS_TO_DATE | DATE |  |  | Yes | To date of the event processing range. |
| EVENT_DATA_COLLECTION_FLAG | VARCHAR2 | 3 |  | Yes | This column is used to identify whether the data collection is successful or not. |
| EVENT_RAISE_FLAG | VARCHAR2 | 3 |  |  | This flag is used to identify whether the Event is raised or not. |
| BULK_MODE | VARCHAR2 | 3 |  |  | This is used to identify the Bulk mode event |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_EVENT_PROCESS_STAGE_PK | Unique | FUSION_TS_TX_DATA | EVENT_PROCESS_STAGE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
