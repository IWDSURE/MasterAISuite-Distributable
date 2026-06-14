# CMP_TCS_ITEM_CALC_LIST

This object stores the information ablout the calcualted item's expression items

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsitemcalclist-7580.html#cmptcsitemcalclist-7580](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsitemcalclist-7580.html#cmptcsitemcalclist-7580)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_ITEM_CALC_LIST_PK | ITEM_CALC_LIST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ITEM_CALC_LIST_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| ITEM_ID | NUMBER |  | 18 | Yes | Foreign key of calculated item |
| CALC_ITEM_ID | NUMBER |  | 18 |  | Foreign key of calculated item |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_ITEM_CALC_LIST_N1 | Non Unique | Default | ITEM_ID |
| CMP_TCS_ITEM_CALC_LIST_N2 | Non Unique | Default | CALC_ITEM_ID |
| CMP_TCS_ITEM_CALC_LIST_U1 | Unique | Default | ITEM_CALC_LIST_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
