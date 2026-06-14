# PER_CHK_SURVEY_QSTN_SUMMARY

Table to store survey questions summary

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchksurveyqstnsummary-7908.html#perchksurveyqstnsummary-7908](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchksurveyqstnsummary-7908.html#perchksurveyqstnsummary-7908)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_SURVEY_QSTN_SUMMARY_PK | QUESTION_SUMMARY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QUESTION_SUMMARY_ID | NUMBER |  | 18 | Yes | QUESTION_SUMMARY_ID |
| SENTIMENT_ANALYSIS_COMPUTED | VARCHAR2 | 4 |  |  | SENTIMENT_ANALYSIS_COMPUTED |
| TEXT_SUMMARY_COMPUTED | VARCHAR2 | 4 |  |  | TEXT_SUMMARY_COMPUTED |
| SURVEY_RESPONSES_SUMMARY_ID | NUMBER |  | 18 | Yes | SURVEY_RESPONSES_SUMMARY_ID |
| QUESTION_ID | NUMBER |  | 18 | Yes | QUESTION_ID |
| QSTN_VERSION_NUM | NUMBER |  | 18 |  | QSTN_VERSION_NUM |
| QUESTION_TYPE | VARCHAR2 | 30 |  | Yes | QUESTION_TYPE |
| TOTAL_RESPONDENTS | NUMBER |  | 9 |  | TOTAL_RESPONDENTS |
| TEXT_RESPONSE_SUMMARY | CLOB |  |  |  | TEXT_RESPONSE_SUMMARY |
| ANSWER_SUMMARY_PAYLOAD | CLOB |  |  |  | ANSWER_SUMMARY_PAYLOAD |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHK_SURVEY_QSTN_SUMMARY_PK | Unique | Default | QUESTION_SUMMARY_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
