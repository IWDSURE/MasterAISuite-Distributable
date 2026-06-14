# HRT_ESS_CHUNKS

This table is used to hold details about chunks registered for profile keyword crawling ess job.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtesschunks-19969.html#hrtesschunks-19969](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtesschunks-19969.html#hrtesschunks-19969)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_ESS_CHUNKS_PK | CHUNK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHUNK_ID | NUMBER |  | 18 | Yes | System generated primary key |
| START_RECORD_ID | NUMBER |  | 18 | Yes | Start Profile Id |
| END_RECORD_ID | NUMBER |  | 18 | Yes | End Profile Id |
| THREAD_REQUEST_ID | NUMBER |  | 10 | Yes | Enterprise Service Scheduler: indicates the request ID of the child job that created the row. |
| PARENT_REQUEST_ID | NUMBER |  | 10 | Yes | Enterprise Service Scheduler: indicates the request ID of the Parent job that created the row |
| CHUNK_STATUS | VARCHAR2 | 64 |  | Yes | Status Code if the chunk is 'UNPROCESSED', 'ALLOCATED' or 'COMPLETED' |
| PROFILE_USAGE_CODE | VARCHAR2 | 32 |  | Yes | Usage code which identifies it is used for Person profile or Model profile |
| CHUNK_TOTAL_LINE_COUNT | NUMBER |  | 18 |  | Total records present in the chunk |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_ESS_CHUNKS_N1 | Non Unique | Default | PARENT_REQUEST_ID, THREAD_REQUEST_ID, CHUNK_STATUS |
| HRT_ESS_CHUNKS_PK | Unique | Default | CHUNK_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
