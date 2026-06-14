# HTS_SCHED_RESET_EVENTS

Schedule events indicating schedule data that needs to be reset.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedresetevents-15822.html#htsschedresetevents-15822](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedresetevents-15822.html#htsschedresetevents-15822)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_RESET_EVENTS_PK | SCHED_RESET_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_RESET_EVENT_ID | NUMBER |  | 18 | Yes | Primary key identifiying a schedule reset event record by a system generated ID |
| PERSON_ID | NUMBER |  | 18 | Yes | Identifies the person whose schedule needs to be reset. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | The employee assignment ID on which schedule needs to be reset. |
| EVENT_START_DATE | DATE |  |  | Yes | The first date of the date range for which the schedule needs to be reset. |
| EVENT_END_DATE | DATE |  |  |  | The last date of the date range for which the schedule needs to be reset. |
| EVENT_STATUS | NUMBER |  | 2 |  | EVENT_STATUS |
| PROCESS_ID | NUMBER |  | 18 |  | ESS process ID for current Reset process |
| RESET_TYPE | NUMBER |  | 2 | Yes | Identifies the target layer to which the schedule needs to be reset |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_RESET_EVENTS_N1 | Non Unique | FUSION_TS_TX_IDX | PERSON_ID, EVENT_START_DATE, EVENT_END_DATE, RESET_TYPE, ASSIGNMENT_ID |
| HTS_SCHED_RESET_EVENTS_N2 | Non Unique | FUSION_TS_TX_IDX | PROCESS_ID, PERSON_ID |
| HTS_SCHED_RESET_EVENTS_U1 | Unique | FUSION_TS_TX_IDX | SCHED_RESET_EVENT_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
