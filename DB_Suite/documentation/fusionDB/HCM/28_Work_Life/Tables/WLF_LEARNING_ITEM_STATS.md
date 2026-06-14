# WLF_LEARNING_ITEM_STATS

Table to store all the stats for a learningItem

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearningitemstats-3363.html#wlflearningitemstats-3363](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearningitemstats-3363.html#wlflearningitemstats-3363)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LEARNING_ITEM_STATS_PK | LEARNING_ITEM_STATS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LEARNING_ITEM_STATS_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | Learning ItemId for which stats are calculated |
| STAT_COUNT | NUMBER |  |  |  | Represents count of view , ratings etc |
| AVERAGE_STAT_COUNT | NUMBER |  |  |  | Aggregate value of stats |
| STAT_TYPE | VARCHAR2 | 32 |  |  | Discriminator for stas type |
| CREATED_BY_ID | NUMBER |  | 18 | Yes | Indicates the person identifier who created the content object. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LEARNING_ITEM_STATS_N1 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_LEARNING_ITEM_STATS_U1 | Unique | Default | LEARNING_ITEM_STATS_ID |
| WLF_LEARNING_ITEM_STATS_U2 | Unique | Default | STAT_TYPE, LEARNING_ITEM_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
