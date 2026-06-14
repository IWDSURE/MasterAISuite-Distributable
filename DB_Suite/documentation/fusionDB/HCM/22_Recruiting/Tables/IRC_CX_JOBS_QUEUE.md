# IRC_CX_JOBS_QUEUE

Stores posting changes to requisitions in Hcm Recruiting

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxjobsqueue-14752.html#irccxjobsqueue-14752](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxjobsqueue-14752.html#irccxjobsqueue-14752)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_JOBS_QUEUE_PK | QUEUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QUEUE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_REQUISITIONS_B. |
| JOB_PUBLISH_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the status indicating if the job posting has been changed or removed. Corresponding lookup is ORA_IRC_CX_JOB_PUBLISH_TYPE |
| REFERENCE_COUNT | NUMBER |  | 1 |  | Value of this column shows that row is already being picked up by a job for publishing, so that no other job pick up the row again for publishing. |
| RETRY_COUNT | NUMBER |  | 1 |  | Value of this column indicates the number of times the publish job has tried to process this row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_JOBS_QUEUE_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_CX_JOBS_QUEUE_PK | Unique | Default | QUEUE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
