# HRC_DL_DATASET_DETAILS

Tables to save the dataset  object summary information when Purge process is run.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdldatasetdetails-22230.html#hrcdldatasetdetails-22230](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdldatasetdetails-22230.html#hrcdldatasetdetails-22230)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_DATASET_DETAILS_PK | DATA_SET_BUS_OBJ_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 | Yes | DATA_SET_BUS_OBJ_ID |
| DATA_FILE_NAME | VARCHAR2 | 200 |  |  | DATA_FILE_NAME |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| TRANSFER_STATUS | VARCHAR2 | 30 |  | Yes | TRANSFER_STATUS |
| IMPORTED_STATUS | VARCHAR2 | 30 |  | Yes | IMPORTED_STATUS |
| LOADED_STATUS | VARCHAR2 | 30 |  | Yes | LOADED_STATUS |
| IMPORT_LINES_SUCCESS_COUNT | NUMBER |  | 9 | Yes | IMPORT_LINES_SUCCESS_COUNT |
| IMPORT_LINES_ERROR_COUNT | NUMBER |  | 9 | Yes | IMPORT_LINES_ERROR_COUNT |
| IMPORT_LINES_TOTAL_COUNT | NUMBER |  | 9 | Yes | IMPORT_LINES_TOTAL_COUNT |
| IMPORT_SUCCESS_COUNT | NUMBER |  | 9 | Yes | IMPORT_SUCCESS_COUNT |
| IMPORT_ERROR_COUNT | NUMBER |  | 9 | Yes | IMPORT_ERROR_COUNT |
| VALIDATED_COUNT | NUMBER |  | 9 | Yes | VALIDATED_COUNT |
| LOADED_COUNT | NUMBER |  | 9 | Yes | LOADED_COUNT |
| ERROR_COUNT | NUMBER |  | 9 | Yes | ERROR_COUNT |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DATA_SET_ID | NUMBER |  | 18 | Yes | DATA_SET_ID |
| DS_BO_CREATION_DATE | TIMESTAMP |  |  |  | DS_BO_CREATION_DATE |
| DS_BO_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | DS_BO_LAST_UPDATE_DATE |
| PROCESSING_ORDER | NUMBER |  | 18 |  | PROCESSING_ORDER |
| CORRECTED_COUNT | NUMBER |  | 9 | Yes | CORRECTED_COUNT |
| UNPROCESSED_COUNT | NUMBER |  | 9 | Yes | UNPROCESSED_COUNT |
| ROLLBACK_ERROR_COUNT | NUMBER |  | 9 | Yes | ROLLBACK_ERROR_COUNT |
| DAT_FILE_SIZE | NUMBER |  | 18 |  | This denotes the dat file size in bytes |
| MSG_COUNT | NUMBER |  | 9 |  | This denotes the data set business object messages count. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_DATASET_DETAILS_N1 | Non Unique | Default | DATA_SET_ID, BUSINESS_OBJECT_ID |
| HRC_DL_DATASET_DETAILS_U1 | Unique | Default | DATA_SET_BUS_OBJ_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
