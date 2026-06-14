# HWM_GRP_PROC_EVT_QUE

This stores info from the Events generated.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpprocevtque-3210.html#hwmgrpprocevtque-3210](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpprocevtque-3210.html#hwmgrpprocevtque-3210)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_GRP_PROC_EVT_QUE_PK | GRP_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GRP_EVENT_ID | NUMBER |  | 18 | Yes | Primary Key |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise id is stored |
| PERSON_ID | NUMBER |  | 18 | Yes | Column wll store the person_id |
| EVENT_ID | NUMBER |  | 18 | Yes | Column will store the condition_id |
| EVENT_DATE | DATE |  |  | Yes | Column will store the effective date |
| EVENT_PROCESSING_STATUS | NUMBER |  | 9 | Yes | Column  will store the processing status |
| ESS_REQUEST_ID | NUMBER |  | 18 | Yes | Column will store the ess request id |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_GRP_PROC_EVT_QUE_N1 | Non Unique | Default | ESS_REQUEST_ID, PERSON_ID, EVENT_PROCESSING_STATUS |
| HWM_GRP_PROC_EVT_QUE_N2 | Non Unique | Default | PERSON_ID, EVENT_DATE |
| HWM_GRP_PROC_EVT_QUE_U1 | Unique | FUSION_TS_TX_DATA | GRP_EVENT_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
