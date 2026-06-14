# PER_NUDGE_PLAN_EXECUTIONS

This table records the information of nudge plan executions.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeplanexecutions-11683.html#pernudgeplanexecutions-11683](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeplanexecutions-11683.html#pernudgeplanexecutions-11683)

## Primary Key

| Name | Columns |
|------|----------|
| PER_NUDGE_PLAN_EXECUTIONS_PK | PLAN_EXECUTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_EXECUTION_ID | NUMBER |  | 18 | Yes | PLAN_EXECUTION_ID |
| NUDGE_PLAN_ID | NUMBER |  | 18 | Yes | NUDGE_PLAN_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| EXECUTION_START | TIMESTAMP |  |  |  | EXECUTION_START |
| EXECUTION_END | TIMESTAMP |  |  |  | EXECUTION_END |
| EXECUTION_STATUS | VARCHAR2 | 30 |  | Yes | EXECUTION_STATUS |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | ERROR_MESSAGE |
| ERROR_STACK_TRACE | CLOB |  |  |  | ERROR_STACK_TRACE |
| POPULATION_COUNT | NUMBER |  | 9 |  | POPULATION_COUNT |
| PERIOD_ID | NUMBER |  | 18 |  | PERIOD_ID |
| RUN_TYPE | VARCHAR2 | 30 |  | Yes | RUN_TYPE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| POPULATION_REQUEST_ID | NUMBER |  | 18 |  | POPULATION_REQUEST_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_NUDGE_PLAN_EXECUTIONS_N1 | Non Unique | Default | NUDGE_PLAN_ID |
| PER_NUDGE_PLAN_EXECUTIONS_PK | Unique | Default | PLAN_EXECUTION_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
