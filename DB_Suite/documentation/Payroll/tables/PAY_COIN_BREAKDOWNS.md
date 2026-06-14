# PAY_COIN_BREAKDOWNS

The table holds the details of any Cash Payments with the breakdown on the currency amounts needed.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycoinbreakdowns-13781.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycoinbreakdowns-13781.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_COIN_BREAKDOWNS_PK | COIN_BREAKDOWN_ID |

## Columns

| Name | Datatype | Precision | Not-null | Comments |
|---|---|---|---|---|
| COIN_BREAKDOWN_ID | NUMBER | 18 | Yes | COIN_BREAKDOWN_ID |
| PRE_PAYMENT_ID | NUMBER | 18 | Yes | PRE_PAYMENT_ID |
| MONETARY_UNIT_ID | NUMBER | 18 | Yes | MONETARY_UNIT_ID |
| NUMBER_OF_MONETARY_UNITS | NUMBER | 18 | Yes | NUMBER_OF_MONETARY_UNITS |
| ENTERPRISE_ID | NUMBER | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_COIN_BREAKDOWNS_N1 | Non Unique | Default | PRE_PAYMENT_ID |
| PAY_COIN_BREAKDOWNS_PK | Unique | Default | COIN_BREAKDOWN_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
