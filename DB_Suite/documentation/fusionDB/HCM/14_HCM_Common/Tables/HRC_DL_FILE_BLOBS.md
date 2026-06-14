# HRC_DL_FILE_BLOBS

This table holds information about the blob Objects referred in a given data set.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlfileblobs-11838.html#hrcdlfileblobs-11838](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlfileblobs-11838.html#hrcdlfileblobs-11838)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_FILE_BLOBS_PK | BLOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BLOB_ID | NUMBER |  | 18 | Yes | BLOB_ID, Primary Key Column for this table |
| DATA_SET_ID | NUMBER |  | 18 | Yes | DATA_SET_ID, Foreign key reference from HRC_DL_DATA_SETS |
| LOB_FILE_NAME | VARCHAR2 | 300 |  | Yes | LOB_FILE_NAME, file name from the zip folder |
| PBLOB | BLOB |  |  |  | BLOB Content |
| PBLOB_SECURE | BLOB |  |  |  | PBLOB_SECURE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_FILE_BLOBS_U1 | Unique | Default | BLOB_ID |
| HRC_DL_FILE_BLOBS_U2 | Unique | Default | DATA_SET_ID, LOB_FILE_NAME |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
