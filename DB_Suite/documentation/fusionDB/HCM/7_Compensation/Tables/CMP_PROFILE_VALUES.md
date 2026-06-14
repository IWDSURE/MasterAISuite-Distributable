# CMP_PROFILE_VALUES

Stores profile values common to all compensation modules.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpprofilevalues-20306.html#cmpprofilevalues-20306](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpprofilevalues-20306.html#cmpprofilevalues-20306)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_PROFILE_VALUES_PK | BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| GSP_BATCH_ALLOW_LOW_SAL_CD | VARCHAR2 | 30 |  |  | Options for havin proposed salary less than the current salary |
| GSP_BATCH_ERR_FUT_STEP_FLAG | VARCHAR2 | 1 |  |  | Flag for erroring if future grade step change exists |
| GSP_BATCH_ERR_FUT_ASG_FLAG | VARCHAR2 | 1 |  |  | Flag for erroring if future assignment change exists |
| GSP_ELIG_LOOKBACK_DAYS | NUMBER |  | 18 |  | Number of LOOKBACK DAYS for Progression. |
| GSP_BATCH_ERR_CORR_STEP_FLAG | VARCHAR2 | 1 |  |  | Flag for erroring if step change exists as of same date |
| GSP_UI_ALLOW_LOW_SAL_FLAG | VARCHAR2 | 1 |  |  | Flag for allowing salary change when proposed salary is less than current salary |
| GSP_UI_ERR_FUT_SAL_FLAG | VARCHAR2 | 1 |  |  | Flag for erroring when salary record exists with future date |
| GSP_UI_ERR_CORR_SAL_FLAG | VARCHAR2 | 1 |  |  | Flag for erroring when salary record exists with same date |
| GSP_BATCH_ERR_FUT_SAL_FLAG | VARCHAR2 | 1 |  |  | Flag for erroring when salary record exists with a future date |
| GSP_BATCH_ERR_CORR_SAL_FLAG | VARCHAR2 | 1 |  |  | Flag for erroring when salary record exists with same date |
| GSP_EXCLUDE_FRM_RT_SYNC_FLAG | VARCHAR2 | 1 |  |  | Flag to exclude from rate sync if excluded from GSP |
| ENABLE_CLK_TO_EDIT_WKSHT_FLAG | VARCHAR2 | 1 |  |  | ENABLE_CLK_TO_EDIT_WKSHT_FLAG |
| ENABLE_MANAGER_SWITCHING_FLAG | VARCHAR2 | 1 |  |  | ENABLE_MANAGER_SWITCHING_FLAG |
| ENABLE_WORKER_STMTS_IN_FUSE | VARCHAR2 | 1 |  |  | ENABLE_WORKER_STMTS_IN_FUSE |
| MAX_STATEMENT_PERIODS | NUMBER |  | 18 |  | MAX_STATEMENT_PERIODS |
| ENABLE_MODELING_FLAG | VARCHAR2 | 1 |  |  | ENABLE_MODELING_FLAG |
| MAX_SWITCH_MANAGERS | NUMBER |  | 18 |  | MAX_SWITCH_MANAGERS |
| NOTIFY_BUDGET_PUBLISH | VARCHAR2 | 30 |  |  | NOTIFY_BUDGET_PUBLISH |
| NOTIFY_WORK_SUBMIT | VARCHAR2 | 30 |  |  | NOTIFY_WORK_SUBMIT |
| NOTIFY_WORK_REJECT | VARCHAR2 | 30 |  |  | NOTIFY_WORK_REJECT |
| NOTIFY_MANAGER_APPROVAL | VARCHAR2 | 30 |  |  | NOTIFY_MANAGER_APPROVAL |
| NOTIFY_FINAL_APPROVAL | VARCHAR2 | 30 |  |  | NOTIFY_FINAL_APPROVAL |
| NOTIFY_MANAGER_OVERRIDE | VARCHAR2 | 30 |  |  | NOTIFY_MANAGER_OVERRIDE |
| NOTIFY_CHANGE_ACCESS | VARCHAR2 | 30 |  |  | NOTIFY_CHANGE_ACCESS |
| NOTIFY_REASSIGN | VARCHAR2 | 30 |  |  | NOTIFY_REASSIGN |
| NOTIFY_CHANGE_ELIG | VARCHAR2 | 30 |  |  | NOTIFY_CHANGE_ELIG |
| NOTIFY_WORK_RECALL | VARCHAR2 | 30 |  |  | NOTIFY_WORK_RECALL |
| WATCH_NUM_PLANS_FLAG | VARCHAR2 | 1 |  |  | WATCH_NUM_PLANS_FLAG |
| WATCH_NUM_POOLS_FLAG | VARCHAR2 | 1 |  |  | WATCH_NUM_POOLS_FLAG |
| WATCH_BUDGET_PUBLISH_FLAG | VARCHAR2 | 1 |  |  | WATCH_BUDGET_PUBLISH_FLAG |
| WATCH_NEW_PLANS_DAYS | NUMBER |  | 18 |  | WATCH_NEW_PLANS_DAYS |
| WATCH_BUDGET_PUBLISH_DAYS | NUMBER |  | 18 |  | WATCH_BUDGET_PUBLISH_DAYS |
| WATCH_NEW_PLANS_FLAG | VARCHAR2 | 1 |  |  | WATCH_NEW_PLANS_FLAG |
| WATCH_STATEMENT_DAYS | NUMBER |  | 18 |  | WATCH_STATEMENT_DAYS |
| EST_STOCK_PRICE | NUMBER |  |  |  | EST_STOCK_PRICE |
| EST_STOCK_PRICE_CURRENCY_CD | VARCHAR2 | 30 |  |  | EST_STOCK_PRICE_CURRENCY_CD |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| WATCH_STATEMENT_FLAG | VARCHAR2 | 1 |  |  | WATCH_STATEMENT_FLAG |
| NOTIFY_BUDGET_RECALL | VARCHAR2 | 30 |  |  | NOTIFY_BUDGET_RECALL |
| PANE_COMPENSATE_TASK_COUNT | NUMBER |  | 18 |  | PANE_COMPENSATE_TASK_COUNT |
| PANE_BUDGET_TASK_COUNT | NUMBER |  | 18 |  | PANE_BUDGET_TASK_COUNT |
| PANE_MODEL_TASK_COUNT | NUMBER |  | 18 |  | PANE_MODEL_TASK_COUNT |
| NOTIFY_WORKER_DELEGATION | VARCHAR2 | 30 |  |  | NOTIFY_WORKER_DELEGATION |
| NOTIFY_RMV_WORKER_DELEGATION | VARCHAR2 | 30 |  |  | NOTIFY_RMV_WORKER_DELEGATION |
| ENABLE_COUNTRY_BUDGETS_FLAG | VARCHAR2 | 1 |  |  | ENABLE_COUNTRY_BUDGETS_FLAG |
| NOTIFY_CHANGE_DUE_DATE | VARCHAR2 | 30 |  |  | NOTIFY_CHANGE_DUE_DATE |
| MGR_ASG_DIFF_FLAG | VARCHAR2 | 1 |  |  | MGR_ASG_DIFF_FLAG |
| MGR_ASG_DIFF_CODE1 | VARCHAR2 | 30 |  |  | MGR_ASG_DIFF_CODE1 |
| MGR_ASG_DIFF_CODE2 | VARCHAR2 | 30 |  |  | MGR_ASG_DIFF_CODE2 |
| WS_SAVE_CLOSE_CODE | VARCHAR2 | 30 |  |  | WS_SAVE_CLOSE_CODE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_PROFILE_VALUES_UK1 | Unique | Default | BUSINESS_GROUP_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
