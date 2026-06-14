# PAY_STATS_FLOW_ACTIONS

PAY_STATS_FLOW_ACTIONS table created for payroll flows subject area

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paystatsflowactions-20553.html#paystatsflowactions-20553](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paystatsflowactions-20553.html#paystatsflowactions-20553)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LDG_ID | NUMBER |  | 18 |  | LDG_ID |
| FI_TASK_STATUS | VARCHAR2 | 20 |  |  | FI_TASK_STATUS |
| ROLLBACK_ERROR_FLAG | VARCHAR2 | 1 |  |  | ROLLBACK_ERROR_FLAG |
| ACTIVE_FLAG | VARCHAR2 | 2 |  |  | ACTIVE_FLAG |
| STAT_RB_TOTAL | NUMBER |  |  |  | STAT_RB_TOTAL |
| RB_SUB_STATUS | VARCHAR2 | 30 |  |  | RB_SUB_STATUS |
| ERROR_SUB_STATUS | VARCHAR2 | 30 |  |  | ERROR_SUB_STATUS |
| MFR_SUB_STATUS | VARCHAR2 | 30 |  |  | MFR_SUB_STATUS |
| STAT_MFR_TOTAL | NUMBER |  |  |  | STAT_MFR_TOTAL |
| FLOW_NAME | VARCHAR2 | 200 |  |  | FLOW_NAME |
| FLOW_PATTERN_ID | NUMBER |  | 18 | Yes | FLOW_PATTERN_ID |
| FLOW_TATUS | VARCHAR2 | 30 |  |  | FLOW_TATUS |
| FLOW_SUBMITTED_ON | TIMESTAMP |  |  | Yes | FLOW_SUBMITTED_ON |
| FLOW_SUBMITTED_BY | VARCHAR2 | 64 |  | Yes | FLOW_SUBMITTED_BY |
| FLOW_GRP_STATUS | VARCHAR2 | 30 |  |  | FLOW_GRP_STATUS |
| FLOW_SUB_STATUS | VARCHAR2 | 30 |  |  | FLOW_SUB_STATUS |
| TASK_ID | NUMBER |  | 18 | Yes | TASK_ID |
| FLOW_TASK_ID | NUMBER |  | 18 | Yes | FLOW_TASK_ID |
| CHECKLIST_ID | NUMBER |  | 18 | Yes | CHECKLIST_ID |
| TASK_GRP_STATUS | VARCHAR2 | 30 |  |  | TASK_GRP_STATUS |
| TASK_SUB_STATUS | VARCHAR2 | 30 |  |  | TASK_SUB_STATUS |
| ACTION_ID | NUMBER |  | 18 |  | ACTION_ID |
| TASK_STATUS | VARCHAR2 | 30 |  |  | TASK_STATUS |
| TASK_SUBMITTED_ON | TIMESTAMP |  |  | Yes | TASK_SUBMITTED_ON |
| TASK_SUBMITTED_BY | VARCHAR2 | 64 |  | Yes | TASK_SUBMITTED_BY |
| FLOW_INSTANCE_ID | NUMBER |  | 18 | Yes | FLOW_INSTANCE_ID |
| FLOW_TASK_INSTANCE_ID | NUMBER |  | 18 | Yes | FLOW_TASK_INSTANCE_ID |
| TI_REQUEST_ID | NUMBER |  |  |  | TI_REQUEST_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| ESS_ID | NUMBER |  | 18 |  | ESS_ID |
| PARENT_ESS_ID | NUMBER |  | 18 | Yes | PARENT_ESS_ID |
| ESS_STATUS_CODE | VARCHAR2 | 11 |  |  | ESS_STATUS_CODE |
| PROCESS_STATUS_CODE | VARCHAR2 | 120 |  |  | PROCESS_STATUS_CODE |
| PROCESS_DATE | DATE |  |  |  | PROCESS_DATE |
| PAYROLL_ID | NUMBER |  |  |  | PAYROLL_ID |
| CONSOLIDATION_SET_ID | NUMBER |  |  |  | CONSOLIDATION_SET_ID |
| BATCH_ID | NUMBER |  |  |  | BATCH_ID |
| BATCH_NAME | VARCHAR2 | 2000 |  |  | BATCH_NAME |
| FILE_NAME | VARCHAR2 | 2000 |  |  | FILE_NAME |
| PSU_ID | NUMBER |  |  |  | PSU_ID |
| TRU_ID | NUMBER |  |  |  | TRU_ID |
| LOCATION_ID | NUMBER |  |  |  | LOCATION_ID |
| LEGAL_EMPLOYER_ID | NUMBER |  |  |  | LEGAL_EMPLOYER_ID |
| ORGANIZATION_ID | NUMBER |  |  |  | ORGANIZATION_ID |
| DATA_SET_ID | NUMBER |  |  |  | DATA_SET_ID |
| ACTION_PARAM_GROUP_ID | NUMBER |  |  |  | ACTION_PARAM_GROUP_ID |
| LOGGING_LEVEL | VARCHAR2 | 80 |  |  | LOGGING_LEVEL |
| PAYROLL_ACTION_ID | NUMBER |  |  |  | PAYROLL_ACTION_ID |
| TIME_TAKEN_MINS | NUMBER |  |  |  | TIME_TAKEN_MINS |
| STATISTIC_GROUP_ID | NUMBER |  | 18 |  | STATISTIC_GROUP_ID |
| ESS_REQUESTS_COUNT | NUMBER |  |  |  | ESS_REQUESTS_COUNT |
| TOTAL_COMPLETED | NUMBER |  |  |  | TOTAL_COMPLETED |
| UNPROCESSED | NUMBER |  |  |  | UNPROCESSED |
| ARCHIVED_INFORMATION | NUMBER |  |  |  | ARCHIVED_INFORMATION |
| RETO_ACTION_COUNT | NUMBER |  |  |  | RETO_ACTION_COUNT |
| RR_COUNT | NUMBER |  |  |  | RR_COUNT |
| RRV_COUNT | NUMBER |  |  |  | RRV_COUNT |
| STAT_ERROR_TOTAL | NUMBER |  |  |  | STAT_ERROR_TOTAL |
| ERROR_MESSAGE_COUNT | NUMBER |  |  |  | ERROR_MESSAGE_COUNT |
| TIME_TAKEN_SINGLE_MINS | NUMBER |  |  |  | TIME_TAKEN_SINGLE_MINS |
| TIME_TAKEN_AVG_MINS | NUMBER |  |  |  | TIME_TAKEN_AVG_MINS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_STATS_FLOW_ACTIONS_N1 | Non Unique | Default | TASK_SUBMITTED_ON, TASK_SUBMITTED_BY |
| PAY_STATS_FLOW_ACTIONS_N2 | Non Unique | Default | PARENT_ESS_ID |
| PAY_STATS_FLOW_ACTIONS_N3 | Non Unique | Default | FLOW_INSTANCE_ID, FLOW_TASK_INSTANCE_ID |
| PAY_STATS_FLOW_ACTIONS_N4 | Non Unique | Default | LDG_ID, FLOW_PATTERN_ID, TASK_ID, PROCESS_DATE, PAYROLL_ID, CONSOLIDATION_SET_ID |
| PAY_STATS_FLOW_ACTIONS_U1 | Unique | Default | REQUEST_ID |
| PAY_STATS_FLOW_ACTIONS_N5 | Non Unique | Default | CREATION_DATE |
| PAY_STATS_FLOW_ACTIONS_N6 | Non Unique | Default | FLOW_TASK_INSTANCE_ID |
| PAY_STATS_FLOW_ACTIONS_N7 | Non Unique | Default | TI_REQUEST_ID |
| PAY_STATS_FLOW_ACTIONS_N8 | Non Unique | Default | PAYROLL_ACTION_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
