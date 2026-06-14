# PER_ASSIGNMENT_NOTES_

This stores notes related to each transaction performned.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentnotes-8415.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentnotes-8415.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ASSIGNMENT_NOTES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ASSIGNMENT_NOTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNMENT_NOTE_ID | NUMBER |  | 18 | Yes | This is a system generated primary key. Surrogate key. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Identifies the assignment to which the assignment note is assigned too. Foreign key to PER_ALL_ASSIGNMENTS_M. |
| ASG_EFFECTIVE_START_DATE | DATE |  |  |  | Identified the Effective Start Date on the Assignment to which this note is assigned too. |
| ASG_EFFECTIVE_SEQUENCE | NUMBER |  | 4 |  | Identified the Effective Sequence on the Assignment to which this note is assigned too. |
| ASG_ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Identifies the action occurrence of the transaction |
| PERSON_ID | NUMBER |  | 18 |  | Identifies person holding the assignment note. Foreign key to PER_PERSONS. |
| RECORD_CREATOR | VARCHAR2 | 30 |  |  | Record created By Module |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| NOTES | VARCHAR2 | 4000 |  |  | user specified notes related to the assignment transaction. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ASSIGNMENT_NOTESN1_ | Non Unique | Default | ASSIGNMENT_NOTE_ID |
| PER_ASSIGNMENT_NOTESU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ASSIGNMENT_NOTE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
