# HWM_TM_ACT_ALLOC_DAY_STATUSES

Daily statuses with regards to activity allocation

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmactallocdaystatuses-15104.html#hwmtmactallocdaystatuses-15104](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmactallocdaystatuses-15104.html#hwmtmactallocdaystatuses-15104)

## Primary Key

| Name | Columns |
|------|----------|
| hwm_tm_act_alloc_day_stat_PK | TM_ACT_ALLOC_DAY_STATUS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_ACT_ALLOC_DAY_STATUS_ID | NUMBER |  | 18 | Yes | auto-generated row ID |
| RESOURCE_ID | NUMBER |  | 18 | Yes | Contains Person/Resource ID |
| STATUS_DATE | DATE |  |  | Yes | Day to which the status refer |
| STATUS | VARCHAR2 | 30 |  | Yes | To represent Day status of allocation depending on hours to allocate and hours allocated. |
| HOURS_TO_ALLOCATE | NUMBER |  |  |  | total duration to allocate, in minutes, computed while evaluating the daily status. Saved each time we update the status |
| HOURS_ALLOCATED | NUMBER |  |  |  | total duration allocated, in minutes, computed while evaluating the daily status. Saved each time we update the status |
| REFRESH_CODE | NUMBER |  | 9 | Yes | To represent current status or type of refresh action to perform. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_ACT_ALLOC_DAY_STAT_U1 | Unique | Default | TM_ACT_ALLOC_DAY_STATUS_ID |
| HWM_TM_ACT_ALLOC_DAY_STAT_U2 | Unique | Default | RESOURCE_ID, STATUS_DATE |
| HWM_TM_ACT_ALLOC_DAY_STAT_U3 | Unique | Default | STATUS, STATUS_DATE, RESOURCE_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
