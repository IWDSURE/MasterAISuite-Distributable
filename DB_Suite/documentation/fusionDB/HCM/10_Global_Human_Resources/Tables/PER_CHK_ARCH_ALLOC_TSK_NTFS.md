# PER_CHK_ARCH_ALLOC_TSK_NTFS

Archive table for task notifications

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkarchalloctskntfs-14596.html#perchkarchalloctskntfs-14596](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkarchalloctskntfs-14596.html#perchkarchalloctskntfs-14596)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_ARCH_ALLOC_TSK_NTFS_PK | ALLOC_TASK_NOTIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALLOC_TASK_NOTIFICATION_ID | NUMBER |  | 18 | Yes | ALLOC_TASK_NOTIFICATION_ID |
| PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | PERFORMER_TEMPLATE_ID |
| OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | OWNER_TEMPLATE_ID |
| EXP_PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | EXP_PERFORMER_TEMPLATE_ID |
| EXP_OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | EXP_OWNER_TEMPLATE_ID |
| REJ_PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | REJ_PERFORMER_TEMPLATE_ID |
| REJ_OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | REJ_OWNER_TEMPLATE_ID |
| FCL_PERFORMER_TEMPLATE_ID | NUMBER |  | 18 |  | FCL_PERFORMER_TEMPLATE_ID |
| FCL_OWNER_TEMPLATE_ID | NUMBER |  | 18 |  | FCL_OWNER_TEMPLATE_ID |
| ALLOCATED_TASK_ID | NUMBER |  | 18 | Yes | ALLOCATED_TASK_ID |
| TASK_NOTIFICATION_ID | NUMBER |  | 18 |  | TASK_NOTIFICATION_ID |
| TASK_EVENT | VARCHAR2 | 30 |  | Yes | TASK_EVENT |
| NOTIFY_PERFORMER | VARCHAR2 | 30 |  | Yes | NOTIFY_PERFORMER |
| NOTIFY_OWNER | VARCHAR2 | 30 |  | Yes | NOTIFY_OWNER |
| PERFORMER_CONTENT_TYPE | VARCHAR2 | 30 |  |  | PERFORMER_CONTENT_TYPE |
| OWNER_CONTENT_TYPE | VARCHAR2 | 30 |  |  | OWNER_CONTENT_TYPE |
| PERFORMER_CONTENT_DEFN_ID | NUMBER |  | 18 |  | PERFORMER_CONTENT_DEFN_ID |
| OWNER_CONTENT_DEFN_ID | NUMBER |  | 18 |  | OWNER_CONTENT_DEFN_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
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
| PER_CHK_ARCH_ALLOC_TSK_NTFS_PK | Unique | Default | ALLOC_TASK_NOTIFICATION_ID |
| PER_CHK_ARCH_ALLOC_TSK_NTFS_N1 | Non Unique | Default | ALLOCATED_TASK_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
