# HWM_XFR_READY_STATUS_EVENTS

Insert the time card id in staging table HWM_XFR_READY_STATUS_EVENTS

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmxfrreadystatusevents-16148.html#hwmxfrreadystatusevents-16148](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmxfrreadystatusevents-16148.html#hwmxfrreadystatusevents-16148)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_XFR_READY_STATUS_EVEN_PK | XFR_READY_STATUS_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| XFR_READY_STATUS_EVENT_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TM_REC_GRP_ID | NUMBER |  | 18 | Yes | Id of the reported time record group (time card  GRP_TYPE_ID=100) |
| EVENT_STATUS | NUMBER |  | 2 | Yes | Status of the record: 1=Pending, 2=InProcess, 3=Finish,.. |
| RESOURCE_ID | NUMBER |  | 18 | Yes | RESOURCE_ID |
| SOURCE | NUMBER |  | 1 | Yes | Indicates which process made the time card transferable. 1 = Timecard flow, 2 Crunch |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_XFR_READY_STATUS_EVENTS_U1 | Unique | Default | XFR_READY_STATUS_EVENT_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
