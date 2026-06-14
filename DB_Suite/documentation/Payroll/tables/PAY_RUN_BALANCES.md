# PAY_RUN_BALANCES

This table contains calculated run-level balance values, which are used for performant balance calculations.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrunbalances-15221.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrunbalances-15221.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_RUN_BALANCES_PK | RUN_BALANCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_BALANCE_ID | NUMBER |  | 18 | Yes | System generated primary key |
| DEFINED_BALANCE_ID | NUMBER |  | 18 | Yes | Foreign key to pay_defined_balances. |
| EFFECTIVE_DATE | DATE |  |  | Yes | Effective date of the associated payroll action. |
| BALANCE_VALUE | NUMBER |  |  | Yes | The balance value. |
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 |  | PAYROLL_REL_ACTION_ID |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | PAYROLL_RELATIONSHIP_ID |
| PAYROLL_TERM_ID | NUMBER |  | 18 |  | PAYROLL_TERM_ID |
| PAYROLL_ASSIGNMENT_ID | NUMBER |  | 18 |  | PAYROLL_ASSIGNMENT_ID |
| ACTION_SEQUENCE | NUMBER |  | 18 |  | The action sequence for the assignment action id. |
| PAYROLL_ACTION_ID | NUMBER |  | 18 |  | Associated payroll action id. |
| TAX_UNIT_ID | NUMBER |  | 18 |  | Government Reporting Entity, or Legal Entity context value for the balance. |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | LEGAL_EMPLOYER_ID |
| ELEMENT_ENTRY_ID | NUMBER |  | 18 |  | ELEMENT_ENTRY_ID |
| PAYROLL_ID | NUMBER |  | 18 |  | PAYROLL_ID |
| BALANCE_DATE | DATE |  |  |  | Value of the Balance Date Context |
| AREA1 | NUMBER |  | 18 |  | AREA1 |
| AREA2 | NUMBER |  | 18 |  | AREA2 |
| AREA3 | NUMBER |  | 18 |  | AREA3 |
| AREA4 | NUMBER |  | 18 |  | AREA4 |
| THIRD_PARTY_PAYEE_ID | NUMBER |  | 18 |  | THIRD_PARTY_PAYEE_ID |
| TIME_DEFINITION_ID | NUMBER |  | 18 |  | Foreign Key to PAY_TIME_DEFINITIONS. |
| CALC_BREAKDOWN_ID | NUMBER |  | 18 |  | The Calculation Breakdown |
| PROCESSING_SPAN | NUMBER |  | 18 |  | The Julian Processing Span of the balance |
| DEDUCTION_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to Deduction Types |
| CONTEXT_VALUE1 | VARCHAR2 | 60 |  |  | CONTEXT_VALUE1 |
| CONTEXT_VALUE2 | VARCHAR2 | 60 |  |  | CONTEXT_VALUE2 |
| CONTEXT_VALUE3 | VARCHAR2 | 60 |  |  | CONTEXT_VALUE3 |
| CONTEXT_VALUE4 | VARCHAR2 | 60 |  |  | CONTEXT_VALUE4 |
| CONTEXT_VALUE5 | VARCHAR2 | 60 |  |  | CONTEXT_VALUE5 |
| CONTEXT_VALUE6 | VARCHAR2 | 60 |  |  | CONTEXT_VALUE6 |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| ORA_PART_KEY | DATE |  |  | Yes | The partition key used to determine the range interval. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_RUN_BALANCES_N1 | Non Unique | Default | PAYROLL_ASSIGNMENT_ID, DEFINED_BALANCE_ID, EFFECTIVE_DATE |
| PAY_RUN_BALANCES_N2 | Non Unique | Default | PAYROLL_REL_ACTION_ID, DEFINED_BALANCE_ID |
| PAY_RUN_BALANCES_N3 | Non Unique | Default | DEFINED_BALANCE_ID, TAX_UNIT_ID, EFFECTIVE_DATE |
| PAY_RUN_BALANCES_N4 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID, DEFINED_BALANCE_ID, EFFECTIVE_DATE, ACTION_SEQUENCE |
| PAY_RUN_BALANCES_N5 | Non Unique | Default | PAYROLL_ACTION_ID, DEFINED_BALANCE_ID, EFFECTIVE_DATE |
| PAY_RUN_BALANCES_PK | Unique | Default | RUN_BALANCE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
