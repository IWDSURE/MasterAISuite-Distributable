# PAY_PRE_PAYMENTS

Pre-Payment details for an assignment, including the currency, the amount and the specific payment method.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprepayments-13584.html#payprepayments-13584](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprepayments-13584.html#payprepayments-13584)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PRE_PAYMENTS_PK | PRE_PAYMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRE_PAYMENT_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| PERSONAL_PAYMENT_METHOD_ID | NUMBER |  | 18 |  | Foreign key to PAY_PERSONAL_PAYMENT_METHODS. |
| ORG_PAYMENT_METHOD_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_ORG_PAYMENT_METHODS. |
| VALUE | NUMBER |  |  | Yes | Value of payment in target currency. |
| BASE_CURRENCY_VALUE | NUMBER |  |  |  | Payment value in base currency. |
| SOURCE_ACTION_ID | NUMBER |  | 18 |  | Foreign Key to PAY_ASSIGNMENT_ACTIONS.  Used, for example, to identify part payments for a particular run type. |
| PAYROLL_ACTION_ID | NUMBER |  | 18 |  | PAYROLL_ACTION_ID |
| THIRD_PARTY_PAYEE_ID | NUMBER |  | 18 |  | THIRD_PARTY_PAYEE_ID |
| PAYEE_ORG_PAYMENT_METHOD_ID | NUMBER |  | 18 |  | PAYEE_ORG_PAYMENT_METHOD_ID |
| EFFECTIVE_DATE | DATE |  |  |  | EFFECTIVE_DATE |
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 |  | PAYROLL_REL_ACTION_ID |
| PAYEE_BANK_ACCOUNT_ID | NUMBER |  | 18 |  | PAYEE_BANK_ACCOUNT_ID |
| PAYER_BANK_ACCOUNT_ID | NUMBER |  | 18 | Yes | PAYER_BANK_ACCOUNT_ID |
| CALC_BREAKDOWN_ID | NUMBER |  | 18 |  | CALC_BREAKDOWN_ID |
| TAX_UNIT_ID | NUMBER |  | 18 |  | TAX_UNIT_ID |
| PAYER_ORG_PAYMENT_METHOD_ID | NUMBER |  | 18 |  | PAYER_ORG_PAYMENT_METHOD_ID |
| REFERENCE_NUMBER | VARCHAR2 | 60 |  |  | Reference Number for Third Party Payment |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_PRE_PAYMENTS_FK1 | Non Unique | Default | PAYROLL_REL_ACTION_ID |
| PAY_PRE_PAYMENTS_N1 | Non Unique | Default | PERSONAL_PAYMENT_METHOD_ID |
| PAY_PRE_PAYMENTS_N3 | Non Unique | Default | ORG_PAYMENT_METHOD_ID |
| PAY_PRE_PAYMENTS_N4 | Non Unique | Default | PAYROLL_ACTION_ID |
| PAY_PRE_PAYMENTS_N5 | Non Unique | Default | CALC_BREAKDOWN_ID |
| PAY_PRE_PAYMENTS_N6 | Non Unique | Default | PAYEE_BANK_ACCOUNT_ID |
| PAY_PRE_PAYMENTS_PK | Unique | Default | PRE_PAYMENT_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
