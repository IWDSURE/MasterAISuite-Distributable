# PER_ACCRUAL_CALC_RULES

Element entry values which contribute to the net value of Paid Time Off.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraccrualcalcrules-19314.html#peraccrualcalcrules-19314](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraccrualcalcrules-19314.html#peraccrualcalcrules-19314)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ACCRUAL_CALC_RULE_PK | ACCRUAL_CALC_RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACCRUAL_CALC_RULE_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| ACCRUAL_PLAN_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ACCRUAL_PLANS_B. Identifies the plan to which these calculation rules belongs to . |
| ABSENCE_ATTENDANCE_TYPE_ID | NUMBER |  | 18 |  | Foreign key to PER_ABSENCE_ATTENDANCE_TYPES. Identifies the 'absence' to which this accrual plan is associated . |
| USE_ELEMENT_LINK | VARCHAR2 | 30 |  |  | Determines whether the element link ( of the  absence element) has been used when creating the PTO shadow elements ( accrual , carry over, tagging , balance ). It accepts "Yes" or "No". |
| INPUT_VALUE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_INPUT_VALUES; the value to be included in the net calculation. |
| DATE_INPUT_VALUE_ID | NUMBER |  | 18 |  | Foreign key to PAY_INPUT_VALUES |
| ADD_OR_SUBTRACT | VARCHAR2 | 30 |  | Yes | Add or subtract the input value when calculating the net value of the PTO. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ACCRUAL_CALC_RULES_N1 | Non Unique | Default | ACCRUAL_PLAN_ID |
| PER_ACCRUAL_CALC_RULES_N2 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_ACCRUAL_CALC_RULES_PK | Unique | Default | ACCRUAL_CALC_RULE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
