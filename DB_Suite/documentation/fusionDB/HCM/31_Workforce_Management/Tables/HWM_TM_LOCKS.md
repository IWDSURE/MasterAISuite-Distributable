# HWM_TM_LOCKS

Corresponds to a particular period for a particular resource in the repository that is in-use by some interface in the application.  Entries in this table ensure two interfaces do not try to update the same information simultaneously.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmlocks-19757.html#hwmtmlocks-19757](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmlocks-19757.html#hwmtmlocks-19757)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_LOCKS_PK | LOCK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOCK_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| GROUPING | VARCHAR2 | 50 |  |  | GROUPING |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TIME_BLDG_BLK_ID | NUMBER |  | 18 |  | Foreign Key to the Time Building Blocks |
| TIME_BLDG_BLK_VERSION | NUMBER |  | 9 |  | Foreign Key to the Time Building Blocks |
| PROCESS_MODE_ID | NUMBER |  | 18 |  | Foreign Key to the Time Processes that is holding the lock |
| RESOURCE_ID | NUMBER |  | 18 |  | The Resource of the Pending Timecard |
| START_TIME | TIMESTAMP |  |  |  | The Start Time of the pending Timecard |
| STOP_TIME | TIMESTAMP |  |  |  | The Stop Time of the Pending Timecard |
| LOCK_ACQUIRED_TIME | TIMESTAMP |  |  |  | The Date and Time that the lock was acquired |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_LOCKS_PK | Unique | FUSION_TS_TX_DATA | LOCK_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
