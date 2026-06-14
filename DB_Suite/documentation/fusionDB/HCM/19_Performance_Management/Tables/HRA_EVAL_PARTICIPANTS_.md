# HRA_EVAL_PARTICIPANTS_

This table stores the participants that are taking part Performance Document review.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevalparticipants-19611.html#hraevalparticipants-19611](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevalparticipants-19611.html#hraevalparticipants-19611)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_EVAL_PARTICIPANTS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, EVAL_PARTICIPANT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVAL_PARTICIPANT_ID | NUMBER |  | 18 | Yes | Primary key of the Participant |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| EVALUATION_ID | NUMBER |  | 18 |  | Primary key of Evaluation. |
| PERSON_ID | NUMBER |  | 18 |  | The global ID of the person who is nominated as the participant |
| EVAL_ROLE_ID | NUMBER |  | 18 |  | Indicates the role type of the participant |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Stores the questionnaire for the participant |
| ROLE_TYPE_CODE | VARCHAR2 | 30 |  |  | Indicates the code to identify the type of role (MANAGER, WORKER or PARTICIPANT) |
| PARTICIPATION_STATUS_CODE | VARCHAR2 | 30 |  |  | Stores the status of the participant. |
| STATUS_UPDATE_DATE | TIMESTAMP |  |  |  | Stores the date when the participant status was last updated. |
| DUE_DATE | DATE |  |  |  | Stores the due date for the participant to provide the feedback |
| ADDED_BY_PERSON_ID | NUMBER |  | 18 |  | Stores the person_id who added the participant into the document |
| ADDED_BY_ROLE | VARCHAR2 | 30 |  |  | Stores the role type code of who added the participant into the document |
| NOTIFIED_FLAG | VARCHAR2 | 30 |  |  | Stores whether the participant was notified. |
| NOTIFIED_BY_ROLE | VARCHAR2 | 30 |  |  | Stores which role sent the request notification to the participant. |
| NOTIFIED_BY_PERSON_ID | NUMBER |  | 18 |  | Stores the person_id who send request |
| FDBACK_STARTED_FLAG | VARCHAR2 | 30 |  |  | Stores if the participant has started giving the feedback. |
| FDBACK_SENT_BACK_FLAG | VARCHAR2 | 30 |  |  | Stores whether the participant feedback was sent back by the manager for rework. |
| LOCKED_OUT_FLAG | VARCHAR2 | 30 |  |  | Stores whether the participant is locked out or not. |
| LOCKED_OUT_DATE | DATE |  |  |  | Stores the date on which the participant was locked out. |
| FDBACK_COMPLETION_DATE | TIMESTAMP |  |  |  | Stores when the participant feedback was completed. |
| PCPN_COMMENTS_FOR_WRK | VARCHAR2 | 4000 |  |  | Stores the comments given by the participant that the worker can see. |
| MATRIX_PARTICIPANT_FLAG | VARCHAR2 | 30 |  |  | Indicates that role is matrix participant role. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PCPN_COMMENT_TEXT_FOR_WRK | CLOB |  |  |  | Stores the comments given by the participant that the worker can see. |
| ACTION_CODE | VARCHAR2 | 30 |  |  | Action Code for performing the action on the participant. |
| ACTION_REASON | VARCHAR2 | 30 |  |  | Reason for performing the action on the participant. |
| ACTION_PERFORMED_BY | NUMBER |  | 18 |  | Stores the Person Id of the person performing the action. |
| ACTION_PERFORMED_DATE | TIMESTAMP |  |  |  | Timestamp when the action was performed. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_EVAL_PARTICIPANTSN1_ | Non Unique | Default | EVAL_PARTICIPANT_ID, LAST_UPDATE_DATE |
| HRA_EVAL_PARTICIPANTS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, EVAL_PARTICIPANT_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
