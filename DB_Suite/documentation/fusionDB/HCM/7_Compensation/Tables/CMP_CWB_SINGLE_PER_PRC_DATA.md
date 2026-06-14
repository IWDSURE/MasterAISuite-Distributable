# CMP_CWB_SINGLE_PER_PRC_DATA

Stores batch process stats information for reprocess or add new plan

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbsingleperprcdata-3865.html#cmpcwbsingleperprcdata-3865](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbsingleperprcdata-3865.html#cmpcwbsingleperprcdata-3865)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_SINGLE_PER_PRC_DATA_PK | SINGLE_PERSON_PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SINGLE_PERSON_PROCESS_ID | NUMBER |  | 18 | Yes | SINGLE_PERSON_PROCESS_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| EFFECTIVE_DATE | DATE |  |  | Yes | EFFECTIVE_DATE |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |
| PERSON_EVENT_ID | NUMBER |  | 18 |  | PERSON_EVENT_ID |
| PREV_PERSON_EVENT_ID | NUMBER |  | 18 |  | PREV_PERSON_EVENT_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| BACKOUT_NEEDED_FLAG | VARCHAR2 | 1 |  |  | BACKOUT_NEEDED_FLAG |
| PERSON_NUMBER | VARCHAR2 | 30 |  |  | PERSON_NUMBER |
| ASSIGNMENT_NUMBER | VARCHAR2 | 50 |  |  | ASSIGNMENT_NUMBER |
| JOB_ID | NUMBER |  | 18 |  | JOB_ID |
| ORGANIZATION_ID | NUMBER |  | 18 |  | ORGANIZATION_ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| ELIG_FLAG | VARCHAR2 | 1 |  |  | ELIG_FLAG |
| ESS_STATUS_CODE | VARCHAR2 | 30 |  |  | ESS_STATUS_CODE |
| PROCESS_STATUS_CODE | VARCHAR2 | 120 |  |  | PROCESS_STATUS_CODE |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | ERROR_MESSAGE |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | BUSINESS_UNIT_ID |
| SUBMISSION_TIME | TIMESTAMP |  |  |  | SUBMISSION_TIME |
| COMPLETION_TIME | TIMESTAMP |  |  |  | COMPLETION_TIME |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_SINGLE_PER_PRC_DATA_N1 | Non Unique | Default | PERIOD_ID, PLAN_ID |
| CMP_CWB_SINGLE_PER_PRC_DATA_N2 | Non Unique | Default | ASSIGNMENT_ID, PERIOD_ID, PLAN_ID |
| CMP_CWB_SINGLE_PER_PRC_DATA_PK | Unique | Default | SINGLE_PERSON_PROCESS_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
