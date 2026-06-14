# CMP_CWB_PLAN_ACCESS

Table to record access by a person to the worksheet of a manager

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbplanaccess-5269.html#cmpcwbplanaccess-5269](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbplanaccess-5269.html#cmpcwbplanaccess-5269)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_PLAN_ACCESS_PK | PERSON_ID, PERSON_EVENT_ID, ACCESS_TYPE, PLAN_TYPE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_ACCESS_ID | NUMBER |  | 18 | Yes | Unique id for plan access |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Identifier |
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | Identifier for a manager's assignment in a plan cycle |
| ACCESS_TYPE | VARCHAR2 | 30 |  | Yes | Type of worksheet accessed based on role |
| PLAN_TYPE | VARCHAR2 | 30 |  | Yes | Type of plan accessed based on hierarchy |
| ACCESS_CODE | VARCHAR2 | 30 |  | Yes | Code that indicates the kind of access person has to a manager's worksheet |
| PLAN_ID | NUMBER |  | 18 | Yes | Plan Identifier |
| PERIOD_ID | NUMBER |  | 18 | Yes | Period Identifier |
| ACTING_PERSON_ID | NUMBER |  | 18 |  | Acting person identifier |
| ACTING_ASSIGNMENT_ID | NUMBER |  | 18 |  | Acting person's assignment identifier |
| PRIOR_ACCESS_DATE | TIMESTAMP |  |  |  | Indicates the date and time of the prior access |
| PRIOR_ACCESS_CODE | VARCHAR2 | 30 |  |  | Indicates the kind of prior access the person had to a manager's worksheet |
| LAST_SAVE_DATE | TIMESTAMP |  |  |  | Indicates the date and time of the last save |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_PLAN_ACCESS_N1 | Non Unique | Default | PERSON_EVENT_ID, ACCESS_TYPE, PLAN_TYPE |
| CMP_CWB_PLAN_ACCESS_PK | Unique | Default | PERSON_ID, PERSON_EVENT_ID, ACCESS_TYPE, PLAN_TYPE |
| CMP_CWB_PLAN_ACCESS_U1 | Unique | Default | PLAN_ACCESS_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
