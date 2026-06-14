# IRC_TN_JOB_APPLICATIONS

This is the table for storing job applications by an agent on Talent Network.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobapplications-8933.html#irctnjobapplications-8933](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobapplications-8933.html#irctnjobapplications-8933)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_JOB_APPLICATIONS_PK | JOB_APP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_APP_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | To store the subscriber id. Foreign Key to IRC_TN_SUBSCRIBERS. |
| TN_JOB_ID | NUMBER |  | 18 | Yes | To store the TN job id. Foreign Key to IRC_TN_JOBS_B. |
| AGENCY_ID | NUMBER |  | 18 | Yes | Stores the AGENCY_ID of the Agent who submitted the candidate job application. Foreign key to IRC_TN_AGENCIES table. |
| AGENT_ID | NUMBER |  | 18 | Yes | Stores the AGENT_ID of the Agent who submitted the candidate job application. Foreign key to IRC_TN_AGENTS table. |
| APPLICATION_DATE | DATE |  |  | Yes | Stores the date when this job application was submitted. |
| ACTIVE_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether the talent network job application is active or not. |
| FA_SUBMISSION_ID | NUMBER |  | 18 | Yes | Stores the SUBMISSION_ID of the requisition's submission. |
| FA_CANDIDATE_NUMBER | VARCHAR2 | 30 |  | Yes | The person id related to the candidate that is stored in the IRC_CANDIDATES table. |
| FA_REQUISITION_NUMBER | VARCHAR2 | 240 |  | Yes | Stores the REQUISITION_NUMBER from IRC_REQUISITIONS_B table. |
| FA_CURRENT_PHASE_ID | NUMBER |  | 18 | Yes | Stores the current phase of the job application. |
| FA_CURRENT_STATE_ID | NUMBER |  | 18 | Yes | Stores the current state of the job application. |
| FA_APPLICATION_LANGUAGE_CODE | VARCHAR2 | 4 |  | Yes | Stores the language code for the job application. |
| TN_STATUS_CODE | VARCHAR2 | 240 |  | Yes | Talent Network Job Application Status as a lookup code. |
| FA_PUBLIC_STATUS | VARCHAR2 | 240 |  | Yes | Stores the status which is shown to the external. |
| FA_ACTIVE_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether the FA job application is active or not. |
| FA_CONFIRMED_FLAG | VARCHAR2 | 1 |  | Yes | This flag is used to determine whether job application is confirmed or not. |
| CANDIDATE_LAST_NAME | VARCHAR2 | 150 |  | Yes | To store the Candidate's Last name. |
| CANDIDATE_FIRST_NAME | VARCHAR2 | 150 |  | Yes | To store the Candidate's First name. |
| CANDIDATE_EMAIL | VARCHAR2 | 240 |  | Yes | To store the Candidate Email. |
| OBJECT_STATUS | VARCHAR2 | 30 |  | Yes | Indicates the status of the object. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TN_JOB_APPLICATIONS_FK1 | Non Unique | Default | SUBSCRIBER_ID |
| IRC_TN_JOB_APPLICATIONS_FK2 | Non Unique | Default | TN_JOB_ID |
| IRC_TN_JOB_APPLICATIONS_FK3 | Non Unique | Default | AGENCY_ID |
| IRC_TN_JOB_APPLICATIONS_FK4 | Non Unique | Default | AGENT_ID |
| IRC_TN_JOB_APPLICATIONS_PK | Unique | Default | JOB_APP_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
