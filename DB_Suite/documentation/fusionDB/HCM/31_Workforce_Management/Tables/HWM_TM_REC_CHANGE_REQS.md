# HWM_TM_REC_CHANGE_REQS

Table to store change requests for time entries or time events.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecchangereqs-24291.html#hwmtmrecchangereqs-24291](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecchangereqs-24291.html#hwmtmrecchangereqs-24291)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_REC_CHANGE_REQS_PK | TM_REC_CHANGE_REQ_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REC_CHANGE_REQ_ID | NUMBER |  |  | Yes | TM_REC_CHANGE_REQ_ID |
| TIMECARD_START_TIME | TIMESTAMP |  |  |  | TimeCard Start Time |
| TIMECARD_STOP_TIME | TIMESTAMP |  |  |  | TimeCard Stop Time |
| CHANGE_DATE | DATE |  |  |  | Date of the entry/event which is being modified. |
| RESOURCE_ID | NUMBER |  |  |  | RESOURCE_ID |
| TM_REC_GRP_ID | NUMBER |  |  |  | TM_REC_GRP_ID |
| STATUS | NUMBER |  |  | Yes | STATUS |
| SUBMISSION_DATE | TIMESTAMP |  |  | Yes | SUBMISSION_DATE |
| CHANGE_REASON | VARCHAR2 | 30 |  |  | CHANGE_REASON |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_REC_CHANGE_REQS_N3 | Non Unique | Default | STATUS, RESOURCE_ID, TIMECARD_START_TIME, TIMECARD_STOP_TIME |
| hwm_tm_rec_change_reqs_N1 | Non Unique | Default | TM_REC_GRP_ID |
| hwm_tm_rec_change_reqs_N2 | Non Unique | Default | CHANGE_DATE, RESOURCE_ID, STATUS |
| hwm_tm_rec_change_reqs_U1 | Unique | FUSION_TS_TX_DATA | TM_REC_CHANGE_REQ_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
