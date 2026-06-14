# CEL_FEED_SUMMARY

Stores feed summary data for rewards and recognition programs.

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celfeedsummary-5615.html#celfeedsummary-5615](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celfeedsummary-5615.html#celfeedsummary-5615)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_FEED_SUMMARY_PK | SUMMARY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUMMARY_ID | NUMBER |  | 18 | Yes | Unique identifier for summary record |
| PROGRAM_ID | NUMBER |  | 18 | Yes | Program identifier |
| MAIN_OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Main Object type |
| MAIN_OBJECT_KEY | NUMBER |  | 18 | Yes | Main Object key |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Type of object |
| OBJECT_KEY | NUMBER |  | 18 | Yes | Key of object |
| SUMMARY_TYPE | VARCHAR2 | 30 |  | Yes | Summary type |
| PRIMARY_FLAG | VARCHAR2 | 1 |  |  | Primary flag |
| COUNT_DIRECT | NUMBER |  | 18 |  | Direct count |
| COUNT_ALL | NUMBER |  | 18 |  | All count |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_FEED_SUMMARY_N1 | Non Unique | Default | OBJECT_TYPE, OBJECT_KEY, SUMMARY_TYPE |
| CEL_FEED_SUMMARY_N2 | Non Unique | Default | MAIN_OBJECT_TYPE, MAIN_OBJECT_KEY, PRIMARY_FLAG |
| CEL_FEED_SUMMARY_PK | Unique | Default | SUMMARY_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
