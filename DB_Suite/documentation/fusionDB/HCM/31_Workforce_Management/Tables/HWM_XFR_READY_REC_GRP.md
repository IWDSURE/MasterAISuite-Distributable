# HWM_XFR_READY_REC_GRP

A new tables is needed in order to store the time card ready to transfer.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmxfrreadyrecgrp-26833.html#hwmxfrreadyrecgrp-26833](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmxfrreadyrecgrp-26833.html#hwmxfrreadyrecgrp-26833)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_XFR_READY_REC_GRP_PK | XFR_READY_REC_GRP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| XFR_READY_REC_GRP_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CALC_REC_GRP_ID | NUMBER |  | 18 | Yes | Id of the calculated time record group (time card GRP_TYPE_ID=200) |
| CALC_REC_GRP_VERSION | NUMBER |  | 9 | Yes | Version of the calculated time record group |
| TM_REC_GRP_ID | NUMBER |  | 18 | Yes | Id of the reported time record group (time card  GRP_TYPE_ID=100) |
| TM_REC_GRP_VERSION | NUMBER |  | 9 | Yes | Version of the reported time record group |
| START_TIME | TIMESTAMP |  |  | Yes | Start time of the time record group |
| STOP_TIME | TIMESTAMP |  |  | Yes | Stop time of the time record group |
| RESOURCE_ID | NUMBER |  | 18 | Yes | RESOURCE_ID |
| SUBRESOURCE_ID | NUMBER |  | 18 | Yes | SUBRESOURCE_ID |
| TCSMRS_ID | NUMBER |  | 18 | Yes | Time consumer id |
| LDG_OR_BU_ID | NUMBER |  | 18 | Yes | LDG (Payroll) or Business id (Project) |
| XFR_STATUS | NUMBER |  | 2 | Yes | Status of the record: 1=Pending, 2=Selected, 3=Finish,... |
| XFR_JOB | NUMBER |  | 18 |  | Transfer job associated with the record. |
| SOURCE | NUMBER |  | 1 | Yes | Indicates which process made the time card transferable. 1 = Approval, 2 Crunch |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| GRP_REC_COUNT | NUMBER |  | 5 |  | GRP_REC_COUNT |
| MARK_FOR_TRANSFER | NUMBER |  | 18 |  | Used to mark the row as ready for transfer |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_XFR_READY_REC_GRP_N1 | Non Unique | Default | TCSMRS_ID, LDG_OR_BU_ID, START_TIME |
| HWM_XFR_READY_REC_GRP_N2 | Non Unique | Default | TM_REC_GRP_ID, TM_REC_GRP_VERSION, XFR_STATUS |
| HWM_XFR_READY_REC_GRP_N3 | Non Unique | Default | CALC_REC_GRP_ID |
| hwm_xfr_ready_rec_grp_U1 | Unique | Default | XFR_READY_REC_GRP_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
