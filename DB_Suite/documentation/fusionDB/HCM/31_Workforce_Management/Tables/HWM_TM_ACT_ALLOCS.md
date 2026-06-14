# HWM_TM_ACT_ALLOCS

Activity allocations entered against the reported times for a person and a date

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmactallocs-13453.html#hwmtmactallocs-13453](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmactallocs-13453.html#hwmtmactallocs-13453)

## Primary Key

| Name | Columns |
|------|----------|
| hwm_tm_act_allocs_PK | TM_ACT_ALLOC_ID, TM_ACT_ALLOC_VERSION |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_ACT_ALLOC_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| TM_ACT_ALLOC_VERSION | NUMBER |  | 9 | Yes | Part of Primary Key column with incremental value starting from 1 for every unique TM_ACT_ALLOC_ID. |
| RESOURCE_ID | NUMBER |  | 18 | Yes | Contains Person/Resource ID |
| ALLOCATION_DATE | DATE |  |  | Yes | Respective Date for which allocation details is being applied |
| DURATION | NUMBER |  | 9 | Yes | Minutes converted value for Allocation |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LATEST_VERSION | VARCHAR2 | 1 |  | Yes | Y/N. Indicates if this is the most recent version of the Activity Allocation entry. |
| DELETE_FLAG | VARCHAR2 | 1 |  | Yes | Y/N. Indicates if the Activity Allocation entry has been deleted or not. |
| DATE_FROM | TIMESTAMP |  |  | Yes | validity start time of the row |
| DATE_TO | TIMESTAMP |  |  | Yes | validity end time of the row |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hwm_tm_act_allocs_N1 | Non Unique | Default | LATEST_VERSION, ALLOCATION_DATE, RESOURCE_ID |
| hwm_tm_act_allocs_N2 | Non Unique | Default | RESOURCE_ID, ALLOCATION_DATE, LATEST_VERSION, DELETE_FLAG |
| hwm_tm_act_allocs_U1 | Unique | Default | TM_ACT_ALLOC_ID, TM_ACT_ALLOC_VERSION |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
