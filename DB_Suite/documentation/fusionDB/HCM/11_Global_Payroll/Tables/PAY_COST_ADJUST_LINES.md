# PAY_COST_ADJUST_LINES

This table contains details of what was changed as a result of a costing adjustment.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycostadjustlines-12393.html#paycostadjustlines-12393](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycostadjustlines-12393.html#paycostadjustlines-12393)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_COST_ADJUST_LINES_PK | COST_ADJUST_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COST_ADJUST_LINE_ID | NUMBER |  | 18 | Yes | COST_ADJUST_LINE_ID |
| COST_ADJUSTMENT_ID | NUMBER |  | 18 | Yes | COST_ADJUSTMENT_ID |
| DEBIT_OR_CREDIT | VARCHAR2 | 30 |  | Yes | DEBIT_OR_CREDIT |
| COST_ID | NUMBER |  | 18 |  | COST_ID |
| LINE_VALUE | NUMBER |  |  |  | LINE_VALUE |
| LINE_START_DATE | DATE |  |  |  | LINE_START_DATE |
| LINE_END_DATE | DATE |  |  |  | LINE_END_DATE |
| COST_ALLOCATION_KEYFLEX_ID | NUMBER |  | 18 |  | COST_ALLOCATION_KEYFLEX_ID |
| ID_FLEX_NUM | NUMBER |  |  |  | ID_FLEX_NUM |
| REVERSAL_ENTRY_FLAG | VARCHAR2 | 1 |  |  | REVERSAL_ENTRY_FLAG |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_COST_ADJUST_LINES_N1 | Non Unique | Default | COST_ADJUSTMENT_ID |
| PAY_COST_ADJUST_LINES_PK | Unique | Default | COST_ADJUST_LINE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
