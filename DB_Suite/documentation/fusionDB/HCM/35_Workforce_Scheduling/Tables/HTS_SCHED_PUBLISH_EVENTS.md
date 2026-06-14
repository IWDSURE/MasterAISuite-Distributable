# HTS_SCHED_PUBLISH_EVENTS

Schedules events indicating schedules changes not yet published

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedpublishevents-21527.html#htsschedpublishevents-21527](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedpublishevents-21527.html#htsschedpublishevents-21527)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_PUBLISH_EVENTS_PK | SCHED_PUBLISH_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_PUBLISH_EVENT_ID | NUMBER |  | 18 | Yes | Primary key identifiying the publish event record by a system generated ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| PERSON_ID | NUMBER |  | 18 |  | Identifies the person for whom the schedule needs to be published |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | The employee assignment ID for which the schedule needs to be published. |
| EVENT_DATE | DATE |  |  |  | The date for which the schedule needs to be published |
| EVENT_STATUS | NUMBER |  | 2 |  | Status of the publish event (0: new, 1: in process) |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_PUBLISH_EVENTS_N1 | Non Unique | FUSION_TS_TX_IDX | PERSON_ID, EVENT_DATE, EVENT_STATUS, ASSIGNMENT_ID |
| HTS_SCHED_PUBLISH_EVENTS_PK | Unique | FUSION_TS_TX_IDX | SCHED_PUBLISH_EVENT_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
