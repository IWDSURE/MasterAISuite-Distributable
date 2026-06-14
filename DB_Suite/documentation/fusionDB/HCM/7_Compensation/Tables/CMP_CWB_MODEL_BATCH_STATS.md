# CMP_CWB_MODEL_BATCH_STATS

Stores batch process stats information for Apply Model process

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbmodelbatchstats-15143.html#cmpcwbmodelbatchstats-15143](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbmodelbatchstats-15143.html#cmpcwbmodelbatchstats-15143)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_MODEL_BATCH_PK | MODEL_BATCH_STAT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MODEL_BATCH_STAT_ID | NUMBER |  | 18 | Yes | MODEL_BATCH_STAT_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_NAME | VARCHAR2 | 120 |  |  | JOB_NAME |
| JOB_DISPLAY_NAME | VARCHAR2 | 2000 |  |  | JOB_DISPLAY_NAME |
| PROCESS_STATUS_CODE | VARCHAR2 | 120 |  |  | PROCESS_STATUS_CODE |
| ESS_STATUS_CODE | VARCHAR2 | 120 |  |  | ESS_STATUS_CODE |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |
| MODEL_ID | NUMBER |  |  | Yes | MODEL_ID |
| MODEL_NAME | VARCHAR2 | 240 |  |  | MODE_NAME to be displayed from this column, in case a previously applied model is deleted. |
| COMPONENT_ID | NUMBER |  |  |  | COMPONENT_ID |
| ALLOCATION_METHOD | VARCHAR2 | 100 |  |  | ALLOCATION_METHOD |
| SELECT_PURPOSE | VARCHAR2 | 100 |  |  | SELECT_PURPOSE |
| MODEL_MODE | VARCHAR2 | 20 |  |  | MODEL_MODE |
| MGR_USER_PERSON_ID | NUMBER |  |  |  | MGR_USER_PERSON_ID |
| TOTAL_WORKERS | NUMBER |  |  |  | TOTAL_WORKERS |
| PLAN_DYN_CALC_NUM | NUMBER |  |  |  | PLAN_DYN_CALC_NUM |
| NUM_THREADS_DYN_CALC | NUMBER |  |  |  | NUM_THREADS_DYN_CALC |
| FAILED_DYN_CALC_IDS | VARCHAR2 | 2000 |  |  | Comma (,) separated Process IDS of Child Dyn Calc Request which Complete with some Error |
| TOTAL_PROCESSED_DYN_CALC | NUMBER |  |  |  | TOTAL_PROCESSED_DYN_CALC |
| TOTAL_UNPROCESSED_DYN_CALC | NUMBER |  |  |  | TOTAL_UNPROCESSED_DYN_CALC |
| PROCESS_START | TIMESTAMP |  |  |  | PROCESS_START |
| PROCESS_END | TIMESTAMP |  |  |  | PROCESS_END |
| TIME_TAKEN_MINS | NUMBER |  |  |  | TIME_TAKEN_MINS |
| ERROR_MESSAGE | VARCHAR2 | 2000 |  |  | ERROR_MESSAGE |
| ATTRIBUTE_1 | VARCHAR2 | 120 |  |  | ATTRIBUTE_1 |
| ATTRIBUTE_2 | VARCHAR2 | 120 |  |  | ATTRIBUTE_2 |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_MODEL_STATS_N1 | Non Unique | Default | REQUEST_ID |
| CMP_CWB_MODEL_STATS_N2 | Non Unique | Default | PLAN_ID, PERIOD_ID |
| CMP_CWB_MODEL_STATS_UK1 | Unique | Default | MODEL_BATCH_STAT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
