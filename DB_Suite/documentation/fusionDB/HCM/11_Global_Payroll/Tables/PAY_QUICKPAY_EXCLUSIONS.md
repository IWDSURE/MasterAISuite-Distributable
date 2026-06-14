# PAY_QUICKPAY_EXCLUSIONS

This table contains a list of element entries that are to be excluded from a QuickPay run.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payquickpayexclusions-27381.html#payquickpayexclusions-27381](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payquickpayexclusions-27381.html#payquickpayexclusions-27381)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_QUICKPAY_EXCLUSIONS_PK | PAYROLL_REL_ACTION_ID, ELEMENT_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELEMENT_ENTRY_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_ELEMENT_ENTRIES. |
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_REL_ACTION_ID |
| PAY_REQUEST_ID | NUMBER |  | 18 |  | PAY_REQUEST_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_QUICKPAY_EXCLUSIONS_N1 | Non Unique | Default | PAY_REQUEST_ID |
| PAY_QUICKPAY_EXCLUSIONS_PK | Unique | Default | PAYROLL_REL_ACTION_ID, ELEMENT_ENTRY_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
