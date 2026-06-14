# HRC_TXN_CHILD_OBJECTS

Transaction Model table: stores one row for each database row that the parent transaction will change. It is used to detect concurrent changes where traditional database locking can't reach.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnchildobjects-6364.html#hrctxnchildobjects-6364](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnchildobjects-6364.html#hrctxnchildobjects-6364)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_CHILD_OBJECTS_PK | CHILD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHILD_ID | NUMBER |  | 18 | Yes | the primary key column |
| OVN_AT_SUBMIT | NUMBER |  | 9 |  | The OVN of the child record at the time of submit |
| PARENT_TXN_ID | NUMBER |  | 18 | Yes | The transaction which this change is part of. Foreign key to hrc_txn_header transaction_id |
| PARENT_OBJ_ID | NUMBER |  | 18 | Yes | The ObjectId from the transaction this is part of |
| CHILD_OBJ | VARCHAR2 | 100 |  | Yes | The table name of the row being changed |
| CHILD_OBJ_ID | NUMBER |  | 18 | Yes | The primary key value of the row being changed |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_CHILD_OBJECTS_N1 | Non Unique | Default | PARENT_TXN_ID |
| HRC_TXN_CHILD_OBJECTS_N2 | Non Unique | Default | CHILD_OBJ, CHILD_OBJ_ID |
| HRC_TXN_CHILD_OBJECTS_U1 | Unique | Default | CHILD_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
