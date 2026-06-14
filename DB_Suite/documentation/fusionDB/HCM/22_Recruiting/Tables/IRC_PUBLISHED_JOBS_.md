# IRC_PUBLISHED_JOBS_

This table stores all the published jobs.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircpublishedjobs-30612.html#ircpublishedjobs-30612](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircpublishedjobs-30612.html#ircpublishedjobs-30612)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_PUBLISHED_JOBS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PUBLISHED_JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PUBLISHED_JOB_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 |  | Foreign key to IRC_REQUISITIONS_B |
| SITE_ID | NUMBER |  | 18 |  | Foreign key to IRC_CX_SITES_B table. |
| PUBLISHED_JOB_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the type of job posting (internal VS external) as a lookup code. The corresponding lookup type is ORA_IRC_PUBLISHED_JOB_TYPE. |
| PUBLISHED_JOB_STATUS_CODE | VARCHAR2 | 30 |  |  | Stores the status of the published job as a lookup code. |
| PUBLISH_START_DATE | DATE |  |  |  | Stores the end date of the published job. |
| PUBLISH_END_DATE | DATE |  |  |  | Stores the end date of the published job. |
| PUBLISH_TIMEZONE_CODE | VARCHAR2 | 50 |  |  | Stores the timezone used of the published job. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_PUBLISHED_JOBSN1_ | Non Unique | Default | PUBLISHED_JOB_ID, LAST_UPDATE_DATE |
| IRC_PUBLISHED_JOBS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, PUBLISHED_JOB_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
