# BEN_WORK_PATTERN

BEN_WORK_PATTERN identifies  default work pattern.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benworkpattern-18181.html#benworkpattern-18181](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benworkpattern-18181.html#benworkpattern-18181)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_WORK_PATTERN_PK | WORK_PATTERN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORK_PATTERN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| WORK_PATTERN_NAME | VARCHAR2 | 30 |  | Yes | Name of work pattern. |
| START_DAY | VARCHAR2 | 30 |  | Yes | Identifies starting day of the work pattern. |
| TOTAL_NUMBER_OF_DAYS | NUMBER |  |  | Yes | Identifies total number of days in the work pattern. |
| AVERAGE_WORKING_DAYS | NUMBER |  |  | Yes | Identifies average working days in the work pattern. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_WORK_PATTERN_PK | Unique | FUSION_TS_TX_DATA | WORK_PATTERN_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
