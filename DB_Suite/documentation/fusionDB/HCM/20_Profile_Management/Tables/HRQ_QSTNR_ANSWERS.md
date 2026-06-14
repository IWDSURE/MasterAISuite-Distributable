# HRQ_QSTNR_ANSWERS

List the score or weight of each of the questionnaire answer.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnranswers-6145.html#hrqqstnranswers-6145](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnranswers-6145.html#hrqqstnranswers-6145)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QSTNR_ANSWERS_PK | QSTNR_ANSWER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTNR_ANSWER_ID | NUMBER |  | 18 | Yes | Unique identifier for a questionnaire answer.  System generated primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| RATING_LEVEL_ID | NUMBER |  | 18 |  | Identifies the rating level id. |
| QSTNR_QUESTION_ID | NUMBER |  | 18 |  | Identifies the questionnaire question id. |
| SUB_QUESTION_ID | NUMBER |  | 18 |  | Identifies the sub question id. |
| ANSWER_ID | NUMBER |  | 18 |  | Identifies the answer id. |
| SCORE | NUMBER |  | 18 |  | The score/weight of this answer. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QSTNR_ANSWERS_N2 | Non Unique | Default | ANSWER_ID |
| HRQ_QSTNR_ANSWERS_PK | Unique | Default | QSTNR_ANSWER_ID |
| HRQ_QSTNR_ANSWERS_U1 | Unique | Default | QSTNR_QUESTION_ID, ANSWER_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
