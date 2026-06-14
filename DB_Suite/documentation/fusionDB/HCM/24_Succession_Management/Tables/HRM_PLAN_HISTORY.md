# HRM_PLAN_HISTORY

Plan history table stores the history records of the plan. It contains history data with old and new values.

## Details

**Schema:** FUSION

**Object owner:** HRM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplanhistory-23879.html#hrmplanhistory-23879](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplanhistory-23879.html#hrmplanhistory-23879)

## Primary Key

| Name | Columns |
|------|----------|
| HRM_PLAN_HISTORY_PK | PLAN_HISTORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_HISTORY_ID | NUMBER |  | 18 | Yes | Plan history id uniquely represents the plan history row. |
| PLAN_ID | NUMBER |  | 18 | Yes | Plan id represents the primary key for plan. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise id represents enterprise id for the plan. |
| MODIFIED_DATE | TIMESTAMP |  |  | Yes | modified date represents the date on which this change is committed. |
| MODIFIED_BY | NUMBER |  | 18 | Yes | modified by represents the person id who made this change. |
| MODIFIED_COLUMN | VARCHAR2 | 40 |  |  | Modified column represents the name of modified column. |
| OLD_VALUE | VARCHAR2 | 4000 |  |  | Old value represents the old value of what changed attribute. |
| NEW_VALUE | VARCHAR2 | 4000 |  |  | New value represents the new value of what changed attribute. |
| OPERATION_TYPE | VARCHAR2 | 20 |  | Yes | Operation type represents the type of operation committed. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRM_PLAN_HISTORY_N1 | Non Unique | HRM_PLAN_HISTORY_N1 | PLAN_ID |
| HRM_PLAN_HISTORY_N2 | Non Unique | HRM_PLAN_HISTORY_N2 | MODIFIED_DATE |
| HRM_PLAN_HISTORY_PK | Unique | Default | PLAN_HISTORY_ID |

---

[← Back to Index](../24_Succession_Management_Tables_Index.md)
