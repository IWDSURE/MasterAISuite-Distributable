# HWR_SRVY_QSTN_BASE_B

This table will be used to store information regarding the Questions being
used in the Survey

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvyqstnbaseb-28358.html#hwrsrvyqstnbaseb-28358](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvyqstnbaseb-28358.html#hwrsrvyqstnbaseb-28358)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_QSTN_BASE_B_PK | SUBSCRIBER_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, QUESTION_ID, QUESTION_VERSION |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | This is the Subscriber ID associated with the Survey. Used to differentiate between different survey projects. |  |
| SUBSCRIBER_CODE | VARCHAR2 | 30 |  | Yes | This is the Subscriber Code associated with the Survey. Used to differentiate between different survey projects. |  |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | This is the Questionnaire ID associated with the Survey. |  |
| QUESTIONNAIRE_VERSION | NUMBER |  | 18 | Yes | This is the Questionnaire Version associated with the Questionnaire ID of this Survey. |  |
| QUESTION_ID | NUMBER |  | 18 | Yes | This is the Question ID associated with the Questionnaire. |  |
| QUESTION_VERSION | NUMBER |  | 18 | Yes | This is the Question Version associated with the Question ID. |  |
| QUESTION_OWNER | VARCHAR2 | 500 |  |  | This is the FUSION id of the owner of this question. |  |
| QUESTION_TYPE | NUMBER |  | 18 | Yes | This determines the type of this question.
QUESTION_TYPE ::
0 --> Text Questions
1 --> Multiple Choice Questions – Single Selection
2 --> Multiple Choice Questions – Multiple Selection – 2 or more selections are possible
3 --> No Response |  |
| QUESTION_TIMESTAMP | TIMESTAMP |  |  | Yes | This determines the timestamp of last action on this question. |  |
| QUESTIONS_BASE_ATTR_1 | VARCHAR2 | 100 |  |  | QUESTIONS_BASE_ATTR_1. This is the extra attribute in case if needed. |  |
| QUESTIONS_BASE_ATTR_2 | VARCHAR2 | 100 |  |  | QUESTIONS_BASE_ATTR_2. This is the extra attribute in case if needed. |  |
| QUESTIONS_BASE_ATTR_3 | VARCHAR2 | 100 |  |  | QUESTIONS_BASE_ATTR_3. This is the extra attribute in case if needed. |  |
| QUESTIONS_BASE_ATTR_4 | VARCHAR2 | 100 |  |  | QUESTIONS_BASE_ATTR_4. This is the extra attribute in case if needed. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SRVY_QSTN_BASE_B_N1 | Non Unique | Default | QUESTION_OWNER |
| HWR_SRVY_QSTN_BASE_B_N2 | Non Unique | Default | QUESTION_TYPE |
| HWR_SRVY_QSTN_BASE_B_U1 | Unique | Default | SUBSCRIBER_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, QUESTION_ID, QUESTION_VERSION |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
