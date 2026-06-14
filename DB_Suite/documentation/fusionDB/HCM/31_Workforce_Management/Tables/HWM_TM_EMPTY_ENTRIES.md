# HWM_TM_EMPTY_ENTRIES

table to store timecard entries with only attribute values

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmemptyentries-13470.html#hwmtmemptyentries-13470](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmemptyentries-13470.html#hwmtmemptyentries-13470)

## Primary Key

| Name | Columns |
|------|----------|
| hwm_tm_empty_entries_PK | TIMECARD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TIMECARD_ID | NUMBER |  | 18 | Yes | Timecard identifier |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAYOUT_ID | NUMBER |  | 18 | Yes | Timecard Layout Id |
| SNAPSHOT | CLOB |  |  | Yes | Time attributes |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hwm_tm_empty_entries_PK | Unique | Default | TIMECARD_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
