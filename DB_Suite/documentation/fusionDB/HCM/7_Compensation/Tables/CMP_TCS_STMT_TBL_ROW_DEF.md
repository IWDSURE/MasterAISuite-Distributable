# CMP_TCS_STMT_TBL_ROW_DEF

Stores the row details and the item and subcategory details for the summary page section and Category page table. It captures the row details for the item page.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmttblrowdef-16079.html#cmptcsstmttblrowdef-16079](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmttblrowdef-16079.html#cmptcsstmttblrowdef-16079)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STMT_TBL_ROW_DEF_PK | STMT_TBL_ROW_DEF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STMT_TBL_ROW_DEF_ID | NUMBER |  | 18 | Yes | STMT_TBL_ROW_DEF_ID |
| STMT_PERD_ID | NUMBER |  | 18 | Yes | STMT_PERD_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| STMT_PAGE_DEF_ID | NUMBER |  | 18 | Yes | STMT_PAGE_DEF_ID |
| SUBCAT_ID | NUMBER |  | 18 |  | SUBCAT_ID |
| ROW_IN_CAT_ID | NUMBER |  | 18 | Yes | ROW_IN_CAT_ID |
| ORDR_NUM | NUMBER |  | 18 |  | ORDR_NUM |
| URL | VARCHAR2 | 2000 |  |  | URL |
| SUBCAT_HAS_ER_ITEMS_FLAG | VARCHAR2 | 1 |  |  | SUBCAT_HAS_ER_ITEMS_FLAG |
| SUBCAT_HAS_EE_ITEMS_FLAG | VARCHAR2 | 1 |  |  | SUBCAT_HAS_EE_ITEMS_FLAG |
| SUBCAT_CNTRBS_TYPE_CD | VARCHAR2 | 30 |  |  | SUBCAT_CNTRBS_TYPE_CD |
| SUBCAT_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | SUBCAT_NNMNTRY_UOM |
| COLUMN1_ROUNDING_CD | VARCHAR2 | 30 |  |  | COLUMN1_ROUNDING_CD |
| COLUMN1_ITEM_ID | NUMBER |  | 18 |  | COLUMN1_ITEM_ID |
| COLUMN1_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | COLUMN1_NNMNTRY_UOM |
| COLUMN1_ESTIMATED_FLAG | VARCHAR2 | 1 |  |  | COLUMN1_ESTIMATED_FLAG |
| COLUMN2_ROUNDING_CD | VARCHAR2 | 30 |  |  | COLUMN2_ROUNDING_CD |
| COLUMN2_ITEM_ID | NUMBER |  | 18 |  | COLUMN2_ITEM_ID |
| COLUMN2_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | COLUMN2_NNMNTRY_UOM |
| COLUMN2_ESTIMATED_FLAG | VARCHAR2 | 1 |  |  | COLUMN2_ESTIMATED_FLAG |
| COLUMN3_ROUNDING_CD | VARCHAR2 | 30 |  |  | COLUMN3_ROUNDING_CD |
| COLUMN3_ITEM_ID | NUMBER |  | 18 |  | COLUMN3_ITEM_ID |
| COLUMN3_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | COLUMN3_NNMNTRY_UOM |
| COLUMN3_ESTIMATED_FLAG | VARCHAR2 | 1 |  |  | COLUMN3_ESTIMATED_FLAG |
| COLUMN4_ROUNDING_CD | VARCHAR2 | 30 |  |  | COLUMN4_ROUNDING_CD |
| COLUMN4_ITEM_ID | NUMBER |  | 18 |  | COLUMN4_ITEM_ID |
| COLUMN4_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | COLUMN4_NNMNTRY_UOM |
| COLUMN4_ESTIMATED_FLAG | VARCHAR2 | 1 |  |  | COLUMN4_ESTIMATED_FLAG |
| COLUMN5_ROUNDING_CD | VARCHAR2 | 30 |  |  | COLUMN5_ROUNDING_CD |
| COLUMN5_ITEM_ID | NUMBER |  | 18 |  | COLUMN5_ITEM_ID |
| COLUMN5_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | COLUMN5_NNMNTRY_UOM |
| COLUMN5_ESTIMATED_FLAG | VARCHAR2 | 1 |  |  | COLUMN5_ESTIMATED_FLAG |
| ZERO_VALUE_OPTIONS | VARCHAR2 | 30 |  |  | ZERO_VALUE_OPTIONS |
| HIDE_ZERO_ALERT_FLAG | VARCHAR2 | 1 |  |  | HIDE_ZERO_ALERT_FLAG |
| EXCLUDE_FROM_SMRY_FLAG | VARCHAR2 | 1 |  |  | EXCLUDE_FROM_SMRY_FLAG |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| COLUMN1_DATA_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN1_DATA_TYPE_CD |
| COLUMN2_DATA_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN2_DATA_TYPE_CD |
| COLUMN3_DATA_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN3_DATA_TYPE_CD |
| COLUMN4_DATA_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN4_DATA_TYPE_CD |
| COLUMN5_DATA_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN5_DATA_TYPE_CD |
| HISTORY_DATA_FLAG | VARCHAR2 | 1 |  |  | HISTORY_DATA_FLAG |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_STMT_ROW_DEF_UK1 | Unique | Default | STMT_TBL_ROW_DEF_ID |
| CMP_TCS_STMT_TBL_ROW_DEF_N1 | Non Unique | Default | PERD_RUN_ID, ROW_IN_CAT_ID |
| CMP_TCS_STMT_TBL_ROW_DEF_N2 | Non Unique | Default | STMT_PAGE_DEF_ID, PERD_RUN_ID |
| CMP_TCS_STMT_TBL_ROW_DEF_N3 | Non Unique | Default | STMT_TBL_ROW_DEF_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
