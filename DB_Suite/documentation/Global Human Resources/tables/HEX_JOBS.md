# HEX_JOBS

The table stores individual job run details.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexjobs-16936.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexjobs-16936.html)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_JOBS_PK | JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_ID | NUMBER |  |  | Yes | The column indicates a unique sequence generated value. |
| JOB_NAME | VARCHAR2 | 2000 |  |  | The column indicates the Job Name |
| JOB_TYPE | VARCHAR2 | 30 |  |  | The column indicates the type of job being triggered. |
| JOB_PROCESS_STATUS | VARCHAR2 | 30 |  |  | The column indicates the process status of the job. |
| JOB_PARAMETERS | VARCHAR2 | 4000 |  |  | The column indicates the list of parameters passed as input to the job. |
| EFFECTIVE_DATE | DATE |  |  |  | The column indicates the effective date of the job run. |
| EXPIRY_ID | NUMBER |  |  |  | The column indicates the eligibility of the record for purge. |
| ESS_REQUEST_ID | NUMBER |  |  |  | The column indicates the process request id for the job. |
| CONFIG_PARAM_GROUP_ID | NUMBER |  |  |  | The column indicates the configuration parameters grouped together. |
| OBJECT_ERROR_COUNT | NUMBER |  |  |  | The column Indicates the count of objects errored as part of the job. |
| CHUNK_RETRIES | NUMBER |  |  |  | The column indicates the number of times the chunk is retried. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTR1 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR2 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR3 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR4 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR5 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR6 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR7 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR8 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR9 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTR10 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HEX_JOBS_N1 | Non Unique | FUSION_TS_TX_DATA | JOB_TYPE, JOB_PROCESS_STATUS |
| HEX_JOBS_N2 | Non Unique | FUSION_TS_TX_DATA | ESS_REQUEST_ID |
| HEX_JOBS_N3 | Non Unique | FUSION_TS_TX_DATA | EXPIRY_ID |
| HEX_JOBS_PK | Unique | FUSION_TS_TX_DATA | JOB_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
