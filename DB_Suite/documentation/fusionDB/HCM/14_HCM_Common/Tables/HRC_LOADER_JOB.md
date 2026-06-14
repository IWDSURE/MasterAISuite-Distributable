# HRC_LOADER_JOB

This table contains information about individual jobs within a batch.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloaderjob-7884.html#hrcloaderjob-7884](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloaderjob-7884.html#hrcloaderjob-7884)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_LOADER_JOB_PK | JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_ID | NUMBER |  | 18 | Yes | JOB_ID |
| LOADER_BATCH_ID | NUMBER |  | 18 | Yes | LOADER_BATCH_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| JOB_SEQUENCE_NUM | NUMBER |  | 5 |  | This column tells the Loader the order in which to process the Job rows (lowest to highest). |
| JOB_STATUS | VARCHAR2 | 200 |  |  | JOB_STATUS |
| JOB_STATUS_TEXT | VARCHAR2 | 2000 |  |  | JOB_STATUS_TEXT |
| CURRENT_RUN_ID | NUMBER |  | 5 |  | CURRENT_RUN_ID |
| READER_AM_NAME | VARCHAR2 | 200 |  |  | READER_AM_NAME |
| WRITER_AM_NAME | VARCHAR2 | 200 |  |  | WRITER_AM_NAME |
| SOURCE_AM_NAME | VARCHAR2 | 200 |  |  | SOURCE_AM_NAME |
| SOURCE_VO_NAME | VARCHAR2 | 200 |  |  | SOURCE_VO_NAME |
| FILTER_CLAUSE | VARCHAR2 | 2000 |  |  | FILTER_CLAUSE |
| BATCH_SIZE | NUMBER |  | 5 |  | BATCH_SIZE |
| CURRENT_ROW_COUNT | NUMBER |  | 10 |  | CURRENT_ROW_COUNT |
| TOTAL_ROW_COUNT | NUMBER |  | 10 |  | TOTAL_ROW_COUNT |
| MAX_ERROR_COUNT | NUMBER |  | 5 |  | MAX_ERROR_COUNT |
| METADATA_ID | NUMBER |  | 18 |  | When defining the column, the DB column comments should be "Optional column to hold the corresponding LBO metadata identifier." |
| EXECUTIONS | NUMBER |  | 9 |  | Executions |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| RETRY | VARCHAR2 | 30 |  |  | Retry |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_LOADER_JOB_N1 | Non Unique | Default | METADATA_ID |
| HRC_LOADER_JOB_N2 | Non Unique | Default | LOADER_BATCH_ID |
| HRC_LOADER_JOB_PK | Unique | Default | JOB_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
