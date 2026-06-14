# BEN_BATCH_HEADER

BEN_BATCH_HEADER contains information related to processing benefits data .

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchheader-7465.html#benbatchheader-7465](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchheader-7465.html#benbatchheader-7465)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BATCH_HEADER_PK | BATCH_HEADER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_HEADER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| NAME | VARCHAR2 | 250 |  | Yes | Batch Name. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| PROCESS_CODE | VARCHAR2 | 250 |  | Yes | Process code for the batch. |
| STATUS | VARCHAR2 | 250 |  |  | Status of the batch before and after processing. |
| ERROR_MESSAGE | VARCHAR2 | 2000 |  |  | Error message. |
| BBH_TXT_VAL_1 | VARCHAR2 | 250 |  |  | Additional batch text information. |
| BBH_TXT_VAL_2 | VARCHAR2 | 250 |  |  | Additional batch text information. |
| BBH_TXT_VAL_3 | VARCHAR2 | 250 |  |  | Additional batch text information. |
| BBH_TXT_VAL_4 | VARCHAR2 | 250 |  |  | Additional batch text information. |
| BBH_TXT_VAL_5 | VARCHAR2 | 250 |  |  | Additional batch text information. |
| BBH_NUM_VAL_1 | NUMBER |  | 18 |  | Additional batch numeric information. |
| BBH_NUM_VAL_2 | NUMBER |  | 18 |  | Additional batch numeric information. |
| BBH_NUM_VAL_3 | NUMBER |  | 18 |  | Additional batch numeric information. |
| BBH_NUM_VAL_4 | NUMBER |  | 18 |  | Additional batch numeric information. |
| BBH_NUM_VAL_5 | NUMBER |  | 18 |  | Additional batch numeric information. |
| BBH_DT_VAL_1 | DATE |  |  |  | Additional batch date information. |
| BBH_DT_VAL_2 | DATE |  |  |  | Additional batch date information. |
| BBH_DT_VAL_3 | DATE |  |  |  | Additional batch date information. |
| BBH_DT_VAL_4 | DATE |  |  |  | Additional batch date information. |
| BBH_DT_VAL_5 | DATE |  |  |  | Additional batch date information. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| UPDATED_REQUEST_ID | NUMBER |  | 18 |  | Updated Request Identification. |
| NUM_OF_THREADS | NUMBER |  | 18 |  | Number of threads used for processing the batch. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| REQUEST_SUBMISSION_DATE | TIMESTAMP |  |  |  | Indicates the date and time of batch submission. |
| REQUEST_COMPLETION_DATE | TIMESTAMP |  |  |  | Indicates the date and time of batch completion. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BATCH_HEADER_N1 | Non Unique | FUSION_TS_TX_IDX | NAME, PROCESS_CODE |
| BEN_BATCH_HEADER_PK | Unique | FUSION_TS_TX_IDX | BATCH_HEADER_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
