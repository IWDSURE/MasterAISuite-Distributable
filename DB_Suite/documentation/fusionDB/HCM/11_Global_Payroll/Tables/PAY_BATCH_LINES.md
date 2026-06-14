# PAY_BATCH_LINES

This table contains batch lines to be transferred into the live schema via the batch loader.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybatchlines-14494.html#paybatchlines-14494](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybatchlines-14494.html#paybatchlines-14494)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BATCH_LINES_PK | BATCH_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_LINE_ID | NUMBER |  | 18 | Yes | BATCH_LINE_ID |
| BATCH_ID | NUMBER |  | 18 | Yes | BATCH_ID |
| TASK_ACTION_ID | NUMBER |  | 18 | Yes | TASK_ACTION_ID |
| LINE_SEQUENCE | NUMBER |  | 6 | Yes | LINE_SEQUENCE |
| BATCH_LINE_STATUS | VARCHAR2 | 30 |  |  | BATCH_LINE_STATUS |
| GROUPING_ID | NUMBER |  | 18 |  | GROUPING_ID |
| GROUPING_VALUE | VARCHAR2 | 4000 |  |  | GROUPING_VALUE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| RECORD_ID | NUMBER |  | 18 |  | Record number |
| EFFECTIVE_START_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| RECORD_MODE | VARCHAR2 | 60 |  |  | Operation Mode of the Batch Line |
| OVN | NUMBER |  | 9 |  | ovn |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_BATCH_LINES_FK1 | Non Unique | Default | BATCH_ID |
| PAY_BATCH_LINES_N1 | Non Unique | Default | RECORD_ID |
| PAY_BATCH_LINES_N99 | Non Unique | Default | GROUPING_ID, BATCH_ID |
| PAY_BATCH_LINES_PK | Unique | Default | BATCH_LINE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
