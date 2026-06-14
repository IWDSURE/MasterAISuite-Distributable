# HRG_PERF_CYCLES_TL

Performance Management cycle translation table

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSIONTS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgperfcyclestl-16207.html#hrgperfcyclestl-16207](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgperfcyclestl-16207.html#hrgperfcyclestl-16207)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_PERF_CYCLES_TL_PK | PERF_CYCLE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERF_CYCLE_ID | NUMBER |  | 18 | Yes | Primary key to Performance Management Cycle |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| PERF_CYCLE_NAME | VARCHAR2 | 400 |  | Yes | Performance Management CYCLE name |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRG_PERF_CYCLES_TL_FK1 | Non Unique | Default | PERF_CYCLE_ID | Obsolete |
| HRG_PERF_CYCLES_TL_N1 | Non Unique | DEFAULT | PERF_CYCLE_NAME |  |
| HRG_PERF_CYCLES_TL_PK | Unique | DEFAULT | PERF_CYCLE_ID, LANGUAGE |  |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
