# PAY_QUICKPAY_CIR_EXCLUSIONS

This table contains a list of element entries that are to be excluded from a QuickPay run.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payquickpaycirexclusions-20424.html#payquickpaycirexclusions-20424](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payquickpaycirexclusions-20424.html#payquickpaycirexclusions-20424)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_QUICKPAY_CIR_EXCLUSIONS_PK | ACTION_ID, OBJECT_ID, ACTION_TYPE, OBJECT_TYPE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_ID | NUMBER |  | 18 | Yes | Foreign key to the Object. |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Object Type of the Object ID |
| ACTION_ID | NUMBER |  | 18 | Yes | Foreign Key to the Action |
| ACTION_TYPE | VARCHAR2 | 30 |  | Yes | Action Type of the Action_IS |
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
| PAY_QUICKPAY_CIR_EXCLUSIONS_N1 | Non Unique | Default | PAY_REQUEST_ID |
| PAY_QUICKPAY_CIR_EXCLUSIONS_PK | Unique | Default | ACTION_ID, OBJECT_ID, ACTION_TYPE, OBJECT_TYPE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
