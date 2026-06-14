# WLF_LRN_ASSIGN_STATS_BY_CATG

This table stores the assignment stats by learner and category

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflrnassignstatsbycatg-16777.html#wlflrnassignstatsbycatg-16777](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflrnassignstatsbycatg-16777.html#wlflrnassignstatsbycatg-16777)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LRN_ASSIGN_STATS_BY_C_PK | LRN_ASSIGN_STATS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LRN_ASSIGN_STATS_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| CATEGORY_ID | NUMBER |  | 18 | Yes | This column stores the category id |
| LEARNER_ID | NUMBER |  | 18 | Yes | This column stores the learner id |
| ASSIGN_COUNT | NUMBER |  | 18 |  | This column stores total number of assignments for the category |
| ACTIVE_ASSIGN_COUNT | NUMBER |  | 18 |  | This column stores total number of active assignments for the category |
| WITHDRAWN_ASSIGN_COUNT | NUMBER |  | 18 |  | This column stores total number of assignments in withdrawn status for the category |
| LAST_STAT_GATHERED_DATE | TIMESTAMP |  |  |  | This column stores the date and time of last time stat was gathered |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LRN_ASSIGN_STATS_BY_C_N1 | Non Unique | Default | CATEGORY_ID, LEARNER_ID |
| WLF_LRN_ASSIGN_STATS_BY_C_U1 | Unique | Default | LRN_ASSIGN_STATS_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
