# HRC_TXN_COMMENT

Transaction Model Comment table holds the comments added by initiator at review page. The comments added into this table are populated later into the SOA BPM instance with the status updated to the table entry.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxncomment-11917.html#hrctxncomment-11917](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxncomment-11917.html#hrctxncomment-11917)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_COMMENT_PK | COMMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMMENT_ID | NUMBER |  | 18 | Yes | Primary Key and unique identifier |
| OBJECT_ID | NUMBER |  | 18 |  | Object Id |
| COMMENT_TEXT | VARCHAR2 | 2000 |  | Yes | COMMENT TEXT CONTENT |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| TASK_ID | VARCHAR2 | 64 |  |  | Stores the task id from worklist application |
| COMMENT_STATUS | VARCHAR2 | 64 |  |  | Status of the comment |
| TRANSACTION_ID | NUMBER |  | 18 |  | Foreign Key to HRC_TXN_HEADER table |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_COMMENT_N1 | Non Unique | Default | TRANSACTION_ID |
| HRC_TXN_COMMENT_PK | Unique | Default | COMMENT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
