# WLF_OBJECT_STATS

Table to store details of object (Example Grow,Recommendation.. etc.,) stats.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfobjectstats-13878.html#wlfobjectstats-13878](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfobjectstats-13878.html#wlfobjectstats-13878)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_OBJECT_STATS_PK | OBJECT_STATS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_STATS_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| OBJECT_ID | NUMBER |  | 18 | Yes | The object Id for which stats are calculated and stored. |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | The object type (Example: Grow,REcommendation etc.,) of the object ID |
| STAT_COUNT | NUMBER |  |  |  | Represents count of object Id based on stat type. |
| STAT_TYPE | VARCHAR2 | 30 |  |  | Represents stat type for which stats count is calculated. |
| AVERAGE_STAT_COUNT | NUMBER |  |  |  | Represents aggregate value of stats for stats count |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_OBJECT_STATS_U1 | Unique | Default | OBJECT_STATS_ID |
| WLF_OBJECT_STATS_U2 | Unique | Default | OBJECT_ID, STAT_TYPE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
