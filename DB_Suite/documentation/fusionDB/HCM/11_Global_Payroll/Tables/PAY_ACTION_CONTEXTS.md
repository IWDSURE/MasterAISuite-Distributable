# PAY_ACTION_CONTEXTS

This table contains the payroll relationship action contexts used and processed for an employee.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactioncontexts-7414.html#payactioncontexts-7414](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactioncontexts-7414.html#payactioncontexts-7414)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ACTION_CONTEXTS_PK | ACTION_CONTEXT_ID |

## Columns

| Name | Datatype | Precision | Not-null | Comments |
|---|---|---|---|---|
| ACTION_CONTEXT_ID | NUMBER | 18 | Yes | ACTION_CONTEXT_ID |
| PAYROLL_REL_ACTION_ID | NUMBER | 18 | Yes | PAYROLL_REL_ACTION_ID |
| PAYROLL_TERM_ID | NUMBER | 18 |  | PAYROLL_TERM_ID |
| PAYROLL_ASSIGNMENT_ID | NUMBER | 18 |  | PAYROLL_ASSIGNMENT_ID |
| TAX_UNIT_ID | NUMBER | 18 |  | TAX_UNIT_ID |
| LEGAL_EMPLOYER_ID | NUMBER | 18 |  | LEGAL_EMPLOYER_ID |
| AREA1 | NUMBER | 18 |  | AREA1 |
| AREA2 | NUMBER | 18 |  | AREA2 |
| AREA3 | NUMBER | 18 |  | AREA3 |
| AREA4 | NUMBER | 18 |  | AREA4 |
| BALANCE_DATE | DATE |  |  | BALANCE_DATE |
| THIRD_PARTY_PAYEE_ID | NUMBER | 18 |  | THIRD_PARTY_PAYEE_ID |
| TIME_DEFINITION_ID | NUMBER | 18 |  | TIME_DEFINITION_ID |
| CALC_BREAKDOWN_ID | NUMBER | 18 |  | CALC_BREAKDOWN_ID |
| PROCESSING_SPAN | NUMBER | 18 |  | The Julian span of the processing peroid |
| DEDUCTION_TYPE_ID | NUMBER | 18 |  | Foreign Key to Deduction Types |
| ENTERPRISE_ID | NUMBER | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ACTION_CONTEXTS_FK1 | Non Unique | Default | PAYROLL_REL_ACTION_ID |
| PAY_ACTION_CONTEXTS_PK | Unique | Default | ACTION_CONTEXT_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
