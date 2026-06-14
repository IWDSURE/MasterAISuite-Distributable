# CMP_COMPONENTS_B

Stores Compensation components information

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcomponentsb-21227.html#cmpcomponentsb-21227](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcomponentsb-21227.html#cmpcomponentsb-21227)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_COMPONENTS_B_PK | COMPONENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMPONENT_ID | NUMBER |  | 18 | Yes | COMPONENT_ID |
| DOCUMENT_TYPE_ID | NUMBER |  | 18 |  | DOCUMENT_TYPE_ID |
| STOCK_DEFAULTING_CODE | VARCHAR2 | 30 |  |  | STOCK_DEFAULTING_CODE |
| DOR_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | DOR_REQUIRED_FLAG |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 |  | PERIOD_ID |
| CURRENCY_DETERMINATION_CODE | VARCHAR2 | 30 |  |  | CURRENCY_DETERMINATION_CODE |
| SYSTEM_ORDER_NUM | NUMBER |  | 1 |  | SYSTEM_ORDER_NUM |
| ORDER_NUM | NUMBER |  |  |  | ORDER_NUM |
| POOL_ID_TO_CONSUME | NUMBER |  | 18 |  | POOL_ID_TO_CONSUME |
| POST_AS_SALARY_FLAG | VARCHAR2 | 1 |  |  | POST_AS_SALARY_FLAG |
| SALARY_COMPONENT | VARCHAR2 | 30 |  |  | SALARY_COMPONENT |
| RULE_ID | NUMBER |  | 18 |  | RULE_ID |
| GRANT_TYPE | VARCHAR2 | 30 |  |  | GRANT_TYPE |
| TRADING_SYMBOL | VARCHAR2 | 30 |  |  | TRADING_SYMBOL |
| NON_MONETARY_UOM | VARCHAR2 | 30 |  |  | NON_MONETARY_UOM |
| COMP_TYPE | VARCHAR2 | 30 |  |  | COMP_TYPE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SALARY_RATES_USED_FLAG | VARCHAR2 | 1 |  |  | SALARY_RATES_USED_FLAG |
| USE_FOR_ASG_SEG_FLAG | VARCHAR2 | 1 |  |  | USE_FOR_ASG_SEG_FLAG |
| ASG_SEG_AUTO_PUBLISH_FLAG | VARCHAR2 | 1 |  |  | ASG_SEG_AUTO_PUBLISH_FLAG |
| ASG_SEG_WS_COLUMN_CODE | VARCHAR2 | 60 |  |  | ASG_SEG_WS_COLUMN_CODE |
| MANAGER_ENTER_RATES_CODE | VARCHAR2 | 30 |  |  | MANAGER_ENTER_RATES_CODE |
| SALARY_SMPL_COMP_USED_FLAG | VARCHAR2 | 1 |  |  | SALARY_SMPL_COMP_USED_FLAG |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_COMPONENTS_B_N1 | Non Unique | Default | POOL_ID_TO_CONSUME |
| CMP_COMPONENTS_B_N2 | Non Unique | Default | PLAN_ID |
| CMP_COMPONENTS_B_UK1 | Unique | Default | COMPONENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
