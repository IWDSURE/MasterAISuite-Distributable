# HTS_STAFF_PLANS_

Table holding the Schedule Staffing Plan for the Staffing matrix

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffplans-14080.html#htsstaffplans-14080](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffplans-14080.html#htsstaffplans-14080)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_STAFF_PLANS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, STAFF_PLAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STAFF_PLAN_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a Staffing Plan |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| PLAN_NAME | VARCHAR2 | 150 |  |  | Plan name |
| SCHED_UNIT_ID | NUMBER |  | 18 |  | Identifier for the Schedule Unit |
| ACTIVE_START_DATE | DATE |  |  |  | Active start date |
| ACTIVE_END_DATE | DATE |  |  |  | Active end date |
| VOLUME_CAPACITY_MAX | NUMBER |  | 9 |  | Maximum capacity for volume |
| AVERAGE_DAILY_VOLUME | NUMBER |  | 9 |  | Average daily volume |
| STAFF_PLAN_TYPE_CODE | VARCHAR2 | 30 |  |  | Staffing Plan Type of baseline or Override |
| STAFF_PLAN_STATUS_CODE | VARCHAR2 | 30 |  |  | Staffing Plan Status |
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
| HTS_STAFF_PLANS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, STAFF_PLAN_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
