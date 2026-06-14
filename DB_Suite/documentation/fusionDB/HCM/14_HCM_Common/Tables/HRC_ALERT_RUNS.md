# HRC_ALERT_RUNS

Contains alert run data with totals no of success, error and warning counts.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertruns-6246.html#hrcalertruns-6246](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertruns-6246.html#hrcalertruns-6246)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERT_RUNS_PK | RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PARENT_RUN_ID | NUMBER |  | 18 |  | Run Identifier of Parent. Foreign Key to HRC_ALERTS_RUNS.RUN_ID |
| ALERT_ID | NUMBER |  | 18 | Yes | Alert Identifier. Foreign Key to HRC_ALERTS_B.ALERT_ID |
| RUN_START | TIMESTAMP |  |  | Yes | Specifies the start of the run activity. |
| RUN_END | TIMESTAMP |  |  |  | Specifies the end of the run activity. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| STATUS | VARCHAR2 | 30 |  | Yes | Determines the status of the activity run. Valid values are defined in lookup of HRC_ALERT_RUN_STATUS. |
| USER_IDENTIFIER | VARCHAR2 | 2000 |  |  | User Identifier. |
| RUN_PHASE | VARCHAR2 | 30 |  |  | Run Phase of child job |
| PARAMETERS | CLOB |  |  |  | Contains parameters values for the run. |
| RUN_OPTIONS | CLOB |  |  |  | Contains config run option values for the run. |
| LOG | CLOB |  |  |  | Contains a log for the activity run. |
| TOTAL_ALERT_INSTANCES | NUMBER |  | 12 |  | The total number of Alert Instances raised |
| TOTAL_MESSAGES | NUMBER |  | 12 |  | The total number of messages created for the run. TOTAL_SUCCESS_MESSAGES + TOTAL_WARNING_MESSAGES + TOTAL_ERROR_MESSAGES |
| TOTAL_WARNINGS | NUMBER |  | 18 |  | Total number of warnings. |
| TOTAL_ERRORS | NUMBER |  | 12 |  | The total number or errors for the run. |
| TOTAL_KEEPS | NUMBER |  | 18 |  | Total number of keeps. |
| TOTAL_SUCCESS_MESSAGES | NUMBER |  | 12 |  | Total number of successful messages. |
| TOTAL_WARNING_MESSAGES | NUMBER |  | 12 |  | Total number of warning messages. |
| TOTAL_ERROR_MESSAGES | NUMBER |  | 12 |  | Total number of error messages |
| TOTAL_KEEP_MESSAGES | NUMBER |  | 12 |  | Total number of keep messages. |
| TOTAL_SUCCESS_RECIPIENTS | NUMBER |  | 12 |  | Total number of successful recipients. |
| TOTAL_ERROR_RECIPIENTS | NUMBER |  | 12 |  | Total number of recipients in error for an error message |
| TOTAL_WARNING_RECIPIENTS | NUMBER |  | 12 |  | Total number of warning recipients. |
| TOTAL_KEEP_RECIPIENTS | NUMBER |  | 12 |  | Total number of keep recipients. |
| RUN_GROUP_NAME | VARCHAR2 | 80 |  |  | Phase1 Run Group Identifier. |
| RUN_CANCEL_FLAG | VARCHAR2 | 80 |  |  | Identifier used to detect cancelation of a run. |
| RUN_INT_VALUE1 | VARCHAR2 | 80 |  |  | Used to store Internal Value for a run. |
| RUN_INT_VALUE2 | VARCHAR2 | 80 |  |  | Used to store Internal Value for a run. |
| RUN_INT_VALUE3 | VARCHAR2 | 80 |  |  | Used to store Internal Value for a run. |
| RUN_INT_VALUE4 | VARCHAR2 | 80 |  |  | Used to store Internal Value for a run. |
| RETRY_COUNT | NUMBER |  | 18 |  | Number of Retries. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ALERT_RUNS_N1 | Non Unique | Default | ALERT_ID, RUN_START, STATUS |
| HRC_ALERT_RUNS_N2 | Non Unique | Default | REQUEST_ID |
| HRC_ALERT_RUNS_N3 | Non Unique | Default | USER_IDENTIFIER |
| HRC_ALERT_RUNS_N4 | Non Unique | Default | STATUS |
| HRC_ALERT_RUNS_N5 | Non Unique | Default | PARENT_RUN_ID |
| HRC_ALERT_RUNS_PK | Unique | Default | RUN_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
