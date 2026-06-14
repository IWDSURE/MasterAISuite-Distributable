# HWM_CHANGE_EVENTS

The table stores records of changes made to specific objects (e.g., Absence, Assignment) as received from an Atom feed. It captures the details of each change event, including the type of object affected, the operation performed, and relevant metadata.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmchangeevents-13988.html#hwmchangeevents-13988](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmchangeevents-13988.html#hwmchangeevents-13988)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_CHANGE_EVENTS_PK | CHANGE_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHANGE_EVENT_ID | NUMBER |  | 18 | Yes | A unique identifier of change event |
| CHANGE_EVENT_SET_ID | NUMBER |  | 18 | Yes | References the change event set to which this change event belongs |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | The type of object which raises the event |
| OBJECT_ID | NUMBER |  | 18 | Yes | Identifier of the object whose change raised the event. |
| OPERATION | VARCHAR2 | 30 |  | Yes | Type of operation performed on the object |
| EFFECTIVE_DATE | DATE |  |  |  | Date when the event change became or will become effective. |
| CHANGE_ID | NUMBER |  | 18 |  | Identifier of the change event from the Atom response |
| CHANGE_CONTENT | VARCHAR2 | 4000 |  |  | Summary of the atom feed entry content denoting the change event. |
| PUBLISHED_INSTANT | TIMESTAMP |  |  | Yes | Timestamp when the event change was published. |
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
| HWM_CHANGE_EVENTS_N1 | Non Unique | Default | CHANGE_EVENT_SET_ID |
| HWM_CHANGE_EVENTS_PK | Unique | Default | CHANGE_EVENT_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
