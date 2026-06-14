# HTS_SCHEDULE_GROUP_WORKERS

Table holding scheduling group worker's data.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedulegroupworkers-12976.html#htsschedulegroupworkers-12976](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedulegroupworkers-12976.html#htsschedulegroupworkers-12976)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHEDULE_GROUP_WORKERS_PK | SCHEDULE_GROUP_WORKER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_GROUP_WORKER_ID | NUMBER |  | 18 | Yes | System generated unique identifier for the schedule group worker. |
| SCHEDULE_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of the schedule group to which this worker
belongs. |
| PERSON_ID | NUMBER |  | 18 | Yes | Identifier of the person. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Identiifier of the assignment. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise ID. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHEDULE_GROUP_WORKERS_PK | Unique | Default | SCHEDULE_GROUP_WORKER_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
