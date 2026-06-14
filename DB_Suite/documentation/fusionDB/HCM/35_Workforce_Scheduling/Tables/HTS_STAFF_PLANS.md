# HTS_STAFF_PLANS

Table holding the Schedule Staffing Plan for the Staffing matrix

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffplans-24988.html#htsstaffplans-24988](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffplans-24988.html#htsstaffplans-24988)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_STAFF_PLANS_PK | STAFF_PLAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STAFF_PLAN_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a Staffing Plan |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| PLAN_NAME | VARCHAR2 | 150 |  | Yes | Plan name |
| SCHED_UNIT_ID | NUMBER |  | 18 | Yes | Identifier for the Schedule Unit |
| ACTIVE_START_DATE | DATE |  |  | Yes | Active start date |
| ACTIVE_END_DATE | DATE |  |  |  | Active end date |
| VOLUME_CAPACITY_MAX | NUMBER |  | 9 |  | Maximum capacity for volume |
| AVERAGE_DAILY_VOLUME | NUMBER |  | 9 |  | Average daily volume |
| STAFF_PLAN_TYPE_CODE | VARCHAR2 | 30 |  |  | Staffing Plan Type of baseline or Override |
| STAFF_PLAN_STATUS_CODE | VARCHAR2 | 30 |  |  | Staffing Plan Status |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_STAFF_PLANS_PK | Unique | Default | STAFF_PLAN_ID |
| HTS_STAFF_PLANS_U1 | Unique | Default | PLAN_NAME |
| HTS_STAFF_PLANS_U2 | Unique | Default | SCHED_UNIT_ID, ACTIVE_START_DATE |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
