# HRC_ALERT_RUN_LOG_LINES

Contains alert run Logs for a given run.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunloglines-20193.html#hrcalertrunloglines-20193](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunloglines-20193.html#hrcalertrunloglines-20193)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERT_RUN_LOG_LINES_PK | RUN_LOG_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_LOG_LINE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| RUN_ID | NUMBER |  | 18 | Yes | Run Identifier. Foreign Key to HRC_ALERT_RUNS.RUN_ID |
| PHASE | VARCHAR2 | 30 |  | Yes | Specifies the Alert Run Phase. Valid values are: ORA_PHASE1,ORA_PHASE2,ORA_PHASE3 |
| LOG_SOURCE | VARCHAR2 | 30 |  | Yes | Specifies the source of the Alert Log. Valid values are: Run,Message,Recipient,RecipientExpression,GroupByExpression,Template |
| LOG_WEIGHT | NUMBER |  | 18 |  | Specifies the weight of the Alert Log record. |
| RUN_LANGUAGE | VARCHAR2 | 4 |  |  | Run Lanugage in which the Alert template is identified and Alert run is executed. |
| TEMPLATE_NAME | VARCHAR2 | 80 |  |  | Templates user defined name. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SURROGATE_ID | NUMBER |  | 18 |  | SurrogateId of the record of the rest resource related table that is configured in the Alert. |
| PROP_NAME | VARCHAR2 | 80 |  |  | Property Name of the Alert Run Log record. |
| PROP_VALUE | VARCHAR2 | 200 |  |  | Property Value of the Alert Run Log record. |
| FUNC_NAME | VARCHAR2 | 80 |  |  | Function Name of the Alert Run Log record. |
| FUNC_ARG_NAME1 | VARCHAR2 | 80 |  |  | Function First Argument Name of the record. |
| FUNC_ARG_VAL1 | VARCHAR2 | 200 |  |  | Function First Argument Value of the record. |
| FUNC_ARG_NAME2 | VARCHAR2 | 80 |  |  | Function Second Argument Name of the record. |
| FUNC_ARG_VAL2 | VARCHAR2 | 200 |  |  | Function Second Argument Value of the record. |
| FUNC_ARG_NAME3 | VARCHAR2 | 80 |  |  | Function Third Argument Name of the record. |
| FUNC_ARG_VAL3 | VARCHAR2 | 200 |  |  | Function Third Argument Value of the record. |
| LOG_TYPE | VARCHAR2 | 30 |  |  | Log type of the Alert Run Log record. |
| LOG_SUBTYPE | VARCHAR2 | 30 |  |  | Log Subtype of the Alert Run Log record. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ALERT_RUN_LOG_LINES_N1 | Non Unique | Default | RUN_ID, LOG_SOURCE |
| HRC_ALERT_RUN_LOG_LINES_N2 | Non Unique | HRC_ALERT_RUN_LOG_LINES_N2 | RUN_ID, LOG_TYPE, LOG_SUBTYPE |
| HRC_ALERT_RUN_LOG_LINES_N3 | Non Unique | HRC_ALERT_RUN_LOG_LINES_N3 | RUN_ID, PHASE |
| HRC_ALERT_RUN_LOG_LINES_N4 | Non Unique | HRC_ALERT_RUN_LOG_LINES_N4 | RUN_ID, PROP_NAME |
| HRC_ALERT_RUN_LOG_LINES_N5 | Non Unique | HRC_ALERT_RUN_LOG_LINES_N5 | RUN_ID, FUNC_NAME |
| HRC_ALERT_RUN_LOG_LINES_PK | Unique | Default | RUN_LOG_LINE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
