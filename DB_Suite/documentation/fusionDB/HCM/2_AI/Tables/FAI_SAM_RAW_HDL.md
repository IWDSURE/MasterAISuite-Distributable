# FAI_SAM_RAW_HDL

This table holds the raw loader data

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamrawhdl-9345.html#faisamrawhdl-9345](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamrawhdl-9345.html#faisamrawhdl-9345)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_RAW_HDL_PK | RAW_HDL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RAW_HDL_ID | NUMBER |  | 18 | Yes | Primary Key HDL Raw Process Table |
| DAY | DATE |  |  |  | Day of the process in Raw HDL Table |
| PROCESS_STATUS | VARCHAR2 | 80 |  |  | Status of the Process in Raw HDL Table |
| KEY | VARCHAR2 | 80 |  | Yes | Key of the ESS in Raw HDL Table |
| THREAD_COUNT_IMPORT | NUMBER |  |  |  | Thread count for the File import in Raw HDL Table |
| THREAD_COUNT_LOAD | NUMBER |  |  |  | Thread count for the load file in Raw HDL Table |
| LOAD_IMPORT | NUMBER |  |  |  | Number of Record during import in Raw HDL Table |
| LOAD_LINE | NUMBER |  |  |  | Number of Line Records in Raw HDL Table |
| LOAD_SUCCESS | NUMBER |  |  |  | Number of record successfully uploaded |
| PROCESSING_TIME | NUMBER |  |  |  | Time of the Processing in Raw HDL Table |
| ID_METRIC | VARCHAR2 | 240 |  |  | Request Id of the Process in Raw HDL Table |
| UCM_ID | VARCHAR2 | 240 |  |  | Id Reference to the metadata in Raw HDL Table |
| CHUNK | NUMBER |  |  |  | Chunk used on the process in Raw HDL Table |
| LOAD_LINE_IN_ERROR | NUMBER |  |  |  | Number of Record in Error during the line load |
| START_TIME | TIMESTAMP |  |  |  | Start Time of the Process in Raw HDL Table |
| STOP_TIME | TIMESTAMP |  |  |  | Stop Time of the Process in Raw HDL Table |
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
| FAI_SAM_RAW_HDL_N1 | Non Unique | FUSION_TS_TX_IDX | ID_METRIC, KEY |
| FAI_SAM_RAW_HDL_N2 | Non Unique | FUSION_TS_TX_IDX | DAY |
| FAI_SAM_RAW_HDL_PK | Unique | FUSION_TS_TX_IDX | RAW_HDL_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
