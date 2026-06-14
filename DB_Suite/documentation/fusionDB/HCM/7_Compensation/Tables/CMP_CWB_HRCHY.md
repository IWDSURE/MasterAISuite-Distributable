# CMP_CWB_HRCHY

Stores the hierarchies used to determine the approval chain for a budget or reward. The hierarchy can be based on the supervisor, a standard position hierarchy, or a completely customized logic.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbhrchy-30565.html#cmpcwbhrchy-30565](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbhrchy-30565.html#cmpcwbhrchy-30565)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_HRCHY_PK | MGR_PERSON_EVENT_ID, EMP_PERSON_EVENT_ID, LVL_NUM |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MGR_PERSON_EVENT_ID | NUMBER |  | 18 | Yes | MGR_PERSON_EVENT_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| EMP_PERSON_EVENT_ID | NUMBER |  | 18 | Yes | EMP_PERSON_EVENT_ID |
| LVL_NUM | NUMBER |  | 18 | Yes | LVL_NUM |
| NUMBER_VALUE1 | NUMBER |  |  |  | MODEL_NUM_VAL_ONE |
| NUMBER_VALUE2 | NUMBER |  |  |  | MODEL_NUM_VAL_TWO |
| TEXT_VALUE | VARCHAR2 | 150 |  |  | MODEL_TEXT_VAL |
| MGR_PERSON_ID | NUMBER |  | 18 |  | MGR_PERSON_ID |
| MGR_ASSIGNMENT_ID | NUMBER |  | 18 |  | MGR_ASSIGNMENT_ID |
| EMP_PERSON_ID | NUMBER |  | 18 |  | EMP_PERSON_ID |
| EMP_ASSIGNMENT_ID | NUMBER |  | 18 |  | EMP_ASSIGNMENT_ID |
| HRCHY_PLAN_ID | NUMBER |  | 18 |  | HRCHY_PLAN_ID |
| HRCHY_PERIOD_ID | NUMBER |  | 18 |  | HRCHY_PERIOD_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_HRCHY_N1 | Non Unique | Default | EMP_PERSON_EVENT_ID, LVL_NUM |
| CMP_CWB_HRCHY_N2 | Non Unique | Default | MGR_PERSON_EVENT_ID, LVL_NUM |
| CMP_CWB_HRCHY_N3 | Non Unique | Default | MGR_PERSON_ID, EMP_PERSON_ID |
| CMP_CWB_HRCHY_N4 | Non Unique | Default | HRCHY_PERIOD_ID, HRCHY_PLAN_ID, LVL_NUM |
| CMP_CWB_HRCHY_PK | Unique | Default | MGR_PERSON_EVENT_ID, EMP_PERSON_EVENT_ID, LVL_NUM |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
