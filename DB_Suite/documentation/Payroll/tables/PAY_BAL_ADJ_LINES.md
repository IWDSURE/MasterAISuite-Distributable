# PAY_BAL_ADJ_LINES

This table contains details of individual balance adjustment entries. It is a child table of PAY_BAL_ADJ_GROUPS.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybaladjlines-4553.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybaladjlines-4553.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BAL_ADJ_LINES_PK | BAL_ADJ_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BAL_ADJ_LINE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BAL_ADJ_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_BAL_ADJ_GROUPS. |
| BATCH_LINE_STATUS | VARCHAR2 | 30 |  | Yes | Batch line Status. Unprocessed, Processing, Complete, Incomplete. |
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 |  | Payroll Relationship Action created by the system. |
| BATCH_LINE_SEQUENCE | NUMBER |  | 18 |  | BATCH_LINE_SEQUENCE |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | PAYROLL_RELATIONSHIP_ID |
| PAYROLL_TERM_ID | NUMBER |  | 18 |  | PAYROLL_TERM_ID |
| PAYROLL_ASSIGNMENT_ID | NUMBER |  | 18 |  | PAYROLL_ASSIGNMENT_ID |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | Element type of the adjustment. |
| CALC_BREAKDOWN_ID | NUMBER |  | 18 |  | CALC_BREAKDOWN_ID |
| TAX_UNIT_ID | NUMBER |  | 18 |  | TAX_UNIT_ID |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | LEGAL_EMPLOYER_ID |
| BALANCE_DATE | DATE |  |  |  | BALANCE_DATE |
| THIRD_PARTY_PAYEE_ID | NUMBER |  | 18 |  | THIRD_PARTY_PAYEE_ID |
| TIME_DEFINITION_ID | NUMBER |  | 18 |  | TIME_DEFINITION_ID |
| COST_ALLOC_ACCOUNT_ID | NUMBER |  | 18 |  | Foreign key to pay_cost_alloc_accounts. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_BAL_ADJ_LINES_FK1 | Non Unique | Default | BAL_ADJ_GROUP_ID |
| PAY_BAL_ADJ_LINES_FK2 | Non Unique | Default | PAYROLL_REL_ACTION_ID |
| PAY_BAL_ADJ_LINES_PK | Unique | Default | BAL_ADJ_LINE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
