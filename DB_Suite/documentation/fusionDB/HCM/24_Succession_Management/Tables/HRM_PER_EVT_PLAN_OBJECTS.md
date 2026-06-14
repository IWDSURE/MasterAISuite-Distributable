# HRM_PER_EVT_PLAN_OBJECTS

This table store the information about the plans and plan candidates which are processed via HCM events.

## Details

**Schema:** FUSION

**Object owner:** HRM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmperevtplanobjects-7979.html#hrmperevtplanobjects-7979](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmperevtplanobjects-7979.html#hrmperevtplanobjects-7979)

## Primary Key

| Name | Columns |
|------|----------|
| hrm_per_evt_plan_objects_PK | PER_EVT_PLAN_OBJECT_ID, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_EVT_PLAN_OBJECT_ID | NUMBER |  | 18 | Yes | Primary key of the processed plan objects. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |
| PERSON_CHG_EVENT_ID | NUMBER |  | 18 | Yes | Foreign key to HRM_PERSON_CHG_EVENTS. |
| PLAN_ID | NUMBER |  | 18 |  | Identifier of the Plan being processed for notification. |
| PLAN_CANDIDATE_ID | NUMBER |  | 18 |  | Identifier of the Plan Candidate record being processed for notification. |
| INCUMBENT_PERSON_ID | NUMBER |  | 18 |  | Identifier of the Plan incumbent being processed for notification. |
| OWNER_PERSON_ID | NUMBER |  | 18 | Yes | Identifier of the person getting succession alert. |
| ALERT_RUN_ID | NUMBER |  | 18 |  | Stores Alert Run ID for the Alert sent to the Owner |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRM_PER_EVT_PLAN_OBJECTS_PK | Unique | Default | PER_EVT_PLAN_OBJECT_ID, ENTERPRISE_ID |

---

[← Back to Index](../24_Succession_Management_Tables_Index.md)
