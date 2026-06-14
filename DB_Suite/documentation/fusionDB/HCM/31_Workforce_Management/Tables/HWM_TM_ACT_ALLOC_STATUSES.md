# HWM_TM_ACT_ALLOC_STATUSES

Activity allocation entries statuses

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmactallocstatuses-18127.html#hwmtmactallocstatuses-18127](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmactallocstatuses-18127.html#hwmtmactallocstatuses-18127)

## Primary Key

| Name | Columns |
|------|----------|
| hwm_tm_act_alloc_statuses_PK | TM_ACT_ALLOC_STATUS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_ACT_ALLOC_STATUS_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number. This column is not updateable. |
| TM_ACT_ALLOC_ID | NUMBER |  | 18 | Yes | Foreign Key column from HWM_TM_ACT_ALLOCS table |
| TM_ACT_ALLOC_VERSION | NUMBER |  | 9 | Yes | Foreign Key column from HWM_TM_ACT_ALLOCS table |
| ALLOCATION_STATUS | VARCHAR2 | 30 |  | Yes | To represent allocation status depending on Attributes. |
| TRANSFER_STATUS | VARCHAR2 | 30 |  | Yes | To represent transfer status of allocation and it's attribute details. |
| TRANSFER_PROCESS_END_TIME | TIMESTAMP |  |  |  | Transfer process completion time that is provided by the consumer, converted in UTC time. |
| TRANSFER_PROCESS_END_TIME_STR | VARCHAR2 | 100 |  |  | Transfer process completion time that is provided by the consumer |
| DATE_FROM | TIMESTAMP |  |  | Yes | validity start time of the row |
| DATE_TO | TIMESTAMP |  |  | Yes | validity end time of the row |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_ACT_ALLOC_STATUSES_N1 | Non Unique | Default | TM_ACT_ALLOC_ID, TM_ACT_ALLOC_VERSION, TRANSFER_STATUS, DATE_FROM, DATE_TO |
| HWM_TM_ACT_ALLOC_STATUSES_U1 | Unique | Default | TM_ACT_ALLOC_STATUS_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
