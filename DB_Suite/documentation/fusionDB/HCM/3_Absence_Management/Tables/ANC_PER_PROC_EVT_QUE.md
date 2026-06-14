# ANC_PER_PROC_EVT_QUE

This table is designed to capture person event.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperprocevtque-23267.html#ancperprocevtque-23267](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperprocevtque-23267.html#ancperprocevtque-23267)

## Primary Key

| Name | Columns |
|------|----------|
| anc_per_proc_evt_que_PK | PERSON_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | Person Event Id |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise Id |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Id |
| PRD_OF_SVC_ID | NUMBER |  | 18 | Yes | Period of service Id |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Assignment Id |
| LEGAL_ENTITY_ID | NUMBER |  | 18 | Yes | Legal entity Id |
| EVENT_ID | NUMBER |  | 18 | Yes | Event Id |
| EVENT_DATE | DATE |  |  | Yes | The date on which event occurred |
| EVENT_PROCESSING_STATUS | VARCHAR2 | 32 |  | Yes | ORA_ANC_UNPROCESSED     
ORA_ANC_PROCESSED       
ORA_ANC_WARNING
ORA_ANC_ERROR |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | Ess Request Id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PLAN_ENRL_STATUS | VARCHAR2 | 32 |  |  | For future use |
| ACCRL_STATUS | VARCHAR2 | 32 |  |  | For future use |
| EVAL_ABS_STATUS | VARCHAR2 | 32 |  |  | For future use |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_PROC_EVT_QUE_N1 | Non Unique | Default | PERSON_ID, EVENT_ID, EVENT_DATE |
| ANC_PER_PROC_EVT_QUE_N2 | Non Unique | Default | LEGAL_ENTITY_ID, EVENT_ID, EVENT_DATE |
| ANC_PER_PROC_EVT_QUE_N3 | Non Unique | Default | EVENT_DATE |
| ANC_PER_PROC_EVT_QUE_U1 | Unique | Default | PERSON_EVENT_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
