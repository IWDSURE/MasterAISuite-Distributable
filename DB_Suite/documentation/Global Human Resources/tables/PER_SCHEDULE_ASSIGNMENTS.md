# PER_SCHEDULE_ASSIGNMENTS

This table holds Schedule assignment data for each resource

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perscheduleassignments-27807.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perscheduleassignments-27807.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SCHEDULE_ASSIGNMENTS_PK | SCHEDULE_ASSIGNMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Primary key for schedule assignment |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SCHEDULE_ID | NUMBER |  | 18 | Yes | Schedule Id for the associated Schedule |
| RESOURCE_TYPE | VARCHAR2 | 30 |  | Yes | Type of resource like assignment,position,job etc |
| RESOURCE_ID | NUMBER |  | 18 | Yes | Unique Id of Identified Resource |
| START_DATE | DATE |  |  | Yes | Start date for Schedule assignment |
| END_DATE | DATE |  |  | Yes | End date for Schedule assignment |
| START_PATTERN_DTL_ID | NUMBER |  | 18 |  | Start pattern Detail Id |
| PRIMARY_FLAG | VARCHAR2 | 30 |  |  | Flag to represent Primary Schedule |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_SCHEDULE_ASSIGNMENTS_N1 | Non Unique | Default | SCHEDULE_ID |
| PER_SCHEDULE_ASSIGNMENTS_N2 | Non Unique | Default | RESOURCE_TYPE, RESOURCE_ID |
| PER_SCHEDULE_ASSIGNMENTS_U1 | Unique | Default | SCHEDULE_ASSIGNMENT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
