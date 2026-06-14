# HRG_PERF_CYCLE_OBJECTS

Performance Management Cycle Objects

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgperfcycleobjects-13296.html#hrgperfcycleobjects-13296](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgperfcycleobjects-13296.html#hrgperfcycleobjects-13296)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_PERF_CYCLE_OBJECTS_PK | PERF_CYCLE_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERF_CYCLE_OBJECT_ID | NUMBER |  | 18 | Yes | Primary key to Performance Management Cycle object |
| PERF_CYCLE_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to group objects with-in a type or otherwise |
| OBJECT_ID | NUMBER |  | 18 | Yes | Foreign key to objects(Goal plans/check-ins/performance documents) |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_PERF_CYCLE_OBJECTS_N1 | Non Unique | DEFAULT | PERF_CYCLE_GROUP_ID |
| HRG_PERF_CYCLE_OBJECTS_PK | Unique | DEFAULT | PERF_CYCLE_OBJECT_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
