# ANC_CAL_EVENTSET_EVENT

Table for Events in Calendar Events Set.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/anccaleventsetevent-8484.html#anccaleventsetevent-8484](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/anccaleventsetevent-8484.html#anccaleventsetevent-8484)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_CAL_EVENTSET_EVENT_PK | CAL_EVENTSET_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAL_EVENTSET_EVENT_ID | NUMBER |  | 18 | Yes | Calendar Event Set Event ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Eneterprise ID |
| CAL_EVENTSET_ID | NUMBER |  | 18 | Yes | Calendar Event Set ID |
| CALENDAR_EVENT_ID | NUMBER |  | 18 |  | Calendar Event ID |
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
| ANC_CAL_EVENTSET_EVENT_FK1 | Non Unique | Default | CAL_EVENTSET_ID |
| ANC_CAL_EVENTSET_EVENT_PK | Unique | Default | CAL_EVENTSET_EVENT_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
