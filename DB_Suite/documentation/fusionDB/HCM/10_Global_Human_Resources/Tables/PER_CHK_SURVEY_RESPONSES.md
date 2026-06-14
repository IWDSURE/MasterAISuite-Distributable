# PER_CHK_SURVEY_RESPONSES

Table to store survey journey responses

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchksurveyresponses-12226.html#perchksurveyresponses-12226](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchksurveyresponses-12226.html#perchksurveyresponses-12226)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_SURVEY_RESPONSES_PK | SURVEY_RESPONSE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SURVEY_RESPONSE_ID | NUMBER |  | 18 | Yes | SURVEY_RESPONSE_ID |
| SUBJECT_TYPE | VARCHAR2 | 240 |  |  | SUBJECT_TYPE |
| SUBJECT_KEY | VARCHAR2 | 240 |  |  | SUBJECT_KEY |
| SURVEY_TYPE | VARCHAR2 | 30 |  | Yes | SURVEY_TYPE |
| SURVEY_CATEGORY | VARCHAR2 | 30 |  | Yes | SURVEY_CATEGORY |
| CHECKLIST_ALLOCATION_ID | NUMBER |  | 18 |  | CHECKLIST_ALLOCATION_ID |
| CHECKLIST_SCHEDULE_ID | NUMBER |  | 18 | Yes | CHECKLIST_SCHEDULE_ID |
| CHECKLIST_PERIOD_ID | NUMBER |  | 18 | Yes | CHECKLIST_PERIOD_ID |
| PERIOD_START_DATE | DATE |  |  | Yes | PERIOD_START_DATE |
| PERIOD_END_DATE | DATE |  |  | Yes | PERIOD_END_DATE |
| FREQUENCY | VARCHAR2 | 30 |  | Yes | FREQUENCY |
| CHECKLIST_INTEGRATION_CODE | VARCHAR2 | 120 |  |  | CHECKLIST_INTEGRATION_CODE |
| CHECKLIST_ID | NUMBER |  | 18 | Yes | CHECKLIST_ID |
| TASK_IN_CHECKLIST_ID | NUMBER |  | 18 | Yes | TASK_IN_CHECKLIST_ID |
| SURVEY_CODE | VARCHAR2 | 240 |  |  | SURVEY_CODE |
| NAME | VARCHAR2 | 240 |  | Yes | NAME |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | QUESTIONNAIRE_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| RESPONSE_STATUS | VARCHAR2 | 30 |  | Yes | RESPONSE_STATUS |
| QSTNR_PARTICIPANT_ID | NUMBER |  | 18 |  | QSTNR_PARTICIPANT_ID |
| SCORE | NUMBER |  | 18 |  | SCORE |
| SUBMIT_DATE | DATE |  |  |  | SUBMIT_DATE |
| SUBMITTED_BY_PERSON_ID | NUMBER |  | 18 |  | SUBMITTED_BY_PERSON_ID |
| CHECKLIST_BATCH_ACTION_ID | NUMBER |  | 18 |  | CHECKLIST_BATCH_ACTION_ID |
| BATCH_NAME | VARCHAR2 | 4000 |  |  | BATCH_NAME |
| INITIATOR_PERSON_ID | NUMBER |  | 18 |  | INITIATOR_PERSON_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHK_SURVEY_RESPONSES_N1 | Non Unique | Default | SURVEY_TYPE, SURVEY_CATEGORY, PERIOD_START_DATE, PERIOD_END_DATE, CHECKLIST_ID, PERSON_ID |
| PER_CHK_SURVEY_RESPONSES_N2 | Non Unique | Default | SURVEY_TYPE, SURVEY_CATEGORY, PERIOD_START_DATE, PERIOD_END_DATE, QUESTIONNAIRE_ID, PERSON_ID |
| PER_CHK_SURVEY_RESPONSES_N3 | Non Unique | Default | SURVEY_TYPE, SURVEY_CATEGORY, CHECKLIST_PERIOD_ID, CHECKLIST_ID, TASK_IN_CHECKLIST_ID, PERSON_ID |
| PER_CHK_SURVEY_RESPONSES_PK | Unique | Default | SURVEY_RESPONSE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
