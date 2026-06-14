# IRC_DA_PARTNER_NOTIF

This table contains the partner notification information for third party job site direct apply.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdapartnernotif-24048.html#ircdapartnernotif-24048](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdapartnernotif-24048.html#ircdapartnernotif-24048)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_DA_PARTNER_NOTIF_PK | DA_PARTNER_NOTIF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DA_PARTNER_NOTIF_ID | NUMBER |  | 18 | Yes | Primary key for the table. System generated. |
| SUBMISSION_ID | NUMBER |  | 18 | Yes | Job Application for which configured action is invoked in the candidate selection process. Foreign Key to IRC_SUBMISSIONS table. |
| CURRENT_PHASE_ID | NUMBER |  | 18 | Yes | Current Phase of Job Application for which this direct apply notification action is invoked. Foreign Key to IRC_PHASES_B table. |
| CURRENT_STATE_ID | NUMBER |  | 18 | Yes | Current State of Job Application for which this direct apply notification action is invoked. Foreign Key to IRC_STATES_B table. |
| STEP_ACTION_USAGE_ID | NUMBER |  | 18 | Yes | Foreign key IRC_LC_ACTION_USAGES_B table. (Life cycle action context) |
| PUBLIC_STATE_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_STATES_B table. This refers to public job application status that can be shared with candidates. |
| EVENT_DATE | TIMESTAMP |  |  |  | Occurrence time stamp when the direct apply notification action is invoked. |
| PROCESSING_STATUS | VARCHAR2 | 64 |  |  | Processing Status of this direct apply notification.  Possible values are "Success", "Not Implemented", "Error", "N/A" etc.  Not look up values. |
| TRY_COUNT | NUMBER |  | 4 |  | This column stores the number of tries made to invoke the partner service. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_DA_PARTNER_NOTIF_FK1 | Non Unique | Default | SUBMISSION_ID |
| IRC_DA_PARTNER_NOTIF_FK2 | Non Unique | Default | CURRENT_PHASE_ID |
| IRC_DA_PARTNER_NOTIF_FK3 | Non Unique | Default | CURRENT_STATE_ID |
| IRC_DA_PARTNER_NOTIF_FK4 | Non Unique | Default | STEP_ACTION_USAGE_ID |
| IRC_DA_PARTNER_NOTIF_FK5 | Non Unique | Default | PUBLIC_STATE_ID |
| IRC_DA_PARTNER_NOTIF_PK | Unique | Default | DA_PARTNER_NOTIF_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
