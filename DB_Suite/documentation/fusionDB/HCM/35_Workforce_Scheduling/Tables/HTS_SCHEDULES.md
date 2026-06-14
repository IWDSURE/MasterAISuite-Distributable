# HTS_SCHEDULES

Table holding the schedule information of schedule units.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedules-17420.html#htsschedules-17420](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedules-17420.html#htsschedules-17420)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHEDULES_PK | SCHEDULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_ID | NUMBER |  |  | Yes | PrimaryKey.System generated unique identifier for a schedule |
| SCHEDULE_UNIT_ID | NUMBER |  |  | Yes | Schedule UnitId  for which schedule is created. |
| SCHED_GEN_PROFILE_ID | NUMBER |  |  | Yes | ScheduleGenerationProfileId used for creating the schedule |
| START_DATE | DATE |  |  | Yes | Start Date of a Schedule Period. |
| END_DATE | DATE |  |  | Yes | End Date of a Schedule Period |
| OPEN_DATE | DATE |  |  |  | Date from which the manager can access the Schedule for updates. |
| PUBLISH_DUE_DATE | DATE |  |  |  | Due Date for manager to publish the schedule. |
| PUBLISHED_DATE | DATE |  |  |  | Date on which schedule is published |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Status of the Schedule. |
| SELF_SCHEDULE_OPEN_DATE | DATE |  |  |  | Date from which  workers can perform self-scheduling. |
| SELF_SCHEDULE_CLOSE_DATE | DATE |  |  |  | Date until which workers can perform self-scheduling |
| SELF_SCHEDULE_ROTATION_TYPE | VARCHAR2 | 30 |  |  | Rotation type used for self-scheduling. |
| SCHEDULE_UPDATE_DATE | TIMESTAMP |  |  |  | Latest updated timestamp for the schedule |
| WORKLOAD_UPDATE_DATE | TIMESTAMP |  |  |  | Latest updated timestamp for the workload |
| PUBLISHED_BY | NUMBER |  |  |  | Used to indicate the person's id who published the schedule |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | EnterpriseId |
| COMMENTS | VARCHAR2 | 4000 |  |  | Comment that may be provided as information at creation or when updating the shift. |
| UNPUBLISHED_BY | NUMBER |  | 18 |  | Identifier of the person who unpublished the schedule |
| UNPUBLISH_DATE | TIMESTAMP |  |  |  | Date and Time when the schedule was Unpublished |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHEDULES_N1 | Non Unique | Default | STATUS_CODE, START_DATE, END_DATE |
| HTS_SCHEDULES_PK | Unique | Default | SCHEDULE_ID |
| HTS_SCHEDULES_U1 | Unique | Default | SCHEDULE_UNIT_ID, START_DATE, END_DATE |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
