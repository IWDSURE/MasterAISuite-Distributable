# HRQ_QSTN_PARTICIPANTS

For adhoc questions that have been added to a questionnaire for specific participants only, this is a list of those participants.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnparticipants-31248.html#hrqqstnparticipants-31248](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnparticipants-31248.html#hrqqstnparticipants-31248)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QSTN_PARTICIPANTS_PK | QSTN_PARTICIPANT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTN_PARTICIPANT_ID | NUMBER |  | 18 | Yes | Unique identifier for question participant.  System generated primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| QSTNR_QUESTION_ID | NUMBER |  | 18 | Yes | Identifies the question on the Questionnaire. |
| SUBSCRIBER_ID | NUMBER |  | 18 |  | Identifies the consuming subscriber. |
| PARTICIPANT_TYPE | VARCHAR2 | 30 |  |  | The type of unique id used to identify the person completing the Questionnaire. |
| PARTICIPANT_ID | VARCHAR2 | 240 |  | Yes | The unique id the person completing the Questionnaire. |
| SUBJECT_CODE | VARCHAR2 | 240 |  |  | The type of unique id used to identify the subject of the Questionnaire. |
| SUBJECT_ID | VARCHAR2 | 240 |  |  | The unique id identifying the subject of the Questionnaire (i.e. for Performance, the Performance Doc Id) |
| INCLUDE_EXCLUDE | VARCHAR2 | 30 |  |  | Identifies if the participant is included or excluded from the question. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QSTN_PARTICIPANTS_N1 | Non Unique | Default | BUSINESS_GROUP_ID, QSTNR_QUESTION_ID, SUBSCRIBER_ID, SUBJECT_ID, SUBJECT_CODE |
| HRQ_QSTN_PARTICIPANTS_N2 | Non Unique | Default | QSTNR_QUESTION_ID |
| HRQ_QSTN_PARTICIPANTS_PK | Unique | Default | QSTN_PARTICIPANT_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
