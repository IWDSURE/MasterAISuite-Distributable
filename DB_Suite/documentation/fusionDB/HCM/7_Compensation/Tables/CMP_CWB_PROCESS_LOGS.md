# CMP_CWB_PROCESS_LOGS

This table stores detailed logs for CWB batch processes which are generated during process execution and used to track its progress.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbprocesslogs-6696.html#cmpcwbprocesslogs-6696](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbprocesslogs-6696.html#cmpcwbprocesslogs-6696)

## Primary Key

| Name | Columns |
|------|----------|
| cmp_cwb_process_logs_PK | LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOG_ID | NUMBER |  | 18 | Yes | LOG_ID |
| LOG_TYPE | VARCHAR2 | 30 |  | Yes | LOG_TYPE |
| PROCESS_NAME | VARCHAR2 | 80 |  |  | PROCESS_NAME |
| PLAN_ID | NUMBER |  | 18 |  | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 |  | PERIOD_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| PERSON_EVENT_ID | NUMBER |  | 18 |  | PERSON_EVENT_ID |
| RULE_ID | NUMBER |  | 18 |  | RULE_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| LOG_MESSAGE | VARCHAR2 | 4000 |  |  | LOG_MESSAGE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| cmp_cwb_process_logs_N1 | Non Unique | Default | PLAN_ID, PERIOD_ID |
| cmp_cwb_process_logs_N2 | Non Unique | Default | ASSIGNMENT_ID, PERIOD_ID, PLAN_ID |
| cmp_cwb_process_logs_U1 | Unique | Default | LOG_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
