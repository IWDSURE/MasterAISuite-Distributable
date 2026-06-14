# CMP_TCS_STOCK_GRANT_TYPES

Table holds Cmp Tcs Stock Grant Types records.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstockgranttypes-21496.html#cmptcsstockgranttypes-21496](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstockgranttypes-21496.html#cmptcsstockgranttypes-21496)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STOCK_GRANT_TYPES_PK | STOCK_GRANT_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STOCK_GRANT_TYPE_ID | NUMBER |  | 18 | Yes | STOCK_GRANT_TYPE_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PERD_RUN_ID | NUMBER |  | 18 |  | PERD_RUN_ID |
| CAT_ID | NUMBER |  | 18 |  | CAT_ID |
| STOCK_GRANT_TYPE_CD | VARCHAR2 | 30 |  |  | STOCK_GRANT_TYPE_CD |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_STOCK_GRANT_TYPES_N1 | Non Unique | Default | PERD_RUN_ID, CAT_ID, STOCK_GRANT_TYPE_CD |
| CMP_TCS_STOCK_GRANT_TYPES_UK1 | Unique | Default | STOCK_GRANT_TYPE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
