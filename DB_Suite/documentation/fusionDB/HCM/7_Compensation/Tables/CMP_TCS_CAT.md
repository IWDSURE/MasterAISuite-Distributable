# CMP_TCS_CAT

Setup Table that stores the Category Details.Captures Category Name, Category Type Code, Contribution Type, Unit of measure, Drill down Options, number of columns, additional information, description text, graph details, display order of components.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcscat-28055.html#cmptcscat-28055](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcscat-28055.html#cmptcscat-28055)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_CAT_PK | CAT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CAT_ID | NUMBER |  | 18 | Yes | System generated primary key column. | Active |
| NAME | VARCHAR2 | 240 |  |  | NAME |  |
| STOCK_GRANT_TYPE_CD | VARCHAR2 | 250 |  |  | STOCK_GRANT_TYPE_CD | Active |
| CAT_TYPE_CD | VARCHAR2 | 30 |  | Yes | Category Type Code | Active |
| STAT_CD | VARCHAR2 | 30 |  | Yes | STAT_CD | Active |
| CONTRIBUTIONS_TYPE_CD | VARCHAR2 | 30 |  |  | Compensation Type | Active |
| NNMNTRY_UOM | VARCHAR2 | 30 |  |  | Nonmonetary Code for Nonmonetary Compensation Category | Active |
| NUMBER_OF_COLUMNS | NUMBER |  | 18 |  | Number of custom columns in the category | Active |
| HIDE_ADDL_INFO_FLAG | VARCHAR2 | 1 |  |  | HIDE_ADDL_INFO_FLAG | Active |
| HIDE_DESC_TXT_FLAG | VARCHAR2 | 1 |  |  | HIDE_DESC_TXT_FLAG | Active |
| DESC_TXT_ORDR_NUM | NUMBER |  | 18 |  | DESC_TXT_ORDR_NUM | Active |
| CHART1_TYPE_CD | VARCHAR2 | 30 |  |  | CHART1_TYPE_CD | Active |
| CHART2_TYPE_CD | VARCHAR2 | 30 |  |  | CHART2_TYPE_CD | Active |
| CHART2_TITLE | VARCHAR2 | 240 |  |  | CHART2_TITLE | Active |
| HIDE_CHART_RN_FLAG | VARCHAR2 | 1 |  |  | HIDE_CHART_RN_FLAG | Active |
| HIDE_TABLE_FLAG | VARCHAR2 | 1 |  |  | Dispaly category without table region. |  |
| CHART_RN_ORDR_NUM | NUMBER |  | 18 |  | CHART_RN_ORDR_NUM | Active |
| TABLE_ORDR_NUM | NUMBER |  | 18 |  | TABLE_ORDR_NUM | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| LEVEL_OF_DETAIL | VARCHAR2 | 30 |  |  | LEVEL_OF_DETAIL | Active |
| STOCK_TRADING_SYMBOL | VARCHAR2 | 30 |  |  | STOCK_TRADING_SYMBOL | Active |
| HISTORY_DATA_FLAG | VARCHAR2 | 1 |  |  | HISTORY_DATA_FLAG | Active |
| VALID_CHART1_FLAG | VARCHAR2 | 1 |  |  | VALID_CHART1_FLAG |  |
| VALID_CHART2_FLAG | VARCHAR2 | 1 |  |  | VALID_CHART2_FLAG |  |
| HIDE_PDF_ITEM_DETAILS_CD | VARCHAR2 | 30 |  |  | Setup Option to configure the display of line item details section in PDF |  |
| HIDE_OL_ITEM_DETAILS_CD | VARCHAR2 | 30 |  |  | Setup Option to configure the display of line item details section in Online Statement |  |
| HIDE_CALC_STOCK_BTN_FLAG | VARCHAR2 | 1 |  |  | Option to control the visibility of Calculate Stock Value button in Stock History category |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_CAT_N1 | Non Unique | Default | CAT_TYPE_CD |
| CMP_TCS_CAT_N2 | Non Unique | Default | CONTRIBUTIONS_TYPE_CD |
| CMP_TCS_CAT_N3 | Non Unique | Default | STAT_CD |
| CMP_TCS_CAT_UK1 | Unique | Default | CAT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
