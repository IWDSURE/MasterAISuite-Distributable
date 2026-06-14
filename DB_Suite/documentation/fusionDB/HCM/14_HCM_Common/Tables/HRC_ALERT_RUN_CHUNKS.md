# HRC_ALERT_RUN_CHUNKS

Contains alert run data with totals no of success, error and warning counts.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunchunks-27284.html#hrcalertrunchunks-27284](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunchunks-27284.html#hrcalertrunchunks-27284)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERT_RUN_CHUNKS_PK | RUN_CHUNK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_CHUNK_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| CHUNK_SIZE | NUMBER |  | 18 |  | Chunk Size |
| CHUNK_TYPE | VARCHAR2 | 80 |  | Yes | Chunk Type |
| CHUNK_NUM | NUMBER |  | 18 | Yes | Chunk Number |
| RUN_ID | NUMBER |  | 18 | Yes | Run Identifier. Foreign Key to HRC_ALERTS_RUNS.RUN_ID |
| CHUNK_LANGUAGE | VARCHAR2 | 80 |  |  | Chunk Language |
| STATUS | VARCHAR2 | 80 |  | Yes | Determines the status of the activity run. Valid values are defined in lookup of HRC_ALERT_RUN_STATUS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ALERT_RUN_CHUNKS_PK | Unique | Default | RUN_CHUNK_ID |
| HRC_ALERT_RUN_CHUNKS_U1 | Unique | Default | CHUNK_TYPE, CHUNK_NUM, RUN_ID, STATUS, CHUNK_LANGUAGE |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
