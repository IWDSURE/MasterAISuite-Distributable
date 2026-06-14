# CMP_TCS_REPORT_DETAILS

Table that stores the batch process run details.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsreportdetails-18323.html#cmptcsreportdetails-18323](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsreportdetails-18323.html#cmptcsreportdetails-18323)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_REPORT_DETAILS_PK | REPORT_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REPORT_DETAIL_ID | NUMBER |  | 18 | Yes | REPORT_DETAIL_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| BENEFIT_ACTION_ID | NUMBER |  | 18 | Yes | BENEFIT_ACTION_ID |
| PERD_RUN_ID | NUMBER |  | 18 |  | PERD_RUN_ID |
| PER_PERD_STMT_ID | NUMBER |  | 18 |  | PER_PERD_STMT_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| PERSON_NUMBER | VARCHAR2 | 30 |  |  | PERSON_NUMBER |
| WORKER_NUMBER | VARCHAR2 | 30 |  |  | WORKER_NUMBER |
| JOB_ID | NUMBER |  | 18 |  | JOB_ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| ERR_CODE | VARCHAR2 | 30 |  |  | ERR_CODE |
| ERR_MESSAGE | VARCHAR2 | 600 |  |  | ERR_MESSAGE |
| STAT_CD | VARCHAR2 | 30 |  |  | STAT_CD |
| END_DATE | DATE |  |  |  | END_DATE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_REPORT_DETAILS_N1 | Non Unique | Default | REQUEST_ID |
| CMP_TCS_REPORT_DETAILS_UK1 | Unique | Default | REPORT_DETAIL_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
