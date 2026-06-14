# HRY_EVENT_FETCH_RUNS

Event Fetch details data for whom the archive job to be submitted.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryeventfetchruns-6938.html#hryeventfetchruns-6938](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryeventfetchruns-6938.html#hryeventfetchruns-6938)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_EVENT_FETCH_RUNS_PK | HRY_EVENT_FETCH_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HRY_EVENT_FETCH_RUN_ID | NUMBER |  | 18 | Yes | Event Fetch Run ID. Primary Key of the table. |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| LATEST_RUN | VARCHAR2 | 1 |  |  | This indicates if a event enabled person is picked up in the Latest Run or not. |
| PARAM_PAYROLL_ID | NUMBER |  | 18 |  | Payroll Id Value for Archive Write job submission. |
| PARAM_START_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| PARAM_EFFECTIVE_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PARAM_PROCESS_CONFIG_GROUP | NUMBER |  | 18 |  | Process Configuration Group Value for Archive Write job submission. |
| FLOW_INSTANCE_ID | NUMBER |  | 18 |  | Can be any ID value. FLOW_INSTANCE_ID for Archive Write job. |
| EVENT_FETCH_TIME | TIMESTAMP |  |  |  | Event Fetch Time for Payroll Connect. |
| JOB_START_TIME | TIMESTAMP |  |  |  | Start Time of the ESS Job submitted. |
| JOB_END_TIME | TIMESTAMP |  |  |  | End Time of the ESS Job submitted. |
| STATUS | VARCHAR2 | 30 |  |  | Describes the status of the Job. |
| STATUS_DETAILS | VARCHAR2 | 4000 |  |  | Detailed Message of the Status. |
| EVENTS_FETCH_COUNT | NUMBER |  | 18 |  | Number of the rows processed in a particular run. |
| PURGE_DATE | DATE |  |  | Yes | Date to be Purged for Payroll Connect. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_EVENT_FETCH_RUNS_N1 | Non Unique | Default | PARAM_PAYROLL_ID, LATEST_RUN |
| HRY_EVENT_FETCH_RUNS_PK | Unique | Default | HRY_EVENT_FETCH_RUN_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
