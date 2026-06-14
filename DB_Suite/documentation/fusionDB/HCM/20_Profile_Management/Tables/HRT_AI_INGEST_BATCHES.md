# HRT_AI_INGEST_BATCHES

The batch information for ingest runs.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtaiingestbatches-22967.html#hrtaiingestbatches-22967](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtaiingestbatches-22967.html#hrtaiingestbatches-22967)

## Primary Key

| Name | Columns |
|------|----------|
| hrt_ai_ingest_batches_PK | BATCH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_ID | NUMBER |  | 18 | Yes | Primary key, system generated |
| INGEST_RUN_ID | NUMBER |  | 18 |  | Foreign Key to hrt_ai_ingest_run |
| ERROR_MESSAGE_DETAIL | CLOB |  |  |  | Error Message of the batch process |
| BATCH_STATUS | VARCHAR2 | 64 |  | Yes | Status Code of the batch.  Possible values are  'UNPROCESSED', 'ALLOCATED', 'FAIL' or 'SUCCESS'. |
| INGEST_FILE_NAME | VARCHAR2 | 300 |  |  | Ingest file name which has json string for a batch of profiles |
| HTTP_STATUS_CODE | VARCHAR2 | 20 |  |  | Status received after each batch of profile data is pushed to AI rest service |
| CHILD_REQUEST_ID | NUMBER |  | 18 |  | Child ESS job request id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hrt_ai_ingest_batches_U1 | Unique | Default | BATCH_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
