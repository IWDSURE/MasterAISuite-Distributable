# HRC_LOADER_BATCH_HEADER

The header table is the top level table for a batch data load.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloaderbatchheader-6325.html#hrcloaderbatchheader-6325](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloaderbatchheader-6325.html#hrcloaderbatchheader-6325)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_LOADER_BATCH_HEADER_PK | LOADER_BATCH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOADER_BATCH_ID | NUMBER |  | 18 | Yes | LOADER_BATCH_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LOADER_AM_NAME | VARCHAR2 | 200 |  |  | LOADER_AM_NAME |
| LOADER_AM_CONFIG_NAME | VARCHAR2 | 200 |  |  | LOADER_AM_CONFIG_NAME |
| BATCH_STATUS | VARCHAR2 | 200 |  |  | Status of the batch load job. |
| BATCH_STATUS_TEXT | VARCHAR2 | 2000 |  |  | Status description for the batch load job. |
| VALIDATE_ONLY | VARCHAR2 | 1 |  |  | If true, then only validate data and no data base commit. |
| NUM_THREADS | NUMBER |  | 5 |  | Number of threads to process job. |
| CURRENT_CHUNK_NUM | NUMBER |  | 10 |  | Current chunk being processed if running in parallel. |
| TOTAL_NUM_CHUNKS | NUMBER |  | 10 |  | Total number of discrete chunks of data in the batch lines table. |
| USER_ID | VARCHAR2 | 32 |  |  | User id of the user to start the batch load job. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| NOTIFICATION_CLASS | VARCHAR2 | 2000 |  |  | Full path name for the class used to notify pre and post processing for this batch. |
| UPDATE_REQUEST_ID | NUMBER |  | 18 |  | When defining the column, the DB column comments should be "Enterprise Service Scheduler: indicates the request ID of the job that last updated the row." |
| XFER_JOB_ID | NUMBER |  | 18 |  | Holds the file transfer identifier if the header was created from due to file processing. |
| BATCH_NAME | VARCHAR2 | 300 |  |  | Batch Name |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_LOADER_BATCH_HEADER_N1 | Non Unique | Default | REQUEST_ID |
| HRC_LOADER_BATCH_HEADER_N2 | Non Unique | Default | UPDATE_REQUEST_ID |
| HRC_LOADER_BATCH_HEADER_N3 | Non Unique | Default | XFER_JOB_ID |
| HRC_LOADER_BATCH_HEADER_N4 | Non Unique | Default | BATCH_NAME, ENTERPRISE_ID |
| HRC_LOADER_BATCH_HEADER_PK | Unique | Default | LOADER_BATCH_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
