# CMP_PLAN_NOTIFICATION_SETTINGS

Stores notification values for a plan.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplannotificationsettings-17002.html#cmpplannotificationsettings-17002](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplannotificationsettings-17002.html#cmpplannotificationsettings-17002)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_PLAN_NOTIFICATION_SET_PK | PLAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| NOTIFY_BUDGET_PUBLISH | VARCHAR2 | 30 |  |  | NOTIFY_BUDGET_PUBLISH |
| NOTIFY_WORK_SUBMIT | VARCHAR2 | 30 |  |  | NOTIFY_WORK_SUBMIT |
| NOTIFY_WORK_REJECT | VARCHAR2 | 30 |  |  | NOTIFY_WORK_REJECT |
| NOTIFY_MANAGER_APPROVAL | VARCHAR2 | 30 |  |  | NOTIFY_MANAGER_APPROVAL |
| NOTIFY_FINAL_APPROVAL | VARCHAR2 | 30 |  |  | NOTIFY_FINAL_APPROVAL |
| NOTIFY_MANAGER_OVERRIDE | VARCHAR2 | 30 |  |  | NOTIFY_MANAGER_OVERRIDE |
| NOTIFY_CHANGE_ACCESS | VARCHAR2 | 30 |  |  | NOTIFY_CHANGE_ACCESS |
| NOTIFY_REASSIGN | VARCHAR2 | 30 |  |  | NOTIFY_REASSIGN |
| NOTIFY_CHANGE_ELIG | VARCHAR2 | 30 |  |  | NOTIFY_CHANGE_ELIG |
| NOTIFY_WORK_RECALL | VARCHAR2 | 30 |  |  | NOTIFY_WORK_RECALL |
| NOTIFY_BUDGET_RECALL | VARCHAR2 | 30 |  |  | NOTIFY_BUDGET_RECALL |
| NOTIFY_WORKER_DELEGATION | VARCHAR2 | 30 |  |  | NOTIFY_WORKER_DELEGATION |
| NOTIFY_RMV_WORKER_DELEGATION | VARCHAR2 | 30 |  |  | NOTIFY_RMV_WORKER_DELEGATION |
| NOTIFY_CHANGE_DUE_DATE | VARCHAR2 | 30 |  |  | NOTIFY_CHANGE_DUE_DATE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_PLAN_NOTIFICATION_SET_U1 | Unique | Default | PLAN_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
