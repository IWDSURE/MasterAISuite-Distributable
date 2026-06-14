# HTS_COVERAGE_DETAILS

Stores the coverage detail records of the workload plan and schedule shift, fully expanded to every 15 minute time slot.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htscoveragedetails-26656.html#htscoveragedetails-26656](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htscoveragedetails-26656.html#htscoveragedetails-26656)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_COVERAGE_DETAILS_PK | COVERAGE_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COVERAGE_DETAIL_ID | NUMBER |  | 18 | Yes | Table primary key. Ideally values are automatically incremented using a database sequence |
| COVERAGE_ID | NUMBER |  | 18 | Yes | Identifier to uniquely refer to a coverage record |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard enterprise identifier column for multi tenancy support |
| SCHED_UNIT_ID | NUMBER |  | 18 | Yes | Identifier for the department, that the relevant schedule coverage calculation applies to |
| SCHED_SKILL_ID | NUMBER |  | 18 | Yes | Identifier for the schedule coverage skill |
| COVERAGE_DATE | DATE |  |  |  | Date that the coverage calculation applies to |
| COVERAGE_START_DATE_TIME | DATE |  |  |  | Date and time when the coverage starts, such as 1-JUL-2023 00:15 |
| WORKLOAD_BASELINE_DURATION | NUMBER |  | 9 |  | Baseline duraiton for the workload plan, measured in minutes |
| WORKLOAD_ACTUAL_DURATION | NUMBER |  | 9 |  | Actual duration from the workload plan, measured in minutes |
| ASSIGNED_SHIFTS_DURATION | NUMBER |  | 9 |  | Assigned shift duration determined from the schedule shift, measured in minutes |
| OPEN_SHIFTS_DURATION | NUMBER |  | 9 |  | Open shift duration determined from scheduled shifts, measured in minutes |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_COVERAGE_DETAILS_N1 | Non Unique | Default | COVERAGE_ID, COVERAGE_DATE |
| HTS_COVERAGE_DETAILS_U1 | Unique | Default | COVERAGE_DETAIL_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
