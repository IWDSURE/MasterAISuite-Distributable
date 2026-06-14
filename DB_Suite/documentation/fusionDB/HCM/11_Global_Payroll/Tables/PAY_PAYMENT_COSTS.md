# PAY_PAYMENT_COSTS

This table contains the results from the Costing of Payments process to enable reconciliation with the Financials Cash Accounts.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypaymentcosts-28385.html#paypaymentcosts-28385](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypaymentcosts-28385.html#paypaymentcosts-28385)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PAYMENT_COSTS_PK | PAYMENT_COST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYMENT_COST_ID | NUMBER |  | 18 | Yes | Primary Key |
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_REL_ACTION_ID |
| PRE_PAYMENT_ID | NUMBER |  | 18 | Yes | Identifier for the Pre Payment process. |
| ACCOUNT_TYPE | VARCHAR2 | 30 |  | Yes | ACCOUNT_TYPE |
| COST_ALLOCATION_KEYFLEX_ID | NUMBER |  |  | Yes | COST_ALLOCATION_KEYFLEX_ID |
| VALUE | NUMBER |  |  | Yes | Costed amount |
| CURRENCY_CODE | VARCHAR2 | 30 |  | Yes | Currency code of costed amount |
| DEBIT_OR_CREDIT | VARCHAR2 | 30 |  | Yes | Debit or Credit. (UseLookup DEBIT_CREDIT) |
| ACCOUNTING_DATE | DATE |  |  | Yes | Payment Date or Cleared Date or Voided Date |
| SOURCE_TYPE | VARCHAR2 | 30 |  | Yes | Pre-Payment or Cheque or Magnetic Tape or Void or External/Manual Payment |
| SOURCE_ACTION_ID | NUMBER |  | 18 | Yes | AAC ID of the source |
| PAYROLL_ID | NUMBER |  | 18 | Yes | PAYROLL_ID |
| TRANSFER_TO_GL_FLAG | VARCHAR2 | 30 |  |  | Transfer the cost to GL or not |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_PAYMENT_COSTS_N1 | Non Unique | Default | PAYROLL_REL_ACTION_ID |
| PAY_PAYMENT_COSTS_N2 | Non Unique | Default | PRE_PAYMENT_ID |
| PAY_PAYMENT_COSTS_N3 | Non Unique | Default | SOURCE_ACTION_ID |
| PAY_PAYMENT_COSTS_PK | Unique | Default | PAYMENT_COST_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
