# PAY_CE_TRANSACTIONS

Populated as a result of running the payment processes to keep track of how employees were paid.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycetransactions-21431.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycetransactions-21431.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_CE_TRANSACTIONS_PK | PAYROLL_REL_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_REL_ACTION_ID |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | SOURCE_TYPE |
| PRE_PAYMENT_ID | NUMBER |  | 18 | Yes | PRE_PAYMENT_ID |
| CHECK_NUMBER | VARCHAR2 | 30 |  |  | CHECK_NUMBER |
| PAYMENT_DATE | DATE |  |  |  | PAYMENT_DATE |
| PAYER_BANK_ACCOUNT_ID | NUMBER |  | 18 | Yes | PAYER_BANK_ACCOUNT_ID |
| PAYEE_BANK_ACCOUNT_ID | NUMBER |  | 18 |  | PAYEE_BANK_ACCOUNT_ID |
| AMOUNT | NUMBER |  |  | Yes | AMOUNT |
| CURRENCY_CODE | VARCHAR2 | 15 |  | Yes | CURRENCY_CODE |
| PAYMENT_STATUS | VARCHAR2 | 15 |  | Yes | PAYMENT_STATUS |
| RECON_FLAG | VARCHAR2 | 1 |  | Yes | RECON_FLAG |
| CLEARED_DATE | DATE |  |  |  | CLEARED_DATE |
| ACTUAL_VALUE_DATE | DATE |  |  |  | ACTUAL_VALUE_DATE |
| PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_ACTION_ID |
| PAYROLL_ID | NUMBER |  | 18 |  | PAYROLL_ID |
| VOID_PAYROLL_REL_ACTION_ID | NUMBER |  | 18 |  | VOID_PAYROLL_REL_ACTION_ID |
| ORG_PAYMENT_METHOD_ID | NUMBER |  | 18 | Yes | ORG_PAYMENT_METHOD_ID |
| ORG_PAYMENT_METHOD_NAME | VARCHAR2 | 80 |  | Yes | ORG_PAYMENT_METHOD_NAME |
| PAYMENT_TYPE_ID | NUMBER |  | 18 | Yes | PAYMENT_TYPE_ID |
| BASE_PAYMENT_TYPE_ID | NUMBER |  | 18 | Yes | BASE_PAYMENT_TYPE_ID |
| LEGISLATION_CODE | VARCHAR2 | 2 |  | Yes | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| PAYMENT_TYPE_NAME | VARCHAR2 | 80 |  | Yes | PAYMENT_TYPE_NAME |
| BASE_PAYMENT_TYPE_NAME | VARCHAR2 | 80 |  | Yes | BASE_PAYMENT_TYPE_NAME |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_CE_TRANSACTIONS_N1 | Non Unique | Default | PAYER_BANK_ACCOUNT_ID, RECON_FLAG |
| PAY_CE_TRANSACTIONS_PK | Unique | Default | PAYROLL_REL_ACTION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
