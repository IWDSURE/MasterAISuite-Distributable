# HTS_STAFF_PLAN_GRIDS

Table holding the Schedule Staffing grid Day of week and grid segment detail definitions

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffplangrids-15454.html#htsstaffplangrids-15454](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffplangrids-15454.html#htsstaffplangrids-15454)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_STAFF_PLAN_GRIDS_PK | STAFF_PLAN_GRID_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STAFF_PLAN_GRID_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a Staffing Plan |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| STAFF_PLAN_GRID_NAME | VARCHAR2 | 100 |  |  | Grid Unique Name for the plan |
| STAFF_PLAN_ID | NUMBER |  | 18 | Yes | Staffing Plan Id |
| STAFF_GRID_ID | NUMBER |  | 18 |  | Grid unique id |
| DESCRIPTIVE_FLEXFIELD_CODE | VARCHAR2 | 40 |  | Yes | Flex Filed Code used in Grid rable |
| STAFF_CONTEXT_CODE | VARCHAR2 | 80 |  |  | Context Code |
| VOLUME_IN_RANGE_CODE | VARCHAR2 | 30 |  |  | Indicates if Volume is in Range or Single |
| RANGE_INCREMENTS | NUMBER |  | 9 |  | Range increments |
| TOTAL_SEGMENTS | NUMBER |  | 9 |  | Total volume segments |
| LAST_DEPLOYED_CONTEXT_CODE | VARCHAR2 | 80 |  |  | Last deployed Context Code |
| MON_IS_INCLUDED_FLAG | VARCHAR2 | 1 |  |  | Monday is part of day of week for this grid |
| TUE_IS_INCLUDED_FLAG | VARCHAR2 | 1 |  |  | Tuesday is part of day of week for this grid |
| WED_IS_INCLUDED_FLAG | VARCHAR2 | 1 |  |  | Wednesday is part of day of week for this grid |
| THU_IS_INCLUDED_FLAG | VARCHAR2 | 1 |  |  | Thursday is part of day of week for this grid |
| FRI_IS_INCLUDED_FLAG | VARCHAR2 | 1 |  |  | Friday is part of day of week for this grid |
| SAT_IS_INCLUDED_FLAG | VARCHAR2 | 1 |  |  | Saturday is part of day of week for this grid |
| SUN_IS_INCLUDED_FLAG | VARCHAR2 | 1 |  |  | Sunday part of day of week for this grid |
| AVERAGE_DAILY_VOLUME | NUMBER |  | 9 |  | Average daily volume |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_STAFF_PLAN_GRIDS_PK | Unique | Default | STAFF_PLAN_GRID_ID |
| HTS_STAFF_PLAN_GRIDS_U1 | Unique | Default | STAFF_PLAN_GRID_NAME, STAFF_PLAN_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
