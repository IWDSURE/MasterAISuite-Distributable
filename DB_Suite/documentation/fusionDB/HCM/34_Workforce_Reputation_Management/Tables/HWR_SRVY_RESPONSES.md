# HWR_SRVY_RESPONSES

This table will be used to store the responses from Surveys as they are submitted by
the participants. This will be used for all the three types of questions: Text, single selection, multiple selection.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvyresponses-20513.html#hwrsrvyresponses-20513](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvyresponses-20513.html#hwrsrvyresponses-20513)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_RESPONSES_PK | SURVEY_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, QUESTION_ID, QUESTION_VERSION, PARTICIPANT_PRFL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SURVEY_ID | NUMBER |  | 18 | Yes | This is the Survey Id identifying the Survey entry in this table. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | This is the Questionnaire ID associated with the Survey. |
| QUESTIONNAIRE_VERSION | NUMBER |  | 18 | Yes | This is the Questionnaire Version associated with the Questionnaire ID of this Survey. |
| QUESTION_ID | NUMBER |  | 18 | Yes | This is the Question ID associated with the Questionnaire. |
| QUESTION_VERSION | NUMBER |  | 18 | Yes | This is the Question Version associated with the Question ID in the Questionnaire. |
| PARTICIPANT_PRFL_ID | VARCHAR2 | 500 |  | Yes | This is the Fusion Id of the participant who took this Survey. |
| QUESTION_TYPE | NUMBER |  | 18 | Yes | This determines the type of this question. |
| RESPONSE_ID_SINGLE_CHOICE | NUMBER |  | 18 |  | This is the Answer ID associated with the question that the participant selected. |
| RESPONSE_ID_MLT_CHOICE | VARCHAR2 | 1000 |  |  | This is a comma separated list of Answer ID(s) associated with the question that the participant selected. |
| RESPONSE_TEXT | VARCHAR2 | 4000 |  |  | This is the response text that the participant wrote for the associated Question. |
| RESPONSE_ATTR_1 | VARCHAR2 | 100 |  |  | RESPONSE_ATTR_1. This is the extra attribute in case if needed. |
| RESPONSE_ATTR_2 | VARCHAR2 | 100 |  |  | RESPONSE_ATTR_2. This is the extra attribute in case if needed. |
| RESPONSE_ATTR_3 | VARCHAR2 | 100 |  |  | RESPONSE_ATTR_3. This is the extra attribute in case if needed. |
| RESPONSE_ATTR_4 | VARCHAR2 | 100 |  |  | RESPONSE_ATTR_4. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SRVY_RESPONSES_N1 | Non Unique | Default | QUESTION_TYPE |
| HWR_SRVY_RESPONSES_U1 | Unique | Default | SURVEY_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, QUESTION_ID, QUESTION_VERSION, PARTICIPANT_PRFL_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
