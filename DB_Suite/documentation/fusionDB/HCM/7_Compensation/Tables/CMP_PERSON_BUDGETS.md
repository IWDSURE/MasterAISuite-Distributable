# CMP_PERSON_BUDGETS

Stores Budget Funding for a given plan, pool and period.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmppersonbudgets-4717.html#cmppersonbudgets-4717](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmppersonbudgets-4717.html#cmppersonbudgets-4717)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_PERSON_BUDGETS_PK | PERSON_EVENT_ID, PLAN_ID, POOL_ID, PERIOD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | Person Event ID. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  |
| POOL_ID | NUMBER |  | 18 | Yes | Pool Id | Active |
| PLAN_ID | NUMBER |  | 18 | Yes | Plan Id | Active |
| PERIOD_ID | NUMBER |  | 18 | Yes | Period Id | Active |
| BUDGET_POP_CD | VARCHAR2 | 30 |  |  | Budget Population Code . | Active |
| ACCESS_CD | VARCHAR2 | 30 |  |  | Access Code . | Active |
| DIST_BUDGET_VAL | NUMBER |  |  |  | Distribution Budget Value . | Active |
| WS_BUDGET_VAL | NUMBER |  |  |  | Worksheet Budget Value . | Active |
| DIST_BUDGET_ISSUE_VAL | NUMBER |  |  |  | Distribution Budget Issued Value | Active |
| WS_BUDGET_ISSUE_VAL | NUMBER |  |  |  | Worksheet Budget Issued Value | Active |
| DFLT_DIST_BUDGET_VAL | NUMBER |  |  |  | Default Distribution Bugdet Value | Active |
| DFLT_WS_BUDGET_VAL | NUMBER |  |  |  | Worksheet Distribution Budget Value. | Active |
| DIST_BUDGET_ISSUE_DATE | DATE |  |  |  | Distribution Budget Issued Date | Active |
| WS_BUDGET_ISSUE_DATE | DATE |  |  |  | Worksheet Budget Issued Date | Active |
| WS_BUDGET_VAL_LAST_UPD_DATE | DATE |  |  |  | Worksheet Budget Update Date | Active |
| DIST_BUDGET_VAL_LAST_UPD_DATE | DATE |  |  |  | Distribution Budget Update Date | Active |
| WS_BUDGET_VAL_LAST_UPD_BY | NUMBER |  | 18 |  | Worksheet Budget Updated by Person | Active |
| DIST_BUDGET_VAL_LAST_UPD_BY | NUMBER |  | 18 |  | Distribution Budget Updated by Person | Active |
| BUDGET_VAL_AMOUNT | NUMBER |  |  |  | Budget Val Amount |  |
| BUDGET_VAL_PERCENT | NUMBER |  |  |  | Budget Val Percent |  |
| OVERRIDE_OVER_BUDGET_CODE | VARCHAR2 | 30 |  |  | Override Over Budget Code |  |
| OVERRIDE_OVER_ALLOCATE_CODE | VARCHAR2 | 30 |  |  | Override Over Allocation Code |  |
| BUDGET_LAST_UPD_DATE | DATE |  |  |  | Budget Last Update Date |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_PERSON_BUDGETS_N1 | Non Unique | Default | PLAN_ID, PERIOD_ID |
| CMP_PERSON_BUDGETS_UK1 | Unique | Default | PERSON_EVENT_ID, PLAN_ID, POOL_ID, PERIOD_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
