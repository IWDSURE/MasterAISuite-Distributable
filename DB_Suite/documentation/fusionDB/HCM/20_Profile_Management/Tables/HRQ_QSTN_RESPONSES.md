# HRQ_QSTN_RESPONSES

This contains a participant's response to a specific question within a questionnaire.  This may reference the answer the user selected, or a rating level, or the actual entered text.  For multi-part questions (such as matching questions) it may also reference a sub-question.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnresponses-15508.html#hrqqstnresponses-15508](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnresponses-15508.html#hrqqstnresponses-15508)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QSTN_RESPONSES_PK | QSTN_RESPONSE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTN_RESPONSE_ID | NUMBER |  | 18 | Yes | Unique identifier for question response.  System generated primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| QSTNR_RESPONSE_ID | NUMBER |  | 18 |  | Identifies the questionnaire response. |
| QSTNR_QUESTION_ID | NUMBER |  | 18 |  | Identifies the questionnaire question. |
| SUB_QUESTION_ID | NUMBER |  | 18 |  | Identifies the sub question. |
| QSTN_ANSWER_ID | NUMBER |  | 18 |  | Identifies the answer for a question. |
| ANSWER_TEXT | VARCHAR2 | 4000 |  |  | The answer for free text questions. |
| ANSWER_LIST | VARCHAR2 | 2000 |  |  | Identifies the list of answers for a question that allows multiple selections to be made. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SCORE | NUMBER |  | 18 |  | Score for the Question response. |
| ANSWER_CLOB | CLOB |  |  |  | The answer for free text questions. |
| CHOICE_LIST | VARCHAR2 | 2000 |  |  | List of Choices presented out of the pool of choices for current response. |
| ANSWER_COMMENTS | VARCHAR2 | 4000 |  |  | This field is used for capturing comments from the user. |
| RESPONSE_SENTIMENT | VARCHAR2 | 80 |  |  | This field is used for capturing sentiment analysis from the response. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QSTN_RESPONSES_N1 | Non Unique | Default | BUSINESS_GROUP_ID, QSTNR_RESPONSE_ID |
| HRQ_QSTN_RESPONSES_N2 | Non Unique | Default | QSTNR_RESPONSE_ID |
| HRQ_QSTN_RESPONSES_PK | Unique | Default | QSTN_RESPONSE_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
