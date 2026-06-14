# PAY_ARCHIVE_ITEMS

Archive table which holds individual items of data to allow archive retrieval via database items

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payarchiveitems-18402.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payarchiveitems-18402.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ARCHIVE_ITEMS_PK | ARCHIVE_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ARCHIVE_ITEM_ID | NUMBER |  | 18 | Yes | ARCHIVE_ITEM_ID |
| ARCHIVE_TYPE | VARCHAR2 | 10 |  | Yes | ARCHIVE_TYPE |
| CONTEXT1 | NUMBER |  | 18 | Yes | CONTEXT1 |
| NAME | VARCHAR2 | 240 |  |  | NAME |
| VALUE | VARCHAR2 | 240 |  |  | VALUE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ARCHIVE_ITEMS_PK | Unique | Default | ARCHIVE_ITEM_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
