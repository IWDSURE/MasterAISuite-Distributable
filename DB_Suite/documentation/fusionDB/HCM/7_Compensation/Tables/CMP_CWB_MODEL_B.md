# CMP_CWB_MODEL_B

CMP_CWB_MODEL identifies the matrix for a particular person

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbmodelb-24572.html#cmpcwbmodelb-24572](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbmodelb-24572.html#cmpcwbmodelb-24572)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_MODEL_PK | MODEL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MODEL_ID | NUMBER |  | 18 | Yes | System generated Primary key column. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PERIOD_ID | NUMBER |  | 18 |  | Period id this model belongs to |
| COMPONENT_ID | NUMBER |  | 18 |  | COMPONENT_ID |
| DATE_SAVED | DATE |  |  |  | Date saved. |
| PERSON_EVENT_ID | NUMBER |  | 18 |  | PERSON_EVENT_ID |
| VAL_TYPE_CD | VARCHAR2 | 30 |  |  | Value is percent or amount |
| PLAN_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_F. |
| PERSON_ID | NUMBER |  | 18 |  | Foreign Key to PER_PEOPLE_F. |
| CRIT_CD1 | VARCHAR2 | 30 |  | Yes | Criteria One. |
| CRIT_CD2 | VARCHAR2 | 30 |  |  | Criteria Two. |
| CRIT_CD3 | VARCHAR2 | 30 |  |  | Criteria Three. |
| CRIT_CD4 | VARCHAR2 | 30 |  |  | Criteria  Four. |
| ALCT_BY_CD | VARCHAR2 | 30 |  | Yes | Allocate by. |
| ACCESS_CD | VARCHAR2 | 30 |  |  | Access of the model |
| SHOW_PROPERTIES_FLAG | VARCHAR2 | 30 |  |  | SHOW_PROPERTIES_FLAG |
| SHOW_SUMMARY_FLAG | VARCHAR2 | 30 |  |  | SHOW_SUMMARY_FLAG |
| REFERENCE_ONLY | VARCHAR2 | 30 |  |  | REFERENCE_ONLY |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| SELECT_PURPOSE | VARCHAR2 | 30 |  |  | SELECT_PURPOSE |
| BUDGET_FUND_LEVEL | VARCHAR2 | 30 |  |  | BUDGET_FUND_LEVEL |
| OVERWRITE_BUDGETS_FLAG | VARCHAR2 | 30 |  |  | OVERWRITE_BUDGETS_FLAG |
| PUBLISH_LEVEL_FLAG | VARCHAR2 | 30 |  |  | PUBLISH_LEVEL_FLAG |
| IS_BATCH_MODE | VARCHAR2 | 20 |  |  | MODEL_MODE |
| LOGIN_PERSON_ID | NUMBER |  | 18 |  | USER_PERSON_ID of logged-in user when model was created |
| ROLE | VARCHAR2 | 1 |  |  | M- If Model is created by Manager A- If Model created by Compensation Admin or Proxy User |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_MODEL_N1 | Non Unique | Default | PLAN_ID |
| CMP_CWB_MODEL_N2 | Non Unique | Default | PERSON_ID |
| CMP_CWB_MODEL_UK1 | Unique | Default | MODEL_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
