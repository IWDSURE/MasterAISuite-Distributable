# PAY_ADJUSTED_COSTING_DETAILS

This table contains adjusted costing details.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payadjustedcostingdetails-11815.html#payadjustedcostingdetails-11815](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payadjustedcostingdetails-11815.html#payadjustedcostingdetails-11815)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ADJUSTED_COSTING_DETA_PK | ADJUSTED_COSTING_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ADJUSTED_COSTING_DETAIL_ID | NUMBER |  | 18 | Yes | ADJUSTED_COSTING_DETAILS_ID |
| ADJUSTMENT_ROW | VARCHAR2 | 1 |  |  | ADJUSTMENT_ROW |
| COST_ID | NUMBER |  | 18 | Yes | COST_ID |
| RUN_RESULT_ID | NUMBER |  | 18 |  | RUN_RESULT_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| EMPLOYMENT_TERM | VARCHAR2 | 80 |  |  | EMPLOYMENT_TERM |
| ASSIGNMENT_TYPE | VARCHAR2 | 80 |  |  | ASSIGNMENT_TYPE |
| ENTRY_TYPE | VARCHAR2 | 80 |  |  | ENTRY_TYPE |
| MESSAGE | VARCHAR2 | 2000 |  |  | MESSAGE |
| LINE_START_DATE | DATE |  |  |  | LINE_START_DATE |
| LINE_END_DATE | DATE |  |  |  | LINE_END_DATE |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| COST_ALLOCATION_KEYFLEX_ID | NUMBER |  | 18 |  | COST_ALLOCATION_KEYFLEX_ID |
| ID_FLEX_NUM | NUMBER |  |  |  | ID_FLEX_NUM |
| ELEMENT_NAME | VARCHAR2 | 80 |  |  | ELEMENT_NAME |
| OUTPUT_CURRENCY_CODE | VARCHAR2 | 15 |  |  | OUTPUT_CURRENCY_CODE |
| UOM | VARCHAR2 | 80 |  |  | UOM |
| INPUT_VALUE_NAME | VARCHAR2 | 80 |  |  | INPUT_VALUE_NAME |
| MONEY_DEBIT | NUMBER |  |  |  | MONEY_DEBIT |
| MONEY_CREDIT | NUMBER |  |  |  | MONEY_CREDIT |
| HOURS_DEBIT | NUMBER |  |  |  | HOURS_DEBIT |
| HOURS_CREDIT | NUMBER |  |  |  | HOURS_CREDIT |
| DEBIT_OR_CREDIT | VARCHAR2 | 30 |  |  | DEBIT_OR_CREDIT |
| LINE_VALUE | NUMBER |  |  |  | LINE_VALUE |
| REVERSAL_ENTRY_FLAG | VARCHAR2 | 1 |  |  | REVERSAL_ENTRY_FLAG |
| COST_ADJUST_LINE_ID | NUMBER |  | 18 |  | COST_ADJUST_LINE_ID |
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 |  | PAYROLL_REL_ACTION_ID |
| SECONDARY_STATUS | VARCHAR2 | 30 |  |  | SECONDARY_STATUS |
| CONCATENATED_SEGMENTS | VARCHAR2 | 2000 |  |  | CONCATENATED_SEGMENTS |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Columns |
|---|---|---|
| PAY_ADJUSTED_COSTING_DETA_PK | Unique | ADJUSTED_COSTING_DETAIL_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
