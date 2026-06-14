# HEX_RUNS

The table stores the individual run details for each extract.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexruns-27061.html#hexruns-27061](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexruns-27061.html#hexruns-27061)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_RUNS_PK | EXT_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXT_RUN_ID | NUMBER |  |  | Yes | The column contains the corresponding JOB_ID value from the table HEX_JOBS. |
| OUTPUT_STORE | VARCHAR2 | 30 |  |  | The column stores the name of the output table which stores the final xml |
| OUTPUT_FRAGMENT_CNT | NUMBER |  | 18 |  | This column contains the number of output fragments generated |
| RUN_NAME | VARCHAR2 | 2000 |  |  | This column contains the Run Name |
| EXT_DEFINITION_ID | NUMBER |  | 18 |  | This column contains the Extract definition ID |
| FLOW_TASK_INSTANCE_ID | NUMBER |  | 18 |  | This column contains the Flow Task Instance ID |
| FLOW_INSTANCE_ID | NUMBER |  |  |  | The column indicates the current flow instance id. |
| PAY_REQUEST_ID | NUMBER |  |  |  | The column indicates the corresponding request id of the flow instance. |
| EXT_PARAMETERS | VARCHAR2 | 4000 |  |  | The column indicates the parameters used by the run of the extract. |
| EXT_PARAMETERS_EXTEND | VARCHAR2 | 4000 |  |  | The column indicates the extended parameters used by the run of the extract. |
| REPORT_CATEGORY_ID | NUMBER |  |  |  | The column indicates the report category id for the current run. |
| EXPIRY_ID | NUMBER |  |  |  | The column indicates the eligibility of the record for purge. The date has to be entered in the format YYYYMMDD. |
| PROCESS_STATUS | VARCHAR2 | 30 |  |  | The column indicates the valid status for the current run. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  |  |  | The column indicates the legislative data group referred to in the current run. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LEGISLATION_CODE | VARCHAR2 | 20 |  |  | The column indicates the legislation code derived from the Legal Entity. |
| ESS_REQUEST_ID | NUMBER |  |  |  | The column indicates the request ID of the Flow Request. |
| CONFIG_PARAM_GROUP_ID | NUMBER |  |  |  | The column indicates the configuration parameter group id. |
| START_DATE | TIMESTAMP |  |  |  | The column indicates the start date of the current run. |
| END_DATE | TIMESTAMP |  |  |  | The column indicates the end date of the current run. |
| EFFECTIVE_DATE | DATE |  |  |  | The column indicates the effective date of the current run. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
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

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HEX_RUNS_N1 | Non Unique | Default | PAY_REQUEST_ID |  |
| HEX_RUNS_N2 | Non Unique | Default | REPORT_CATEGORY_ID, PROCESS_STATUS |  |
| HEX_RUNS_N3 | Non Unique | Default | EXPIRY_ID |  |
| HEX_RUNS_N4 | Non Unique | Default | ESS_REQUEST_ID |  |
| HEX_RUNS_N5 | Non Unique | Default | ATTRIBUTE_CATEGORY, ATTRIBUTE1 | Obsolete |
| HEX_RUNS_N6 | Non Unique | Default | FLOW_INSTANCE_ID |  |
| HEX_RUNS_N7 | Non Unique | Default | FLOW_TASK_INSTANCE_ID |  |
| HEX_RUNS_N8 | Non Unique | Default | EXT_DEFINITION_ID |  |
| HEX_RUNS_PK | Unique | Default | EXT_RUN_ID |  |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
