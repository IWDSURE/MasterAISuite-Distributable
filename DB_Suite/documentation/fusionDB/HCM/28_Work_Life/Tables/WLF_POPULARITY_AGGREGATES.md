# WLF_POPULARITY_AGGREGATES

Table to store popular system recommendars aggregation data

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpopularityaggregates-16017.html#wlfpopularityaggregates-16017](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpopularityaggregates-16017.html#wlfpopularityaggregates-16017)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_POPULARITY_AGGREGATE_PK | POPULARITY_AGGREGATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POPULARITY_AGGREGATE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| POPULARITY_CATEGORY | VARCHAR2 | 30 |  | Yes | Specifies popularity category |
| POPULARITY_CATEGORY_ID | NUMBER |  | 18 | Yes | Specifies the identifier for the popularity category. |
| OBJECT_CATEGORY | VARCHAR2 | 30 |  | Yes | Specifies the object category. Corresponds to the lookup code from lookup type WLF_OBJECT_CATEGORY |
| OBJECT_ID | NUMBER |  | 18 | Yes | Identifier of the object (e.g., Learning Item Id, Journey Id etc.,) |
| POPULARITY_EFFECTIVE_DATE | DATE |  |  | Yes | Specifies the effective date of the calculated metrics |
| POPULARITY_COUNT | NUMBER |  | 18 |  | Specifies the total number of object completions for a specified period |
| ESS_JOB_ID | NUMBER |  | 18 |  | Identifier for the ESS Job processing the popularity metrics. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_POPULARITY_AGGREGATES_N1 | Non Unique | Default | POPULARITY_CATEGORY, POPULARITY_CATEGORY_ID |
| WLF_POPULARITY_AGGREGATES_N2 | Non Unique | Default | ESS_JOB_ID |
| WLF_POPULARITY_AGGREGATES_N3 | Non Unique | Default | OBJECT_CATEGORY, OBJECT_ID |
| WLF_POPULARITY_AGGREGATES_U1 | Unique | Default | POPULARITY_AGGREGATE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
