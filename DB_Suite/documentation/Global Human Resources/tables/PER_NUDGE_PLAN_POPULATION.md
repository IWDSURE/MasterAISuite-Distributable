# PER_NUDGE_PLAN_POPULATION

This table records the nudge plan population.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeplanpopulation-30539.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeplanpopulation-30539.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_NUDGE_PLAN_POPULATION_PK | PLAN_POPULATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_POPULATION_ID | NUMBER |  | 18 | Yes | PLAN_POPULATION_ID |
| NUDGE_PLAN_ID | NUMBER |  | 18 | Yes | NUDGE_PLAN_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| FIRST_PLAN_EXECUTION_ID | NUMBER |  | 18 | Yes | FIRST_PLAN_EXECUTION_ID |
| LAST_PLAN_EXECUTION_ID | NUMBER |  | 18 | Yes | LAST_PLAN_EXECUTION_ID |
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
| PER_NUDGE_PLAN_POPULATION_N1 | Non Unique | Default | NUDGE_PLAN_ID, PERSON_ID |
| PER_NUDGE_PLAN_POPULATION_N2 | Non Unique | Default | NUDGE_PLAN_ID, LAST_PLAN_EXECUTION_ID |
| PER_NUDGE_PLAN_POPULATION_PK | Unique | Default | PLAN_POPULATION_ID |
| PER_NUDGE_PLAN_POPULATION_U1 | Unique | Default | NUDGE_PLAN_ID, ASSIGNMENT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
