# HWM_TM_REC_GRP_SUM

Summarized information of complex time record and time record groups.  For example, highlights the total number of hours associated to a time card time record group.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecgrpsum-24448.html#hwmtmrecgrpsum-24448](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecgrpsum-24448.html#hwmtmrecgrpsum-24448)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_REC_GRP_SUM_PK | TM_REC_GRP_ID, TM_REC_GRP_VERSION |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REC_GRP_ID | NUMBER |  | 18 | Yes | Time Record Group Id |
| TM_REC_GRP_VERSION | NUMBER |  | 9 | Yes | Time Record Group version |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| GRP_TYPE_ID | NUMBER |  | 18 |  | GRP_TYP_ID |
| STATUS | VARCHAR2 | 30 |  |  | Time Record Group Status |
| START_TIME | TIMESTAMP |  |  |  | Start time of the time record group |
| STOP_TIME | TIMESTAMP |  |  |  | Stop time of Time Record Group |
| RESOURCE_ID | NUMBER |  | 18 |  | Resource for whom time was entered |
| RECORDED_HOURS | NUMBER |  |  |  | Total Hours recorded for the Time Record Group |
| HAS_REASONS | VARCHAR2 | 30 |  |  | HAS_REASONS |
| SUBMISSION_DATE | TIMESTAMP |  |  |  | Date when the time record group status was changed to submitted |
| ABSENCE_HOURS | NUMBER |  |  |  | ABSENCE_HOURS |
| ABSENCE_DAYS | NUMBER |  |  |  | Total numer of Absences with Days UOM |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ERROR_SEVERITY | VARCHAR2 | 30 |  |  | Message error level |
| PROCESS_REQUEST_ID | NUMBER |  | 18 |  | Process request id |
| OFF_CYCLE | VARCHAR2 | 150 |  |  | Off cycle status |
| PAYROLL_TRANSFER | VARCHAR2 | 30 |  |  | Payroll Transfer Status |
| PAYROLL_PROCESSING | VARCHAR2 | 30 |  |  | Payroll Processing Status |
| PROJECT_TRANSFER | VARCHAR2 | 30 |  |  | Project Costing Transfer Status |
| SUBRESOURCE_ID | VARCHAR2 | 18 |  |  | Assignment Id of the person |
| SCHEDULED_HOURS | NUMBER |  |  |  | Total Scheduled hours for the time card period |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_REC_GRP_SUM_N1 | Non Unique | Default | RESOURCE_ID, GRP_TYPE_ID, START_TIME, STOP_TIME, STATUS |
| HWM_TM_REC_GRP_SUM_N2 | Non Unique | Default | GRP_TYPE_ID, TRUNC("START_TIME"), TRUNC("STOP_TIME"), RESOURCE_ID, STATUS |
| HWM_TM_REC_GRP_SUM_N3 | Non Unique | Default | GRP_TYPE_ID, STATUS, TRUNC("START_TIME"), TRUNC("STOP_TIME"), ENTERPRISE_ID, RESOURCE_ID |
| HWM_TM_REC_GRP_SUM_PK | Unique | "Default" | TM_REC_GRP_ID, TM_REC_GRP_VERSION |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
