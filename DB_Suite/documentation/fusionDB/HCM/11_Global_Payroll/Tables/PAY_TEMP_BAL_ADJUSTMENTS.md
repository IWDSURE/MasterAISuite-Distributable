# PAY_TEMP_BAL_ADJUSTMENTS

This table contains temporary balance adjustment records, created by the Balance Initialization process, to calculate correct balance values to adjust. The records are deleted on completion of the process.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytempbaladjustments-4179.html#paytempbaladjustments-4179](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytempbaladjustments-4179.html#paytempbaladjustments-4179)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TEMP_BAL_ADJUSTMENTS_PK | BATCH_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_LINE_ID | NUMBER |  | 18 | Yes | BATCH_LINE_ID |
| BALANCE_TYPE_ID | NUMBER |  | 18 |  | BALANCE_TYPE_ID |
| BALANCE_DIMENSION_ID | NUMBER |  | 18 |  | BALANCE_DIMENSION_ID |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | ELEMENT_TYPE_ID |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | INPUT_VALUE_ID |
| ADJUSTMENT_DATE | DATE |  |  |  | ADJUSTMENT_DATE |
| ADJUSTMENT_AMOUNT | NUMBER |  |  |  | ADJUSTMENT_AMOUNT |
| PAYROLL_TERM_ID | NUMBER |  | 18 |  | PAYROLL_TERM_ID |
| PAYROLL_ASSIGNMENT_ID | NUMBER |  | 18 |  | PAYROLL_ASSIGNMENT_ID |
| TAX_UNIT_ID | NUMBER |  | 18 |  | TAX_UNIT_ID |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | LEGAL_EMPLOYER_ID |
| ELEMENT_ENTRY_ID | NUMBER |  | 18 |  | ELEMENT_ENTRY_ID |
| PAYROLL_ID | NUMBER |  | 18 |  | PAYROLL_ID |
| AREA1 | NUMBER |  | 18 |  | AREA1 |
| AREA2 | NUMBER |  | 18 |  | AREA2 |
| AREA3 | NUMBER |  | 18 |  | AREA3 |
| AREA4 | NUMBER |  | 18 |  | AREA4 |
| THIRD_PARTY_PAYEE_ID | NUMBER |  | 18 |  | THIRD_PARTY_PAYEE_ID |
| TIME_DEFINITION_ID | NUMBER |  | 18 |  | TIME_DEFINITION_ID |
| CALC_BREAKDOWN_ID | NUMBER |  | 18 |  | CALC_BREAKDOWN_ID |
| BALANCE_DATE | DATE |  |  |  | BALANCE_DATE |
| DEDUCTION_TYPE_ID | NUMBER |  | 18 |  | Deduction Type ID. |
| PROCESSING_SPAN | NUMBER |  | 18 |  | Processing Span. |
| CONTEXT1_ID | NUMBER |  | 18 |  | CONTEXT1_ID |
| CONTEXT1_VALUE | VARCHAR2 | 60 |  |  | CONTEXT1_VALUE |
| CONTEXT2_ID | NUMBER |  | 18 |  | CONTEXT2_ID |
| CONTEXT2_VALUE | VARCHAR2 | 60 |  |  | CONTEXT2_VALUE |
| CONTEXT3_ID | NUMBER |  | 18 |  | CONTEXT3_ID |
| CONTEXT3_VALUE | VARCHAR2 | 60 |  |  | CONTEXT3_VALUE |
| CONTEXT4_ID | NUMBER |  | 18 |  | CONTEXT4_ID |
| CONTEXT4_VALUE | VARCHAR2 | 60 |  |  | CONTEXT4_VALUE |
| CONTEXT5_ID | NUMBER |  | 18 |  | CONTEXT5_ID |
| CONTEXT5_VALUE | VARCHAR2 | 60 |  |  | CONTEXT5_VALUE |
| CONTEXT6_ID | NUMBER |  | 18 |  | CONTEXT6_ID |
| CONTEXT6_VALUE | VARCHAR2 | 60 |  |  | CONTEXT6_VALUE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_TEMP_BAL_ADJUSTMENTS_N1 | Non Unique | Default | BALANCE_TYPE_ID, ADJUSTMENT_DATE |
| PAY_TEMP_BAL_ADJUSTMENTS_PK | Unique | Default | BATCH_LINE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
