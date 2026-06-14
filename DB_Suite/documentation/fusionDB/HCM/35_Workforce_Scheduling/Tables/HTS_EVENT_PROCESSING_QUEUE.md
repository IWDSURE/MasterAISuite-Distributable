# HTS_EVENT_PROCESSING_QUEUE

Table to store the polled events information to be processed.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htseventprocessingqueue-11610.html#htseventprocessingqueue-11610](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htseventprocessingqueue-11610.html#htseventprocessingqueue-11610)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_EVENT_PROCESSING_QUEUE_PK | EVENT_PROCESSING_QUEUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_PROCESSING_QUEUE_ID | NUMBER |  | 18 | Yes | Unique system generated identifier for an event row that is to be processed |
| PERSON_ID | NUMBER |  | 18 | Yes | Person ID for which event is generated. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Assignment ID for which event is generated. |
| EVENT_CHANGE_ID | NUMBER |  | 18 | Yes | Identifier that maps to the ChangeID in hrc_evt_obj_changes. |
| EVENT_EFFECTIVE_DATE | DATE |  |  | Yes | Effective date of the event. |
| EVENT_DML_OPERATION | VARCHAR2 | 240 |  | Yes | Operation that generated the event. |
| PROCESSING_STATUS | VARCHAR2 | 30 |  | Yes | Processing status of this event record. |
| POLLED_ESS_REQUEST_ID | NUMBER |  | 18 | Yes | ESS request ID which polled this event record. |
| PROCESSED_ESS_REQUEST_ID | NUMBER |  | 18 |  | ESS request ID which last processed this event record. |
| PROCESS_LOGS | VARCHAR2 | 2000 |  |  | To capture information on processing of events like which work pattern was created, updated, deleted etc. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_EVENT_PROCESSING_QUEUE_N1 | Non Unique | Default | PERSON_ID, EVENT_EFFECTIVE_DATE, PROCESSING_STATUS |
| HTS_EVENT_PROCESSING_QUEUE_U1 | Unique | Default | EVENT_PROCESSING_QUEUE_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
