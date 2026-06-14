# HTS_CONSOL_CHANGE_EVENTS

The table is to store one record for each impacted schedule unit, allowing for efficient tracking and processing of events and their impact on schedule units.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsconsolchangeevents-17167.html#htsconsolchangeevents-17167](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsconsolchangeevents-17167.html#htsconsolchangeevents-17167)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_CONSOL_CHANGE_EVENTS_PK | CONSOLIDATED_CHANGE_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONSOLIDATED_CHANGE_EVENT_ID | NUMBER |  | 18 | Yes | Unique identifier for each consolidated change event record. |
| CHANGE_EVENT_SET_ID | NUMBER |  | 18 | Yes | References the change event set this consolidated event change belongs. |
| CHANGE_EVENT_IDS | VARCHAR2 | 4000 |  | Yes | A comma-separated list of the ids of the change events that are consolidated
into this record. |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Type of the object affected by the consolidated change event. |
| OBJECT_ID | NUMBER |  | 18 | Yes | Identifier of the object affected by the consolidated change event. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Identifier of the assignment related to the consolidated change event. |
| PERSON_ID | NUMBER |  | 18 |  | Identifier of the person related to the consolidated change event. |
| SCHEDULE_UNIT_ID | NUMBER |  | 18 | Yes | Identifier of the schedule unit impacted by the consolidated change event. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PUBLISH_INSTANT | TIMESTAMP |  |  |  | Timestamp when the consolidated change event was published. |
| ATTRIBUTE_CHANGES_CONSOLIDATED | VARCHAR2 | 4000 |  |  | Consolidated attribute changes related to the consolidated change event. |
| DELETE_EVENT_FLAG | VARCHAR2 | 1 |  |  | Flag indicating whether the consolidated change event denotes a deletion. |
| NOTIFIABLE_FLAG | VARCHAR2 | 1 |  |  | Flag indicating if the consolidated event needs to be considered as origin of notified impacts. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_CONSOL_CHANGE_EVENTS_N1 | Non Unique | Default | CHANGE_EVENT_SET_ID |
| HTS_CONSOL_CHANGE_EVENTS_PK | Unique | Default | CONSOLIDATED_CHANGE_EVENT_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
