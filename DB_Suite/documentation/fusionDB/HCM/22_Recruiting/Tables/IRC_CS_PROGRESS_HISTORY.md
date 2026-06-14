# IRC_CS_PROGRESS_HISTORY

This table is used for storing Contingent Submissions progress history details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccsprogresshistory-22321.html#irccsprogresshistory-22321](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccsprogresshistory-22321.html#irccsprogresshistory-22321)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CS_PROGRESS_HISTORY_PK | CS_PROGRESS_HISTORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CS_PROGRESS_HISTORY_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| CONTINGENT_SUBMISSION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CONTINGENT_SUBMISSIONS table. |
| STEP_STATUS_CODE | VARCHAR2 | 64 |  |  | Stores Contingent Submission Workflow Step Code after the move |
| STEP_SUB_STATUS_CODE | VARCHAR2 | 64 |  |  | Stores Contingent Submission Workflow Secondary Step Code after the move |
| STEP_CHANGED_DATE | TIMESTAMP |  |  |  | Date/Time when the step was updated |
| STEP_UPDATED_BY_PERSON_ID | NUMBER |  | 18 |  | Stores the Person Id if the move is done by FA User |
| STEP_UPDATED_BY_AGENT_ID | NUMBER |  | 18 |  | Stores the Agent Id if the move is done by TN User |
| STEP_UPDATED_BY_AGENT_NAME | VARCHAR2 | 300 |  |  | Stores the Agent Name if the move is done by TN User |
| OBJECT_STATUS | VARCHAR2 | 30 |  |  | Indicates the status of the object. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CS_PROGRESS_HISTORY_FK1 | Non Unique | Default | CONTINGENT_SUBMISSION_ID |
| IRC_CS_PROGRESS_HISTORY_PK | Unique | Default | CS_PROGRESS_HISTORY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
