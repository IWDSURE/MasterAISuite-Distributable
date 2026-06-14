# HRC_ALERT_RUN_FILTERS_DATA

Stores alert filters data  for a run.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunfiltersdata-9891.html#hrcalertrunfiltersdata-9891](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunfiltersdata-9891.html#hrcalertrunfiltersdata-9891)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERT_RUN_FILTERS_DATA_PK | FILTER_DATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FILTER_DATA_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| RUN_ID | NUMBER |  | 18 | Yes | Run Identifier. Foreign Key to HRC_ALERTS_RUNS.RUN_ID |
| FILTER_DATA_SURROGATE_ID | NUMBER |  | 18 |  | Key identifier of the Node data |
| FILTER_DATA_LANG | VARCHAR2 | 8 |  | Yes | Node data (i.e Json node) retrieved language |
| FILTER_DATA | CLOB |  |  |  | Node data (i.e Json node) |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CHUNK_NUM | NUMBER |  | 18 |  | Chunk Number |
| RANGE_INDEX | NUMBER |  | 18 |  | Stores the Range Index. |
| RUN_RANGE_ID | NUMBER |  | 18 |  | Run Range Identifier. Foreign Key to HRC_ALERT_RUN_RANGES.RUN_RANGE_ID |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ALERT_RUN_FILTERS_DATA_N1 | Non Unique | Default | RUN_ID, FILTER_DATA_SURROGATE_ID, FILTER_DATA_LANG, CHUNK_NUM |
| HRC_ALERT_RUN_FILTERS_DATA_PK | Unique | Default | FILTER_DATA_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
