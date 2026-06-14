# HRA_DISCUSSION_TOPICS

It will store UI field values for creating different discussion topics for a check-in meeting.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hradiscussiontopics-27366.html#hradiscussiontopics-27366](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hradiscussiontopics-27366.html#hradiscussiontopics-27366)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_DISCUSSION_TOPICS_PK | DISCUSSION_TOPIC_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DISCUSSION_TOPIC_ID | NUMBER |  | 18 | Yes | Primary key of Discussion Topics |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| CHECK_IN_MEETING_ID | NUMBER |  | 18 | Yes | Foreign key to HRA_CHECK_IN_MEETINGS |
| OBJECT_ID | NUMBER |  | 18 |  | Foreign key to tables like HRG_GOALS |
| NAME | VARCHAR2 | 240 |  |  | Generic Discussion Topic name of the Check-In meeting |
| TOPIC_TYPE | VARCHAR2 | 240 |  | Yes | Discussion Topic Type of the Check-In meeting |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Context or description of Discussion Topic. |
| DISCUSSED_FLAG | VARCHAR2 | 30 |  |  | Identify if the discussion topic has been discussed or not. |
| SCHEDULE_OWNER_ID | NUMBER |  | 18 |  | Parent key for PER_CHECKLIST_SCHEDULES.	SCHEDULE_OWNER_ID for recurring check-ins |
| RECURRENCE_ID | NUMBER |  | 18 |  | Identifies recurring discussion topic series within recurring check-ins. |
| CREATED_BY_PERSON_ID | NUMBER |  | 18 |  | Identifies the person who created this discussion topic. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_DISCUSSION_TOPICS_FK1 | Non Unique | Default | CHECK_IN_MEETING_ID |
| HRA_DISCUSSION_TOPICS_N1 | Non Unique | Default | TOPIC_TYPE |
| HRA_DISCUSSION_TOPICS_N2 | Non Unique | Default | OBJECT_ID, CHECK_IN_MEETING_ID, TOPIC_TYPE |
| HRA_DISCUSSION_TOPICS_PK | Unique | Default | DISCUSSION_TOPIC_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
