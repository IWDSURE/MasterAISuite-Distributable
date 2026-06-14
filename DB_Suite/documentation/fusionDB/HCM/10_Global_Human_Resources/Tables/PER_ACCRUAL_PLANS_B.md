# PER_ACCRUAL_PLANS_B

The base table used to store PTO accrual plan definitions, (Paid time off).

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraccrualplansb-3298.html#peraccrualplansb-3298](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraccrualplansb-3298.html#peraccrualplansb-3298)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ACCRUAL_PLANS_B_PK | ACCRUAL_PLAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ACCRUAL_PLAN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identify the ENTERPRISE  to which the plan belongs.  
Foreign key to PER_ENTERPRISES. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Identify the LDG to which the plan belongs.  Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  | Yes | Identify the Legislation code (of the LDG) to which the plan belongs. Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| ACCRUAL_CATEGORY | VARCHAR2 | 30 |  | Yes | Indicates whether a plan is Sickness or Vacation. |  |
| ACCRUAL_START_RULE | VARCHAR2 | 30 |  |  | Indicates accrual start rule.  This can be hire date, beginning of year, or six months after hire. |  |
| ACCRUAL_UNITS | VARCHAR2 | 30 |  | Yes | Indicates whether the accrual units are hours or days. |  |
| ACCRUAL_ELEMENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_ELEMENT_TYPES.  Identifies the element that is used to enroll employees in the accrual plan. |  |
| CO_INPUT_VALUE_ID | NUMBER |  | 18 | Yes | Identifies the input value that is used to record carryover entitlement from one period to the next. |  |
| CO_DATE_INPUT_VALUE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_INPUT_VALUES_F. Identifies the element and input value which stores the date when carried over time becomes effective. |  |
| CO_EXP_DATE_INPUT_VALUE_ID | NUMBER |  | 18 |  | Foreign key to PAY_INPUT_VALUES_F. Identifies the element and input value which stores the date when carried over time expires. |  |
| RESIDUAL_INPUT_VALUE_ID | NUMBER |  | 18 | Yes | Identifies the element and input value that is used to record residual leave at the end of a period. |  |
| RESIDUAL_DATE_INPUT_VALUE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_INPUT_VALUES_F. Identifies the element and input value which stores the date when residual time becomes effective. |  |
| TAGGING_ELEMENT_TYPE_ID | NUMBER |  | 18 |  | Foreign key to PAY_ELEMENT_TYPES.  Identifies the element that is used to flag retrospective net calculation rule element entries. |  |
| ACCRUAL_DEFINED_BALANCE_ID | NUMBER |  | 18 |  | Foreign key to PAY_DEFINED_BALANCES. Identifies the defined balance used to store Accruals. |  |
| ACCRUAL_BALANCE_ELEMENT_ID | NUMBER |  | 18 |  | Foreign key to PAY_ELEMENT_TYPES.  Identifies the element that is used to manage the maintenance of an accrual payroll balance. |  |
| LIABILITY_DEFINED_BALANCE_ID | NUMBER |  | 18 |  | Foreign key to PAY_DEFINED_BALANCES. Identifies the defined liability amount for the stored Accruals   . |  |
| LIABILITY_BALANCE_ELEMENT_ID | NUMBER |  | 18 |  | Foreign key to PAY_ELEMENT_TYPES.  Identifies the element that is used to manage the maintenance of an liability balance    . |  |
| ACCRUAL_TERM_TYPE | VARCHAR2 | 30 |  |  | Indicates the type of the accrual term . Typical values are 'simple' ,'Rolling','Hire Date Anniversary'. |  |
| ACCRUAL_TERM_LENGTH | NUMBER |  | 5 |  | Indicates the accrual term length , for example '1 year'. |  |
| ACCRUAL_TERM_LENGTH_UOM | VARCHAR2 | 30 |  |  | Indicates the accrual term length , for example '1 year'. |  |
| ACCRUAL_FREQUENCY_TYPE | VARCHAR2 | 30 |  |  | Indicates the accrual period type . Typical values are 'Standard' ,'Payroll' . |  |
| ACCRUAL_FREQUENCY_LENGTH | NUMBER |  | 5 |  | Indicates the accrual period length , for example '1 month'. |  |
| ACCRUAL_FREQUENCY_LENGTH_UOM | VARCHAR2 | 30 |  |  | Indicates the accrual period length , for example '1 month'. |  |
| ACCRUAL_TERM_START | VARCHAR2 | 30 |  |  | Start date of the accrual term . Only required in case of 'Simple' accrual term. |  |
| ACCRUAL_TERM_END | VARCHAR2 | 30 |  |  | End date of the accrual term . Only required in case of 'Simple' accrual term. |  |
| CO_EXPIRY_LENGTH | NUMBER |  | 5 |  | Expiry length (date) of the carry over entitlement , for example "6 months". |  |
| CO_EXPIRY_LENGTH_UOM | VARCHAR2 | 30 |  |  | Expiry length (date) unit of measure of the carry over entitlement. |  |
| INELIGIBLE_PERIOD_LENGTH | NUMBER |  | 5 |  | User defined period of ineligibility, in conjunction with the ineligible period uom. |  |
| INELIGIBLE_PERIOD_LENGTH_UOM | VARCHAR2 | 30 |  |  | Period uom for the INELIGIBLE_PERIOD_LENGTH, for example, weeks or months. |  |
| ACCRUAL_FORMULA_ID | NUMBER |  | 18 | Yes | Foreign key to FF_FORMULAS_F. Identifies the formula used to calculate accrued time. |  |
| CO_FORMULA_ID | NUMBER |  | 18 | Yes | Foreign key to FF_FORMULAS_F. Identifies the formula to be used to calculate values for the PTO carryover process. |  |
| PAYROLL_FORMULA_ID | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. Identifies the formula specified in run result rules used by payroll processing. |  |
| INELIGIBILITY_FORMULA_ID | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. Identifies the formula used to calculate whether an employee is eligible to accrue time. |  |
| ACCRUAL_BAND_GROUP | VARCHAR2 | 30 |  | Yes | Accrual Plan's Band group |  |
| ACCRUAL_BAND_RANGE | VARCHAR2 | 30 |  | Yes | Accrual Plan's Band Range |  |
| INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION1 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION2 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION3 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION4 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION5 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION6 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION7 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION8 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION9 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION10 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION11 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION12 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION13 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION14 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION15 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION16 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION17 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION18 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION19 | VARCHAR2 | 150 |  |  | Standard developer  descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION20 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION21 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION22 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION23 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION24 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION25 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION26 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION27 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION28 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION29 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION30 | VARCHAR2 | 150 |  |  | Standard developer descriptive flexfield column. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Accrual Plan Attributes (PER_ACCRUAL_PLAN_LEG_DDF) |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ACCRUAL_PLANS_B_N1 | Non Unique | FUSION_TS_TX_DATA | ACCRUAL_ELEMENT_TYPE_ID |
| PER_ACCRUAL_PLANS_B_N2 | Non Unique | FUSION_TS_TX_DATA | CO_INPUT_VALUE_ID |
| PER_ACCRUAL_PLANS_B_N3 | Non Unique | FUSION_TS_TX_DATA | RESIDUAL_INPUT_VALUE_ID |
| PER_ACCRUAL_PLANS_B_N4 | Non Unique | FUSION_TS_TX_DATA | LEGISLATIVE_DATA_GROUP_ID |
| PER_ACCRUAL_PLANS_B_N5 | Non Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE |
| PER_ACCRUAL_PLANS_B_PK | Unique | FUSION_TS_TX_DATA | ACCRUAL_PLAN_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
