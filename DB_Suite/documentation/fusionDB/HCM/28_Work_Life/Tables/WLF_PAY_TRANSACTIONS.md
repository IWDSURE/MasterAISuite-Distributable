# WLF_PAY_TRANSACTIONS

Table to store details of payment transactions.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpaytransactions-17728.html#wlfpaytransactions-17728](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpaytransactions-17728.html#wlfpaytransactions-17728)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PAY_TRANSACTIONS_PK | PAYMENT_TRANSACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYMENT_TRANSACTION_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| PAY_SYSTEM_ORDER_NUMBER | VARCHAR2 | 250 |  |  | Indicates payment external reference id. |
| AUTHORIZATION_STATUS_CODE | VARCHAR2 | 250 |  |  | Indicates transaction authorization status code. |
| TRANSACTION_PERFORMEDBY_ID | NUMBER |  | 18 |  | Indicates transaction performed by id. |
| ASSIGNMENT_RECORD_ID | NUMBER |  | 18 |  | Indicates assignment record id for which payment is made. |
| TRANSACTION_DATE | TIMESTAMP |  |  |  | Indicates date on which transaction is made. |
| EXTERNAL_IDENTIFIER_TYPE | VARCHAR2 | 30 |  |  | Indicates payment external identifier type. |
| EXTERNAL_IDENTIFIER | VARCHAR2 | 250 |  |  | Indicates payment external identifier. |
| TRANSACTION_TYPE | VARCHAR2 | 30 |  |  | Indicates transaction type of payment. |
| TRXN_EXTENSION_ID | NUMBER |  | 18 |  | Indicates transaction type of extension id. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| COMMENTS | VARCHAR2 | 4000 |  |  | This column stores comments for the payment transaction |
| TRANSACTION_AMOUNT | NUMBER |  |  |  | This column stores amount for the payment transaction |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | This column stores currency code for the payment transaction |
| REASON_CODE | VARCHAR2 | 30 |  |  | This column stores reason code of refund transaction |
| STATUS | VARCHAR2 | 30 |  |  | This column stores status of transaction |
| PROCESSED_BY | NUMBER |  | 18 |  | Indicates user who processed the transaction |
| RELATED_PAY_TRANSACTION_ID | NUMBER |  | 18 |  | RELATED_PAY_TRANSACTION_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PAY_TRANSACTIONS_N1 | Non Unique | Default | ASSIGNMENT_RECORD_ID |
| WLF_PAY_TRANSACTIONS_U1 | Unique | Default | PAYMENT_TRANSACTION_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
