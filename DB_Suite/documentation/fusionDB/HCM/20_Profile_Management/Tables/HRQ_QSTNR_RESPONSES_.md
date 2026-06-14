# HRQ_QSTNR_RESPONSES_

Contains participant???s attempts at responding to a Questionnaire.  In some cases, a Participant may have more than one attempt at responding to a Questionnaire.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrresponses-25058.html#hrqqstnrresponses-25058](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrresponses-25058.html#hrqqstnrresponses-25058)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QSTNR_RESPONSES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, QSTNR_RESPONSE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTNR_RESPONSE_ID | NUMBER |  | 18 | Yes | Unique identifier for a questionnaire response.  System generated primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| QSTNR_PARTICIPANT_ID | NUMBER |  | 18 |  | Identifies the questionnaire participant id. |
| QSTNR_VERSION_NUM | NUMBER |  | 18 |  | Identifies the questionnaire version number. |
| ATTEMPT_NUM | NUMBER |  | 18 |  | Identifies the attempt number of this response from the participant. |
| STATUS | VARCHAR2 | 30 |  |  | Identifies the status of the participant's response. |
| SUBMITTED_DATE_TIME | DATE |  |  |  | Identifies the date and time the participant has submitted this response. |
| TOTAL_SCORE | NUMBER |  | 18 |  | Saves the total score for the questionnaire |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LATEST_ATTEMPT_FLAG | VARCHAR2 | 30 |  |  | Identifies the latest submitted attempt by the participant |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QSTNR_RESPONSEN1_ | Non Unique | Default | QSTNR_RESPONSE_ID, LAST_UPDATE_DATE |
| HRQ_QSTNR_RESPONSES_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, QSTNR_RESPONSE_ID |
| HRQ_QSTNR_RESPONSES_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, QSTNR_PARTICIPANT_ID, ATTEMPT_NUM |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
