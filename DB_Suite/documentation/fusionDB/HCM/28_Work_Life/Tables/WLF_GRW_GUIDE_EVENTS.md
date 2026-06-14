# WLF_GRW_GUIDE_EVENTS

Table to store Events for Guide.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwguideevents-22183.html#wlfgrwguideevents-22183](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwguideevents-22183.html#wlfgrwguideevents-22183)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_GRW_GUIDE_EVENTS_PK | GUIDE_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GUIDE_EVENT_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| GUIDE_ID | NUMBER |  | 18 | Yes | Guide Id for which event is created |
| EVENT_TYPE | VARCHAR2 | 30 |  | Yes | Represents the type of event |
| EVENT_CREATION_DATE | TIMESTAMP |  |  |  | Date to be captured for event creation date |
| EVENT_REMOVE_DATE | TIMESTAMP |  |  |  | Date to be captured for event removed date |
| EVENT_SOURCE_ID | NUMBER |  | 30 |  | Sourse system ID from where this Guide Id  event is created |
| EVENT_SOURCE_TYPE | VARCHAR2 | 30 |  |  | Sourse system type from where this Guide Id  event is created |
| ATTRIBUTION_ID | NUMBER |  | 18 | Yes | Person Id for which Guide event is created |
| ATTRIBUTION_TYPE | VARCHAR2 | 30 |  | Yes | Represents the attribution type of the owner/person of the event |
| STATUS | VARCHAR2 | 30 |  | Yes | Status of the Event (e.g Active,InActiveetc.) |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_GRW_GUIDE_EVENTS_U1 | Unique | Default | GUIDE_EVENT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
