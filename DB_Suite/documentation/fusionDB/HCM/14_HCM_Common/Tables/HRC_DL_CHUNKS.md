# HRC_DL_CHUNKS

HRC_DL_CHUNKS table is used to hold details about chunks registered for load process. This facilitates parallel loading of data.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlchunks-23487.html#hrcdlchunks-23487](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlchunks-23487.html#hrcdlchunks-23487)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_CHUNKS_PK | CHUNK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHUNK_ID | NUMBER |  | 18 | Yes | CHUNK_ID |
| CHUNK_STATUS | VARCHAR2 | 64 |  |  | CHUNK_STATUS |
| PROCESS_ID | NUMBER |  | 18 | Yes | PROCESS_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_CHUNKS_F1 | Non Unique | Default | PROCESS_ID |
| HRC_DL_CHUNKS_PK | Unique | Default | CHUNK_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
