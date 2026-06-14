# IRC_PUBLISHED_JOBS

This table stores all the published jobs.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircpublishedjobs-16932.html#ircpublishedjobs-16932](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircpublishedjobs-16932.html#ircpublishedjobs-16932)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_PUBLISHED_JOBS_PK | PUBLISHED_JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PUBLISHED_JOB_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITIONS_B |
| SITE_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CX_SITES_B table. |
| PUBLISHED_JOB_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the type of job posting (internal VS external) as a lookup code. The corresponding lookup type is ORA_IRC_PUBLISHED_JOB_TYPE. |
| PUBLISHED_JOB_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores the status of the published job as a lookup code. |
| PUBLISH_START_DATE | DATE |  |  | Yes | Stores the end date of the published job. |
| PUBLISH_END_DATE | DATE |  |  |  | Stores the end date of the published job. |
| PUBLISH_TIMEZONE_CODE | VARCHAR2 | 50 |  |  | Stores the timezone used of the published job. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_PUBLISHED_JOBS_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_PUBLISHED_JOBS_FK2 | Non Unique | Default | SITE_ID |
| IRC_PUBLISHED_JOBS_PK | Unique | Default | PUBLISHED_JOB_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
