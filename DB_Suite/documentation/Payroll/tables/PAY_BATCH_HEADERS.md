# PAY_BATCH_HEADERS

This table contains header information that defines the contents of a batch to be transferred into the live schema.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybatchheaders-5689.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybatchheaders-5689.html)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_ID | NUMBER |  | 18 | Yes | BATCH_ID |
| BATCH_NAME | VARCHAR2 | 100 |  | Yes | Name of the batch (non-unique). |
| BATCH_STATUS | VARCHAR2 | 30 |  |  | Shows the status the batch is currently in. |
| PAY_REQUEST_ID | NUMBER |  | 18 | Yes | PAY_REQUEST_ID is the FK to PAY_REQUESTS table |
| BATCH_SOURCE_ID | NUMBER |  | 18 |  | BATCH_SOURCE_ID |
| BATCH_SOURCE | VARCHAR2 | 30 |  |  | BATCH_SOURCE |
| BATCH_SOURCE_CATEGORY | VARCHAR2 | 30 |  |  | BATCH_SOURCE_CATEGORY |
| UPLOAD_DATE | DATE |  |  |  | Upload Date |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BATCH_CONTENT | CLOB |  |  |  | File data for Load Batch from File |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_BATCH_HEADERS_PK | Unique | Default | BATCH_ID |
| PAY_BATCH_HEADERS_U1 | Unique | Default | BATCH_NAME, LEGISLATIVE_DATA_GROUP_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
