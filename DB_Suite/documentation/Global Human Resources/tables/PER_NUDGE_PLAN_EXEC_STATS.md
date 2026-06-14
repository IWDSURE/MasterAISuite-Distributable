# PER_NUDGE_PLAN_EXEC_STATS

This table records the nudges execution status information.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeplanexecstats-23802.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeplanexecstats-23802.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_NUDGE_PLAN_EXEC_STATS_PK | PLAN_EXECUTION_STAT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_EXECUTION_STAT_ID | NUMBER |  | 18 | Yes | PLAN_EXECUTION_STAT_ID |
| PLAN_EXECUTION_ID | NUMBER |  | 18 | Yes | PLAN_EXECUTION_ID |
| PLAN_NUDGE_ID | NUMBER |  | 18 | Yes | PLAN_NUDGE_ID |
| STATUS | VARCHAR2 | 30 |  | Yes | STATUS |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | ERROR_MESSAGE |
| ERROR_STACK_TRACE | CLOB |  |  |  | ERROR_STACK_TRACE |
| NUDGE_COUNT | NUMBER |  | 18 |  | NUDGE_COUNT |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_NUDGE_PLAN_EXEC_STATS_N1 | Non Unique | Default | PLAN_EXECUTION_ID |
| PER_NUDGE_PLAN_EXEC_STATS_PK | Unique | Default | PLAN_EXECUTION_STAT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
