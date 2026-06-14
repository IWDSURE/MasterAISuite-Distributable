# CMP_CWB_SCHEDULED_STATEMENTS

Stores all relevant data of scheduled statements

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbscheduledstatements-20523.html#cmpcwbscheduledstatements-20523](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbscheduledstatements-20523.html#cmpcwbscheduledstatements-20523)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_SCHEDULED_STATEMEN_PK | SCHEDULED_STATEMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULED_STATEMENT_ID | NUMBER |  | 18 | Yes | SCHEDULED_STATEMENT_ID |
| JOB_ID | NUMBER |  | 18 |  | REPORT_JOB_ID |
| JOB_STATUS_CODE | VARCHAR2 | 30 |  |  | JOB_STATUS_CODE |
| JOB_STATUS_DETAIL | VARCHAR2 | 4000 |  |  | JOB_STATUS_DETAIL |
| PLAN_ID | NUMBER |  | 18 |  | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 |  | PERIOD_ID |
| PERSON_EVENT_ID | NUMBER |  | 18 |  | PERSON_EVENT_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| ASSIGNMENT_ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ASSIGNMENT_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
| STMT_TEMPLATE_ID | NUMBER |  | 18 |  | STMT_TEMPLATE_ID |
| STMT_OUTPUT_FORMAT | VARCHAR2 | 30 |  |  | STMT_OUTPUT_FORMAT |
| TOTAL_WORKERS | NUMBER |  |  |  | TOTAL_WORKERS |
| ARGUMENT1 | VARCHAR2 | 4000 |  |  | ARGUMENT1 |
| SUBMITTED_BY | VARCHAR2 | 64 |  |  | SUBMISSION_BY |
| SUBMISSION_DATE | TIMESTAMP |  |  |  | SUBMISSION_DATE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ACTING_MGR_PERSON_EVENT_ID | NUMBER |  | 18 |  | ACTING_MGR_PERSON_EVENT_ID |
| JOB_SOURCE | VARCHAR2 | 30 |  |  | JOB_SOURCE |
| LOGON_PERSON_ID | NUMBER |  | 18 |  | LOGON_PERSON_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_SCHEDULED_STATEMEN_N1 | Non Unique | Default | LOGON_PERSON_ID, PERIOD_ID, PLAN_ID, JOB_SOURCE |
| CMP_CWB_SCHEDULED_STATEMEN_N2 | Non Unique | Default | PERIOD_ID, PLAN_ID, SUBMISSION_DATE, JOB_SOURCE |
| CMP_CWB_SCHEDULED_STATEMEN_PK | Unique | Default | SCHEDULED_STATEMENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
