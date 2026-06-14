# PAY_BATCH_LINE_VALUES

This table contains individual values of a parameter in a batch line used in the generic batch loader.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybatchlinevalues-23417.html#paybatchlinevalues-23417](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybatchlinevalues-23417.html#paybatchlinevalues-23417)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BATCH_LINE_VALUES_PK | BATCH_LINE_VALUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_LINE_VALUE_ID | NUMBER |  | 18 | Yes | BATCH_LINE_VALUE_ID |
| BATCH_LINE_ID | NUMBER |  | 18 | Yes | BATCH_LINE_ID |
| ACTION_PARAMETER_ID | NUMBER |  | 18 | Yes | ACTION_PARAMETER_ID |
| ACTION_PARAMETER_VALUE | VARCHAR2 | 4000 |  | Yes | ACTION_PARAMETER_VALUE |
| SEQUENCE | NUMBER |  | 18 |  | SEQUENCE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_BATCH_LINE_VALUES_FK1 | Non Unique | Default | BATCH_LINE_ID |
| PAY_BATCH_LINE_VALUES_PK | Unique | Default | BATCH_LINE_VALUE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
