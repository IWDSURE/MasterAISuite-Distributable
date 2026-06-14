# HRQ_QSTNR_QUESTIONS

Associates specific Questions with a Questionnaire Section.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrquestions-10431.html#hrqqstnrquestions-10431](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrquestions-10431.html#hrqqstnrquestions-10431)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QSTNR_QUESTIONS_PK | QSTNR_QUESTION_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTNR_QUESTION_ID | NUMBER |  | 18 | Yes | Unique identifier for a questionnaire question.  System generated id.  This attribute combined with business group id forms the primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| QSTNR_SECTION_ID | NUMBER |  | 18 |  | Identifies the questionnaire section id. |
| SEQ_NUM | NUMBER |  | 18 |  | Sequence in which the questions are displayed. |
| KEEP_WITH_PREV | VARCHAR2 | 30 |  |  | Used to ensure this question always displays after the previous question when question order is random. |
| RESPONSE_TYPE_ID | NUMBER |  | 18 |  | Identifies the response type id. |
| QUESTION_ID | NUMBER |  | 18 |  | Identifies the question id. |
| QSTN_VERSION_NUM | NUMBER |  | 18 |  | Identifies the version number of the question. |
| ADHOC_QSTN | VARCHAR2 | 30 |  | Yes | Identifies if this is an adhoc question. |
| MANDATORY | VARCHAR2 | 30 |  |  | Indicates if the question must be answered. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LOCK_QUESTION_FLAG | VARCHAR2 | 8 |  | Yes | If set to Y, user cannot remove or update question from questionnaire. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| MAX_POSSIBLE_SCORE | NUMBER |  | 18 |  | Maximum possible score for the question in the Questionnaire. Value should be within the range of Minimum Threshold and Maximum Threshold score defined for Question in Questionnaire. |
| MAX_THRESHOLD_SCORE | NUMBER |  | 18 |  | Maximum threshold score for the question in the Questionnaire. |
| MIN_THRESHOLD_SCORE | NUMBER |  | 18 |  | Mininum threshold score for the question in the Questionnaire. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QSTNR_QUESTIONS_N1 | Non Unique | Default | BUSINESS_GROUP_ID, QUESTION_ID, QSTN_VERSION_NUM |
| HRQ_QSTNR_QUESTIONS_PK | Unique | Default | QSTNR_QUESTION_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRQ_QSTNR_QUESTIONS_PK1 | Unique | Default | QSTNR_QUESTION_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |
| HRQ_QSTNR_QUESTIONS_U1 | Unique | Default | BUSINESS_GROUP_ID, QSTNR_SECTION_ID, QSTNR_QUESTION_ID, ORA_SEED_SET1 |
| HRQ_QSTNR_QUESTIONS_U11 | Unique | Default | BUSINESS_GROUP_ID, QSTNR_SECTION_ID, QSTNR_QUESTION_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
