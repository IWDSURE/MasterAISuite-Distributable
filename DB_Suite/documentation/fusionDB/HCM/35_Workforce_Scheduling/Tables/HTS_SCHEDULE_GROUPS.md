# HTS_SCHEDULE_GROUPS

Table holding scheduling groups data which are used for self scheduling.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedulegroups-22394.html#htsschedulegroups-22394](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedulegroups-22394.html#htsschedulegroups-22394)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHEDULE_GROUPS_PK | SCHEDULE_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_GROUP_ID | NUMBER |  | 18 | Yes | System generated unique identifier for the schedule group. |
| SCHEDULE_ID | NUMBER |  | 18 | Yes | Identifier of the schedule to which the schedule group belongs. |
| START_DATE | DATE |  |  | Yes | Date from which filtered list is considered for self-scheduling. |
| END_DATE | DATE |  |  | Yes | Date until which filtered list is considered for self-scheduling. |
| LIST_ID | NUMBER |  | 18 | Yes | Identifier of the HCM filtered list. |
| LIST_EXTRACTION_DATE | TIMESTAMP |  |  |  | Indicates the date and time of the list extraction. |
| OFFSET_DAYS | NUMBER |  | 3 |  | Specifies the number of days to offset when scheduling open shifts. |
| GROUP_USAGE_CONTEXT | VARCHAR2 | 30 |  |  | Identifies the usage context of the group in scheduling. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise_id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHEDULE_GROUPS_N1 | Non Unique | Default | SCHEDULE_ID |
| HTS_SCHEDULE_GROUPS_PK | Unique | Default | SCHEDULE_GROUP_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
