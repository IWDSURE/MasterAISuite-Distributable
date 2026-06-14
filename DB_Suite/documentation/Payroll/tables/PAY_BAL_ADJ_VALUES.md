# PAY_BAL_ADJ_VALUES

This table contains adjustment value information. It is a child table of PAY_BAL_ADJ_LINES.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybaladjvalues-21363.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybaladjvalues-21363.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BAL_ADJ_VALUES_PK | BAL_ADJ_VALUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BAL_ADJ_VALUE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BAL_ADJ_LINE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_BAL_ADJ_LINES. |
| INPUT_VALUE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_INPUT_VALUES_F.. |
| ENTRY_VALUE | VARCHAR2 | 60 |  |  | ENTRY_VALUE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_BAL_ADJ_VALUES_PK | Unique | Default | BAL_ADJ_VALUE_ID |
| PAY_BAL_ADJ_VALUES_U1 | Unique | Default | BAL_ADJ_LINE_ID, INPUT_VALUE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
