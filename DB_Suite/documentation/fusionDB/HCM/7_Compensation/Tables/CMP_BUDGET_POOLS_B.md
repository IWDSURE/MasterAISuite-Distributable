# CMP_BUDGET_POOLS_B

Stores budget pool information in the database.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbudgetpoolsb-26248.html#cmpbudgetpoolsb-26248](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbudgetpoolsb-26248.html#cmpbudgetpoolsb-26248)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_BUDGET_POOLS_B_PK | POOL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POOL_ID | NUMBER |  | 18 | Yes | POOL_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| SYSTEM_ORDER_NUM | NUMBER |  | 1 |  | SYSTEM_ORDER_NUM |
| ORDER_NUM | NUMBER |  |  |  | ORDER_NUM |
| PRIMARY_COMPONENT_ID | NUMBER |  | 18 |  | PRIMARY_COMPONENT_ID |
| NON_MONETARY_UOM | VARCHAR2 | 30 |  |  | NON_MONETARY_UOM |
| BUDGETING_STYLE | VARCHAR2 | 30 |  |  | BUDGETING_STYLE |
| AUTO_ISSUE_FLAG | VARCHAR2 | 1 |  |  | AUTO_ISSUE_FLAG |
| PREVENT_OVER_BUDGET_FLAG | VARCHAR2 | 1 |  |  | PREVENT_OVER_BUDGET_FLAG |
| PREVENT_OVER_ALLOCATE_FLAG | VARCHAR2 | 1 |  |  | PREVENT_OVER_ALLOCATE_FLAG |
| OVER_ALLOCATE_TOLERANCE | NUMBER |  |  |  | OVER_ALLOCATE_TOLERANCE |
| OVER_BUDGET_TOLERANCE | NUMBER |  |  |  | OVER_BUDGET_TOLERANCE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| HIDE_FROM_MANAGERS_FLAG | VARCHAR2 | 1 |  |  | HIDE_FROM_MANAGERS_FLAG |
| ENABLE_SCOREBOARD_VIEW_FLAG | VARCHAR2 | 1 |  |  | ENABLE_SCOREBOARD_VIEW_FLAG |
| ENFORCE_BDGT_BY_GRP_FLAG | VARCHAR2 | 1 |  |  | ENFORCE_BDGT_BY_GRP_FLAG |
| MAX_PCT_OVER_ALLOCATE | NUMBER |  |  |  | MAX_PCT_OVER_ALLOCATE |
| GROUPING_COLUMN_CODE | VARCHAR2 | 60 |  |  | GROUPING_COLUMN_CODE |
| OVER_BUDGET_SEVERITY_CODE | VARCHAR2 | 30 |  |  | OVER_BUDGET_SEVERITY_CODE |
| UNDER_BUDGET_SEVERITY_CODE | VARCHAR2 | 30 |  |  | UNDER_BUDGET_SEVERITY_CODE |
| OVER_BUDGET_GROUP_SEV_CODE | VARCHAR2 | 30 |  |  | OVER_BUDGET_GROUP_SEV_CODE |
| NULL_BUDGET_SEVERITY_CODE | VARCHAR2 | 30 |  |  | NULL_BUDGET_SEVERITY_CODE |
| RESET_BDGT_ON_WITHDRAW_FLAG | VARCHAR2 | 1 |  |  | RESET_BDGT_ON_WITHDRAW_FLAG |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_BUDGET_POOLS_B_N1 | Non Unique | Default | PRIMARY_COMPONENT_ID |
| CMP_BUDGET_POOLS_B_UK1 | Unique | Default | POOL_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
