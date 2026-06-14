# IRC_EMP_TO_CAND_QUEUE

This table is a queue processing table which is used for load employees to candidates  ess job.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircemptocandqueue-18512.html#ircemptocandqueue-18512](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircemptocandqueue-18512.html#ircemptocandqueue-18512)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_EMP_TO_CAND_QUEUE_PK | QUEUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QUEUE_ID | NUMBER |  | 18 | Yes | Primary Key of the table. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| PERSON_ID | NUMBER |  | 18 | Yes | PersonId of the worker. Foreign key to Per_Persons |
| PERSON_TYPE_CODE | VARCHAR2 | 32 |  | Yes | Specifies the Person Type i.e. internal or external, honoring the CWK profile option.

Introducing this column as a performance optimization. This column prevents an extra join to get the system person type once batch processing starts. |
| REFERENCE_COUNT | NUMBER |  | 1 | Yes | Flag to specify processing status for a batch. 1 : Being Processed ; 2 : No Processing |
| PROCESSOR_ID | NUMBER |  | 18 |  | Sequence generated unique Id. Used for multi threaded processing |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_EMP_TO_CAND_QUEUE_PK | Unique | Default | QUEUE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
