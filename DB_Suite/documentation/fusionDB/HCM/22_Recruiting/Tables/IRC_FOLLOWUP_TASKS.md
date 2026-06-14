# IRC_FOLLOWUP_TASKS

This table stores the interaction for a person in the context of a Submission, Candidate Pool, Prospect and Candidate General Profile.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircfollowuptasks-8156.html#ircfollowuptasks-8156](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircfollowuptasks-8156.html#ircfollowuptasks-8156)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_FOLLOWUP_TASKS_PK | TASK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated value. |
| ENTITY_ID | NUMBER |  | 18 | Yes | Stores the ID of entity object for which the followup task is created. Eg. PERSON_ID etc. |
| ENTITY_TYPE | VARCHAR2 | 30 |  | Yes | Stores the entity against which the followup task is created. Eg. ORA_CANDIDATE etc. |
| CONTEXT_TYPE | VARCHAR2 | 30 |  |  | Stores the context against which the followup task is created. Eg. Submission, Pool, Prospect, General Profile etc. |
| CONTEXT_ID | NUMBER |  | 18 |  | Stores the ID of the context object for which the followup task is created. Eg. SUBMISSION_ID, POOL_ID, PERSON_ID etc. |
| DUE_DATE | DATE |  |  | Yes | Stores the date by which the followup task has to be done. |
| COMPLETION_DATE | TIMESTAMP |  |  |  | Stores the timestamp when the followup task was marked as completed. |
| STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores the status of the followup task. Lookup type is ORA_IRC_FOLLOWUP_TASK_STATUS |
| NOTE_TEXT | VARCHAR2 | 1000 |  | Yes | Stores the text for the followup task. |
| COMPLETED_BY_PERSON_ID | NUMBER |  | 18 |  | Foreign key to per_persons table. Stores the PERSON_ID of the person who completed the followup task. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_FOLLOWUP_TASKS_FK1 | Non Unique | Default | COMPLETED_BY_PERSON_ID |
| IRC_FOLLOWUP_TASKS_N1 | Non Unique | Default | CONTEXT_ID, CONTEXT_TYPE, ENTITY_ID, ENTITY_TYPE, STATUS_CODE |
| IRC_FOLLOWUP_TASKS_N2 | Non Unique | Default | ENTITY_ID, ENTITY_TYPE, STATUS_CODE |
| IRC_FOLLOWUP_TASKS_N3 | Non Unique | Default | CONTEXT_TYPE |
| IRC_FOLLOWUP_TASKS_N4 | Non Unique | Default | DUE_DATE |
| IRC_FOLLOWUP_TASKS_PK | Unique | Default | TASK_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
