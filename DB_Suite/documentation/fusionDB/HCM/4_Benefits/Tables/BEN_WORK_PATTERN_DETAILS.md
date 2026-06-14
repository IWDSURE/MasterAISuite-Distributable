# BEN_WORK_PATTERN_DETAILS

BEN_WORK_PATTERN_DETAILS identifies work pattern details.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benworkpatterndetails-31268.html#benworkpatterndetails-31268](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benworkpatterndetails-31268.html#benworkpatterndetails-31268)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_WORK_PATTERN_DETAILS_PK | WORK_PATTERN_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORK_PATTERN_DETAIL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| WORK_PATTERN_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_WORK_PATTERN.WORK_PATTERN_ID. |
| WP_SEQUENCE | NUMBER |  | 18 | Yes | Order the days used to process. |
| DAY_INFO | VARCHAR2 | 30 |  | Yes | Identifies days in the pattern. |
| VALUE | NUMBER |  |  | Yes | Identifies duration of the day. |
| WP_UOM | VARCHAR2 | 30 |  | Yes | Unit of measure for work pattern. Day, hours etc. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_WORK_PATTERN_DET_PK | Unique | FUSION_TS_TX_DATA | WORK_PATTERN_DETAIL_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
