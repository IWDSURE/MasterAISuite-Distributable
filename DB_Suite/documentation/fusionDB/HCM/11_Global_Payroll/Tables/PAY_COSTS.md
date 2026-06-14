# PAY_COSTS

This table contains cost details and values for payroll run results.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycosts-6088.html#paycosts-6088](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycosts-6088.html#paycosts-6088)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_COSTS_PK | COST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COST_ID | NUMBER |  | 18 | Yes | Surrogate primary key. |
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_REL_ACTION_ID |
| START_DATE | DATE |  |  |  | START_DATE |
| INPUT_VALUE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_INPUT_VALUES. |
| END_DATE | DATE |  |  |  | END_DATE |
| RUN_RESULT_ID | NUMBER |  | 18 |  | Foreign key to PAY_RUN_RESULTS. |
| COST_ALLOCATION_KEYFLEX_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_COST_ALLOCATION_KEYFLEX. |
| ID_FLEX_NUM | NUMBER |  |  |  | ID_FLEX_NUM |
| BALANCE_OR_COST | VARCHAR2 | 30 |  | Yes | Indicates if the record is from the cost or balancing flexfield structures. |
| COSTED_VALUE | NUMBER |  |  | Yes | Actual value to be costed. |
| DEBIT_OR_CREDIT | VARCHAR2 | 30 |  | Yes | Indicates whether the value is a debit (D) or credit (C). |
| TRANSFER_TO_GL_FLAG | VARCHAR2 | 30 |  |  | Indicates whether Cost should be Transferred to the General Ledger |
| TRANSFER_TO_PROJ_FLAG | VARCHAR2 | 30 |  |  | Indicates whether Cost should be Transferred to Projects |
| IMPORTED_TO_PROJ_FLAG | VARCHAR2 | 30 |  |  | Indicates whether Cost has been Imported to Projects |
| DISTRIBUTED_INPUT_VALUE_ID | NUMBER |  | 18 |  | Component of foreign key to Run Result Value whose costing is distributed. |
| DISTRIBUTED_RUN_RESULT_ID | NUMBER |  | 18 |  | Component of foreign key to Run Result Value whose costing is distributed. |
| SOURCE_ID | NUMBER |  | 18 |  | Points to Parent COST_ID |
| COST_TYPE | VARCHAR2 | 30 |  |  | COST_TYPE |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| SEQUENCE | NUMBER |  | 18 |  | SEQUENCE |
| SECONDARY_STATUS | VARCHAR2 | 30 |  |  | SECONDARY_STATUS |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| PAYROLL_ASSIGNMENT_ID | NUMBER |  | 18 |  | PAYROLL_ASSIGNMENT_ID |
| RETRO_ELEMENT_ENTRY_ID | NUMBER |  | 18 |  | RETRO_ELEMENT_ENTRY_ID |
| REVERSED_COST_ID | NUMBER |  | 18 |  | REVERSED_COST_ID |
| TAX_UNIT_ID | NUMBER |  | 18 |  | TAX_UNIT_ID |
| CALC_BREAKDOWN_ID | NUMBER |  | 18 |  | CALC_BREAKDOWN_ID |
| EARN_TIME_PERIOD_ID | NUMBER |  | 18 |  | EARN_TIME_PERIOD_ID |
| DEDN_TIME_PERIOD_ID | NUMBER |  | 18 |  | DEDN_TIME_PERIOD_ID |
| BASE_EARN_TIME_PERIOD_ID | NUMBER |  | 18 |  | BASE_EARN_TIME_PERIOD_ID |
| BASE_DEDN_TIME_PERIOD_ID | NUMBER |  | 18 |  | BASE_DEDN_TIME_PERIOD_ID |
| SOURCE_ELEMENT_TYPE_ID | NUMBER |  | 18 |  | SOURCE_ELEMENT_TYPE_ID |
| RUN_TYPE_ID | NUMBER |  | 18 |  | RUN_TYPE_ID |
| HOURS | NUMBER |  |  |  | HOURS |
| ORA_PART_KEY | DATE |  |  | Yes | The partition key used to determine the range interval. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_COSTS_FK1 | Non Unique | Default | PAYROLL_REL_ACTION_ID |
| PAY_COSTS_N2 | Non Unique | Default | RUN_RESULT_ID, INPUT_VALUE_ID |
| PAY_COSTS_N3 | Non Unique | Default | COST_ALLOCATION_KEYFLEX_ID |
| PAY_COSTS_PK | Unique | Default | COST_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
