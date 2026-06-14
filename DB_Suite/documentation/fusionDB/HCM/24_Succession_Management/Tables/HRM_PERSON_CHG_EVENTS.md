# HRM_PERSON_CHG_EVENTS

This table store the assignment change/delete event for a person, to notify plan owner on effective date.

## Details

**Schema:** FUSION

**Object owner:** HRM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmpersonchgevents-30970.html#hrmpersonchgevents-30970](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmpersonchgevents-30970.html#hrmpersonchgevents-30970)

## Primary Key

| Name | Columns |
|------|----------|
| HRM_PERSON_CHG_EVENTS_PK | PERSON_CHG_EVENT_ID, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_CHG_EVENT_ID | NUMBER |  | 18 | Yes | Person change event id is used to uniquely identify records. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |
| PERSON_ID | NUMBER |  | 18 |  | Person id represents global unique id for the person. |
| OLD_ASSIGNMENT_ID | NUMBER |  | 18 |  | Old Assignment Id of the person. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | New/Existing Assignment Id of the the person. |
| OLD_JOB_ID | NUMBER |  | 18 |  | Old job id column represents the old job id of the person. |
| JOB_ID | NUMBER |  | 18 |  | New/Existing Job ID of the person. |
| OLD_POSITION_ID | NUMBER |  | 18 |  | Old position Id of the the person. |
| POSITION_ID | NUMBER |  | 18 |  | New/Existing position Id of the the person. |
| EFFECTIVE_DATE | DATE |  |  |  | Date on which this change is effective. |
| PROCESSED_DATE | TIMESTAMP |  |  |  | Actual processing date and time on which the Succession Alerts are processed. |
| EVENT_NAME | VARCHAR2 | 64 |  |  | Event name column represent the name of hcm event. |
| EVENT_CREATION_DATE | TIMESTAMP |  |  |  | Event creation date and time on which the event was added to this table. |
| CHANGE_ID | NUMBER |  | 18 |  | Id of the HCM Event created. Foreign key to HRC_EVT_OBJ_CHANGES. |
| STATUS | VARCHAR2 | 64 |  |  | Processing status of the succession notifications. |
| COMMENTS | VARCHAR2 | 4000 |  |  | Processing error or comments of this operation. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRM_PERSON_CHG_EVENTS_PK | Unique | Default | PERSON_CHG_EVENT_ID, ENTERPRISE_ID |

---

[← Back to Index](../24_Succession_Management_Tables_Index.md)
