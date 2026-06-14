# HEX_JOB_PREPROCESS_RANGE

The table stores the status of preprocess chunk progress.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexjobpreprocessrange-4180.html#hexjobpreprocessrange-4180](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexjobpreprocessrange-4180.html#hexjobpreprocessrange-4180)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_JOB_PREPROCESS_RANGE_PK | PREPROCESS_JOB_ID, CHUNK_NUMBER |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PREPROCESS_JOB_ID | NUMBER |  |  | Yes | The column indicates the JOB_ID from the HEX_JOBS table. |
| PARENT_JOB_ID | NUMBER |  |  | Yes | The column indicates the parent job id for the current job. |
| CHUNK_PROCESS_STATUS | VARCHAR2 | 30 |  |  | The column indicates the current processing status of the chunk. |
| CHUNK_NUMBER | NUMBER |  |  | Yes | The column indicates the number of the chunk being processed. |
| CHUNK_THREAD_NUMBER | NUMBER |  |  |  | The column indicates the thread number processing the current chunk. |
| THREAD_ESS_ID | NUMBER |  |  |  | The column indicates the process request id for the thread. |
| SEQ_NO | NUMBER |  |  |  | The column indicates the unique sequence number associated with each chunk. |
| START_VALUE | NUMBER |  |  |  | The column indicates the start value within the range. |
| END_VALUE | NUMBER |  |  |  | The column indicates the end value within the range. |
| PROCESSING_TYPE | VARCHAR2 | 15 |  |  | The column indicates the processing type. Valid values are PREPROCESS, PROCESS and POSTPROCESS. |
| GROUP_TAG_VALUE | VARCHAR2 | 4000 |  |  | The column indicates the value reference for the parent child link. |
| GROUP_TAG_NUMBER | NUMBER |  |  |  | The column indicates the number reference for the parent child link. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HEX_JOB_PREPROCESS_RANGE_N1 | Non Unique | FUSION_TS_TX_DATA | PREPROCESS_JOB_ID, CHUNK_PROCESS_STATUS |
| HEX_JOB_PREPROCESS_RANGE_N2 | Non Unique | FUSION_TS_TX_DATA | PREPROCESS_JOB_ID, SEQ_NO |
| HEX_JOB_PREPROCESS_RANGE_N3 | Non Unique | FUSION_TS_TX_DATA | PREPROCESS_JOB_ID, GROUP_TAG_VALUE |
| HEX_JOB_PREPROCESS_RANGE_PK | Unique | FUSION_TS_TX_DATA | PREPROCESS_JOB_ID, CHUNK_NUMBER |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
