# WLF_PLAN_RECORDS_F

Learning Planning Records for budgeted planned learning.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfplanrecordsf-27520.html#wlfplanrecordsf-27520](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfplanrecordsf-27520.html#wlfplanrecordsf-27520)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PLAN_RECORDS_F_PK | PLAN_RECORD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_RECORD_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PLAN_PROFILE_ID | NUMBER |  | 18 | Yes | Plan profile id of the planning record |
| LEARNING_PLAN_ID | NUMBER |  | 18 | Yes | LEARNING_PLAN_ID |
| STATUS | VARCHAR2 | 30 |  | Yes | Plan record status |
| ASSIGNMENT_RECORD_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_RECORD_ID |
| AREC_EFFECTIVE_DATE | TIMESTAMP |  |  |  | Assignment record effective date |
| WAGE_COST | NUMBER |  |  |  | Indicates the learner wage cost |
| WAGE_COST_CURRENCY | VARCHAR2 | 30 |  |  | Indicates the wage cost currency |
| AREC_STATE_ON_EXECUTE | VARCHAR2 | 30 |  |  | Assignment records status on plan execution |
| PRICING_RULE_ID | NUMBER |  | 18 |  | Identifier of pricing rule. Foreign key to WLF_PRICING_RULES_F. |
| PRICING_RULE_LOCK_DATE | DATE |  |  |  | Indicates date when price is locked. |
| EXPECTED_EFFORT | NUMBER |  |  |  | Expected duration to complete the learning item |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PLAN_RECORDS_F_N1 | Non Unique | Default | STATUS |
| WLF_PLAN_RECORDS_F_N2 | Non Unique | Default | LEARNING_PLAN_ID |
| WLF_PLAN_RECORDS_F_N3 | Non Unique | Default | ASSIGNMENT_RECORD_ID |
| WLF_PLAN_RECORDS_F_U1 | Unique | Default | PLAN_RECORD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
