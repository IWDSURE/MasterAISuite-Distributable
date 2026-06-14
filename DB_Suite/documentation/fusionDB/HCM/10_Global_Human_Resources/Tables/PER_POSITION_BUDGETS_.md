# PER_POSITION_BUDGETS_

Position Budgets table that stores allocated values for headcount, FTE & amount.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpositionbudgets-6217.html#perpositionbudgets-6217](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpositionbudgets-6217.html#perpositionbudgets-6217)

## Primary Key

| Name | Columns |
|------|----------|
| PER_POSITION_BUDGETS_PK_ | POSITION_BUDGET_ID, LAST_UPDATED_BY, LAST_UPDATE_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POSITION_BUDGET_ID | NUMBER |  | 18 | Yes | Unique identifier of the position budget. |
| BUDGET_PERIOD_START_DATE | DATE |  |  |  | Start date of the budgetary period for which the position budget is being entered. |
| BUDGET_PERIOD_END_DATE | DATE |  |  |  | End date of the budgetary period for which the position budget is being entered. |
| CODE | VARCHAR2 | 30 |  |  | Code of the Position Budget. |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Unique identifier of the business unit for which the position budget is being entered. |
| DEPARTMENT_ID | NUMBER |  | 18 |  | Unique identifier of the department for which the position budget is being entered. |
| LOCATION_ID | NUMBER |  | 18 |  | Unique identifier of the location for which the position budget is being entered. |
| ALLOCATED_HEADCOUNT | NUMBER |  | 4 |  | Headcount allocated for the budgetary period. Sum of headcount of all applicable positions should not exceed this value. |
| ALLOCATED_FTE | NUMBER |  | 30 |  | FTE allocated for the budgetary period. Sum of FTE of all applicable positions should not exceed this value. |
| ALLOCATED_AMOUNT | NUMBER |  |  |  | Amount allocated for the budgetary period. Sum of amount of all applicable positions should not exceed this value. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_POSITION_BUDGETS_PK_ | Unique | PER_POSITION_BUDGETS_PK_ | POSITION_BUDGET_ID, LAST_UPDATED_BY, LAST_UPDATE_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
