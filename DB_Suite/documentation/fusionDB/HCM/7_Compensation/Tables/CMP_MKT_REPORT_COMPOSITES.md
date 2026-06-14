# CMP_MKT_REPORT_COMPOSITES

Table to record market data composite for a person assignment

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktreportcomposites-11802.html#cmpmktreportcomposites-11802](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktreportcomposites-11802.html#cmpmktreportcomposites-11802)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_REPORT_COMPOSITES_PK | PERSON_EVENT_ID, COMP_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | Identifier for a person assignment in a plan cycle |
| COMP_TYPE_ID | NUMBER |  | 18 | Yes | Compensation type Indentifier |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Person Assignment Identifier |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Identifier |
| JOB_ID | NUMBER |  | 18 |  | Job Identifier |
| POSITION_ID | NUMBER |  | 18 |  | Position Identifier |
| LOCATION_ID | NUMBER |  | 18 |  | Location Identifier |
| COMPOSITE_ID | NUMBER |  | 18 |  | Market Composite Identifier |
| BENCHMARK_JOB_ID | NUMBER |  | 18 |  | Benchmark Job Identifier |
| SEGMENT_ID | NUMBER |  | 18 |  | Segment Identifier |
| PERIOD_ID | NUMBER |  | 18 | Yes | Plan Period Identifier |
| PLAN_ID | NUMBER |  | 18 | Yes | Plan Identifier |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_REPORT_COMPOSITES_PK | Unique | Default | PERSON_EVENT_ID, COMP_TYPE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
