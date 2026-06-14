# PAY_RUN_RESULTS

This table contains the result of processing a single element entry.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrunresults-20144.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrunresults-20144.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_RUN_RESULTS_PK | RUN_RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_RESULT_ID | NUMBER |  | 18 | Yes | Primary key. |
| SEQUENCE_NUMBER | NUMBER |  | 18 |  | SEQUENCE_NUMBER |
| ELEMENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_ELEMENT_TYPES. |
| SOURCE_ID | NUMBER |  | 18 | Yes | Source element entry. |
| SOURCE_TYPE | VARCHAR2 | 1 |  | Yes | For example, E-normal entry, I-indirect result. |
| STATUS | VARCHAR2 | 2 |  | Yes | Processing status of the result. |
| ENTRY_TYPE | VARCHAR2 | 1 |  | Yes | Denormalised from element entry. |
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_REL_ACTION_ID |
| DIR_CARD_COMP_ID | NUMBER |  | 18 |  | The Component that this result is related to. |
| TAX_UNIT_ID | NUMBER |  | 18 |  | TAX_UNIT_ID |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | LEGAL_EMPLOYER_ID |
| PAYROLL_TERM_ID | NUMBER |  | 18 |  | PAYROLL_TERM_ID |
| PAYROLL_ASSIGNMENT_ID | NUMBER |  | 18 |  | PAYROLL_ASSIGNMENT_ID |
| ELEMENT_ENTRY_ID | NUMBER |  | 18 |  | Foreign key to PAY_ELEMENT_ENTRIES_F. |
| SOURCE_RESULT_ID | NUMBER |  | 18 |  | SOURCE_RESULT_ID |
| DEDUCTION_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to Deduction Types |
| START_DATE | DATE |  |  |  | Start date of the prorated result |
| END_DATE | DATE |  |  |  | End date of the Prorated result |
| PROCESSING_SPAN | NUMBER |  | 18 |  | Julian Span of the processing period. |
| AREA_CODE1 | NUMBER |  | 18 |  | AREA_CODE1 |
| AREA_CODE2 | NUMBER |  | 18 |  | AREA_CODE2 |
| AREA_CODE3 | NUMBER |  | 18 |  | AREA_CODE3 |
| AREA_CODE4 | NUMBER |  | 18 |  | AREA_CODE4 |
| TIME_DEFINITION_ID | NUMBER |  | 18 |  | Foreign key to PAY_TIME_DEFINITIONS. |
| THIRD_PARTY_PAYEE_ID | NUMBER |  | 18 |  | THIRD_PARTY_PAYEE_ID |
| CALC_BREAKDOWN_ID | NUMBER |  | 18 |  | CALC_BREAKDOWN_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| ORA_PART_KEY | DATE |  |  | Yes | The partition key used to determine the range interval. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_RUN_RESULTS_N50 | Non Unique | Default | PAYROLL_REL_ACTION_ID, TAX_UNIT_ID, AREA_CODE1, AREA_CODE2, AREA_CODE3, AREA_CODE4 |
| PAY_RUN_RESULTS_N51 | Non Unique | Default | SOURCE_ID, SOURCE_TYPE, PAYROLL_REL_ACTION_ID |
| PAY_RUN_RESULTS_N52 | Non Unique | Default | ELEMENT_ENTRY_ID, PAYROLL_REL_ACTION_ID |
| PAY_RUN_RESULTS_N53 | Non Unique | Default | ELEMENT_TYPE_ID |
| PAY_RUN_RESULTS_PK | Unique | Default | RUN_RESULT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
