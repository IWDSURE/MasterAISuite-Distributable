# HRC_DL_REM_PROCESSES

When "Remove Person" ESS job is invoked, this table stores information of the corresponding Run.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremprocesses-27905.html#hrcdlremprocesses-27905](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremprocesses-27905.html#hrcdlremprocesses-27905)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_REM_PROCESSES_PK | PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_ID | NUMBER |  |  | Yes | PROCESS_ID |
| PARENT_PROCESS_ID | NUMBER |  |  | Yes | PARENT_PROCESS_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| STATUS | VARCHAR2 | 30 |  | Yes | STATUS |
| JOB_PROCESS_NAME | VARCHAR2 | 40 |  |  | Job Process Name |
| CHECK_POINT | VARCHAR2 | 100 |  |  | Stores the Check Point value for different Processes. Processes include ESS jobs and the file generation process |
| CANCEL_REQUESTED | VARCHAR2 | 1 |  |  | Cancel Requested Flag |
| PROCESS_LOG | CLOB |  |  |  | PROCESS_LOG |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_REM_PROCESSES_U1 | Unique | Default | PROCESS_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
