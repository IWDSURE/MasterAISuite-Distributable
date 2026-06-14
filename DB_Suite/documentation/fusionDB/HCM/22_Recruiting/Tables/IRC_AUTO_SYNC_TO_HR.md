# IRC_AUTO_SYNC_TO_HR

This table is used for staging Submissions to Auto Create Offers and Move to HR.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircautosynctohr-20782.html#ircautosynctohr-20782](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircautosynctohr-20782.html#ircautosynctohr-20782)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AUTO_SYNC_TO_HR_PK | AUTO_SYNC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AUTO_SYNC_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| SUBMISSION_ID | NUMBER |  | 18 | Yes | Foreign key to irc_submissions.submission_id table. |
| REQUISITION_ID | NUMBER |  | 18 |  | Foreign key to irc_requisitions_b.requisition_id table. |
| API_ROUTE | VARCHAR2 | 30 |  |  | To store the record processed via OFFER_HDL or GHR_CWK_API |
| PROCESS_STATUS | VARCHAR2 | 64 |  |  | To store the current status of AutoSync To HR Process. |
| PROCESS_SUB_STATUS | VARCHAR2 | 64 |  |  | To store the current substatus of Auto SyncTo HR Process. |
| REQUEST_NUMBER | VARCHAR2 | 64 |  |  | To store the HDL Submission Request Number( Latest Request Number) |
| RETRY_COUNT | NUMBER |  | 5 |  | To store the number of times retried for HDL_Processing (max is 3) |
| OFFER_ID | NUMBER |  | 18 |  | Foreign key to irc_offers table. |
| OBJECT_STATUS | VARCHAR2 | 30 |  | Yes | Stores the status of the object as a lookup code. The corresponding lookup type is ORA_IRC_OBJECT_STATUS |
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
| IRC_AUTO_SYNC_TO_HR_FK1 | Non Unique | Default | SUBMISSION_ID |
| IRC_AUTO_SYNC_TO_HR_FK2 | Non Unique | Default | REQUISITION_ID |
| IRC_AUTO_SYNC_TO_HR_FK3 | Non Unique | Default | OFFER_ID |
| IRC_AUTO_SYNC_TO_HR_PK | Unique | Default | AUTO_SYNC_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
