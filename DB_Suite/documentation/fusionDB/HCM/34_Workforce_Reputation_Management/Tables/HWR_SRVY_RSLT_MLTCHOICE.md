# HWR_SRVY_RSLT_MLTCHOICE

This table will be used to store analyzed result for multiple choice
questions used in the surveys – both single selection and multiple selection

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvyrsltmltchoice-24211.html#hwrsrvyrsltmltchoice-24211](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvyrsltmltchoice-24211.html#hwrsrvyrsltmltchoice-24211)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_RSLT_MLTCHOICE_PK | SURVEY_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, QUESTION_ID, QUESTION_VERSION, RESPONSE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | This is the Subscriber ID associated with the Survey. Used to differentiate between different survey projects. |
| SURVEY_ID | NUMBER |  | 18 | Yes | This is the Survey Id identifying the Survey entry in this table. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | This is the Questionnaire ID associated with the Survey. |
| QUESTIONNAIRE_VERSION | NUMBER |  | 18 | Yes | This is the Questionnaire Version associated with the Questionnaire ID of this Survey. |
| QUESTION_ID | NUMBER |  | 18 | Yes | This is the Question ID associated with the Questionnaire. |
| QUESTION_VERSION | NUMBER |  | 18 | Yes | This is the Question Version associated with the Question ID in the Questionnaire. |
| SURVEY_DATE | TIMESTAMP |  |  | Yes | This is the date when the Survey was created or conducted. |
| RESPONSE_ID | NUMBER |  | 18 | Yes | This is the Answer ID associated with the question that the participants selected. |
| MEASURE | NUMBER |  | 18 | Yes | This is the Quantitative Measure of how many candidates selected the corresponding answer id for this question for this Survey. |
| RESULT_ATTR_1 | VARCHAR2 | 100 |  |  | RESULT_ATTR_1. This is the extra attribute in case if needed. |
| RESULT_ATTR_2 | VARCHAR2 | 100 |  |  | RESULT_ATTR_2. This is the extra attribute in case if needed. |
| RESULT_ATTR_3 | VARCHAR2 | 100 |  |  | RESULT_ATTR_3. This is the extra attribute in case if needed. |
| RESULT_ATTR_4 | VARCHAR2 | 100 |  |  | RESULT_ATTR_4. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SRVY_RSLT_MLTCHOICE_U1 | Unique | Default | SURVEY_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, QUESTION_ID, QUESTION_VERSION, RESPONSE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
