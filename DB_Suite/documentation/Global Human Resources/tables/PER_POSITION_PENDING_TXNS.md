# PER_POSITION_PENDING_TXNS

The table will store the data about status of changes done on different positions from Graphical Positions Ui.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpositionpendingtxns-12304.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpositionpendingtxns-12304.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_POSITION_PENDING_TXNS_PK | POS_PENDING_TXN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POS_PENDING_TXN_ID | NUMBER |  | 18 | Yes | POS_PENDING_TXN_ID |
| POSITION_ID | NUMBER |  | 18 |  | POSITION_ID |
| TRANSACTION_ID | NUMBER |  | 18 |  | TRANSACTION_ID |
| TOP_POSITION_ID | NUMBER |  | 18 |  | TOP_POSITION_ID |
| OPERATION | VARCHAR2 | 60 |  |  | OPERATION |
| STATE | VARCHAR2 | 60 |  |  | STATE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_POSITION_PENDING_TXNS_U1 | Unique | Default | POS_PENDING_TXN_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
