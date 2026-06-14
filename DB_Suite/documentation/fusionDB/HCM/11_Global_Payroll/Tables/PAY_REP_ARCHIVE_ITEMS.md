# PAY_REP_ARCHIVE_ITEMS

Archive table which holds parameter value information for a relationship action

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payreparchiveitems-8961.html#payreparchiveitems-8961](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payreparchiveitems-8961.html#payreparchiveitems-8961)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REP_ARCHIVE_ITEMS_PK | REP_ARCHIVE_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REP_ARCHIVE_ITEM_ID | NUMBER |  | 18 | Yes | REP_ARCHIVE_ITEM_ID |
| ARCHIVE_TYPE | VARCHAR2 | 10 |  | Yes | ARCHIVE_TYPE |
| CONTEXT | NUMBER |  | 18 | Yes | CONTEXT |
| NAME | VARCHAR2 | 240 |  |  | NAME |
| VALUE | VARCHAR2 | 240 |  | Yes | VALUE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_REP_ARCHIVE_ITEMS_N1 | Non Unique | Default | CONTEXT |
| PAY_REP_ARCHIVE_ITEMS_PK | Unique | Default | REP_ARCHIVE_ITEM_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
