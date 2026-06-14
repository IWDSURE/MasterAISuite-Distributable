# HRY_EVENT_EXT_RUNS

Updated details of the persons processed in the event enabled extracts.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryeventextruns-26081.html#hryeventextruns-26081](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryeventextruns-26081.html#hryeventextruns-26081)

## Primary Key

| Name | Columns |
|------|----------|
| hry_event_ext_runs_PK | HRY_EVENT_EXT_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HRY_EVENT_EXT_RUN_ID | NUMBER |  | 18 | Yes | Event Extract Run ID. Primary Key of the table. |
| HRY_EVENT_CATEGORY_ID | NUMBER |  | 18 |  | Event Category ID. Reference ID mapping column to HRY_EVENT_CATEGOTIES table. |
| LEGISLATIVE_PARAMETERS | VARCHAR2 | 4000 | 4000 |  | Legislative Parameters required for the extract to be submitted. |
| PARAM_START_DATE | DATE |  |  |  | Start Date passed in the ESS Job Parameter Section. |
| PARAM_END_DATE | DATE |  |  |  | End Date passed in the ESS Job Parameter Section. |
| REPORT_CATEGORY_ID | NUMBER |  | 18 |  | Report Category Id for Archive Write job submission. |
| PAYROLL_ID | NUMBER |  | 18 |  | Payroll Id Value for Archive Write job submission. |
| SOURCE_RUN_ID | NUMBER |  | 18 |  | Can be any ID value. FLOW_INSTANCE_ID for Archive Write job. |
| SOURCE_RUN_TYPE | VARCHAR2 | 60 |  |  | Source Run Type value. FLOW_INSTANCE is the source run type for Instance ID as source run id. |
| LATEST_RUN | VARCHAR2 | 1 |  |  | This indicates if a event enabled person is picked up in the Latest Run or not. |
| EVENT_FETCH_TIME | TIMESTAMP |  |  |  | What time is the event fetched. |
| PREVIOUS_EVENT_FETCH_TIME | TIMESTAMP |  |  |  | What time is the Previous Event Fetched. |
| STATUS | VARCHAR2 | 30 |  |  | Describes the status of the Event. |
| STATUS_MSG | VARCHAR2 | 4000 |  |  | Detailed Message of the Status. |
| ROWS_PROCESSED | NUMBER |  | 18 |  | Number of the rows processed in a particular run. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| EXT_DEFINITION_ID | NUMBER |  | 18 |  | Extract Definition ID Value for which event is processed. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_EVENT_EXT_RUNS_N1 | Non Unique | hry_event_ext_runs_N1 | HRY_EVENT_CATEGORY_ID, EXT_DEFINITION_ID, LATEST_RUN |
| HRY_EVENT_EXT_RUNS_N2 | Non Unique | hry_event_ext_runs_N2 | STATUS |
| HRY_EVENT_EXT_RUNS_N3 | Non Unique | hry_event_ext_runs_N3 | SOURCE_RUN_ID |
| HRY_EVENT_EXT_RUNS_N4 | Non Unique | hry_event_ext_runs_N4 | EXT_DEFINITION_ID, LATEST_RUN |
| HRY_EVENT_EXT_RUNS_PK | Unique | Default | HRY_EVENT_EXT_RUN_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
