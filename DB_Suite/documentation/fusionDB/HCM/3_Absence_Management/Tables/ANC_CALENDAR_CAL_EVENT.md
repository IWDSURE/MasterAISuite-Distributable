# ANC_CALENDAR_CAL_EVENT

Table for events in organization calendars

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/anccalendarcalevent-16995.html#anccalendarcalevent-16995](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/anccalendarcalevent-16995.html#anccalendarcalevent-16995)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_CALENDAR_CAL_EVENT_PK | CALENDAR_CAL_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CALENDAR_CAL_EVENT_ID | NUMBER |  | 18 | Yes | Calendar Event ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Eneterprise ID |
| CALENDAR_ID | NUMBER |  | 18 | Yes | Calendar ID |
| CALENDAR_EVENT_ID | NUMBER |  | 18 | Yes | Event ID |
| EVENT_CATEGORY_CODE | VARCHAR2 | 64 |  |  | Calendar Event Category Code |
| EVENT_TYPE | VARCHAR2 | 64 |  |  | Member Type |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_CALENDAR_CAL_EVENT_FK1 | Non Unique | Default | CALENDAR_ID |
| ANC_CALENDAR_CAL_EVENT_PK | Unique | Default | CALENDAR_CAL_EVENT_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
