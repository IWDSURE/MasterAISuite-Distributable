# HTS_SCHED_EVENTS

Table to store schedule events during import schedule process

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedevents-29991.html#htsschedevents-29991](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedevents-29991.html#htsschedevents-29991)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_EVENTS_PK | SCHED_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_EVENT_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| SCHED_REQUEST_NUMBER | VARCHAR2 | 120 |  |  | Identifier of the request as specified by the exporter |
| SCHED_EVENT_NUMBER | VARCHAR2 | 120 |  |  | Identifier of the schedule event as specified by the exporter |
| SCHED_REQUEST_ID | NUMBER |  | 18 |  | SCHED_REQUEST_ID |
| RESOURCE_REF | VARCHAR2 | 120 |  |  | The resource reference that matches the specified resource reference type. |
| RESOURCE_REF_TYPE | VARCHAR2 | 30 |  |  | Resource reference type. For now,  4 possible values: Assignment id, Assignment Number, Person Id, Person Number. |
| RESOURCE_ID | NUMBER |  | 18 |  | RESOURCE_ID |
| RESOURCE_ASSIGN_ID | NUMBER |  | 18 |  | RESOURCE_ASSIGN_ID |
| IMPORT_MODE | VARCHAR2 | 20 |  |  | Import mode. Values are FULL or  UPDATE. |
| PERIOD_START_DATE | DATE |  |  |  | The period start date of the schedule that is imported |
| PERIOD_END_DATE | DATE |  |  |  | The period end date of the schedule that is imported |
| PUBLISH | VARCHAR2 | 1 |  |  | Specify whether to publish the imported schedules. Values are Y or N. |
| ALLOW_EDITS | VARCHAR2 | 1 |  |  | Specify whether the schedule that is imported can be edited by the scheduler in
the application, on the Manage Planned Schedule page. Values are Y or N. |
| WORKER_NOTIF | VARCHAR2 | 1 |  |  | Specify whether to notify workers after publishing their schedules. Values are Y or N. |
| STATUS_IMP | NUMBER |  | 2 |  | Status for the import phase |
| STATUS_INT | NUMBER |  | 2 |  | Status for the internalization phase |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| GROUP_ID | NUMBER |  | 18 |  | GROUP_ID |
| MASTER_JOB_ID | NUMBER |  | 18 |  | MASTER_JOB_ID |
| SLAVE_JOB_ID | NUMBER |  | 18 |  | SLAVE_JOB_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_EVENTS_N1 | Non Unique | Default | STATUS_INT, RESOURCE_ID |
| HTS_SCHED_EVENTS_N2 | Non Unique | Default | GROUP_ID, STATUS_INT |
| HTS_SCHED_EVENTS_N3 | Non Unique | Default | SCHED_EVENT_NUMBER, SCHED_REQUEST_NUMBER |
| HTS_SCHED_EVENTS_PK | Unique | Default | SCHED_EVENT_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
