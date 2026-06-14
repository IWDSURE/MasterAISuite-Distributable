# IRC_IM_FEEDBK_RESP_DTLS

This table stores the average scores and ratings corresponding to feedback qustionnaire.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimfeedbkrespdtls-27763.html#ircimfeedbkrespdtls-27763](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimfeedbkrespdtls-27763.html#ircimfeedbkrespdtls-27763)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IM_FEEDBK_RESP_DTLS_PK | FEEDBK_RESP_DETAILS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FEEDBK_RESP_DETAILS_ID | NUMBER |  | 18 | Yes | Primary key for this table.System generated. |
| FEEDBACK_ID | NUMBER |  | 18 |  | Stores the feedback ID for the job application. Foreign key to IRC_IM_FEEDBACKS table. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Stores the ID of the questionnaire for which the response details are stored. Foreign key to HRQ_QUESTIONNAIRES_B table. |
| QSTNR_VERSION_NUM | NUMBER |  | 18 |  | Stores the version number of the questionnaire for which the response details are stored. Foreign key to HRQ_QUESTIONNAIRES_B table. |
| SUBMISSION_ID | NUMBER |  | 18 |  | Stores the submission ID for which the feedback request is created. Foreign key to IRC_SUBMISSIONS table. |
| AVG_QSTNR_SCORE | NUMBER |  | 18 |  | Stores average score per questionnaire. |
| QSTNR_MAX_SCORE | NUMBER |  | 18 |  | Stores the value of max score for a questionnaire based on the calculation rule. |
| AVG_QSTNR_RATING | NUMBER |  | 2 |  | Stores average rating per questionnaire. |
| QSTNR_RESPONSE_COUNT | NUMBER |  | 18 |  | Stores number of questionnaire responses. |
| RATING_RESPONSE_COUNT | NUMBER |  | 18 |  | Stores number of rating responses per questionnaire. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IM_FEEDBK_RESP_DTLS_FK1 | Non Unique | Default | FEEDBACK_ID |
| IRC_IM_FEEDBK_RESP_DTLS_FK2 | Non Unique | Default | SUBMISSION_ID |
| IRC_IM_FEEDBK_RESP_DTLS_FK3 | Non Unique | Default | QUESTIONNAIRE_ID, QSTNR_VERSION_NUM |
| IRC_IM_FEEDBK_RESP_DTLS_PK | Unique | Default | FEEDBK_RESP_DETAILS_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
