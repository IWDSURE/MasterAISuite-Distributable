# PAY_LATEST_BALANCES

This table contains calculated balance values of the latest payroll relationship actions, which enable the quick balance calculations in subsequent payroll processes.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylatestbalances-28463.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylatestbalances-28463.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_LATEST_BALANCES_PK | LATEST_BALANCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LATEST_BALANCE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| DEFINED_BALANCE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_DEFINED_BALANCES. |
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_PAYROLL_REL_ACTIONS. |
| VALUE | NUMBER |  |  | Yes | Value of the Balance |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_PAY_RELATIONSHIPS_DN. |
| PAYROLL_TERM_ID | NUMBER |  | 18 |  | Foreign key to PAY_PAYROLL_TERMS. |
| PAYROLL_ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to PAY_PAYROLL_ASSIGNMENTS. |
| EXPIRY_DATE | DATE |  |  |  | Date on which the current balance value will expire |
| EXPIRED_PAYROLL_REL_ACTION_ID | NUMBER |  | 18 |  | EXPIRED_PAYROLL_REL_ACTION_ID |
| EXPIRED_VALUE | NUMBER |  |  |  | Value of Expired Balance |
| EXPIRED_DATE | DATE |  |  |  | Date on which the Expired Value Expired. |
| PREV_PAYROLL_REL_ACTION_ID | NUMBER |  | 18 |  | PREV_PAYROLL_REL_ACTION_ID |
| PREV_BALANCE_VALUE | NUMBER |  |  |  | Prevous Value of the Balance |
| PREV_EXPIRY_DATE | DATE |  |  |  | Date on which the Previous Balance Value will expire |
| TAX_UNIT_ID | NUMBER |  | 18 |  | Foreign Key the HR_ORGANIZATION_UNITS |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | LEGAL_EMPLOYER_ID |
| ELEMENT_ENTRY_ID | NUMBER |  | 18 |  | ELEMENT_ENTRY_ID |
| PAYROLL_ID | NUMBER |  | 18 |  | Payroll Id context value for balance |
| BALANCE_DATE | DATE |  |  |  | BALANCE_DATE |
| AREA1 | NUMBER |  | 18 |  | AREA1 |
| AREA2 | NUMBER |  | 18 |  | AREA2 |
| AREA3 | NUMBER |  | 18 |  | AREA3 |
| AREA4 | NUMBER |  | 18 |  | AREA4 |
| THIRD_PARTY_PAYEE_ID | NUMBER |  | 18 |  | THIRD_PARTY_PAYEE_ID |
| TIME_DEFINITION_ID | NUMBER |  | 18 |  | TIME_DEFINITION_ID |
| CALC_BREAKDOWN_ID | NUMBER |  | 18 |  | CALC_BREAKDOWN_ID |
| DEDUCTION_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to Deduction Types |
| CONTEXT_VALUE1 | VARCHAR2 | 60 |  |  | CONTEXT_VALUE1 |
| CONTEXT_VALUE2 | VARCHAR2 | 60 |  |  | CONTEXT_VALUE2 |
| CONTEXT_VALUE3 | VARCHAR2 | 60 |  |  | CONTEXT_VALUE3 |
| CONTEXT_VALUE4 | VARCHAR2 | 60 |  |  | CONTEXT_VALUE4 |
| CONTEXT_VALUE5 | VARCHAR2 | 60 |  |  | CONTEXT_VALUE5 |
| CONTEXT_VALUE6 | VARCHAR2 | 60 |  |  | CONTEXT_VALUE6 |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| STATUS | VARCHAR2 | 1 |  |  | STATUS |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_LATEST_BALANCES_N1 | Non Unique | Default | PAYROLL_REL_ACTION_ID |
| PAY_LATEST_BALANCES_N2 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID, PAYROLL_ASSIGNMENT_ID |
| PAY_LATEST_BALANCES_N3 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID, DEFINED_BALANCE_ID, PAYROLL_ASSIGNMENT_ID |
| PAY_LATEST_BALANCES_N4 | Non Unique | Default | DEFINED_BALANCE_ID |
| PAY_LATEST_BALANCES_PK | Unique | Default | LATEST_BALANCE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
