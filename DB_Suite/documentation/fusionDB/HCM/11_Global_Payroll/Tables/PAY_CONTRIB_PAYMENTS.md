# PAY_CONTRIB_PAYMENTS

Stores details of payments made to third party from multiple sources. For example, if a number of employees all contribute to a single payment made by the company on their behalf.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycontribpayments-21071.html#paycontribpayments-21071](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycontribpayments-21071.html#paycontribpayments-21071)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_CONTRIB_PAYMENTS_PK | CONTRIBUTING_PRE_PAYMENT_ID |

## Columns

| Name | Datatype | Precision | Not-null | Comments |
|---|---|---|---|---|
| PAYROLL_ACTION_ID | NUMBER | 18 | Yes | PAYROLL_ACTION_ID |
| CONTRIBUTING_PRE_PAYMENT_ID | NUMBER | 18 | Yes | CONTRIBUTING_PRE_PAYMENT_ID |
| PRE_PAYMENT_ID | NUMBER | 18 |  | PRE_PAYMENT_ID |
| PAYROLL_RELATIONSHIP_ACTION_ID | NUMBER | 18 | Yes | PAYROLL_RELATIONSHIP_ACTION_ID |
| ENTERPRISE_ID | NUMBER | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_CONTRIB_PAYMENTS_FK1 | Non Unique | Default | PRE_PAYMENT_ID |
| PAY_CONTRIB_PAYMENTS_PK | Unique | Default | CONTRIBUTING_PRE_PAYMENT_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
