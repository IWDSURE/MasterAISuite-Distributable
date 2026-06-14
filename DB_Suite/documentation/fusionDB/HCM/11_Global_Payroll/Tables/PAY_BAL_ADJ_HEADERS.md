# PAY_BAL_ADJ_HEADERS

This table contains balance adjustment batch headers

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybaladjheaders-22658.html#paybaladjheaders-22658](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybaladjheaders-22658.html#paybaladjheaders-22658)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BAL_ADJ_HEADERS_PK | BAL_ADJ_BATCH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BAL_ADJ_BATCH_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| BATCH_NUMBER | VARCHAR2 | 80 |  | Yes | Batch Number or Name |
| BATCH_STATUS | VARCHAR2 | 30 |  | Yes | Batch Status. Unprocessed, Processing, Complete, Incomplete. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_BAL_ADJ_HEADERS_PK | Unique | Default | BAL_ADJ_BATCH_ID |
| PAY_BAL_ADJ_HEADERS_U1 | Unique | Default | BATCH_NUMBER, LEGISLATIVE_DATA_GROUP_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
