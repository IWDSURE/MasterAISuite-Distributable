# HRQ_QUESTIONS_B

Contains definitions for Questions and how they are presented to participants.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqquestionsb-29487.html#hrqquestionsb-29487](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqquestionsb-29487.html#hrqquestionsb-29487)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QUESTIONS_B_PK | BUSINESS_GROUP_ID, QUESTION_ID, QSTN_VERSION_NUM |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QUESTION_ID | NUMBER |  | 18 | Yes | Unique identifier for a question.  System generated id.  This attribute combined with the version number and business group id forms the primary key. |
| QSTN_VERSION_NUM | NUMBER |  | 18 | Yes | The version number of the question. This attribute combined with the question id and business group id forms the primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| QUESTION_CODE | VARCHAR2 | 240 |  |  | Unique identifier for a question. |
| CATEGORY_ID | NUMBER |  | 18 |  | Identifies the category id. |
| STATUS | VARCHAR2 | 30 |  |  | Identifies the status of the question. |
| QUESTION_TYPE | VARCHAR2 | 30 |  |  | Identifies the type of the question. |
| RESPONSE_TYPE_ID | NUMBER |  | 18 |  | Identifies the response type id. |
| MIN_LENGTH | NUMBER |  | 18 |  | Identifies the minimum length of the response. |
| MAX_LENGTH | VARCHAR2 | 20 |  |  | Identifies the maximum length of the response. |
| MIN_SELECTIONS | NUMBER |  | 18 |  | Identifies the minimum selection for the response. |
| MAX_SELECTIONS | NUMBER |  | 18 |  | Identifies the maximum selection for the response. |
| OWNER | VARCHAR2 | 64 |  |  | Identifies the owner of the question. |
| PRIVACY_FLAG | VARCHAR2 | 30 |  |  | Indicates if the questionnaire is Private or Public.  Private questionnaires can only be updated by the owner. |
| UPDATE_ALLOWED | VARCHAR2 | 30 |  |  | Identifies if updates are allowed to this question. |
| ADHOC_FLAG | VARCHAR2 | 30 |  |  | Identifies if this question is an adhoc question. |
| SUBSCRIBER_ID | NUMBER |  | 18 |  | Identifies the subscriber id. |
| RATING_MODEL_ID | NUMBER |  | 18 |  | Identifies the rating model id. |
| LATEST_VERSION | VARCHAR2 | 30 |  |  | Identifies if this is the latest version of the question. |
| VERSION_DESCRIPTION | VARCHAR2 | 2000 |  |  | Description of changes made when a new version is created. |
| ATTACHMENT_ALLOWED | VARCHAR2 | 30 |  |  | Identifies if attachment is allowed as a response. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OVERRIDE_DESC_FLAG | VARCHAR2 | 30 |  |  | Indicates the rating level description was altered by the user |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SCORED_FLAG | VARCHAR2 | 30 |  |  | Indicates question is a scored question. |
| MIN_THRESHOLD_SCORE | NUMBER |  | 18 |  | Mininum threshold score for the question. |
| MAX_THRESHOLD_SCORE | NUMBER |  | 18 |  | Maximum threshold score for the question. |
| MAX_POSSIBLE_SCORE | NUMBER |  | 18 |  | Maximum possible score for the question. Value should be within the range of Minimum Threshold and Maximum Threshold score. |
| CLASSIFICATION_CODE | VARCHAR2 | 30 |  |  | Classify a question based on its code like Disqualification/ Preliminary. |
| CANDIDATE_CODE | VARCHAR2 | 30 |  |  | Code to identify the candidate as INTERNAL/ EXTERNAL/ BOTH. |
| ALL_LOCATIONS_FLAG | VARCHAR2 | 30 |  |  | Indicates if the question will be considered for all locations or not. |
| ALL_ORGANIZATIONS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the question will be considered for all organizations or not. |
| ALL_JOB_FAMILIES_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the question will be considered for all job families or not. |
| ALL_JOB_FUNCTIONS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the question will be considered for all job functions or not. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CONDITION_QUESTION_ID | NUMBER |  | 18 |  | CONDITION_QUESTION_ID |
| CONDITION_QSTN_VERSION_NUM | NUMBER |  | 18 |  | CONDITION_QSTN_VERSION_NUM |
| CONDITION_ANSWER_ID | NUMBER |  | 18 |  | CONDITION_ANSWER_ID |
| CONDITION_DISPLAY | VARCHAR2 | 30 |  |  | CONDITION_DISPLAY |
| QSTN_SAMPLE_SIZE | NUMBER |  | 18 |  | Count of choices that will be selected randomly out of all choices for a question. The field will be active if question response order is 'R'. |
| QSTN_RESPONSE_ORDER | VARCHAR2 | 30 |  |  | This field can have a value of V/R/Null. Default value is 'V' and in this case all defined answer choices will be presented. Value of 'R' indicates that a random set of answer choice will be presented from the total choices and the count of choices presented will be based on the value defined as sample size |
| MIN_DATE | DATE |  |  |  | Minimum value of date allowed for response of this question |
| MAX_DATE | DATE |  |  |  | Maximum value of date allowed for response of this question |
| ENABLE_COMMENTS | VARCHAR2 | 20 |  |  | This field is used to enable or disable additional comments for the Question. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| SURVEY_TYPE | VARCHAR2 | 80 |  |  | Indicates the survey type of the question. |
| ANALYSIS_GRAPH_TYPE | VARCHAR2 | 80 |  |  | Identifies the Analysis Graph Type of the Question |
| SENTIMENT_ANALYSIS_FLAG | VARCHAR2 | 30 |  |  | Identifies whether Sentiment Analysis is enabled for the Question. |
| SUMMARIZATION_FLAG | VARCHAR2 | 30 |  |  | Identifies whether Summarization is enabled for the Question. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QUESTIONS_B_N1 | Non Unique | Default | BUSINESS_GROUP_ID, ADHOC_FLAG, SUBSCRIBER_ID, QUESTION_CODE, QSTN_VERSION_NUM |
| HRQ_QUESTIONS_B_N2 | Non Unique | Default | QUESTION_ID, QSTN_VERSION_NUM |
| HRQ_QUESTIONS_B_N3 | Non Unique | Default | CONDITION_QUESTION_ID, CONDITION_QSTN_VERSION_NUM, CONDITION_ANSWER_ID, CONDITION_DISPLAY |
| HRQ_QUESTIONS_B_PK | Unique | Default | BUSINESS_GROUP_ID, QUESTION_ID, QSTN_VERSION_NUM, ORA_SEED_SET1 |
| HRQ_QUESTIONS_B_PK1 | Unique | Default | BUSINESS_GROUP_ID, QUESTION_ID, QSTN_VERSION_NUM, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
