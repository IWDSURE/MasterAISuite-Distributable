# HTS_SCHED_REVIEWS

table to store schedule's review data

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedreviews-30845.html#htsschedreviews-30845](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedreviews-30845.html#htsschedreviews-30845)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_REVIEWS_PK | SCHED_REVIEW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_REVIEW_ID | NUMBER |  | 18 | Yes | A unique system-generated identifier for schedule's review |
| SCHEDULE_ID | NUMBER |  | 18 | Yes | Identifier of a schedule |
| REVIEWER_PERSON_ID | NUMBER |  | 18 | Yes | Identifier of a person reviewing a schedule |
| REVIEWED_ON | TIMESTAMP |  |  |  | Timestamp of reviewing a schedule |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | COLUMN1 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_REVIEWS_PK | Unique | Default | SCHED_REVIEW_ID |
| HTS_SCHED_REVIEWS_U1 | Unique | Default | SCHEDULE_ID, REVIEWER_PERSON_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
