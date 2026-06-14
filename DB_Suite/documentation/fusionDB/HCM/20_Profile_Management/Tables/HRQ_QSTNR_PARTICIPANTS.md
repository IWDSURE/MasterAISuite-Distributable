# HRQ_QSTNR_PARTICIPANTS

A list of Participants who have responded to a questionnaire.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrparticipants-30157.html#hrqqstnrparticipants-30157](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrparticipants-30157.html#hrqqstnrparticipants-30157)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QSTNR_PARTICIPANTS_PK | QSTNR_PARTICIPANT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTNR_PARTICIPANT_ID | NUMBER |  | 18 | Yes | Unique identifier for a questionnaire participant.  System generated primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Identifies the questionnaire id. |
| PARTICIPANT_TYPE | VARCHAR2 | 30 |  |  | Identifies the participant type. |
| PARTICIPANT_ID | VARCHAR2 | 240 |  |  | Identifies the participant id. |
| SUBSCRIBER_ID | NUMBER |  | 18 |  | Identifies the subscriber id. |
| SUBJECT_CODE | VARCHAR2 | 240 |  |  | Identifies the subject code. |
| SUBJECT_ID | VARCHAR2 | 240 |  |  | Identifies the subject id. |
| STATUS | VARCHAR2 | 30 |  |  | Identifies the status of the questionnaire participant. |
| SUBMITTED_DATE_TIME | DATE |  |  |  | Identifies the date and time the participant has submitted the response. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QSTNR_PARTICIPANTS_N1 | Non Unique | Default | PARTICIPANT_ID |
| HRQ_QSTNR_PARTICIPANTS_N2 | Non Unique | Default | SUBJECT_ID, PARTICIPANT_ID |
| HRQ_QSTNR_PARTICIPANTS_N3 | Non Unique | Default | QUESTIONNAIRE_ID |
| HRQ_QSTNR_PARTICIPANTS_N4 | Non Unique | Default | BUSINESS_GROUP_ID, SUBJECT_ID |
| HRQ_QSTNR_PARTICIPANTS_N5 | Non Unique | Default | UPPER("SUBJECT_ID") |
| HRQ_QSTNR_PARTICIPANTS_PK | Unique | Default | QSTNR_PARTICIPANT_ID |
| HRQ_QSTNR_PARTICIPANTS_U1 | Unique | Default | BUSINESS_GROUP_ID, SUBSCRIBER_ID, SUBJECT_CODE, SUBJECT_ID, QUESTIONNAIRE_ID, PARTICIPANT_TYPE, PARTICIPANT_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
