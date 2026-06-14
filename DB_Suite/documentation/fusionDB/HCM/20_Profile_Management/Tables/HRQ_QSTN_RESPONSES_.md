# HRQ_QSTN_RESPONSES_

This contains a participant's response to a specific question within a questionnaire.  This may reference the answer the user selected, or a rating level, or the actual entered text.  For multi-part questions (such as matching questions) it may also reference a sub-question.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnresponses-30957.html#hrqqstnresponses-30957](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnresponses-30957.html#hrqqstnresponses-30957)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QSTN_RESPONSES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, QSTN_RESPONSE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTN_RESPONSE_ID | NUMBER |  | 18 | Yes | Unique identifier for question response.  System generated primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| QSTNR_RESPONSE_ID | NUMBER |  | 18 |  | Identifies the questionnaire response. |
| QSTNR_QUESTION_ID | NUMBER |  | 18 |  | Identifies the questionnaire question. |
| SUB_QUESTION_ID | NUMBER |  | 18 |  | Identifies the sub question. |
| QSTN_ANSWER_ID | NUMBER |  | 18 |  | Identifies the answer for a question. |
| ANSWER_TEXT | VARCHAR2 | 4000 |  |  | The answer for free text questions. |
| ANSWER_LIST | VARCHAR2 | 2000 |  |  | Identifies the list of answers for a question that allows multiple selections to be made. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SCORE | NUMBER |  | 18 |  | Score for the Question response. |
| ANSWER_CLOB | CLOB |  |  |  | The answer for free text questions. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |
| CHOICE_LIST | VARCHAR2 | 2000 |  |  | List of Choices presented out of the pool of choices for current response. |
| ANSWER_COMMENTS | VARCHAR2 | 4000 |  |  | This field is used for capturing comments from the user. |
| RESPONSE_SENTIMENT | VARCHAR2 | 80 |  |  | This field is used for capturing sentiment analysis from the response. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QSTN_RESPONSES_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, QSTN_RESPONSE_ID |
| HRQ_RESPONSEN1_ | Non Unique | Default | QSTN_RESPONSE_ID, LAST_UPDATE_DATE |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
