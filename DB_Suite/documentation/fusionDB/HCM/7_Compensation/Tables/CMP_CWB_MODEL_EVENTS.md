# CMP_CWB_MODEL_EVENTS

CMP_CWB_MODEL_EVENTS stores the employees details of a model

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbmodelevents-13346.html#cmpcwbmodelevents-13346](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbmodelevents-13346.html#cmpcwbmodelevents-13346)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_MODEL_EVENTS_PK | MODEL_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MODEL_EVENT_ID | NUMBER |  |  | Yes | MODEL_EVENT_ID |
| MODEL_ID | NUMBER |  | 18 | Yes | MODEL_ID |
| MODEL_DTL_ID | NUMBER |  | 20 | Yes | MODEL_DTL_ID |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |
| COMPONENT_ID | NUMBER |  | 18 | Yes | COMPONENT_ID |
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | PERSON_EVENT_ID |
| MGR_PERSON_EVENT_ID | NUMBER |  | 18 |  | MGR_PERSON_EVENT_ID |
| EVENTS_LVL_NUM | NUMBER |  | 10 |  | EVENTS_LVL_NUM |
| USER_PERSON_ID | NUMBER |  | 18 | Yes | USER_PERSON_ID |
| INCLUSION_FLAG | VARCHAR2 | 1 |  |  | INCLUSION_FLAG |
| CRIT1_VAL | VARCHAR2 | 150 |  |  | CRIT1_VAL |
| CRIT2_VAL | VARCHAR2 | 150 |  |  | CRIT2_VAL |
| CRIT3_VAL | VARCHAR2 | 150 |  |  | CRIT3_VAL |
| CRIT4_VAL | VARCHAR2 | 150 |  |  | CRIT4_VAL |
| NEW_GRADE_VALUE | VARCHAR2 | 30 |  |  | NEW_GRADE_VALUE |
| NUM_VAL1 | NUMBER |  |  |  | NUM_VAL1 |
| NUM_VAL2 | NUMBER |  |  |  | NUM_VAL2 |
| TEXT_VAL | VARCHAR2 | 150 |  |  | TEXT_VAL |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SCND_LVL_MNGR_EVENT_ID | NUMBER |  | 18 |  | SCND_LVL_MNGR_EVENT_ID |
| USER_PERSON_EVENT_ID | NUMBER |  | 18 |  | Manager person event id |
| DATE_VAL | DATE |  |  |  | DATE_VAL |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_MODEL_EVENTS_U1 | Unique | Default | MODEL_ID, USER_PERSON_ID, PERSON_EVENT_ID |
| CMP_CWB_MODEL_EVENTS_UK1 | Unique | Default | MODEL_EVENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
