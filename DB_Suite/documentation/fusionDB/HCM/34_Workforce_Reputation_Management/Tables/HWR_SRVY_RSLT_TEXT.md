# HWR_SRVY_RSLT_TEXT

This table will be used to store analyzed results for text based questions used in
the surveys.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvyrslttext-12713.html#hwrsrvyrslttext-12713](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvyrslttext-12713.html#hwrsrvyrslttext-12713)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_RSLT_TEXT_PK | RESULT_TEXT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RESULT_TEXT_ID | NUMBER |  | 18 | Yes | This is the Result Text Id identifying the Analyzed Survey Response entry in this table. |
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | This is the Subscriber ID associated with the Survey. Used to differentiate between different survey projects. |
| SURVEY_ID | NUMBER |  | 18 | Yes | This is the Survey Id identifying the Survey entry in this table. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | This is the Questionnaire ID associated with the Survey. |
| QUESTIONNAIRE_VERSION | NUMBER |  | 18 | Yes | This is the Questionnaire Version associated with the Questionnaire ID of this Survey. |
| QUESTION_ID | NUMBER |  | 18 | Yes | This is the Question ID associated with the Questionnaire. |
| QUESTION_VERSION | NUMBER |  | 18 | Yes | This is the Question Version associated with the Question ID in the Questionnaire. |
| SURVEY_DATE | TIMESTAMP |  |  | Yes | This is the date when the Survey was created or conducted. |
| OWNER_PRFL_ID | VARCHAR2 | 500 |  | Yes | This is the Fusion Id of the participant who wrote this survey response. |
| REFERENCED_PRFL_ID | VARCHAR2 | 500 |  | Yes | This is the Fusion Id of the person being referred to in this survey response. |
| TOPIC_ID | NUMBER |  | 18 | Yes | This is the Id of the Topic being identified in this survey response. |
| TOPIC_NAME | VARCHAR2 | 500 |  |  | This is the Name aka Text of the Topic being identified in this survey response. |
| SENTIMENT_ID | NUMBER |  | 18 | Yes | This is the Id of Sentiment being identified in this survey response. |
| RESPONSE_TEXT | VARCHAR2 | 4000 |  | Yes | This is the response text that the participant wrote which has been analyzed. |
| EMOTION | VARCHAR2 | 500 |  |  | This is the Emotion Associated with the survey response Id. |
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

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_SRVY_RSLT_TEXT_N1 | Non Unique | Default | OWNER_PRFL_ID |  |
| HWR_SRVY_RSLT_TEXT_N2 | Non Unique | Default | SUBSCRIBER_ID |  |
| HWR_SRVY_RSLT_TEXT_N3 | Non Unique | Default | TOPIC_ID |  |
| HWR_SRVY_RSLT_TEXT_N4 | Non Unique | Default | REFERENCED_PRFL_ID |  |
| HWR_SRVY_RSLT_TEXT_U1 | Unique | Default | SURVEY_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, QUESTION_ID, QUESTION_VERSION, OWNER_PRFL_ID | Obsolete |
| HWR_SRVY_RSLT_TEXT_U2 | Unique | Default | RESULT_TEXT_ID |  |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
