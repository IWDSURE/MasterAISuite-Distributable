# CMP_CWB_BATCH_PROCESS_STATS

Stores batch process stats information for start and refresh process

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbbatchprocessstats-11055.html#cmpcwbbatchprocessstats-11055](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbbatchprocessstats-11055.html#cmpcwbbatchprocessstats-11055)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_BATCH_PROCESS_STATS_PK | BATCH_PROCESS_STAT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_PROCESS_STAT_ID | NUMBER |  | 18 | Yes | BATCH_PROCESS_STAT_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |
| PARENT_REQUEST_ID | NUMBER |  | 18 |  | PARENT_REQUEST_ID |
| JOB_NAME | VARCHAR2 | 120 |  |  | JOB_NAME |
| JOB_DISPLAY_NAME | VARCHAR2 | 2000 |  |  | JOB_DISPLAY_NAME |
| PROCESS_STATUS_CODE | VARCHAR2 | 120 |  |  | PROCESS_STATUS_CODE |
| ESS_STATUS_CODE | VARCHAR2 | 120 |  |  | ESS_STATUS_CODE |
| TOTAL_WORKERS | NUMBER |  |  |  | TOTAL_WORKERS |
| TOTAL_PROCESSED_SUB_PRC | NUMBER |  |  |  | TOTAL_PROCESSED_SUB_PRC |
| TOTAL_UNPROCESSED_SUB_PRC | NUMBER |  |  |  | TOTAL_UNPROCESSED_SUB_PRC |
| TOTAL_PROCESSED_DYN_CALC | NUMBER |  |  |  | TOTAL_PROCESSED_DYN_CALC |
| TOTAL_UNPROCESSED_DYN_CALC | NUMBER |  |  |  | TOTAL_UNPROCESSED_DYN_CALC |
| TIME_TAKEN_MINS | NUMBER |  |  |  | TIME_TAKEN_MINS |
| TIME_TAKEN_SINGLE_MINS | NUMBER |  |  |  | TIME_TAKEN_SINGLE_MINS |
| TIME_TAKEN_AVG_MINS | NUMBER |  |  |  | TIME_TAKEN_AVG_MINS |
| PROCESS_STAT_TYPE | VARCHAR2 | 30 |  | Yes | PROCESS_STAT_TYPE |
| NUM_THREADS_SUB_PRC | NUMBER |  |  |  | NUM_THREADS_SUB_PRC |
| NUM_THREADS_DYN_CALC | NUMBER |  |  |  | NUM_THREADS_DYN_CALC |
| PLAN_FF_NUM | NUMBER |  |  |  | PLAN_FF_NUM |
| PLAN_DYN_CALC_NUM | NUMBER |  |  |  | PLAN_DYN_CALC_NUM |
| PLAN_FF_IDS_LIST | VARCHAR2 | 4000 |  |  | PLAN_FF_IDS_LIST |
| LOGGING_LEVEL | VARCHAR2 | 120 |  |  | LOGGING_LEVEL |
| PROCESS_START | TIMESTAMP |  |  |  | PROCESS_START |
| PROCESS_END | TIMESTAMP |  |  |  | PROCESS_END |
| MANUAL_TASK | VARCHAR2 | 1 |  |  | MANUAL_TASK |
| ARGUMENT1 | VARCHAR2 | 4000 |  |  | ARGUMENT1 |
| ARGUMENT2 | VARCHAR2 | 4000 |  |  | ARGUMENT2 |
| ARGUMENT3 | VARCHAR2 | 4000 |  |  | ARGUMENT3 |
| ARGUMENT4 | VARCHAR2 | 4000 |  |  | ARGUMENT4 |
| ARGUMENT5 | VARCHAR2 | 4000 |  |  | ARGUMENT5 |
| ARGUMENT6 | VARCHAR2 | 4000 |  |  | ARGUMENT6 |
| ARGUMENT7 | VARCHAR2 | 4000 |  |  | ARGUMENT7 |
| ARGUMENT8 | VARCHAR2 | 4000 |  |  | ARGUMENT8 |
| ARGUMENT9 | VARCHAR2 | 4000 |  |  | ARGUMENT9 |
| ARGUMENT10 | VARCHAR2 | 4000 |  |  | ARGUMENT10 |
| ARGUMENT11 | VARCHAR2 | 4000 |  |  | ARGUMENT11 |
| ARGUMENT12 | VARCHAR2 | 4000 |  |  | ARGUMENT12 |
| ARGUMENT13 | VARCHAR2 | 4000 |  |  | ARGUMENT13 |
| ARGUMENT14 | VARCHAR2 | 4000 |  |  | ARGUMENT14 |
| ARGUMENT15 | VARCHAR2 | 4000 |  |  | ARGUMENT15 |
| ARGUMENT16 | VARCHAR2 | 4000 |  |  | ARGUMENT16 |
| ARGUMENT17 | VARCHAR2 | 4000 |  |  | ARGUMENT17 |
| ARGUMENT18 | VARCHAR2 | 4000 |  |  | ARGUMENT18 |
| ARGUMENT19 | VARCHAR2 | 4000 |  |  | ARGUMENT19 |
| ARGUMENT20 | VARCHAR2 | 4000 |  |  | ARGUMENT20 |
| ARGUMENT21 | VARCHAR2 | 4000 |  |  | ARGUMENT21 |
| ARGUMENT22 | VARCHAR2 | 4000 |  |  | ARGUMENT22 |
| ARGUMENT23 | VARCHAR2 | 4000 |  |  | ARGUMENT23 |
| ARGUMENT24 | VARCHAR2 | 4000 |  |  | ARGUMENT24 |
| ARGUMENT25 | VARCHAR2 | 4000 |  |  | ARGUMENT25 |
| ARGUMENT26 | VARCHAR2 | 4000 |  |  | ARGUMENT26 |
| ARGUMENT27 | VARCHAR2 | 4000 |  |  | ARGUMENT27 |
| ARGUMENT28 | VARCHAR2 | 4000 |  |  | ARGUMENT28 |
| ARGUMENT29 | VARCHAR2 | 4000 |  |  | ARGUMENT29 |
| ARGUMENT30 | VARCHAR2 | 4000 |  |  | ARGUMENT30 |
| ARGUMENT31 | VARCHAR2 | 4000 |  |  | ARGUMENT31 |
| ARGUMENT32 | VARCHAR2 | 4000 |  |  | ARGUMENT32 |
| ARGUMENT33 | VARCHAR2 | 4000 |  |  | ARGUMENT33 |
| ARGUMENT34 | VARCHAR2 | 4000 |  |  | ARGUMENT34 |
| ARGUMENT35 | VARCHAR2 | 4000 |  |  | ARGUMENT35 |
| ARGUMENT36 | VARCHAR2 | 4000 |  |  | ARGUMENT36 |
| PROCESS_ALERT | VARCHAR2 | 120 |  |  | PROCESS_ALERT |
| ERROR_MESSAGE | VARCHAR2 | 2000 |  |  | ERROR_MESSAGE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TRACK_INELIGIBLE_FLAG | VARCHAR2 | 1 |  |  | TRACK_INELIGIBLE_FLAG |
| TRIAL_RUN_FLAG | VARCHAR2 | 1 |  |  | TRIAL_RUN_FLAG |
| TOTAL_PLACEHOLDERS_PROCESSED | NUMBER |  |  |  | TOTAL_PLACEHOLDERS_PROCESSED |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_BATCH_PROCESS_STATS_N1 | Non Unique | Default | REQUEST_ID |
| CMP_CWB_BATCH_PROCESS_STATS_PK | Unique | Default | BATCH_PROCESS_STAT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
