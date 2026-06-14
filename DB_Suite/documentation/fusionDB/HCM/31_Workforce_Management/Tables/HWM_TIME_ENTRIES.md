# HWM_TIME_ENTRIES

Table where time card entry data retrieved from related REST services are stored. These time entries display in the Visual Builder Cloud Service time card grid component.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtimeentries-30061.html#hwmtimeentries-30061](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtimeentries-30061.html#hwmtimeentries-30061)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TIME_ENTRIES_PK | TIME_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TIME_ENTRY_ID | NUMBER |  | 18 | Yes | Time entry identifier |
| TIME_ENTRY_VERSION | NUMBER |  | 9 | Yes | Time entry version |
| GROUPING_SEQ | NUMBER |  | 9 |  | Grouping sequence number |
| START_TIME | TIMESTAMP |  |  |  | Time entry start time |
| STOP_TIME | TIMESTAMP |  |  |  | Time entry stop time |
| MEASURE | NUMBER |  |  |  | Time entry quantity |
| UNIT_OF_MEASURE | VARCHAR2 | 30 |  |  | Unit of measure |
| COMMENT_TEXT | VARCHAR2 | 2000 |  |  | Comments about the time entry |
| PERSON_ID | NUMBER |  | 18 |  | Person identifier for the time card |
| TIMECARD_ID | NUMBER |  | 18 | Yes | Time card identifier |
| ABSENCE_TYPE | NUMBER |  | 18 |  | ABSENCE_TYPE |
| ABSENCE_SHIFT_BREAKDOWN_ID | NUMBER |  |  |  | ABSENCE_SHIFT_BREAKDOWN_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TIME_ENTRIES_N1 | Non Unique | DEFAULT | TIMECARD_ID |
| HWM_TIME_ENTRIES_PK | Unique | DEFAULT | TIME_ENTRY_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
