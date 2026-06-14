# PER_NUDGE_PLAN_OBJECTS

This table records the nudge plan objects.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeplanobjects-25491.html#pernudgeplanobjects-25491](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeplanobjects-25491.html#pernudgeplanobjects-25491)

## Primary Key

| Name | Columns |
|------|----------|
| PER_NUDGE_PLAN_OBJECTS_PK | PLAN_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_OBJECT_ID | NUMBER |  | 18 | Yes | PLAN_OBJECT_ID |
| NUDGE_PLAN_ID | NUMBER |  | 18 | Yes | NUDGE_PLAN_ID |
| OBJECT_ID | NUMBER |  | 18 | Yes | OBJECT_ID |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | OBJECT_TYPE |
| FIRST_PLAN_EXECUTION_ID | NUMBER |  | 18 | Yes | FIRST_PLAN_EXECUTION_ID |
| LAST_PLAN_EXECUTION_ID | NUMBER |  | 18 | Yes | LAST_PLAN_EXECUTION_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SOURCE | VARCHAR2 | 30 |  | Yes | SOURCE |
| NUDGE_EVENT_OCCURRENCE_ID | NUMBER |  | 18 |  | NUDGE_EVENT_OCCURRENCE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| PER_NUDGE_PLAN_OBJECTS_N1 | Non Unique | Default | NUDGE_PLAN_ID, LAST_PLAN_EXECUTION_ID |  |
| PER_NUDGE_PLAN_OBJECTS_PK | Unique | Default | PLAN_OBJECT_ID |  |
| PER_NUDGE_PLAN_OBJECTS_U1 | Unique | Default | NUDGE_PLAN_ID, OBJECT_ID, OBJECT_TYPE | Obsolete |
| PER_NUDGE_PLAN_OBJECTS_N2 | Non Unique | Default | NUDGE_PLAN_ID, OBJECT_ID, OBJECT_TYPE |  |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
