# IRC_SUBMISSIONS

This table contains candidate submissions.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsubmissions-31196.html#ircsubmissions-31196](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsubmissions-31196.html#ircsubmissions-31196)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_SUBMISSIONS_PK | SUBMISSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUBMISSION_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CONFIRMED_FLAG | VARCHAR2 | 1 |  |  | This flag is used to determine whether submission is confirmed or not. |
| CONFIRMED_BY_PERSON_ID | NUMBER |  | 18 |  | Foreign Key to PER_PERSONS table. |
| SUBMISSION_CONFIRMED_DATE | DATE |  |  |  | To track when the submission changed from Unconfirmed to Confirmed. |
| INTERNAL_FLAG | VARCHAR2 | 1 |  |  | For reporting, to know if submission was internal application, at the time it was made. |
| DISQUALIFIED_FLAG | VARCHAR2 | 1 |  |  | To track if submission overall was disqualified (aggregate snapshot of DQ answers). |
| MERGED_FLAG | VARCHAR2 | 1 |  |  | To track if the submission has been delinked/merged. |
| QSTNR_SCORE | NUMBER |  | 18 |  | The total questionnaire score for this submission. |
| AF_VERSION_ID | NUMBER |  | 18 |  | Foreign key to IRC_AF_VERSIONS.AF_VERSION_ID. |
| LEGAL_DESC_VERSION_ID | NUMBER |  | 18 |  | To track the legal disclaimer accepted by the applicant. Foreign key to IRC_DESC_VERSIONS_B.DESC_VERSION_ID. |
| ESIGN_DESC_VERSION_ID | NUMBER |  | 18 |  | To track the Signature statement accepted by the applicant. Foreign key to IRC_DESC_VERSIONS_B.DESC_VERSION_ID. |
| OBJECT_STATUS | VARCHAR2 | 30 |  |  | Stores the status of the object. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITIONS_B table. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CANDIDATES table. |
| SYSTEM_PERSON_TYPE | VARCHAR2 | 30 |  |  | Person type of the job applicant when they applied for the job |
| PIPELINE_SUBMISSION_ID | NUMBER |  | 18 |  | Stores the SUBMISSION_ID of the pipeline requisition's submission,  if this submission is created based on a pipeline requisition's submission. |
| IS_COMPLETED_FLAG | VARCHAR2 | 1 |  |  | Stores whether this submission is completed or not i.e whether the candidate completed filling this submission. |
| CURRENT_PHASE_ID | NUMBER |  | 18 |  | Foreign Key to IRC_PHASES_B table. |
| CURRENT_STATE_ID | NUMBER |  | 18 |  | Foreign Key to IRC_STATES_B table. |
| PUBLIC_STATE_ID | NUMBER |  | 18 |  | Foreign Key to IRC_STATES_B table. This refers to public job application status that can be shared with candidate. |
| IS_RESTRICTED_FLAG | VARCHAR2 | 1 |  |  | Indicates whether the job application is restricted to access based on the user privilage. |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | Indicates whether the Submission is active or not. |
| DISCARDED_FLAG | VARCHAR2 | 1 |  |  | Indicates whether the applicant has reapplied for the job and the current job is discarded. |
| SUBMISSION_DATE | DATE |  |  |  | Stores the date when this submission was submitted. |
| SUBM_LAST_MODIFIED_DATE | TIMESTAMP |  |  |  | Stores the last modified date for the Submission. This is updated even when the child entitiies of the Submission table are updated. This can be used by customers to export submissions which were updated after a certain date. |
| SUBMISSION_LANGUAGE_CODE | VARCHAR2 | 4 |  |  | Stores the language code for the submission |
| PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to profiles table HRT_PROIFLES_B. |
| PROCESS_ID | NUMBER |  | 18 |  | Foreign Key to process table IRC_PROCESS_B. |
| SITE_NUMBER | VARCHAR2 | 240 |  |  | Foreign Key to sites table IRC_CX_SITES_B.SITE_NUMBER. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CATEGORY_CODE | VARCHAR2 | 80 |  |  | Extensible Flexfield Category Code |
| ADDED_BY_PERSON_ID | NUMBER |  | 18 |  | Person who has submitted the job application. |
| ADDED_BY_CONTEXT_CODE | VARCHAR2 | 30 |  |  | Source of the context through which this JA was submitted. |
| SUB_ID_CHAR | VARCHAR2 | 20 |  |  | This column is used to convert Long Submission Id to Char Submission Id. One of the main reason for this column to exists is to join with HRQ_QSTNR_PARTICIPANTS Table where  the SUBJECT_ID is of type varchar. |
| CANDIDATE_WORK_SUMMARY | CLOB |  |  |  | Stores the work summary of job application generated by AI based on candidate input information |
| CURRENT_RANK | NUMBER |  | 5 |  | Current rank number of current job application |
| RANKED_BY_PERSON_ID | NUMBER |  | 18 |  | Person id of person who ranked this job application |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_SUBMISSIONS_FK1 | Non Unique | Default | PERSON_ID |
| IRC_SUBMISSIONS_FK10 | Non Unique | Default | PUBLIC_STATE_ID |
| IRC_SUBMISSIONS_FK11 | Non Unique | Default | PIPELINE_SUBMISSION_ID |
| IRC_SUBMISSIONS_FK12 | Non Unique | default | RANKED_BY_PERSON_ID |
| IRC_SUBMISSIONS_FK13 | Non Unique | default | PROFILE_ID |
| IRC_SUBMISSIONS_FK4 | Non Unique | Default | REQUISITION_ID |
| IRC_SUBMISSIONS_FK5 | Non Unique | Default | PROCESS_ID |
| IRC_SUBMISSIONS_FK6 | Non Unique | Default | AF_VERSION_ID |
| IRC_SUBMISSIONS_FK7 | Non Unique | Default | LEGAL_DESC_VERSION_ID |
| IRC_SUBMISSIONS_FK8 | Non Unique | Default | ESIGN_DESC_VERSION_ID |
| IRC_SUBMISSIONS_FK9 | Non Unique | Default | CONFIRMED_BY_PERSON_ID |
| IRC_SUBMISSIONS_N1 | Non Unique | Default | ADDED_BY_CONTEXT_CODE |
| IRC_SUBMISSIONS_N2 | Non Unique | Default | SUBM_LAST_MODIFIED_DATE |
| IRC_SUBMISSIONS_N3 | Non Unique | Default | SUBMISSION_DATE |
| IRC_SUBMISSIONS_N4 | Non Unique | Default | CURRENT_STATE_ID, CURRENT_PHASE_ID, OBJECT_STATUS |
| IRC_SUBMISSIONS_N5 | Non Unique | Default | CREATION_DATE |
| IRC_SUBMISSIONS_PK | Unique | Default | SUBMISSION_ID |
| IRC_SUBMISSIONS_U1 | Unique | Default | SUB_ID_CHAR |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
