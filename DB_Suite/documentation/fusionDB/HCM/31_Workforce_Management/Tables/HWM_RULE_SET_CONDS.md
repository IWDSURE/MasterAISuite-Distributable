# HWM_RULE_SET_CONDS

Contains Conditions associated to the Rule Set. Each row has a sequence of precessing the condition.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrulesetconds-13292.html#hwmrulesetconds-13292](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrulesetconds-13292.html#hwmrulesetconds-13292)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RULE_SET_CONDS_PK | RULE_SET_COND_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| RULE_SET_COND_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |  |
| RULE_SET_ID | NUMBER |  | 18 | Yes | Foreign key to Ruleset Table |  |
| RULE_SET_UNQ_ID | NUMBER |  | 18 | Yes | Foreign key to Ruleset Table |  |
| CONDITION_ID | NUMBER |  | 18 |  | Condition associated to the rule set |  |
| CONDITION_TYPE | VARCHAR2 | 30 |  | Yes | Condition Type |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RULE_SET_CONDS_N1 | Non Unique | Default | RULE_SET_UNQ_ID, RULE_SET_ID |
| HWM_RULE_SET_CONDS_PK | Unique | Default | RULE_SET_COND_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
