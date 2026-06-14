# HTS_WORKLOADS

Table to store the detailed value of the Workload demand, resulting from the various existing Workload plans.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkloads-28161.html#htsworkloads-28161](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkloads-28161.html#htsworkloads-28161)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_WORKLOADS_PK | WORKLOAD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORKLOAD_ID | NUMBER |  | 18 | Yes | Primary key identifiying the publish event record by a system generated ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SCHED_UNIT_ID | NUMBER |  | 18 | Yes | SCHED_UNIT_ID |
| SCHED_SKILL_ID | NUMBER |  | 18 | Yes | SKILL_ID |
| SHIFT_TYPE_ID | NUMBER |  | 18 |  | Indicates whether the shift is Regular or On-Call or any custom shift type |
| REF_DATE | DATE |  |  | Yes | Reference Date |
| START_TIME_OFFSET | NUMBER |  | 9 | Yes | START_TIME_OFFSET |
| END_TIME_OFFSET | NUMBER |  | 9 | Yes | END_TIME_OFFSET |
| WORKLOAD_VALUE | NUMBER |  | 15 |  | WORKLOAD_VALUE |
| WORKLOAD_UOM | VARCHAR2 | 30 |  |  | WORKLOAD_UOM |
| BREAK_MINUTES | NUMBER |  | 9 |  | Number of break minutes to deduct from the workload quantity |
| ORIGIN | VARCHAR2 | 30 |  |  | Process from which originates the workload value, among Budget, Staffing or Workload Plans |
| ORIGIN_WORKLOAD_TYPE | VARCHAR2 | 30 |  |  | Workload type of the workload item from which originates the workload value, among  Baseline, Adjusted or Actual |
| RESULT_TYPE | VARCHAR2 | 30 |  |  | Specifies the type of workload , among staffing workload, consolidated workload plans, or total consolidated workload |
| WORKLOAD_TYPE | VARCHAR2 | 30 |  |  | Workload type of the result, among Baseline or Current |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_WORKLOADS_N1 | Non Unique | Default | REF_DATE, SCHED_UNIT_ID, WORKLOAD_TYPE, RESULT_TYPE, SCHED_SKILL_ID |
| HTS_WORKLOADS_PK | Unique | Default | WORKLOAD_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
