# IRC_CAND_CLOSEOUT_SCANS

This table stores the last scan time-stamp of the ESS job that scans the PER_ACTION_OCCURRENCES table. There will be only one row in this table, the same row will be updated with new scan_end_time after it is created for the first time.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandcloseoutscans-5469.html#irccandcloseoutscans-5469](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandcloseoutscans-5469.html#irccandcloseoutscans-5469)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_CLOSEOUT_SCANS_PK | CAND_CLOSEOUT_SCAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_CLOSEOUT_SCAN_ID | NUMBER |  | 18 | Yes | Primary key for the candidate closeout scans table |
| SCAN_END_TIME | TIMESTAMP |  |  | Yes | Scan End Time stamp (Should be fetched by scanning query itself) |
| FIRST_EXEC_FLAG | VARCHAR2 | 1 |  |  | Indicates if the closeout job is executed for the first time |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_CLOSEOUT_SCANS_PK | Unique | Default | CAND_CLOSEOUT_SCAN_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
