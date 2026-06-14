# IRC_ASMT_PACKAGE_RESULTS

This table contains the package level assessment results for the submissions.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircasmtpackageresults-30517.html#ircasmtpackageresults-30517](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircasmtpackageresults-30517.html#ircasmtpackageresults-30517)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_ASMT_PACKAGE_RESULT_PK | PACKAGE_RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PACKAGE_RESULT_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| SUBMISSION_ID | NUMBER |  | 18 |  | Foreign key value to IRC_SUBMISSIONS table. |
| APP_DRAFT_ID | NUMBER |  | 18 |  | Foreign key to IRC_CX_APP_DRAFTS table. |
| ICE_APP_DRAFT_ID | NUMBER |  | 18 |  | Foreign key to IRC_ICE_APP_DRAFTS table. |
| REQ_PACKAGE_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_ASMT_REQ_PACKAGES table. |
| PACKAGE_STATUS_CODE | VARCHAR2 | 30 |  |  | Status code of the assessment package. |
| COMMENTS | CLOB |  |  |  | Package level comments provided by the partner. |
| BAND | VARCHAR2 | 30 |  |  | Band value provided by the partner. |
| PERCENTILE | NUMBER |  | 9 |  | Percentile value provided by the partner. |
| SCORE | NUMBER |  | 9 |  | Score value provided by the partner. |
| REQUESTED_BY | VARCHAR2 | 64 |  |  | Stores the user who triggered the assessment package for the submission. |
| REQUEST_DATE | TIMESTAMP |  |  |  | Stores the date on which the assessment package was triggered for the submission. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TRY_COUNT | NUMBER |  | 4 |  | This column stores the number of failed tries made to invoke the partner service. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| DRAFT_ADDITIONAL_RESULTS | CLOB |  |  |  | Stores additional results payload for the draft application Assessments packages. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_ASMT_PACKAGE_RESULT_FK1 | Non Unique | Default | REQ_PACKAGE_ID |
| IRC_ASMT_PACKAGE_RESULT_FK2 | Non Unique | Default | SUBMISSION_ID |
| IRC_ASMT_PACKAGE_RESULT_FK3 | Non Unique | Default | APP_DRAFT_ID |
| IRC_ASMT_PACKAGE_RESULT_FK4 | Non Unique | Default | ICE_APP_DRAFT_ID |
| IRC_ASMT_PACKAGE_RESULT_N1 | Non Unique | Default | PACKAGE_STATUS_CODE |
| IRC_ASMT_PACKAGE_RESULT_N2 | Non Unique | Default | TRY_COUNT, PACKAGE_STATUS_CODE |
| IRC_ASMT_PACKAGE_RESULT_PK | Unique | Default | PACKAGE_RESULT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
