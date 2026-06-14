# FAI_SAM_ONE_VIEW_PROCESS

This table holds the denormalized  processes data

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamoneviewprocess-30635.html#faisamoneviewprocess-30635](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamoneviewprocess-30635.html#faisamoneviewprocess-30635)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_ONE_VIEW_PROCESS_PK | ONE_VIEW_PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ONE_VIEW_PROCESS_ID | NUMBER |  | 18 | Yes | Primary Key of One View Process Table |
| OBJECT_KEY | VARCHAR2 | 240 |  | Yes | Key of the Object in One View Process |
| PROCESS_TYPE | VARCHAR2 | 80 |  |  | Type of the Process in One View Process |
| PROCESS_NAME | VARCHAR2 | 2000 |  |  | Name of the Process in One View Process |
| ID_METRIC | VARCHAR2 | 240 |  |  | Request Id of the Process in One View Process |
| PARENT_ID_METRIC | NUMBER |  |  |  | Id of the parent process in One View Process |
| PROCESS_STATUS | VARCHAR2 | 80 |  |  | Status of the Process in One View Process |
| LOAD | VARCHAR2 | 240 |  |  | Number Of Record in Process in One View Process |
| LOAD_SUCCESS | VARCHAR2 | 240 |  |  | Number of record successfully uploaded in One View Process |
| LOAD_ERROR | VARCHAR2 | 240 |  |  | Number of Record loaded in Error by the process |
| PROCESSING_TIME | NUMBER |  |  |  | Time of the Processing in One View Process |
| THREAD_COUNT | NUMBER |  |  |  | Threadcount of the process in One View Process |
| DAY | DATE |  |  |  | Day of the process in One View Process |
| START_TIME | TIMESTAMP |  |  |  | Start Time of the Process in One View Process |
| STOP_TIME | TIMESTAMP |  |  |  | Stop Time of the Process in One View Process |
| PRODUCT | VARCHAR2 | 80 |  |  | Product associated to the Process in One View Process |
| RAW_DATA_ID | NUMBER |  |  |  | Foreign Key to either raw process tables |
| PARAMETER | CLOB |  |  |  | Parameter of the process in One View Process |
| PARAMETER_COMBINE | CLOB |  |  |  | More Process Parameter in One View Process |
| ANOMALY_LOOP | VARCHAR2 | 80 |  |  | Loop back to the AI on accuracy of the detection |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES Table |
| POD | VARCHAR2 | 24 |  |  | Internal Column Apex Version FAPOD in FA |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_SAM_ONE_VIEW_PROCESS_FK | Non Unique | FUSION_TS_TX_IDX | RAW_DATA_ID |
| FAI_SAM_ONE_VIEW_PROCESS_N2 | Non Unique | FUSION_TS_TX_IDX | POD, ONE_VIEW_PROCESS_ID, DAY |
| FAI_SAM_ONE_VIEW_PROCESS_PK | Unique | FUSION_TS_TX_IDX | ONE_VIEW_PROCESS_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
