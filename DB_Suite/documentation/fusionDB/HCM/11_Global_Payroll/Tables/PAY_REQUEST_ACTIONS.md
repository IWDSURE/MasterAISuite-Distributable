# PAY_REQUEST_ACTIONS

This table contains details of the requests made to process batch payroll processes.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrequestactions-22749.html#payrequestactions-22749](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrequestactions-22749.html#payrequestactions-22749)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REQUEST_ACTIONS_PK | PAY_REQUEST_ID, PAYROLL_ACTION_ID |

## Columns

| Name | Datatype | Precision | Not-null | Comments |
|---|---|---|---|---|
| PAY_REQUEST_ID | NUMBER | 18 | Yes | PAY_REQUEST_ID |
| PAYROLL_ACTION_ID | NUMBER | 18 | Yes | PAYROLL_ACTION_ID |
| ENTERPRISE_ID | NUMBER | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_REQUEST_ACTIONS_PK | Unique | Default | PAY_REQUEST_ID, PAYROLL_ACTION_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
