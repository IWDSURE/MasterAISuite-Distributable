# PAY_MIG_STD_TEMPL_QUES

This table contains the superset of questions used across the relevant element templates, including both core and legislative extensions to those questions. However, questions that apply to an Oracle Fusion element only are included in the main element staging table.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paymigstdtemplques-27264.html#paymigstdtemplques-27264](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paymigstdtemplques-27264.html#paymigstdtemplques-27264)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_MIG_STD_TEMPL_QUES_PK | STANDARD_TEMPLATE_QUESTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STANDARD_TEMPLATE_QUESTION_ID | NUMBER |  | 18 | Yes | Primary key. |
| STAGING_ELEMENTS_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_MIG_STAGING_ELEMENTS. |
| SOURCE_ELEMENT_NAME | VARCHAR2 | 18 |  | Yes | Populated with whatever is considered the unique name of the earnings definition. |
| ELEMENT_NAME | VARCHAR2 | 80 |  |  | Name of element in migration staging area parent table. |
| PROCESS_SEPARATELY_FLAG | VARCHAR2 | 30 |  |  | Process separately element Y/N. |
| DEDUCTION_PROCESS_OPTION | VARCHAR2 | 30 |  |  | Which deductions apply to this earning? |
| CALCULATION_RULE | VARCHAR2 | 30 |  | Yes | What is the calculation rule? |
| AMOUNT_CALCULATION_SOURCE | VARCHAR2 | 30 |  | Yes | How do you want to derive the amount? |
| AMOUNT_PAY_SOURCE | VARCHAR2 | 30 |  |  | Select the amount pay source |
| AMOUNT_USER_TABLE | VARCHAR2 | 30 |  |  | Amount User Table |
| AMOUNT_USER_COLUMN | VARCHAR2 | 30 |  |  | Amount User Column |
| AMOUNT_USER_ROW | VARCHAR2 | 30 |  |  | Amount User Row |
| CALCULATION_SOURCE_BAL | VARCHAR2 | 160 |  |  | Calculation Source Balance |
| CALC_SOURCE_DEF_BAL_ID | NUMBER |  | 18 |  | Foreign key to PAY_DEFINED_BALANCES.DEFINED_BALANCE_ID. |
| EARNINGS_PAY_SOURCE | VARCHAR2 | 30 |  |  | Earnings Pay Source |
| EARNINGS_USER_TABLE | VARCHAR2 | 30 |  |  | Earnings User Table |
| EARNINGS_USER_COLUMN | VARCHAR2 | 30 |  |  | Earnings User Column |
| EARNINGS_USER_ROW | VARCHAR2 | 30 |  |  | Earnings User Row |
| ET_TIME_DEFINITION | VARCHAR2 | 30 |  |  | Time Definition |
| RATE_CALCULATION_SOURCE | VARCHAR2 | 30 |  |  | Rate Calculation Source |
| RATE_PAY_SOURCE | VARCHAR2 | 30 |  |  | Rate Pay Source |
| RATE_USER_TABLE | VARCHAR2 | 30 |  |  | Rate User Table |
| RATE_USER_COLUMN | VARCHAR2 | 30 |  |  | Rate User Column |
| RATE_USER_ROW | VARCHAR2 | 30 |  |  | Rate User Row |
| SUBJECT_TO_PRORATION | VARCHAR2 | 30 |  | Yes | Is this element subject to proration? Y/N |
| PRORATION_FORMULA_NAME | VARCHAR2 | 80 |  |  | Name of proration formula (equivalent to FF_FORMULAS_B_F.BASE_FORMULA_NAME). |
| PRORATION_FORMULA_ID | NUMBER |  | 18 |  | Foreign key reference to FF_FORMULAS_B_F.FORMULA_ID.FORMULA_ID. |
| PRORATION_GROUP_NAME | VARCHAR2 | 80 |  |  | Proration Group |
| PRORATION_GROUP_ID | NUMBER |  | 18 |  | PRORATION_GROUP_ID |
| SUBJECT_TO_RETRO | VARCHAR2 | 30 |  | Yes | Is this element subject to retroactive changes? Y/N |
| RECALC_EVENT_GROUP_NAME | VARCHAR2 | 80 |  |  | Retro Group. |
| RECALC_EVENT_GROUP_ID | NUMBER |  | 18 |  | RECALC_EVENT_GROUP_ID |
| ITERATIVE_INFORMATION | VARCHAR2 | 30 |  |  | Use element to calculate a gross amount from specified net amount? |
| ITERATIVE_FORMULA_NAME | VARCHAR2 | 80 |  |  | Name of iterative formula (equivalent to FF_FORMULAS_B_F.BASE_FORMULA_NAME). |
| ITERATIVE_FORMULA_ID | NUMBER |  | 18 |  | Foreign key reference to FF_FORMULAS_B_F.FORMULA_ID.FORMULA_ID. |
| ITERATIVE_PRIORITY | NUMBER |  | 18 |  | Iterative Priority |
| TOTAL_REACHED | VARCHAR2 | 30 |  |  | Processing Stop when the Total is reached? |
| REDUCE_REGULAR | VARCHAR2 | 30 |  |  | Should this element reduce regular earnings? |
| FLSA_EARN_INCLUDE | VARCHAR2 | 30 |  |  | This question is not applicable for earnings with a classification of non payroll payments. |
| FLSA_HOURS_INCLUDE | VARCHAR2 | 30 |  |  | This question is not applicable for earnings with a classification of non payroll payments. |
| DEDN_START_DATE | DATE |  |  |  | DEDN_START_DATE |
| DEDN_INSUFFICIENT_FUNDS | VARCHAR2 | 30 |  |  | DEDN_INSUFFICIENT_FUNDS |
| DEDN_OVERRIDES_ALLOWED | VARCHAR2 | 30 |  |  | DEDN_OVERRIDES_ALLOWED |
| DEDN_STOP_TOTAL_REACHED | VARCHAR2 | 30 |  |  | DEDN_STOP_TOTAL_REACHED |
| DEDN_FEE_PAYABLE | VARCHAR2 | 30 |  |  | DEDN_FEE_PAYABLE |
| DEDN_ELIGIBLE_TAX_RELIEF | VARCHAR2 | 30 |  |  | DEDN_ELIGIBLE_TAX_RELIEF |
| DEDN_SUPPLEMENTAL_LEVY | VARCHAR2 | 30 |  |  | DEDN_SUPPLEMENTAL_LEVY |
| DEDN_STORE_ARREARS_BALANCE | VARCHAR2 | 30 |  |  | DEDN_STORE_ARREARS_BALANCE |
| DEDN_RUN_TYPE | VARCHAR2 | 30 |  |  | DEDN_RUN_TYPE |
| EMPLOYER_MATCH_ELEMENT | VARCHAR2 | 30 |  |  | EMPLOYER_MATCH_ELEMENT |
| AFTER_TAX_ELEMENT | VARCHAR2 | 30 |  |  | AFTER_TAX_ELEMENT |
| ROTH_ELEMENT | VARCHAR2 | 30 |  |  | ROTH_ELEMENT |
| BUY_BACK_ELEMENT | VARCHAR2 | 30 |  |  | BUY_BACK_ELEMENT |
| CATCH_UP_PROCESS | VARCHAR2 | 30 |  |  | CATCH_UP_PROCESS |
| USE_RRA_PROCESS | VARCHAR2 | 30 |  |  | USE_RRA_PROCESS |
| EE_BONDS_WITHHOLD | VARCHAR2 | 30 |  |  | EE_BONDS_WITHHOLD |
| THIRD_PARTY_ONLY | VARCHAR2 | 30 |  |  | THIRD_PARTY_ONLY |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_MIG_STD_TEMPL_QUES_PK | Unique | Default | STANDARD_TEMPLATE_QUESTION_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
