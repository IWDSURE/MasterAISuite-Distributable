# FAI_SAM_RAW_ESS

This table holds the raw process data

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamrawess-4731.html#faisamrawess-4731](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamrawess-4731.html#faisamrawess-4731)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_RAW_ESS_PK | RAW_ESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RAW_ESS_ID | NUMBER |  | 18 | Yes | Primary Key of Raw Process Table |
| ID_METRIC | VARCHAR2 | 240 |  |  | Request Id of the Process in Raw ESS |
| KEY | VARCHAR2 | 240 |  | Yes | Key of the ESS in Raw ESS Table |
| DAY | DATE |  |  |  | Day of the process in Raw ESS Table |
| START_TIME | TIMESTAMP |  |  |  | Start Time of the Process in Raw ESS |
| STOP_TIME | TIMESTAMP |  |  |  | Stop Time of the Process in Raw ESS |
| PROCESSING_TIME | NUMBER |  | 6 |  | Time of the Processing in Raw ESS |
| THREAD_COUNT | NUMBER |  |  |  | Threadcount of the process in Raw ESS |
| LOAD | NUMBER |  |  |  | Number Of Record in Process in Raw ESS |
| PROCESS_STATUS | VARCHAR2 | 80 |  |  | Status of the Process in Raw ESS |
| LOAD_SUCCESS | NUMBER |  |  |  | Number of record successfully uploaded |
| LOAD_IN_ERROR | NUMBER |  |  |  | Number of Record loaded in Error by the process |
| PARAMETER | CLOB |  |  |  | Parameter of the process in Raw ESS |
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
| FAI_SAM_RAW_ESS_N1 | Non Unique | FUSION_TS_TX_IDX | ID_METRIC, KEY |
| FAI_SAM_RAW_ESS_N2 | Non Unique | FUSION_TS_TX_IDX | KEY, DAY |
| FAI_SAM_RAW_ESS_PK | Unique | FUSION_TS_TX_IDX | RAW_ESS_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
