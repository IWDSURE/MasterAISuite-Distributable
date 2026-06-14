# IRC_CAND_CLOSEOUT_OCCURRENCES

This table stores the ACTION_OCCURRENCE's details that will be processed to perform Candidate Closeout.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandcloseoutoccurrences-22378.html#irccandcloseoutoccurrences-22378](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandcloseoutoccurrences-22378.html#irccandcloseoutoccurrences-22378)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_CLOSEOUT_OCCURRE_PK | CAND_CLOSEOUT_OCCURRENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_CLOSEOUT_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Primary key for the table IRC Cand Closeout Occurences |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ACTION_OCCURRENCES table. |
| ACTION_TYPE_CODE | VARCHAR2 | 230 |  | Yes | Action type code of an PER_ACTION_OCCURRENCES |
| ACTION_OCCURRENCE_DATE | TIMESTAMP |  |  | Yes | LAST_UPDATE_DATE of an PER_ACTION_OCCURRENCES |
| PERSON_ID | NUMBER |  | 18 | Yes | ENTITY_ID of an PER_ACTION_OCCURRENCES (PERSON_ID) |
| PROCESSING_STATUS | VARCHAR2 | 30 |  |  | Processing Status of this PER_ACTION_OCCURRENCES(Success, Failed and etc) |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_CLOSEOUT_OCCURRE_FK | Non Unique | Default | ACTION_OCCURRENCE_ID |
| IRC_CAND_CLOSEOUT_OCCURRE_PK | Unique | Default | CAND_CLOSEOUT_OCCURRENCE_ID |
| IRC_CAND_CLOSEOUT_OCCUR_FK1 | Non Unique | Default | PROCESSING_STATUS, PERSON_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
