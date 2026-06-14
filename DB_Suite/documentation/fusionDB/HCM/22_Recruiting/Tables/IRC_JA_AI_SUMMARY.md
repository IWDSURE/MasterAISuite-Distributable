# IRC_JA_AI_SUMMARY

This table will store both candidate profile and screening and interview summaries for the overview tab.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjaaisummary-14540.html#ircjaaisummary-14540](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjaaisummary-14540.html#ircjaaisummary-14540)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_JA_AI_SUMMARY_PK | JA_AI_SUMMARY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JA_AI_SUMMARY_ID | NUMBER |  | 18 | Yes | Primary Key. Uniquely identifies a job application summary. |
| PROCESSING_STATUS | VARCHAR2 | 64 |  |  | Processing status of this review notification. |
| TRY_COUNT | NUMBER |  | 4 |  | This column stores the number of tries made to invoke the Summary generation. |
| AGENT_JOB_ID | VARCHAR2 | 64 |  |  | Unique identifier for the job assigned to the AI agent. |
| BULK_SUMMARY_FLAG | VARCHAR2 | 1 |  |  | Indicates whether summary generation was initiated via a bulk process. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| SUBMISSION_ID | NUMBER |  | 18 | Yes | Job application submission id.Foreign key to irc_submissions table. |
| SUMMARY_TYPE | VARCHAR2 | 64 |  | Yes | Type of summary (CANDIDATE_PROFILE/SCREENING_AND_INTERVIEW). |
| SUMMARY_CONTENT | CLOB |  |  |  | AI-generated summary of the job application. |
| PROGRESS_FLAG | VARCHAR2 | 1 |  |  | Progress indicator for summary generation. |
| GENERATION_DATE | TIMESTAMP |  |  |  | Timestamp when summary was generated. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_JA_AI_SUMMARY_N1 | Non Unique | Default | SUBMISSION_ID, SUMMARY_TYPE |
| IRC_JA_AI_SUMMARY_N2 | Non Unique | Default | REQUEST_ID, BULK_SUMMARY_FLAG, PROCESSING_STATUS, TRY_COUNT |
| IRC_JA_AI_SUMMARY_N3 | Non Unique | Default | PROCESSING_STATUS, TRY_COUNT, REQUEST_ID |
| IRC_JA_AI_SUMMARY_PK | Unique | Default | JA_AI_SUMMARY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
