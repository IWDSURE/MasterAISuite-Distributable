# HRC_LOADER_STATS

This table contains statistics about Fusion data objects used during a data load.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloaderstats-9814.html#hrcloaderstats-9814](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloaderstats-9814.html#hrcloaderstats-9814)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_LOADER_STATS_PK | STAT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STAT_ID | NUMBER |  | 18 | Yes | Primary Key |
| BO_IGNORED_OBJECTS | NUMBER |  | 9 |  | Ignored Objects |
| BO_IGNORED_RECORDS | NUMBER |  | 9 |  | Ignored Records |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LOADER_BATCH_ID | NUMBER |  | 18 |  | Identifies a batch (header) |
| METADATA_ID | NUMBER |  | 18 |  | Identifies the corresponding top level object metadata definition |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| BO_CURRENT_LEVEL | NUMBER |  | 9 |  | Object current level |
| BO_LEVEL_NAME | VARCHAR2 | 200 |  |  | Object level name |
| BO_LEVEL_NAME_CONCAT | VARCHAR2 | 2010 |  |  | Concatenation of object level names separated by a separator |
| PARENT_STAT_ID | NUMBER |  | 18 |  | Identifies if parent stat id for this object |
| BO_TOTAL_OBJECTS | NUMBER |  | 9 |  | total number of objects count |
| BO_SUCCESSFUL_OBJECTS | NUMBER |  | 9 |  | total number of successful objects |
| BO_FAILED_OBJECTS | NUMBER |  | 9 |  | total number of failed objects |
| BO_PENDING_OBJECTS | NUMBER |  | 9 |  | total number of pending objects |
| BO_TOTAL_RECORDS | NUMBER |  | 9 |  | total number of physical  records |
| BO_SUCCESSFUL_RECORDS | NUMBER |  | 9 |  | total number of successful physical  records |
| BO_FAILED_RECORDS | NUMBER |  | 9 |  | total number of failed  physical  records |
| BO_PENDING_RECORDS | NUMBER |  | 9 |  | total number of pending physical  records |
| IMPEXP_TOTAL_OBJECTS | NUMBER |  | 9 |  | total number of import or export objects |
| IMPEXP_FAILED_OBJECTS | NUMBER |  | 9 |  | total number of failed import or export objects |
| IMPEXP_TOTAL_RECORDS | NUMBER |  | 9 |  | total number of import or export physical records |
| IMPEXP_FAILED_RECORDS | NUMBER |  | 9 |  | total number of import or export failed physical records |
| BO_CHANGED_OBJECTS | NUMBER |  | 9 |  | Changed Objects |
| BO_CHANGED_RECORDS | NUMBER |  | 9 |  | Changed Records |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_LOADER_STATS_N1 | Non Unique | Default | PARENT_STAT_ID |
| HRC_LOADER_STATS_N2 | Non Unique | Default | LOADER_BATCH_ID, REQUEST_ID, METADATA_ID |
| HRC_LOADER_STATS_N3 | Non Unique | Default | LOADER_BATCH_ID, BO_CURRENT_LEVEL |
| HRC_LOADER_STATS_PK | Unique | Default | STAT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
