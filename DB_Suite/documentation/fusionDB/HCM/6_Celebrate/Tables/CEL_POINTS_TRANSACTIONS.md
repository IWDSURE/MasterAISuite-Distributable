# CEL_POINTS_TRANSACTIONS

Stores transaction details of points received and sent

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celpointstransactions-27769.html#celpointstransactions-27769](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celpointstransactions-27769.html#celpointstransactions-27769)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_POINTS_TRANSACTIONS_PK | TRANSACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TRANSACTION_ID | NUMBER |  | 18 | Yes | Unique identifier for a transaction |
| TRANSACTION_CODE | VARCHAR2 | 30 |  | Yes | Type of transaction |
| PERSON_ID | NUMBER |  | 18 |  | Unique identifier for a person |
| OTHER_PERSON_ID | NUMBER |  | 18 |  | Unique identifier of the other person in the transaction |
| POINTS | NUMBER |  |  | Yes | Points |
| POINTS_DATE | DATE |  |  |  | Points date |
| RECOGNITION_ID | NUMBER |  | 18 |  | Unique identifier of a recognition |
| PROGRAM_ID | NUMBER |  | 18 |  | Unique identifier of a program |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_POINTS_TRANSACTIONS_N1 | Non Unique | Default | PERSON_ID, TRANSACTION_CODE |
| CEL_POINTS_TRANSACTIONS_N2 | Non Unique | Default | OTHER_PERSON_ID, TRANSACTION_CODE |
| CEL_POINTS_TRANSACTIONS_PK | Unique | Default | TRANSACTION_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
