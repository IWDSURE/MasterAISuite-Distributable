# FAI_SAM_RAW_PAYROLL_FLOW

This table holds the payroll flow data

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamrawpayrollflow-18236.html#faisamrawpayrollflow-18236](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamrawpayrollflow-18236.html#faisamrawpayrollflow-18236)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_RAW_PAYROLL_FLOW_PK | RAW_PAYROLL_FLOW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RAW_PAYROLL_FLOW_ID | NUMBER |  | 18 | Yes | Primary Key Payroll Raw Process Table |
| PARENT_ID_METRIC | NUMBER |  |  |  | Parent Process id in Raw Payroll Table |
| ACTIVITY | VARCHAR2 | 50 |  |  | Payroll Activity in Raw Payroll Table |
| TASK_GROUP | VARCHAR2 | 50 |  |  | Payroll Task Group in Raw Payroll Table |
| KEY | VARCHAR2 | 255 |  | Yes | Key of the ESS in Raw Payroll Table |
| ACTION_NAME | VARCHAR2 | 100 |  |  | Payroll Action Name in Raw Payroll Table |
| FLOW_NAME | VARCHAR2 | 255 |  |  | Payroll Flow Name in Raw Payroll Table |
| START_TIME | TIMESTAMP |  |  |  | Start Time of the Process in Raw Payroll Table |
| DAY | TIMESTAMP |  |  |  | Day of the process in Raw Payroll Table |
| PROCESS_STATUS | VARCHAR2 | 50 |  |  | Status of the Process in Raw Payroll Table |
| LOAD | VARCHAR2 | 80 |  |  | Number Of Record in Process in Raw Payroll Table |
| LOAD_IN_ERROR | VARCHAR2 | 80 |  |  | Number of Record loaded in Error by the process |
| PROCESSING_TIME | NUMBER |  |  |  | Time of the Processing in Raw Payroll Table |
| THREAD_COUNT | NUMBER |  |  |  | Threadcount of the process in Raw Payroll Table |
| ID_METRIC | NUMBER |  |  |  | Request Id of the Process in Raw Payroll Table |
| STOP_TIME | TIMESTAMP |  |  |  | Stop Time of the Process in Raw Payroll Table |
| PARAMETER | VARCHAR2 | 2400 |  |  | Parameter of the process in Raw Payroll Table |
| FLOW_PATTERN_NAME | VARCHAR2 | 1000 |  |  | Payroll Flow Pattern Name in Raw Payroll Table |
| FLOW_TASK_NAME | VARCHAR2 | 1000 |  |  | Payroll Flow Task Name in Raw Payroll Table |
| PAYROLL_ID | NUMBER |  |  |  | The Payroll Id in Raw Payroll Table |
| PAYROLL_ACTION_EFFECTIVE_DATE | DATE |  |  |  | Payroll Action Effective Date in Raw Payroll Table |
| PAYROLL_ACTION_START_DATE | DATE |  |  |  | Payroll Action Start Date in Raw Payroll Table |
| PAYROLL_ACTION_END_DATE | DATE |  |  |  | Payroll Action End Date in Raw Payroll Table |
| BASE_ACTIVITY | VARCHAR2 | 240 |  |  | Payroll Base Activity in Raw Payroll Table |
| BASE_TASK_GROUP | VARCHAR2 | 240 |  |  | Payroll Base Task Group in Raw Payroll Table |
| BASE_TASK_NAME | VARCHAR2 | 240 |  |  | Payroll Base Task Name in Raw Payroll Table |
| BASE_ACTION_NAME | VARCHAR2 | 240 |  |  | Base Action Name in Raw Payroll Table |
| PAYROLL_ACTION_ID | NUMBER |  |  |  | Payroll Action Id in Raw Payroll Table |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES TABLE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_SAM_RAW_PAYROLL_FLOW_N1 | Non Unique | FUSION_TS_TX_IDX | ID_METRIC |
| FAI_SAM_RAW_PAYROLL_FLOW_N2 | Non Unique | FUSION_TS_TX_IDX | KEY, DAY |
| FAI_SAM_RAW_PAYROLL_FLOW_PK | Unique | FUSION_TS_TX_IDX | RAW_PAYROLL_FLOW_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
