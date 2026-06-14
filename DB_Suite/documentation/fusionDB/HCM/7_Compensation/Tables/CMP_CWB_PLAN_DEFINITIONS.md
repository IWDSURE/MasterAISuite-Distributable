# CMP_CWB_PLAN_DEFINITIONS

Stores the setup details of a compensation plan. It is used to store information about each plan period, its components and budget pools.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbplandefinitions-17655.html#cmpcwbplandefinitions-17655](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbplandefinitions-17655.html#cmpcwbplandefinitions-17655)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_PLAN_DEFINITIONS_PK | PLAN_DEFINITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_DEFINITION_ID | NUMBER |  | 18 | Yes | PLAN_DEFINITION_ID |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |
| DEFINITION_TYPE | VARCHAR2 | 30 |  | Yes | DEFINITION_TYPE |
| COMPONENT_ID | NUMBER |  | 18 | Yes | COMPONENT_ID |
| POOL_ID | NUMBER |  | 18 |  | POOL_ID |
| POOL_COMPONENT_ID | NUMBER |  | 18 |  | POOL_COMPONENT_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| STATUS_CODE | VARCHAR2 | 30 |  |  | STATUS_CODE |
| CORPORATE_CURRENCY | VARCHAR2 | 30 |  |  | CORPORATE_CURRENCY |
| SYSTEM_ORDER_NUM | NUMBER |  | 1 |  | SYSTEM_ORDER_NUM |
| ORDER_NUM | NUMBER |  |  |  | ORDER_NUM |
| PLAN_COMPONENT_COUNT | NUMBER |  | 1 |  | PLAN_COMPONENT_COUNT |
| APPROVAL_MODE | VARCHAR2 | 30 |  |  | APPROVAL_MODE |
| SUBMIT_MODE | VARCHAR2 | 30 |  |  | SUBMIT_MODE |
| BUDGETING_STYLE | VARCHAR2 | 30 |  |  | BUDGETING_STYLE |
| POST_AS_SALARY_FLAG | VARCHAR2 | 1 |  |  | POST_AS_SALARY_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| WITHDRAW_MODE | VARCHAR2 | 30 |  |  | WITHDRAW_MODE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_PLAN_DEFINITIONS_N1 | Non Unique | Default | BUSINESS_GROUP_ID |
| CMP_CWB_PLAN_DEFINITIONS_PK | Unique | Default | PLAN_DEFINITION_ID |
| CMP_CWB_PLAN_DEFINITIONS_U1 | Unique | Default | PERIOD_ID, DEFINITION_TYPE, COMPONENT_ID, POOL_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
