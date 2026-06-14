# HRY_INTERFACE_RUNS

Data to be stored for jobs run with a specific job type.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryinterfaceruns-7796.html#hryinterfaceruns-7796](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryinterfaceruns-7796.html#hryinterfaceruns-7796)

## Primary Key

| Name | Columns |
|------|----------|
| hry_interface_runs_PK | INTERFACE_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERFACE_RUN_ID | NUMBER |  | 18 | Yes | The column indicates a unique sequence generated value. |
| RUN_ID | NUMBER |  | 18 |  | The column indicates the job id value of hex_jobs table. |
| JOB_TYPE | VARCHAR2 | 80 |  |  | The column indicates the type of job being triggered. |
| JOB_TYPE_ID | VARCHAR2 | 80 |  |  | The column indicates the id value for type of job being triggered. |
| STATUS | VARCHAR2 | 30 |  |  | The column indicates the process status of the job. |
| PROCESS_TYPE | VARCHAR2 | 150 |  |  | The column indicates the type of process being triggered for a particular job type. |
| EXPIRY_ID | NUMBER |  |  |  | The column indicates the eligibility of the record for purge. |
| DATA_EXPIRY_ID | NUMBER |  |  |  | The column indicates the eligibility of the record for purge for hry_interface_data table. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hry_interface_runs_N1 | Non Unique | FUSION_TS_TX_DATA | ATTRIBUTE_CATEGORY, ATTRIBUTE1 |
| hry_interface_runs_N2 | Non Unique | FUSION_TS_TX_DATA | EXPIRY_ID |
| hry_interface_runs_N3 | Non Unique | FUSION_TS_TX_DATA | PROCESS_TYPE, STATUS |
| hry_interface_runs_N4 | Non Unique | FUSION_TS_TX_DATA | JOB_TYPE, JOB_TYPE_ID |
| hry_interface_runs_PK | Unique | FUSION_TS_TX_DATA | INTERFACE_RUN_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
