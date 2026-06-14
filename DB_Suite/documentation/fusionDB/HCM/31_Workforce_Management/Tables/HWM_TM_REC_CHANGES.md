# HWM_TM_REC_CHANGES

Table to store changes for time record or time events.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecchanges-27818.html#hwmtmrecchanges-27818](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecchanges-27818.html#hwmtmrecchanges-27818)

## Primary Key

| Name | Columns |
|------|----------|
| hwm_tm_rec_changes_PK | TM_REC_CHANGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REC_CHANGE_ID | NUMBER |  |  | Yes | TM_REC_CHANGE_ID |
| SECONDARY_TM_REC_ID | NUMBER |  |  |  | Time Record Id to store start time entry for OUT_IN Event type. |
| SECONDARY_TM_REC_VER | NUMBER |  |  |  | Time Record Version to store start time entry for OUT_IN Event type. |
| TM_REC_CHANGE_REQ_ID | NUMBER |  |  | Yes | Foreign key to HWM_TM_REC_CHANGE_REQS |
| TM_REC_ID | NUMBER |  |  |  | Time record that needs to be updated, for new time records, this will be null. |
| TM_REC_VERSION | NUMBER |  |  |  | Version of the time record that needs to be updated, it will be used for tracking concurrent updates |
| TM_EVENT_ID | NUMBER |  |  |  | Time event id in case the request is created on time event. |
| CRUD_STATUS | NUMBER |  |  | Yes | Action being performed on the record, we will use the enum that we have. |
| PROCESS_STATUS | NUMBER |  |  | Yes | Status of the event  (SUBMITTED, SUBMITTED PENDING INTERNALIZATION, APPROVED, APPROVED PENDING INTERNALIZATION, REJECTED, CANCELLED, IN-PROCESS, COMPLETE) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| COMMENTS | VARCHAR2 | 250 |  |  | Used to store justification of the change. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hwm_tm_rec_changes_N1 | Non Unique | Default | TM_REC_ID, TM_REC_VERSION |
| hwm_tm_rec_changes_N2 | Non Unique | Default | TM_EVENT_ID |
| hwm_tm_rec_changes_N3 | Non Unique | Default | TM_REC_CHANGE_REQ_ID |
| hwm_tm_rec_changes_N4 | Non Unique | Default | SECONDARY_TM_REC_ID, SECONDARY_TM_REC_VER |
| hwm_tm_rec_changes_U1 | Unique | Default | TM_REC_CHANGE_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
