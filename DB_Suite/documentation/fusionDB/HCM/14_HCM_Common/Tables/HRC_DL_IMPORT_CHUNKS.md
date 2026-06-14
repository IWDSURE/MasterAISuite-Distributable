# HRC_DL_IMPORT_CHUNKS

HRC_DL_IMPORT_CHUNKS table is used to hold details about chunks registered for import process. This facilitates parallel loading of data.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlimportchunks-13442.html#hrcdlimportchunks-13442](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlimportchunks-13442.html#hrcdlimportchunks-13442)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_IMPORT_CHUNKS_PK | CHUNK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHUNK_ID | NUMBER |  | 18 | Yes | CHUNK_ID |
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 | Yes | DATA_SET_BUS_OBJ_ID |
| HEADER_ID | NUMBER |  | 18 | Yes | HEADER_ID |
| START_LOGICAL_ID | NUMBER |  | 18 | Yes | START_LOGICAL_ID |
| END_LOGICAL_ID | NUMBER |  | 18 | Yes | END_LOGICAL_ID |
| CHUNK_STATUS | VARCHAR2 | 64 |  | Yes | CHUNK_STATUS |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CHUNK_TOTAL_LINE_COUNT | NUMBER |  | 10 | Yes | Total physical lines present in the chunk |
| CHUNK_SUCCESS_LINE_COUNT | NUMBER |  | 10 | Yes | Number of physical lines in a chunk that got successfully imported |
| CHUNK_ERROR_LINE_COUNT | NUMBER |  | 10 | Yes | Number of physical lines in a chunk that have import error |
| THREAD_REQUEST_ID | NUMBER |  | 10 |  | RequestId of the import child process that is processing the chunk |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_IMPORT_CHUNKS_F1 | Non Unique | Default | DATA_SET_BUS_OBJ_ID |
| HRC_DL_IMPORT_CHUNKS_U1 | Unique | Default | CHUNK_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
