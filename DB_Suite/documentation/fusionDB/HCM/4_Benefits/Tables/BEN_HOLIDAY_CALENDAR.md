# BEN_HOLIDAY_CALENDAR

BEN_HOLIDAY_CALENDAR is used to define holidays or excluded days for the absence calculation.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benholidaycalendar-8628.html#benholidaycalendar-8628](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benholidaycalendar-8628.html#benholidaycalendar-8628)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_HOLIDAY_CALENDAR_PK | CALENDAR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CALENDAR_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| CALENDAR_NAME | VARCHAR2 | 30 |  | Yes | Name of the Calendar. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Legislative Data Group |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_HOLIDAY_CALDAR_PK | Unique | FUSION_TS_TX_DATA | CALENDAR_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
