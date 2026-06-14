# PER_ALLOC_TASK_NOTIFS

PER_ALLOC_TASK_NOTIFS : This table has notifications for allocated task

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peralloctasknotifs-18172.html#peralloctasknotifs-18172](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peralloctasknotifs-18172.html#peralloctasknotifs-18172)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ALLOC_TASK_NOTIFS_PK | ALLOC_TASK_NOTIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALLOC_TASK_NOTIFICATION_ID | NUMBER |  | 18 | Yes | Primary Key |
| PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | PERFORMER_TEMPLATE_ID |
| OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for owner on task assignment. |
| EXP_PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for performer on task completion via expiry. |
| EXP_OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for owner on task completion via expiry. |
| REJ_PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for performer on task completion via rejection. |
| REJ_OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for owner on task completion via rejection. |
| FCL_PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for performer on task completion via force close. |
| FCL_OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for owner on task completion via force close. |
| ALLOCATED_TASK_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ALLOCATED_TASKS.ALLOCATED_TASK_ID |
| TASK_NOTIFICATION_ID | NUMBER |  | 18 |  | Foreign Key to PER_TASK_NOTIFICATIONS.TASK_NOTIFICATION_ID |
| TASK_EVENT | VARCHAR2 | 30 |  | Yes | Event on the task
System Lookup: ORA_PER_TASK_EVENTS
ORA_TASK_ASSIGNED - Task assigned
ORA_TASK_COMPLETED - Task completed
ORA_TASK_EXPIRED - Task expired
ORA_TASK_CONTENT_UDPATED - Task details updated
ORA_TASK_DELETED - Task deleted |
| NOTIFY_PERFORMER | VARCHAR2 | 30 |  | Yes | Notify the performer of the task when the task event happens on the task
System Lookup: YES_NO
Y - Yes
N - No |
| NOTIFY_OWNER | VARCHAR2 | 30 |  | Yes | Notify the owner of the task when the task event happens on the task
System Lookup: YES_NO
Y - Yes
N - No |
| PERFORMER_CONTENT_TYPE | VARCHAR2 | 30 |  | Yes | PERFORMER_CONTENT_TYPE |
| OWNER_CONTENT_TYPE | VARCHAR2 | 30 |  | Yes | OWNER_CONTENT_TYPE |
| PERFORMER_CONTENT_DEFN_ID | NUMBER |  | 18 |  | PERFORMER_CONTENT_DEFN_ID |
| OWNER_CONTENT_DEFN_ID | NUMBER |  | 18 |  | OWNER_CONTENT_DEFN_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SYNCH_HISTORY | VARCHAR2 | 4000 |  |  | SYNCH_HISTORY |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ALLOC_TASK_NOTIFS_N1 | Non Unique | FUSION_TS_TX_DATA | ALLOCATED_TASK_ID |
| PER_ALLOC_TASK_NOTIFS_PK | Unique | FUSION_TS_TX_DATA | ALLOC_TASK_NOTIFICATION_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
