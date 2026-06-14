# HRC_DL_DATA_SET_BUS_OBJS

Each row in this table corresponds to a DAT file for a given data set.  It also Supports UI by providing DAT file status and counts value during TRANSFER,IMPORT,LOAD and VALIDATE processes. Each Individual DAT file status and counts for a given data set can be  consolidated and derive its data set information.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdldatasetbusobjs-16266.html#hrcdldatasetbusobjs-16266](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdldatasetbusobjs-16266.html#hrcdldatasetbusobjs-16266)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_DATA_SET_BUS_OBJS_PK | DATA_SET_BUS_OBJ_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 | Yes | DATA_SET_BUS_OBJ_ID |
| ROLLBACK_ERROR_COUNT | NUMBER |  | 9 | Yes | ROLLBACK_ERROR_COUNT |
| DATA_FILE_NAME | VARCHAR2 | 200 |  |  | DATA_FILE_NAME |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| IMPORTED_STATUS | VARCHAR2 | 30 |  | Yes | IMPORTED_STATUS |
| TRANSFER_STATUS | VARCHAR2 | 30 |  | Yes | Transfer status for the Data Set Business Object |
| VALIDATED_STATUS | VARCHAR2 | 30 |  | Yes | VALIDATED_STATUS |
| LOADED_STATUS | VARCHAR2 | 30 |  | Yes | LOADED_STATUS |
| SKIPPED_STATUS | VARCHAR2 | 1 |  | Yes | SKIPPED_STATUS |
| IMPORT_LINES_SUCCESS_COUNT | NUMBER |  | 9 | Yes | IMPORT_LINES_SUCCESS_COUNT |
| IMPORT_LINES_ERROR_COUNT | NUMBER |  | 9 | Yes | IMPORT_LINES_ERROR_COUNT |
| IMPORT_LINES_TOTAL_COUNT | NUMBER |  | 9 | Yes | IMPORT_LINES_TOTAL_COUNT |
| IMPORT_SUCCESS_COUNT | NUMBER |  | 9 | Yes | IMPORT_SUCCESS_COUNT |
| IMPORT_ERROR_COUNT | NUMBER |  | 9 | Yes | IMPORT_ERROR_COUNT |
| LINE_LOADED_COUNT | NUMBER |  | 9 | Yes | The count of hrc_dl_physical_lines where the top hrc_dl_logical_line has a validated_loaded_status = LOADED_SUCCESS |
| LINE_HELD_COUNT | NUMBER |  | 9 | Yes | The count of hrc_dl_physical_lines where the top hrc_dl_logical_line has a validated_loaded_status = UNPROCESSED |
| LINE_UNPROCESSED_COUNT | NUMBER |  | 9 | Yes | The count of hrc_dl_physical_lines where the top hrc_dl_logical_line has a validated_loaded_status = UNPROCESSED |
| LINE_ERROR_COUNT | NUMBER |  | 9 | Yes | The sum of the number of file lines not transferred to file rows, the number of file rows not imported to physical lines and the number of physical lines in error. |
| UNPROCESSED_COUNT | NUMBER |  | 9 | Yes | UNPROCESSED_COUNT |
| VALIDATED_COUNT | NUMBER |  | 9 | Yes | VALIDATED_COUNT |
| LOADED_COUNT | NUMBER |  | 9 | Yes | LOADED_COUNT |
| ERROR_COUNT | NUMBER |  | 9 | Yes | ERROR_COUNT |
| SKIPPED_COUNT | NUMBER |  | 9 | Yes | SKIPPED_COUNT |
| CORRECTED_COUNT | NUMBER |  | 9 | Yes | CORRECTED_COUNT |
| PROCESSING_ORDER | NUMBER |  | 18 | Yes | PROCESSING_ORDER |
| PROCESSING_LEVEL | NUMBER |  | 9 | Yes | Processing level of the data set business object |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DATA_SET_ID | NUMBER |  | 18 | Yes | DATA_SET_ID |
| MAPPING_FILE_UCM_CONTENT_ID | VARCHAR2 | 30 |  |  | MAPPING_FILE_UCM_CONTENT_ID |
| MAPPING_FILE_NAME | VARCHAR2 | 200 |  |  | MAPPING_FILE_NAME |
| ERR_ROWS_FILE_GEN_STATUS | VARCHAR2 | 30 |  |  | ERR_ROWS_FILE_GEN_STATUS |
| ERR_ROWS_FILE_UCM_CONTENT_ID | VARCHAR2 | 30 |  |  | ERR_ROWS_FILE_UCM_CONTENT_ID |
| CUSTOM_UCM_CONTENT_ID | VARCHAR2 | 30 |  |  | CUSTOM
_UCM_CONTENT_ID |
| ENCRYPTION_TYPE | VARCHAR2 | 30 |  |  | ENCRYPTION_TYPE |
| ERR_ROWS_FILE_NAME | VARCHAR2 | 200 |  |  | ERR_ROWS_FILE_NAME |
| POST_PROCESS_STATUS | VARCHAR2 | 30 |  |  | POST_PROCESS_STATUS |
| DAT_FILE_SIZE | NUMBER |  | 18 |  | This denotes the dat file size in bytes |
| MSG_COUNT | NUMBER |  | 9 |  | This denotes the data set business object messages count. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_DATA_SET_BUS_OBJS_N1 | Non Unique | Default | DATA_SET_ID, BUSINESS_OBJECT_ID |
| HRC_DL_DATA_SET_BUS_OBJS_PK | Unique | Default | DATA_SET_BUS_OBJ_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
