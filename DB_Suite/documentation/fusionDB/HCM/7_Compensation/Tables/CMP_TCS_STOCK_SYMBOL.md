# CMP_TCS_STOCK_SYMBOL

Table holds Cmp Tcs Stock Symbol records.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstocksymbol-8019.html#cmptcsstocksymbol-8019](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstocksymbol-8019.html#cmptcsstocksymbol-8019)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STOCK_SYMBOL_PK | STOCK_SYMBOL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STOCK_SYMBOL_ID | NUMBER |  | 18 | Yes | Primary Key |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | Process ID , unique for each process |
| CAT_ID | NUMBER |  | 18 | Yes | Category Id, Foreign key of CMP_TCS_CAT_ID |
| TRADING_SYMBOL | VARCHAR2 | 30 |  |  | Trading Symbol , taken from CMP_TCS_CAT.Trading_STOCK_Symbol , matched with CMS_STOCK_DETAILS.TRADING_STOCK_SYMBOL |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_STOCK_SYMBOL_N1 | Non Unique | Default | PERD_RUN_ID, CAT_ID, TRADING_SYMBOL |
| CMP_TCS_STOCK_SYMBOL_UK1 | Unique | Default | STOCK_SYMBOL_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
