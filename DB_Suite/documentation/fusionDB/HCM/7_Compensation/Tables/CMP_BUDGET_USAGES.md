# CMP_BUDGET_USAGES

Stores the budget used by other components like ICD, Pay etc

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbudgetusages-7334.html#cmpbudgetusages-7334](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbudgetusages-7334.html#cmpbudgetusages-7334)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_BUDGET_USAGES_PK | BUDGET_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BUDGET_USAGE_ID | NUMBER |  | 18 | Yes | Primary key |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | Person in Event Id |
| POOL_ID | NUMBER |  | 18 | Yes | Budget Pool Id |
| PLAN_ID | NUMBER |  | 18 | Yes | Plan Id |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |
| FOR_PERSON_ID | NUMBER |  | 18 |  | Person Id for which the amount was used for |
| FOR_ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment id of the person the amount was used for |
| USAGE_VAL | NUMBER |  |  |  | Used Value |
| USAGE_DATE | DATE |  |  |  | Used Date |
| USAGE_TYPE | VARCHAR2 | 30 |  |  | Type of usage, Pay, ICD, CWB |
| USAGE_TYPE_ID | NUMBER |  | 18 |  | USAGE_TYPE_ID |
| ENABLED | VARCHAR2 | 1 |  | Yes | ENABLED |
| CONSUMING_COMPONENT_ID | NUMBER |  |  |  | Consuming component id in case of ICD and CWB |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_BUDGET_USAGES_N1 | Non Unique | Default | PERSON_EVENT_ID, POOL_ID, PERIOD_ID, ENABLED |
| CMP_BUDGET_USAGES_N2 | Non Unique | Default | USAGE_TYPE, USAGE_TYPE_ID, ENABLED |
| CMP_BUDGET_USAGES_UK1 | Unique | Default | BUDGET_USAGE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
