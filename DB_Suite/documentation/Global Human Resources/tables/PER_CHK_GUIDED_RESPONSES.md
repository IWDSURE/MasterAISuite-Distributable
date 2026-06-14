# PER_CHK_GUIDED_RESPONSES

Table to store guided journey responses.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkguidedresponses-21719.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkguidedresponses-21719.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_GUIDED_RESPONSES_PK | JOURNEY_RESPONSE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOURNEY_RESPONSE_ID | NUMBER |  | 18 | Yes | JOURNEY_RESPONSE_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| SUBJECT_PERSON_ID | NUMBER |  | 18 | Yes | SUBJECT_PERSON_ID |
| CONTEXTUAL_ACTION | VARCHAR2 | 240 |  | Yes | CONTEXTUAL_ACTION |
| CONTEXT | VARCHAR2 | 240 |  |  | CONTEXT |
| TASK_IN_CHECKLIST_ID | NUMBER |  | 18 | Yes | TASK_IN_CHECKLIST_ID |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | QUESTIONNAIRE_ID |
| QSTNR_PARTICIPANT_ID | NUMBER |  | 18 | Yes | QSTNR_PARTICIPANT_ID |
| SUBMIT_DATE | DATE |  |  | Yes | SUBMIT_DATE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHK_GUIDED_RESPONSES_N1 | Non Unique | Default | PERSON_ID, SUBJECT_PERSON_ID, CONTEXTUAL_ACTION, TASK_IN_CHECKLIST_ID |
| PER_CHK_GUIDED_RESPONSES_N2 | Non Unique | Default | QSTNR_PARTICIPANT_ID |
| PER_CHK_GUIDED_RESPONSES_PK | Unique | Default | JOURNEY_RESPONSE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
