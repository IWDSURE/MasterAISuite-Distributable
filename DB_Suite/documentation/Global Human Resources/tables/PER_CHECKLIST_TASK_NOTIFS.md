# PER_CHECKLIST_TASK_NOTIFS

PER_CHECKLIST_TASK_NOTIFS : This table has task notifications

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklisttasknotifs-6644.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklisttasknotifs-6644.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_TASK_NOTIFS_PK | TASK_NOTIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_NOTIFICATION_ID | NUMBER |  | 18 | Yes | TASK_NOTIFICATION_ID |
| PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for performer on task assignment. |
| OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for owner on task assignment. |
| EXP_PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for performer on task completion via expiry. |
| EXP_OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for owner on task completion via expiry. |
| REJ_PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for performer on task completion via rejection. |
| REJ_OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for owner on task completion via rejection. |
| FCL_PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for performer on task completion via force close. |
| FCL_OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for owner on task completion via force close. |
| CHECKLIST_TASK_ID | NUMBER |  | 18 | Yes | CHECKLIST_TASK_ID |
| TASK_EVENT | VARCHAR2 | 30 |  | Yes | TASK_EVENT |
| NOTIFY_PERFORMER | VARCHAR2 | 30 |  | Yes | NOTIFY_PERFORMER |
| NOTIFY_OWNER | VARCHAR2 | 30 |  | Yes | NOTIFY_OWNER |
| PERFORMER_CONTENT_TYPE | VARCHAR2 | 30 |  | Yes | PERFORMER_CONTENT_TYPE |
| OWNER_CONTENT_TYPE | VARCHAR2 | 30 |  | Yes | OWNER_CONTENT_TYPE |
| PERFORMER_CONTENT_DEFN_ID | NUMBER |  | 18 |  | PERFORMER_CONTENT_DEFN_ID |
| OWNER_CONTENT_DEFN_ID | NUMBER |  | 18 |  | OWNER_CONTENT_DEFN_ID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHECKLIST_TASK_NOTIFS_N1 | Non Unique | FUSION_TS_TX_DATA | CHECKLIST_TASK_ID |
| PER_CHECKLIST_TASK_NOTIFS_PK | Unique | FUSION_TS_TX_DATA | TASK_NOTIFICATION_ID, ORA_SEED_SET1 |
| PER_CHECKLIST_TASK_NOTIFS_PK1 | Unique | FUSION_TS_TX_DATA | TASK_NOTIFICATION_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
