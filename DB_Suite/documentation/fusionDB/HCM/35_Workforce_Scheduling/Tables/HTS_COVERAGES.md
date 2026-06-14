# HTS_COVERAGES

Stores the aggregated actual and baseline durations for a schedule. Also stores the aggregate durations for assigned and open shifts

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htscoverages-30263.html#htscoverages-30263](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htscoverages-30263.html#htscoverages-30263)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_COVERAGES_PK | COVERAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COVERAGE_ID | NUMBER |  | 18 | Yes | Table primary key. Ideally values are automatically incremented using a database sequence |
| COVERAGE_IN_SYNC_FLAG | VARCHAR2 | 1 |  |  | Flag column to indicate if the coverage data is in sync with the schedule and demand |
| SCHEDULE_ID | NUMBER |  | 18 | Yes | Identifier for the relevant schedule coverage calculation |
| AGGREGATED_BASELINE_DEMAND | NUMBER |  | 9 |  | Aggregate baseline demand value, measured in minutes (BASELINE) |
| AGGREGATED_ACTUAL_DEMAND | NUMBER |  | 9 |  | Aggregate actual demand value, measured in minutes (actual) |
| AGGREGATED_ASSIGNED_SHIFTS | NUMBER |  | 9 |  | Aggregate duration , in minutes, for the assigned shifts
ALUE |
| AGGREGATED_OPEN_SHIFTS | NUMBER |  | 9 |  | Aggregate duration, in minutes, for the open shifts value |
| RECALCULATION_ESS_REQUEST_ID | NUMBER |  | 18 |  | ESS process request ID used in the most recent coverage recalculation |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard enterprise identifier column for multi tenancy support |
| COVERAGE_CALC_DATE | TIMESTAMP |  |  | Yes | Date and time when the coverage was last calculated |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_COVERAGES_U1 | Unique | Default | COVERAGE_ID |
| HTS_COVERAGES_U2 | Unique | Default | SCHEDULE_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
