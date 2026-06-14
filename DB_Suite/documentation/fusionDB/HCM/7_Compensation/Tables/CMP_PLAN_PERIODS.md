# CMP_PLAN_PERIODS

Stores plan Periods and date information such as period name, description, period start/end dates, and freeze date.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplanperiods-7685.html#cmpplanperiods-7685](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplanperiods-7685.html#cmpplanperiods-7685)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_PLAN_PERIODS_PK | PERIOD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| COMP_TYPE | VARCHAR2 | 30 |  |  | COMP_TYPE |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| PERIOD_TYPE | VARCHAR2 | 30 |  |  | PERIOD_TYPE |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| PERIOD_NAME | VARCHAR2 | 80 |  |  | PERIOD_NAME |
| DISPLAY_NAME | VARCHAR2 | 30 |  |  | DISPLAY_NAME |
| AVAIL_START_DATE | DATE |  |  |  | AVAIL_START_DATE |
| AVAIL_END_DATE | DATE |  |  |  | AVAIL_END_DATE |
| UPDATE_START_DATE | DATE |  |  |  | UPDATE_START_DATE |
| UPDATE_END_DATE | DATE |  |  |  | UPDATE_END_DATE |
| FREEZE_DATE | DATE |  |  |  | FREEZE_DATE |
| ELIGIBILITY_DATE | DATE |  |  |  | ELIGIBILITY_DATE |
| EXCHANGE_RATE_DATE | DATE |  |  |  | EXCHANGE_RATE_DATE |
| PERFORMANCE_DATE | DATE |  |  |  | PERFORMANCE_DATE |
| ASSIGNMENT_CHANGE_DATE | DATE |  |  |  | ASSIGNMENT_CHANGE_DATE |
| DEFAULT_DUE_DATE | DATE |  |  |  | DEFAULT_DUE_DATE |
| PLAN_ACCESS_ID | NUMBER |  | 18 |  | PLAN_ACCESS_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MGR_UPD_DUE_DATE_FLAG | VARCHAR2 | 1 |  |  | MGR_UPD_DUE_DATE_FLAG |
| TOP_MGR_DEFAULT_DUE_DATE | DATE |  |  |  | TOP_MGR_DEFAULT_DUE_DATE |
| LVL_1_DEFAULT_DUE_DATE | DATE |  |  |  | LVL_1_DEFAULT_DUE_DATE |
| LVL_2_DEFAULT_DUE_DATE | DATE |  |  |  | LVL_2_DEFAULT_DUE_DATE |
| LVL_3_DEFAULT_DUE_DATE | DATE |  |  |  | LVL_3_DEFAULT_DUE_DATE |
| LVL_4_DEFAULT_DUE_DATE | DATE |  |  |  | LVL_4_DEFAULT_DUE_DATE |
| LVL_5_DEFAULT_DUE_DATE | DATE |  |  |  | LVL_5_DEFAULT_DUE_DATE |
| LVL_6_DEFAULT_DUE_DATE | DATE |  |  |  | LVL_6_DEFAULT_DUE_DATE |
| LVL_7_DEFAULT_DUE_DATE | DATE |  |  |  | LVL_7_DEFAULT_DUE_DATE |
| MARKET_DATA_DATE | DATE |  |  |  | MARKET_DATA_DATE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_PLAN_PERIODS_U1 | Unique | Default | PLAN_ID, PERIOD_NAME |
| CMP_PLAN_PERIODS_UK2 | Unique | Default | PERIOD_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
