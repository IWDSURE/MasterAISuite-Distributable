# CMP_BUDGET_AUDIT

Table to store budget update history

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbudgetaudit-16158.html#cmpbudgetaudit-16158](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbudgetaudit-16158.html#cmpbudgetaudit-16158)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_BUDGET_AUDIT_PK | BUDGET_AUDIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| BUDGET_AUDIT_ID | NUMBER |  | 18 | Yes | Primary Key | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  |
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | Person in Event Id | Active |
| POOL_ID | NUMBER |  | 18 | Yes | Budget Pool Id | Active |
| PLAN_ID | NUMBER |  | 18 | Yes | Plan Id | Active |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |  |
| BUDGET_TYPE | VARCHAR2 | 30 |  |  | Budget Type | Active |
| UPDATE_TYPE | VARCHAR2 | 30 |  |  | Update Type code.
                                               Published/Initial Budgets etc | Active |
| UPDATE_DATE | DATE |  |  |  | Update Date | Active |
| UPDATE_BY | NUMBER |  | 18 |  | Update By | Active |
| BUDGET_VAL | NUMBER |  |  |  | Budget Value | Active |
| ADJUSTMENT_VAL | NUMBER |  |  |  | Adjustment Value | Active |
| PERSON_OF_INTEREST | NUMBER |  | 18 |  | Person Of Interest | Active |
| ADMIN_FLAG | VARCHAR2 | 10 |  |  | Admin Flag to identify if record is from an Admin |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_BUDGET_AUDIT_N1 | Non Unique | Default | PERSON_EVENT_ID, BUDGET_TYPE |
| CMP_BUDGET_AUDIT_UK1 | Unique | Default | BUDGET_AUDIT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
