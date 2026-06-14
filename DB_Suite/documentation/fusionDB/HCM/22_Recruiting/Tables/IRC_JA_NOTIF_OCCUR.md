# IRC_JA_NOTIF_OCCUR

This table is used to store the occurrences when a Job Application is moved to a given Phase/State for the review notification action configured in Candidate Selection Process.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjanotifoccur-22613.html#ircjanotifoccur-22613](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjanotifoccur-22613.html#ircjanotifoccur-22613)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_JA_NOTIF_OCCUR_PK | JA_NOTIF_OCCUR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JA_NOTIF_OCCUR_ID | NUMBER |  | 18 | Yes | Primary Key for the Table. System generated. |
| SUBMISSION_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_SUBMISSIONS table. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_REQUISITIONS_B table. |
| CURRENT_PHASE_ID | NUMBER |  | 18 |  | Current Phase of Job Application for which this review notification action is invoked. Foreign Key to IRC_PHASES_B table. |
| CURRENT_STATE_ID | NUMBER |  | 18 |  | Current State of Job Application for which this review notification action is invoked. Foreign Key to IRC_STATES_B table. |
| PUBLIC_STATE_ID | NUMBER |  | 18 |  | This refers to public job application status that can be shared with candidate. Foreign Key to IRC_STATES_B table. |
| STEP_ACTION_USAGE_ID | NUMBER |  | 18 | Yes | Foreign key IRC_STEP_ACTION_USAGES_B table. (Life cycle action context) |
| OCCURANCE_TIME | TIMESTAMP |  |  | Yes | Occurance time stamp when the action is invoked in Canddiate Selection process. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_JA_NOTIF_OCCUR_FK1 | Non Unique | Default | SUBMISSION_ID |
| IRC_JA_NOTIF_OCCUR_N1 | Non Unique | Default | OCCURANCE_TIME |
| IRC_JA_NOTIF_OCCUR_N2 | Non Unique | Default | REQUISITION_ID, CURRENT_PHASE_ID, CURRENT_STATE_ID, STEP_ACTION_USAGE_ID |
| IRC_JA_NOTIF_OCCUR_PK | Unique | Default | JA_NOTIF_OCCUR_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
