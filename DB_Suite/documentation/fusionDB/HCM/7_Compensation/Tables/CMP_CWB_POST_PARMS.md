# CMP_CWB_POST_PARMS

Stores Post Process Run Paramaters for Salary and Element.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpostparms-18604.html#cmpcwbpostparms-18604](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpostparms-18604.html#cmpcwbpostparms-18604)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_POST_PARMS_PK | RUN_ID, SEQ_NUM |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_ID | NUMBER |  | 18 | Yes | RUN_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| SEQ_NUM | NUMBER |  | 9 | Yes | SEQ_NUM |
| ROW_TYPE | VARCHAR2 | 30 |  | Yes | ROW_TYPE |
| COMPONENT_ID | NUMBER |  | 18 | Yes | COMPONENT_ID |
| SYSTEM_ORDER_NUM | NUMBER |  | 1 |  | SYSTEM_ORDER_NUM |
| PLAN_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | PLAN_ATTRIBUTE_ID |
| ATTRIBUTE_ELEMENT_ID | NUMBER |  | 18 | Yes | ATTRIBUTE_ELEMENT_ID |
| ATTRIBUTE_NAME | VARCHAR2 | 30 |  |  | ATTRIBUTE_NAME |
| ITEM_NAME | VARCHAR2 | 60 |  |  | ITEM_NAME |
| POST_FLAG | VARCHAR2 | 1 |  |  | Post Flag |
| DATE_BEHAVIOR | VARCHAR2 | 30 |  | Yes | DATE_BEHAVIOR |
| STATIC_DATE | DATE |  |  |  | STATIC_DATE |
| SALARY_COMPONENT | VARCHAR2 | 30 |  |  | SALARY_COMPONENT |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_POST_PARMS_PK | Unique | Default | RUN_ID, SEQ_NUM |
| CMP_CWB_POST_PARMS_U1 | Unique | FUSION_TS_TX_DATA | RUN_ID, ROW_TYPE, COMPONENT_ID, PLAN_ATTRIBUTE_ID, ATTRIBUTE_ELEMENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
