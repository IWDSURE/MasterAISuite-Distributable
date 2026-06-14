# HXT_TM_MTRX_DLY_ATR_LNKS

This table contains the additional detail entries for the timecard which are mapped against each detail entry. We will link this table with the  HXT_TM_MTRX table via the TM_MTRX_ROW_ID and to denote which detail entry this additional detail belongs to via the DETAIL_ENTRY_DAY Column.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttmmtrxdlyatrlnks-28953.html#hxttmmtrxdlyatrlnks-28953](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttmmtrxdlyatrlnks-28953.html#hxttmmtrxdlyatrlnks-28953)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_TM_MTRX_DLY_ATR_LNKS_PK | TM_MTRX_DLY_ATR_LNK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TM_MTRX_DLY_ATR_LNK_ID | NUMBER |  | 18 | Yes | Primary Key | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |  |
| TM_MTRX_ROW_ID | NUMBER |  | 18 | Yes | Foriegn key to HXT_TM_MTRX table | Active |
| DETAIL_ENTRY_DAY | NUMBER |  | 18 | Yes | Denotes to which day the addition detail belongs to. | Active |
| COMMENTS | VARCHAR2 | 150 |  |  | Detail level comments. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_TM_MTRX_DLY_ATR_LNKS_PK | Unique | Default | TM_MTRX_DLY_ATR_LNK_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
