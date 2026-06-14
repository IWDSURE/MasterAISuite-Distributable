# IRC_JA_NOTIF_PROCESS

This table is used by ESS job to send the relevant job sharing review notifications per each requisition.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjanotifprocess-26383.html#ircjanotifprocess-26383](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjanotifprocess-26383.html#ircjanotifprocess-26383)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_JA_NOTIF_PROCESS_PK | JA_NOTIF_PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JA_NOTIF_PROCESS_ID | NUMBER |  | 18 | Yes | Primary Key for the Table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_REQUISITIONS_B table. |
| PHASE_ID | NUMBER |  | 18 |  | Phase for which this review notification needs to be processed. Foreign Key to IRC_PHASES_B table. |
| STATE_ID | NUMBER |  | 18 |  | State for which this review notification needs to be processed. Foreign Key to IRC_STATES_B table. |
| STEP_ACTION_USAGE_ID | NUMBER |  | 18 | Yes | Foreign key IRC_STEP_ACTION_USAGES_B table. (Life cycle action context) |
| NOTIFICATION_TYPE | VARCHAR2 | 30 |  |  | To Identify the type of notification that will be proceed. |
| PUBLIC_STATE_ID | NUMBER |  | 18 |  | Foreign Key to IRC_STATES_B table. This refers to public job application status that can be shared with candidate. |
| SUBMISSION_ID | NUMBER |  | 18 |  | Job Application for which configured action is invoked in candidate selection process. Foreign Key to IRC_SUBMISSIONS table. |
| SCHEDULED_TIME | TIMESTAMP |  |  |  | Schedule Time after which candidate notification can be processed. |
| PROCESSING_STATUS | VARCHAR2 | 1000 |  |  | Processing Status of this review notification. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_JA_NOTIF_PROCESS_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_JA_NOTIF_PROCESS_FK2 | Non Unique | Default | PHASE_ID |
| IRC_JA_NOTIF_PROCESS_FK3 | Non Unique | Default | STATE_ID |
| IRC_JA_NOTIF_PROCESS_FK4 | Non Unique | Default | STEP_ACTION_USAGE_ID |
| IRC_JA_NOTIF_PROCESS_FK5 | Non Unique | Default | PUBLIC_STATE_ID |
| IRC_JA_NOTIF_PROCESS_FK6 | Non Unique | Default | SUBMISSION_ID |
| IRC_JA_NOTIF_PROCESS_N1 | Non Unique | Default | NOTIFICATION_TYPE, PROCESSING_STATUS |
| IRC_JA_NOTIF_PROCESS_PK | Unique | Default | JA_NOTIF_PROCESS_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
