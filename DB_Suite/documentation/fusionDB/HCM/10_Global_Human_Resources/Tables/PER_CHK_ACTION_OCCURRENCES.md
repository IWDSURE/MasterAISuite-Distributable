# PER_CHK_ACTION_OCCURRENCES

PER_CHK_ACTION_OCCURRENCES : Run time table to store event for allocating a checklist

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkactionoccurrences-29225.html#perchkactionoccurrences-29225](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkactionoccurrences-29225.html#perchkactionoccurrences-29225)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Primary Key |
| SUBJECT_TYPE | VARCHAR2 | 240 |  |  | SUBJECT_TYPE |
| SUBJECT_KEY | VARCHAR2 | 240 |  |  | SUBJECT_KEY |
| CHECKLIST_BATCH_ACTION_ID | NUMBER |  | 18 |  | CHECKLIST_BATCH_ACTION_ID |
| RUN_MODE | VARCHAR2 | 30 |  |  | RUN_MODE |
| PROCESSING_MODE | VARCHAR2 | 30 |  |  | Processing Mode |
| PROCESSING_STATUS | VARCHAR2 | 30 |  |  | Processing Status |
| PRIMARY_ACTION_TYPE | VARCHAR2 | 80 |  |  | Primary Action Type |
| PRIMARY_EVENT_CODE | VARCHAR2 | 100 |  |  | Primary Event Code |
| PRIMARY_ACTION_ID | NUMBER |  | 18 |  | Primary Action Id |
| EVENT_DATE | DATE |  |  | Yes | Effective Date on which this event was triggered |
| PERSON_ID | NUMBER |  | 18 | Yes | The Person ID of the person for which this event was triggered |
| INITIATOR_USERNAME | VARCHAR2 | 64 |  | Yes | The username of the user who performed this change |
| BATCH_CHUNK_ID | NUMBER |  | 18 |  | Foreign Key to PER_CHECKLIST_BATCH_CHUNKS |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHK_ACTION_OCCURRENCES_N1 | Non Unique | Default | CHECKLIST_BATCH_ACTION_ID |
| PER_CHK_ACTION_OCCURRENCES_N2 | Non Unique | Default | PERSON_ID |
| PER_CHK_ACTION_OCCURRENCES_PK | Unique | Default | CHECKLIST_ACTION_OCCURRENCE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
