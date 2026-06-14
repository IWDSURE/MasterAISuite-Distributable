# HTS_STAFF_PLAN_GRID_CONFIGS_

Table holding the Schedule Staffing Plan configuration used in the Staffing grids

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffplangridconfigs-31710.html#htsstaffplangridconfigs-31710](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffplangridconfigs-31710.html#htsstaffplangridconfigs-31710)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_STAFF_PLAN_GRID_CONFG_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PLAN_GRID_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_GRID_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a Staffing Plan Skills |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| PLAN_GRID_CONFIG_CODE | VARCHAR2 | 80 |  |  | Unique code entered when creating a Plan Grid configuration Code, |
| STAFF_PLAN_ID | NUMBER |  | 18 |  | Foreign key to Staffing Plan table |
| STAFF_PLAN_GRID_ID | NUMBER |  | 18 |  | Foreign key to Staffing Plan Grid table |
| STAFF_PLAN_JOB_ID | NUMBER |  | 18 |  | Foreign key to Staffing Plan Job table |
| STAFF_PLAN_SKILL_ID | NUMBER |  | 18 |  | Skill without Qualifications same as staffing plan jobs |
| APPLY_TO | VARCHAR2 | 30 |  |  | Indicates Calculation Type applies Job  or group |
| CALC_TYPE | VARCHAR2 | 30 |  |  | Ratio Calculation Type |
| MIN_STAFF_VALUE | NUMBER |  |  |  | Minimum Value |
| RATIO_STAFF_VALUE | NUMBER |  |  |  | Staffing Value used to calculate the ratio |
| RATIO_SEGMENT_VOLUME | NUMBER |  |  |  | Segment Volume used to calculate the ratio |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_STAFF_PLAN_GRID_CONFG_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, PLAN_GRID_CONFIG_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
