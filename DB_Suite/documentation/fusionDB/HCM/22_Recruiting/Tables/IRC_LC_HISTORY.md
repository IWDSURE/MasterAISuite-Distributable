# IRC_LC_HISTORY

Stores the history tracking data for the process flexibility.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclchistory-5103.html#irclchistory-5103](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclchistory-5103.html#irclchistory-5103)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LC_HISTORY_PK | HISTORY_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HISTORY_EVENT_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated. |
| STEP_DURATION | NUMBER |  | 18 |  | Duration of the step in seconds |
| EVENT_TYPE_ID | NUMBER |  | 18 | Yes | The identifier of the event type. |
| SOURCE_OBJECT_ID | NUMBER |  | 18 |  | The unique identifier of associated source object. |
| SUBJECT_ID | NUMBER |  | 18 |  | The instance key of associated source object. |
| EVENT_DATE | TIMESTAMP |  |  |  | Date at which the event occurred. Can be different from CREATION_DATE who column value. |
| PERSON_ID | NUMBER |  | 18 |  | The identifier of the person who triggered the event. |
| TRACE_LOG | CLOB |  |  |  | Lifecycle API internal data for troubleshooting purposes. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PROCESS_ID | NUMBER |  | 18 | Yes | The identifier of the lifecycle process for the event. |
| PHASE_ID | NUMBER |  | 18 |  | The identifier of the phase at the time of the event. |
| STATE_ID | NUMBER |  | 18 |  | The identifier of the state at the time of the event. |
| ROUTING_STEP_ID | NUMBER |  | 18 |  | The identifier of the routing step that triggered the event. |
| ACTION_ID | NUMBER |  | 18 |  | The identifier of the action that triggered the event. |
| REASON_ID | NUMBER |  | 18 |  | The identifier of the selected reason for the event update |
| COMMENTS | VARCHAR2 | 1000 |  |  | User entered comments for the event |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LC_HISTORY_FK1 | Non Unique | Default | EVENT_TYPE_ID |
| IRC_LC_HISTORY_FK3 | Non Unique | Default | PROCESS_ID |
| IRC_LC_HISTORY_FK4 | Non Unique | Default | PHASE_ID |
| IRC_LC_HISTORY_FK5 | Non Unique | Default | STATE_ID |
| IRC_LC_HISTORY_FK6 | Non Unique | Default | ROUTING_STEP_ID |
| IRC_LC_HISTORY_FK7 | Non Unique | Default | PERSON_ID |
| IRC_LC_HISTORY_N1 | Non Unique | Default | SOURCE_OBJECT_ID, SUBJECT_ID |
| IRC_LC_HISTORY_N2 | Non Unique | Default | SOURCE_OBJECT_ID, STATE_ID, EVENT_DATE, SUBJECT_ID |
| IRC_LC_HISTORY_PK | Unique | Default | HISTORY_EVENT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
