# WLF_GRW_PROCESSING_DETAILS

Table to store status and errors of reconcile role guides processing information.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwprocessingdetails-17592.html#wlfgrwprocessingdetails-17592](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwprocessingdetails-17592.html#wlfgrwprocessingdetails-17592)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_GRW_PROCESSING_DETAILS_PK | PROCESSING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESSING_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| GROW_OBJECT_ID | NUMBER |  | 18 | Yes | Reference to the grow object id. Example Role Guide Id |
| GROW_OBJECT_TYPE | VARCHAR2 | 32 |  |  | Reference to grow object type. Example Role Guide |
| IS_RECONCILE_READY | VARCHAR2 | 1 |  |  | Indicator to provide hint whether learn object is grow to  be reconciled. |
| LATEST_PROCESSED_DATE | TIMESTAMP |  |  |  | The date when grow object is last reconciled. |
| LATEST_PROCESSING_STATUS | VARCHAR2 | 32 |  |  | The status of last reconciliation |
| LATEST_JOB_ID | NUMBER |  | 18 |  | The latest job id that processed the grow object |
| LAST_SUCC_PROCESSED_DATE | TIMESTAMP |  |  |  | The date when grow object is last reconciled successfully. |
| LAST_SUCC_JOB_ID | NUMBER |  | 18 |  | The job id of last successful reconcile of grow object |
| JOB_NAME | VARCHAR2 | 32 |  |  | Name of the process or Job |
| LOG | VARCHAR2 | 4000 |  |  | Log for the grow assignments reconcile action |
| ERROR_LOG | CLOB |  |  |  | Contains error information about the failed call when grow object is reconciled. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_GRW_PROCESSING_DETAILS_U1 | Unique | Default | PROCESSING_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
