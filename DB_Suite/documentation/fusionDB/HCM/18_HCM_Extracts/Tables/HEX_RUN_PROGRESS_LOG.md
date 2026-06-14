# HEX_RUN_PROGRESS_LOG

The table stores the progress log for the extract run.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexrunprogresslog-27065.html#hexrunprogresslog-27065](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexrunprogresslog-27065.html#hexrunprogresslog-27065)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_RUN_PROGRESS_LOG_PK | EXT_RUN_ID, EXT_LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXT_LOG_ID | NUMBER |  |  | Yes | The column indicates a unique sequence generated value. |
| EXT_RUN_ID | NUMBER |  |  | Yes | The column indicates the EXT_RUN_ID from HEX_RUNS table. |
| ESS_REQUEST_ID | NUMBER |  |  | Yes | The column idicates the request ID of the ess request. |
| PROCESS_TYPE | VARCHAR2 | 30 |  |  | The column indicates the type of the process for which the log is generated. |
| LOG_LEVEL | VARCHAR2 | 30 |  |  | The column indicates the level of the log. |
| LOG_TEXT | VARCHAR2 | 4000 |  |  | The column indicates the text of the log. |
| OBJECTS_FOR_PROCESSING | NUMBER |  |  |  | The column indicates the total number of objects picked for processing. |
| OBJECTS_PROCESSED | NUMBER |  |  |  | The column indicates the number of objects processed successfully. |
| OBJECTS_ERRORRED | NUMBER |  |  |  | The column indicates the number of objects errorred. |
| START_DATE | TIMESTAMP |  |  |  | The column indicates the start time of the process. |
| END_DATE | TIMESTAMP |  |  |  | The column indicates the end time of the process. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HEX_RUN_PROGRESS_LOG_N1 | Non Unique | Default | EXT_RUN_ID, ESS_REQUEST_ID, PROCESS_TYPE |  |
| HEX_RUN_PROGRESS_LOG_N2 | Non Unique | Default | EXT_RUN_ID, LOG_LEVEL | Obsolete |
| HEX_RUN_PROGRESS_LOG_N3 | Non Unique | Default | EXT_RUN_ID, ATTRIBUTE_CATEGORY, ATTRIBUTE1 | Obsolete |
| HEX_RUN_PROGRESS_LOG_PK | Unique | Default | EXT_RUN_ID, EXT_LOG_ID |  |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
