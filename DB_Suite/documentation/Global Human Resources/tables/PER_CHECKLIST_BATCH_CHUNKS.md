# PER_CHECKLIST_BATCH_CHUNKS

This table stores chunks of a batch action.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistbatchchunks-16102.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistbatchchunks-16102.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_BATCH_CHUNKS_PK | BATCH_CHUNK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_CHUNK_ID | NUMBER |  | 18 | Yes | BATCH_CHUNK_ID |
| BATCH_ACTION_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_CHECKLIST_BATCH_ACTIONS |
| CHUNK_STATUS | VARCHAR2 | 30 |  | Yes | Lookup: ORA_PER_CHK_BATCH_CHUNK_STATUS |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| PROCESS_START_TIME | TIMESTAMP |  |  |  | Start time populated when status changed to PROCESSING |
| PROCESS_END_TIME | TIMESTAMP |  |  |  | End time populated when status changed to COMPLETE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHECKLIST_BATCH_CHUNKS_PK | Unique | Default | BATCH_CHUNK_ID |
| PER_CHECKLIST_BATCH_CHUNK_N1 | Non Unique | Default | BATCH_ACTION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
