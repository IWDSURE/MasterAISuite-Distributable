# HRC_DL_DATA_SETS

This table holds information about the source files sent by Customers which will be loaded to fusion. Source files can be a ZIP file or DAT file. If the source file is ZIP then it might contain more than one DAT file. It also Supports UI by providing its  status and counts during TRANSFER,IMPORT,LOAD and VALIDATE processes.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdldatasets-31444.html#hrcdldatasets-31444](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdldatasets-31444.html#hrcdldatasets-31444)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_DATA_SETS_PK | DATA_SET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DATA_SET_ID | NUMBER |  | 18 | Yes | DATA_SET_ID |
| DATA_SET_STATUS | VARCHAR2 | 30 |  |  | DATA_SET_STATUS |
| UCM_CONTENT_ID | VARCHAR2 | 30 |  | Yes | UCM_CONTENT_ID |
| DATA_SET_NAME | VARCHAR2 | 200 |  | Yes | DATA_SET_NAME |
| SOURCE_TYPE | VARCHAR2 | 30 |  | Yes | SOURCE_TYPE |
| INTEGRATION_TYPE | VARCHAR2 | 30 |  |  | Name of the integration solution for data sets created by a packaged integration solution. |
| TRANSFER_STATUS | VARCHAR2 | 30 |  | Yes | IMPORTED_STATUS |
| IMPORTED_STATUS | VARCHAR2 | 30 |  | Yes | IMPORTED_STATUS |
| VALIDATED_STATUS | VARCHAR2 | 30 |  | Yes | VALIDATED_STATUS |
| LOADED_STATUS | VARCHAR2 | 30 |  | Yes | LOADED_STATUS |
| SKIPPED_STATUS | VARCHAR2 | 1 |  | Yes | SKIPPED_STATUS |
| IMPORT_LINES_SUCCESS_COUNT | NUMBER |  | 9 | Yes | IMPORT_LINES_SUCCESS_COUNT |
| IMPORT_LINES_ERROR_COUNT | NUMBER |  | 9 | Yes | IMPORT_LINES_ERROR_COUNT |
| IMPORT_LINES_TOTAL_COUNT | NUMBER |  | 9 | Yes | IMPORT_LINES_TOTAL_COUNT |
| IMPORT_SUCCESS_COUNT | NUMBER |  | 9 | Yes | IMPORT_SUCCESS_COUNT |
| IMPORT_ERROR_COUNT | NUMBER |  | 9 | Yes | IMPORT_ERROR_COUNT |
| LINE_HELD_COUNT | NUMBER |  | 9 | Yes | Sum of LINE_HELD_COUNT values for all the constituting DATA_SET_BUS_OBJ rows |
| LINE_LOADED_COUNT | NUMBER |  | 9 | Yes | Sum of all LINE_LOADED_COUNT values of consituting DATA_SET_BUS_OBJ rows |
| LINE_UNPROCESSED_COUNT | NUMBER |  | 9 | Yes | Sum of all LINE_UNPROCESSED_COUNT values of consituting DATA_SET_BUS_OBJ rows |
| LINE_ERROR_COUNT | NUMBER |  | 9 | Yes | Sum of all LINE_ERROR_COUNT values of the consituting DATA_SET_BUS_OBJ rows |
| UNPROCESSED_COUNT | NUMBER |  | 9 | Yes | UNPROCESSED_COUNT |
| VALIDATED_COUNT | NUMBER |  | 9 | Yes | VALIDATED_COUNT |
| LOADED_COUNT | NUMBER |  | 9 | Yes | LOADED_COUNT |
| ROLLBACK_ERROR_COUNT | NUMBER |  | 9 | Yes | ROLLBACK_ERROR_COUNT |
| ERROR_COUNT | NUMBER |  | 9 | Yes | ERROR_COUNT |
| SKIPPED_COUNT | NUMBER |  | 9 | Yes | SKIPPED_COUNT |
| CORRECTED_COUNT | NUMBER |  | 9 | Yes | CORRECTED_COUNT |
| ARCHIVAL_STATUS | VARCHAR2 | 30 |  |  | ARCHIVAL_STATUS |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ERR_ROWS_FILE_GEN_STATUS | VARCHAR2 | 30 |  |  | ERR_ROWS_FILE_GEN_STATUS |
| ERR_ROWS_FILE_UCM_CONTENT_ID | VARCHAR2 | 30 |  |  | ERR_ROWS_FILE_UCM_CONTENT_ID |
| CUSTOM_UCM_CONTENT_ID | VARCHAR2 | 30 |  |  | CUSTOM_UCM_CONTENT_ID |
| ENCRYPTION_TYPE | VARCHAR2 | 30 |  |  | ENCRYPTION_TYPE |
| ERR_ROWS_FILE_NAME | VARCHAR2 | 200 |  |  | ERROR_FILE_NAME |
| PROTECTED_FLAG | VARCHAR2 | 5 |  |  | This flag is used to indicate whether the data set is protected or not. |
| POST_PROCESS_STATUS | VARCHAR2 | 30 |  |  | POST_PROCESS_STATUS |
| LOAD_CATEGORY | VARCHAR2 | 200 |  |  | This denotes the process from which load job is invoked |
| LOAD_SUB_CATEGORY | VARCHAR2 | 200 |  |  | This denotes the ess job from which load job is invoked as child |
| ZIP_FILE_SIZE | NUMBER |  | 18 |  | This denotes the total zip file size in bytes |
| BLOB_FILES_SIZE | NUMBER |  | 18 |  | This denotes the total blob files size in bytes |
| CLOB_FILES_SIZE | NUMBER |  | 18 |  | This denotes the total clob files size in bytes |
| MSG_COUNT | NUMBER |  | 9 |  | This denotes the data set messages count. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_DATA_SETS_N1 | Non Unique | Default | LAST_UPDATE_DATE |
| HRC_DL_DATA_SETS_N2 | Non Unique | Default | UCM_CONTENT_ID |
| HRC_DL_DATA_SETS_N3 | Non Unique | Default | REQUEST_ID |
| HRC_DL_DATA_SETS_N4 | Non Unique | Default | DATA_SET_NAME |
| HRC_DL_DATA_SETS_PK | Unique | Default | DATA_SET_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
