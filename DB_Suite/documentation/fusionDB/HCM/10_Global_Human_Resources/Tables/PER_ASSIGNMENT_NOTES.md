# PER_ASSIGNMENT_NOTES

This stores notes related to each transaction performned.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentnotes-6939.html#perassignmentnotes-6939](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentnotes-6939.html#perassignmentnotes-6939)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ASSIGNMENT_NOTES_PK | ASSIGNMENT_NOTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNMENT_NOTE_ID | NUMBER |  | 18 | Yes | This is a system generated primary key. Surrogate key. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Identifies the assignment to which the assignment note is assigned too. Foreign key to PER_ALL_ASSIGNMENTS_M. |
| ASG_EFFECTIVE_START_DATE | DATE |  |  |  | Identified the Effective Start Date on the Assignment to which this note is assigned too. |
| ASG_EFFECTIVE_SEQUENCE | NUMBER |  | 4 |  | Identified the Effective Sequence on the Assignment to which this note is assigned too. |
| ASG_ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Identifies the action occurrence of the transaction |
| PERSON_ID | NUMBER |  | 18 |  | Identifies person holding the assignment note. Foreign key to PER_PERSONS. |
| RECORD_CREATOR | VARCHAR2 | 30 |  |  | Record created By Module |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| NOTES | VARCHAR2 | 4000 |  |  | user specified notes related to the assignment transaction. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ASSIGNMENT_NOTES_FK2 | Non Unique | FUSION_TS_TX_IDX | PERSON_ID |
| PER_ASSIGNMENT_NOTES_PK | Unique | FUSION_TS_TX_IDX | ASSIGNMENT_NOTE_ID |
| PER_ASSIGNMENT_NOTES_UK1 | Unique | FUSION_TS_TX_IDX | ASSIGNMENT_ID, ASG_EFFECTIVE_START_DATE, ASG_EFFECTIVE_SEQUENCE, ASG_ACTION_OCCURRENCE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
