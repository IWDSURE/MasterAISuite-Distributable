# PER_TASK_NOTIFICATIONS_

PER_TASK_NOTIFICATIONS : This table has task notifications

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pertasknotifications-11347.html#pertasknotifications-11347](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pertasknotifications-11347.html#pertasknotifications-11347)

## Primary Key

| Name | Columns |
|------|----------|
| PER_TASK_NOTIFICATIONS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, TASK_NOTIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_NOTIFICATION_ID | NUMBER |  | 18 | Yes | TASK_NOTIFICATION_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | SGUID |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | OBSOLETE_FLAG |
| PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for performer on task assignment. |
| OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for owner on task assignment. |
| EXP_PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for performer on task completion via expiry. |
| EXP_OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for owner on task completion via expiry. |
| REJ_PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for performer on task completion via rejection. |
| REJ_OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for owner on task completion via rejection. |
| FCL_PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for performer on task completion via force close. |
| FCL_OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for owner on task completion via force close. |
| TASK_IN_CHECKLIST_ID | NUMBER |  | 18 |  | TASK_IN_CHECKLIST_ID |
| TASK_EVENT | VARCHAR2 | 30 |  |  | TASK_EVENT |
| NOTIFY_PERFORMER | VARCHAR2 | 30 |  |  | NOTIFY_PERFORMER |
| NOTIFY_OWNER | VARCHAR2 | 30 |  |  | NOTIFY_OWNER |
| PERFORMER_CONTENT_TYPE | VARCHAR2 | 30 |  |  | PERFORMER_CONTENT_TYPE |
| OWNER_CONTENT_TYPE | VARCHAR2 | 30 |  |  | OWNER_CONTENT_TYPE |
| PERFORMER_CONTENT_DEFN_ID | NUMBER |  | 18 |  | PERFORMER_CONTENT_DEFN_ID |
| OWNER_CONTENT_DEFN_ID | NUMBER |  | 18 |  | OWNER_CONTENT_DEFN_ID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
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
| PER_TASK_NOTIFICATIONSN1_ | Non Unique | Default | TASK_NOTIFICATION_ID, LAST_UPDATE_DATE |
| PER_TASK_NOTIFICATIONS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, TASK_NOTIFICATION_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
