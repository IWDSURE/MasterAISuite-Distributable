# CMP_CSTM_REGION_ITEMS_B

Stores setup information for regional customization

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcstmregionitemsb-13270.html#cmpcstmregionitemsb-13270](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcstmregionitemsb-13270.html#cmpcstmregionitemsb-13270)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CSTM_REGION_ITEMS_B_PK | CUSTOM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CUSTOM_ID | NUMBER |  | 18 | Yes | CUSTOM_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| CUSTOM_TYPE | VARCHAR2 | 30 |  | Yes | CUSTOM_TYPE |
| CUSTOM_KEY | NUMBER |  | 18 | Yes | CUSTOM_KEY |
| REGION_NAME | VARCHAR2 | 60 |  | Yes | REGION_NAME |
| ITEM_NAME | VARCHAR2 | 60 |  | Yes | ITEM_NAME |
| DISPLAY_FLAG | VARCHAR2 | 1 |  |  | DISPLAY_FLAG |
| UPDATE_ALLOWED_FLAG | VARCHAR2 | 1 |  |  | UPDATE_ALLOWED_FLAG |
| ORDER_NUM | NUMBER |  |  |  | ORDER_NUM |
| SYSTEM_ORDER_NUM | NUMBER |  |  |  | SYSTEM_ORDER_NUM |
| COLUMN_BANDING | VARCHAR2 | 30 |  |  | COLUMN_BANDING |
| INITIALLY_HIDDEN_FLAG | VARCHAR2 | 1 |  |  | INITIALLY_HIDDEN_FLAG |
| OVERRIDE_CODE | VARCHAR2 | 30 |  |  | OVERRIDE_CODE |
| CONDITION_TYPE_CODE | VARCHAR2 | 30 |  |  | CONDITION_TYPE_CODE |
| WRAP_TEXT_FLAG | VARCHAR2 | 1 |  |  | WRAP_TEXT_FLAG |
| COLUMN_WIDTH | NUMBER |  |  |  | COLUMN_WIDTH |
| COLUMN_SHADE_CODE | VARCHAR2 | 30 |  |  | COLUMN_SHADE_CODE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| UPDATE_IN_WORKBOOK_FLAG | VARCHAR2 | 1 |  |  | UPDATE_IN_WORKBOOK_FLAG |
| UPDATE_COND_CODE | VARCHAR2 | 30 |  |  | UPDATE_COND_CODE |
| HIDE_VIEW_PRINT_ICON_FLAG | VARCHAR2 | 1 |  |  | HIDE_VIEW_PRINT_ICON_FLAG |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CSTM_REGION_ITEMS_B_N1 | Non Unique | Default | CUSTOM_TYPE, CUSTOM_KEY, REGION_NAME, ITEM_NAME |
| CMP_CSTM_REGION_ITEMS_B_N2 | Non Unique | Default | CUSTOM_KEY, CUSTOM_TYPE, REGION_NAME |
| CMP_CSTM_REGION_ITEMS_B_UK1 | Unique | Default | CUSTOM_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
