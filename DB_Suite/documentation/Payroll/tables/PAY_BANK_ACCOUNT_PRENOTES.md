# PAY_BANK_ACCOUNT_PRENOTES

This is a bank account prenote table, this will be replaced when the prenote functionality is finalised.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybankaccountprenotes-19532.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybankaccountprenotes-19532.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BANK_ACCOUNT_PRENOTES_PK | BANK_ACCT_PRENOTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BANK_ACCT_PRENOTE_ID | NUMBER |  | 18 | Yes | BANK_ACCT_PRENOTE_ID |
| BANK_ACCOUNT_ID | NUMBER |  | 18 | Yes | Bank Accouhnt ID |
| PRENOTE_DATE | DATE |  |  |  | Pre Note Date |
| PRE_PAYMENT_ID | NUMBER |  | 18 |  | Pre Payment Id |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_BANK_ACCOUNT_PRENOTES_N1 | Non Unique | Default | BANK_ACCOUNT_ID |
| PAY_BANK_ACCOUNT_PRENOTES_PK | Unique | Default | BANK_ACCT_PRENOTE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
