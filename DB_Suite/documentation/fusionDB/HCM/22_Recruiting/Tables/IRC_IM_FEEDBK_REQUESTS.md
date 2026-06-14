# IRC_IM_FEEDBK_REQUESTS

This table stores all the feedback requests for a Requisition.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimfeedbkrequests-21202.html#ircimfeedbkrequests-21202](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimfeedbkrequests-21202.html#ircimfeedbkrequests-21202)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IM_FEEDBK_REQUESTS_PK | FEEDBACK_REQUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| FEEDBACK_REQUEST_ID | NUMBER |  | 18 | Yes | System generated primary key for this entity. |  |
| OBJECT_STATUS | VARCHAR2 | 40 |  |  | This field stores the status of feedback request object. |  |
| FEEDBACK_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_IM_FEEDBACKS table. |  |
| PARTICIPANT_ID | VARCHAR2 | 240 |  | Yes | Stores the same value as of HRQ_QSTNR_PARTICIPANTS.PARTICIPANT_ID column. Created with similar datatype. |  |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITIONS_B table. |  |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | Foreign key to HRQ_QUESTIONNAIRES_B table. |  |
| QSTNR_VERSION_NUM | NUMBER |  | 18 | Yes | Version number of the questionnaire. It identifies the version of the questionnaire if it is modified. |  |
| STATUS_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the status of the feedback request as a lookup code. |  |
| EXPIRY_DATE | TIMESTAMP |  |  |  | Stores the expiry date for this feedback request. |  |
| COMPLETION_DATE | TIMESTAMP |  |  |  | Stores the completed date for this feedback request when respondent submits feedback responses. |  |
| DUE_DATE | TIMESTAMP |  |  |  | Stores the due date for this feedback request. |  |
| CANCEL_DATE | TIMESTAMP |  |  |  | Stores the cancel date for this feedback request. |  |
| RENEW_DATE | TIMESTAMP |  |  |  | Stores the renew date for this feedback request. |  |
| RESEND_COUNT | NUMBER |  | 4 |  | Stores the resend count for this feedback request. |  |
| RENEW_COUNT | NUMBER |  | 4 |  | Stores the renew count for this feedback request. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| RATING_REQUESTED_FLAG | VARCHAR2 | 1 |  |  | Stores the flag for rating request. |  |
| RATING | NUMBER |  | 2 |  | Stores the rating of the candidate as a number. |  |
| SCHEDULE_INTERVIEW_ID | NUMBER |  | 18 |  | Foreign key to IRC_IS_INTERVIEWS table | Obsolete |
| ON_BEHALF_ELEVATED_PERSON_ID | NUMBER |  | 18 |  | Stores the ID of the person who will respond to the feedback on behalf of the real user. Foreign key to PER_PERSONS table. |  |
| INTRVW_REQUESTS_ID | NUMBER |  | 18 |  | Foreign key to IRC_IS_INTRVW_REQUESTS table. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| IRC_IM_FEEDBK_REQUESTS_FK1 | Non Unique | Default | FEEDBACK_ID |  |
| IRC_IM_FEEDBK_REQUESTS_FK2 | Non Unique | Default | REQUISITION_ID |  |
| IRC_IM_FEEDBK_REQUESTS_FK3 | Non Unique | Default | SCHEDULE_INTERVIEW_ID | Obsolete |
| IRC_IM_FEEDBK_REQUESTS_FK4 | Non Unique | Default | ON_BEHALF_ELEVATED_PERSON_ID |  |
| IRC_IM_FEEDBK_REQUESTS_FK5 | Non Unique | Default | INTRVW_REQUESTS_ID |  |
| IRC_IM_FEEDBK_REQUESTS_N1 | Non Unique | Default | STATUS_TYPE_CODE, EXPIRY_DATE |  |
| IRC_IM_FEEDBK_REQUESTS_PK | Unique | Default | FEEDBACK_REQUEST_ID |  |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
