# HTS_STAFF_GRIDS_

Table holding the Schedule Staffing Grid header information

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffgrids-19559.html#htsstaffgrids-19559](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffgrids-19559.html#htsstaffgrids-19559)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_STAFF_GRIDS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, STAFF_GRID_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STAFF_GRID_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a Staffing Plan |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| GRID_CODE | VARCHAR2 | 280 |  |  | Grid Code or Template Name |
| DESCRIPTIVE_FLEXFIELD_CODE | VARCHAR2 | 40 |  |  | Flex Filed Code |
| STAFF_CONTEXT_CODE | VARCHAR2 | 80 |  |  | Context Code |
| VOLUME_CAPACITY_MAX | NUMBER |  | 9 |  | Maximum capacity for volume |
| RANGE_INCREMENTS | NUMBER |  | 9 |  | Range increments |
| TOTAL_SEGMENTS | NUMBER |  | 9 |  | Total volume segments |
| STAFF_GRID_STATUS_CODE | VARCHAR2 | 30 |  |  | Grid Status |
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
| HTS_STAFF_GRIDS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, STAFF_GRID_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
