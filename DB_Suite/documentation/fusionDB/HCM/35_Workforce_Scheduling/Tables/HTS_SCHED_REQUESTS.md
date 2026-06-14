# HTS_SCHED_REQUESTS

Table to store schedule requests

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_INTERFACE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedrequests-8025.html#htsschedrequests-8025](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedrequests-8025.html#htsschedrequests-8025)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_REQUESTS_PK | SCHED_REQUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_REQUEST_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| SCHEDULE_REQUEST_NUMBER | VARCHAR2 | 120 |  |  | Identifier of the request as specified by the exporter |
| REQUEST_TIME | TIMESTAMP |  |  |  | Submission time of the request |
| REQUEST_TIME_STR | VARCHAR2 | 80 |  |  | REQUEST_TIME_STR |
| REQUEST_SOURCE | VARCHAR2 | 30 |  |  | Exporter code or name of the request sender |
| STATUS_IMP | NUMBER |  | 2 |  | Status for the import phase |
| STATUS_INT | NUMBER |  | 2 |  | Status for the internalization phase |
| SCHED_UNIT_ID | NUMBER |  | 18 |  | Stores the resolved schedule unit identifier |
| IMPORT_MODE | VARCHAR2 | 20 |  |  | Stores the import mode, such as FULL or UPDATE |
| IMPORT_START_DATE | DATE |  |  |  | Stores the import period start date for the range |
| IMPORT_END_DATE | DATE |  |  |  | Stores the import period end date for the range |
| GROUP_ID | NUMBER |  | 18 |  | Group identifier. A group contains one or several schedule events and is the partioning unit. Used by the Process Imported Shifts process. |
| PROCESS_ID | NUMBER |  | 9 |  | Identifier for the processed Process Imported Shifts process or the process that's processing the schedule event. |
| CHILD_PROCESS_ID | NUMBER |  | 9 |  | Identifier for the child Process Imported Shifts process that processed the schedule event. |
| PUBLISH_FLAG | VARCHAR2 | 1 |  |  | Indicates whether to publish the schedules |
| VALIDATION_FLAG | VARCHAR2 | 1 |  |  | Indicates whether to validate the schedules |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_REQUESTS_N1 | Non Unique | Default | STATUS_INT, SCHED_UNIT_ID |
| HTS_SCHED_REQUESTS_N2 | Non Unique | Default | GROUP_ID, STATUS_INT |
| HTS_SCHED_REQUESTS_PK | Unique | FUSION_TS_INTERFACE | SCHED_REQUEST_ID |
| HTS_SCHED_REQUESTS_U1 | Unique | FUSION_TS_INTERFACE | SCHEDULE_REQUEST_NUMBER |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
