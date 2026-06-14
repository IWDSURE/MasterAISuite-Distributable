# CMP_PLANS_AUDIT

Stores audit data for changes made to a Compensation Plan.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplansaudit-17462.html#cmpplansaudit-17462](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplansaudit-17462.html#cmpplansaudit-17462)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_PLANS_AUDIT_PK | PLAN_AUDIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_AUDIT_ID | NUMBER |  | 18 | Yes | PLAN_AUDIT_ID |
| AUDIT_TYPE | VARCHAR2 | 60 |  | Yes | AUDIT_TYPE |
| AUDIT_KEY | NUMBER |  | 18 | Yes | AUDIT_KEY |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| AUDIT_COLUMN | VARCHAR2 | 60 |  | Yes | AUDIT_COLUMN |
| ITEM_NAME | VARCHAR2 | 60 |  |  | ITEM_NAME |
| ATTRIBUTE_NAME | VARCHAR2 | 30 |  |  | ATTRIBUTE_NAME |
| COMPONENT_ID | NUMBER |  | 18 |  | COMPONENT_ID |
| POOL_ID | NUMBER |  | 18 |  | POOL_ID |
| CUSTOM_TYPE | VARCHAR2 | 30 |  |  | CUSTOM_TYPE |
| REGION_NAME | VARCHAR2 | 60 |  |  | REGION_NAME |
| ITEM_NAME_BUDGET | VARCHAR2 | 60 |  |  | ITEM_NAME_BUDGET |
| OLD_VAL_VARCHAR | VARCHAR2 | 200 |  |  | OLD_VAL_VARCHAR |
| NEW_VAL_VARCHAR | VARCHAR2 | 200 |  |  | NEW_VAL_VARCHAR |
| OLD_VAL_NUMBER | NUMBER |  |  |  | OLD_VAL_NUMBER |
| NEW_VAL_NUMBER | NUMBER |  |  |  | NEW_VAL_NUMBER |
| OLD_VAL_DATE | DATE |  |  |  | OLD_VAL_DATE |
| NEW_VAL_DATE | DATE |  |  |  | NEW_VAL_DATE |
| SUPPORTING_INFORMATION | VARCHAR2 | 200 |  |  | SUPPORTING_INFORMATION |
| AUDIT_DATE | TIMESTAMP |  |  |  | AUDIT_DATE |
| CHANGE_MADE_BY_PERSON_ID | NUMBER |  | 18 |  | CHANGE_MADE_BY_PERSON_ID |
| CHANGE_MADE_BY_USER_ID | NUMBER |  | 18 |  | CHANGE_MADE_BY_USER_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_PLANS_AUDIT_U1 | Unique | FUSION_TS_TX_DATA | PLAN_AUDIT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
