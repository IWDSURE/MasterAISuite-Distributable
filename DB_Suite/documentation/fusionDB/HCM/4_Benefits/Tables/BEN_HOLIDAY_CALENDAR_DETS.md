# BEN_HOLIDAY_CALENDAR_DETS

BEN_HOLIDAY_CALENDAR_DETS stores dates as the holidays or excluded days.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benholidaycalendardets-21977.html#benholidaycalendardets-21977](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benholidaycalendardets-21977.html#benholidaycalendardets-21977)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_HOLIDAY_CALENDAR_DETS_PK | CALENDAR_DET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CALENDAR_DET_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| CALENDAR_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_HOLIDAY_CALENDAR.CALENDAR_ID. |
| HOLIDAY_NAME | VARCHAR2 | 30 |  | Yes | Name of the holiday. |
| HOLIDAY_DATE | DATE |  |  | Yes | Day of the holiday to exclude from absence. |
| HOLIDAY_TYPE | VARCHAR2 | 30 |  |  | Type of holiday. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_HOL_CALE_DETS_PK | Unique | FUSION_TS_TX_DATA | CALENDAR_DET_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
