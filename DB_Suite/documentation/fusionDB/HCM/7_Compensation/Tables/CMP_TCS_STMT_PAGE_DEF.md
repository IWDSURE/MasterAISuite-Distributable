# CMP_TCS_STMT_PAGE_DEF

Stores the following details for the category page, summary page and summary page section: description, page title, additional information, graph and the table column details.
For item page the table column details are stored with the item_detail_flag set to Y with the cat_id as the parent category id.
For Summary page sections the cat_type_cd is set to MNTRY_SECT or NNMNTRY_SECT and SMRY to Summary page details.
For Categories the Cat_Type_cd is set to the category type and the cat_id indicates the category id.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtpagedef-17985.html#cmptcsstmtpagedef-17985](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtpagedef-17985.html#cmptcsstmtpagedef-17985)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STMT_PAGE_DEF_PK | STMT_PAGE_DEF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STMT_PAGE_DEF_ID | NUMBER |  | 18 | Yes | STMT_PAGE_DEF_ID |
| HIDE_CALC_STOCK_BTN_FLAG | VARCHAR2 | 1 |  |  | Option to hide Calculate Stock Value button in Stock History category |
| STMT_PERD_ID | NUMBER |  | 18 | Yes | STMT_PERD_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| CAT_ID | NUMBER |  | 18 |  | CAT_ID |
| CAT_TYPE_CD | VARCHAR2 | 30 |  |  | CAT_TYPE_CD |
| CONTRIBUTIONS_TYPE_CD | VARCHAR2 | 30 |  |  | CONTRIBUTIONS_TYPE_CD |
| NNMNTRY_UOM | VARCHAR2 | 30 |  |  | NNMNTRY_UOM |
| HIDE_DESC_TXT_FLAG | VARCHAR2 | 1 |  |  | HIDE_DESC_TXT_FLAG |
| DESC_TXT_ORDR_NUM | NUMBER |  | 18 |  | DESC_TXT_ORDR_NUM |
| HIDE_ADDL_INFO_FLAG | VARCHAR2 | 1 |  |  | HIDE_ADDL_INFO_FLAG |
| CHART1_TYPE_CD | VARCHAR2 | 30 |  |  | CHART1_TYPE_CD |
| CHART2_TYPE_CD | VARCHAR2 | 30 |  |  | CHART2_TYPE_CD |
| HIDE_CHART_RN_FLAG | VARCHAR2 | 1 |  |  | HIDE_CHART_RN_FLAG |
| CHART_RN_ORDR_NUM | NUMBER |  | 18 |  | CHART_RN_ORDR_NUM |
| HIDE_TABLE_FLAG | VARCHAR2 | 1 |  |  | Flag to determine whether Details table should be displayed ina category page or not |
| TABLE_ORDR_NUM | NUMBER |  | 18 |  | TABLE_ORDR_NUM |
| DISPLAY_NAME_ORDR_NUM | NUMBER |  | 18 |  | DISPLAY_NAME_ORDR_NUM |
| DESC_COLUMN_HIDE_FLAG | VARCHAR2 | 1 |  |  | DESC_COLUMN_HIDE_FLAG |
| DESC_COLUMN_ORDR_NUM | NUMBER |  | 18 |  | DESC_COLUMN_ORDR_NUM |
| DATE_COLUMN_ORDR_NUM | NUMBER |  | 18 |  | DATE_COLUMN_ORDR_NUM |
| JOB_COLUMN_ORDR_NUM | NUMBER |  | 18 |  | JOB_COLUMN_ORDR_NUM |
| COLUMN1_COLUMN_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN1_COLUMN_TYPE_CD |
| COLUMN1_DATA_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN1_DATA_TYPE_CD |
| COLUMN1_CONTRBR_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN1_CONTRBR_TYPE_CD |
| COLUMN1_HIDE_FLAG | VARCHAR2 | 1 |  |  | COLUMN1_HIDE_FLAG |
| COLUMN1_ORDR_NUM | NUMBER |  | 18 |  | COLUMN1_ORDR_NUM |
| COLUMN2_COLUMN_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN2_COLUMN_TYPE_CD |
| COLUMN2_DATA_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN2_DATA_TYPE_CD |
| COLUMN2_CONTRBR_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN2_CONTRBR_TYPE_CD |
| COLUMN2_HIDE_FLAG | VARCHAR2 | 1 |  |  | COLUMN2_HIDE_FLAG |
| COLUMN2_ORDR_NUM | NUMBER |  | 18 |  | COLUMN2_ORDR_NUM |
| COLUMN3_COLUMN_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN3_COLUMN_TYPE_CD |
| COLUMN3_DATA_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN3_DATA_TYPE_CD |
| COLUMN3_CONTRBR_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN3_CONTRBR_TYPE_CD |
| COLUMN3_HIDE_FLAG | VARCHAR2 | 1 |  |  | COLUMN3_HIDE_FLAG |
| COLUMN3_ORDR_NUM | NUMBER |  | 18 |  | COLUMN3_ORDR_NUM |
| COLUMN4_COLUMN_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN4_COLUMN_TYPE_CD |
| COLUMN4_DATA_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN4_DATA_TYPE_CD |
| COLUMN4_CONTRBR_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN4_CONTRBR_TYPE_CD |
| COLUMN4_HIDE_FLAG | VARCHAR2 | 1 |  |  | COLUMN4_HIDE_FLAG |
| COLUMN4_ORDR_NUM | NUMBER |  | 18 |  | COLUMN4_ORDR_NUM |
| COLUMN5_COLUMN_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN5_COLUMN_TYPE_CD |
| COLUMN5_DATA_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN5_DATA_TYPE_CD |
| COLUMN5_CONTRBR_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN5_CONTRBR_TYPE_CD |
| COLUMN5_HIDE_FLAG | VARCHAR2 | 1 |  |  | COLUMN5_HIDE_FLAG |
| COLUMN5_ORDR_NUM | NUMBER |  | 18 |  | COLUMN5_ORDR_NUM |
| HIDE_SMRY_FLAG | VARCHAR2 | 1 |  |  | HIDE_SMRY_FLAG |
| MNTRY_SECT_ORDR_NUM | NUMBER |  | 18 |  | MNTRY_SECT_ORDR_NUM |
| NNMNTRY_SECT_ORDR_NUM | NUMBER |  | 18 |  | NNMNTRY_SECT_ORDR_NUM |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LEVEL_OF_DETAIL | VARCHAR2 | 30 |  |  | LEVEL_OF_DETAIL |
| SUBCAT_IN_ROW_FLAG | VARCHAR2 | 1 |  |  | SUBCAT_IN_ROW_FLAG |
| COLUMN1_IN_CHART1_FLAG | VARCHAR2 | 1 |  |  | COLUMN1_IN_CHART1_FLAG |
| COLUMN1_IN_CHART2_FLAG | VARCHAR2 | 1 |  |  | COLUMN1_IN_CHART2_FLAG |
| COLUMN2_IN_CHART1_FLAG | VARCHAR2 | 1 |  |  | COLUMN2_IN_CHART1_FLAG |
| COLUMN2_IN_CHART2_FLAG | VARCHAR2 | 1 |  |  | COLUMN2_IN_CHART2_FLAG |
| COLUMN3_IN_CHART1_FLAG | VARCHAR2 | 1 |  |  | COLUMN3_IN_CHART1_FLAG |
| COLUMN3_IN_CHART2_FLAG | VARCHAR2 | 1 |  |  | COLUMN3_IN_CHART2_FLAG |
| COLUMN4_IN_CHART1_FLAG | VARCHAR2 | 1 |  |  | COLUMN4_IN_CHART1_FLAG |
| COLUMN4_IN_CHART2_FLAG | VARCHAR2 | 1 |  |  | COLUMN4_IN_CHART2_FLAG |
| COLUMN5_IN_CHART1_FLAG | VARCHAR2 | 1 |  |  | COLUMN5_IN_CHART1_FLAG |
| COLUMN5_IN_CHART2_FLAG | VARCHAR2 | 1 |  |  | COLUMN5_IN_CHART2_FLAG |
| PDF_LOCAL_CURR_FLAG | VARCHAR2 | 1 |  |  | Stores if the local currency is selected for PDF generation for this statement. |
| PDF_LOCAL_CURR_AVLBL | VARCHAR2 | 30 |  |  | Stores who can view the PDF statement for the local currency. |
| PDF_OTHER_CURR_FLAG | VARCHAR2 | 1 |  |  | Stores if the other currency is selected for PDF generation for this statement. |
| PDF_OTHER_CURR_CODE | VARCHAR2 | 30 |  |  | Stores the value of the other currency code. |
| PDF_OTHER_CURR_AVLBL | VARCHAR2 | 30 |  |  | Stores who can view the PDF statement for the other  currency. |
| HIDE_PDF_ITEM_DETAILS_FLAG | VARCHAR2 | 1 |  |  | Runtime value to check the display configuration of PDF line item details section |
| HIDE_OL_ITEM_DETAILS_FLAG | VARCHAR2 | 1 |  |  | Determines if the details in Online needs to be displayed |
| VALID_CHART1_FLAG | VARCHAR2 | 1 |  |  | Runtime value to find if graph 1 should be displayed for generated statement. |
| VALID_CHART2_FLAG | VARCHAR2 | 1 |  |  | Runtime value to find if graph 2 should be displayed for generated statement. |
| DESC_STATIC_ITEM_FLAG | VARCHAR2 | 1 |  |  | Static Items are added in the Description |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_STMT_PAGE_DEF_N1 | Non Unique | Default | PERD_RUN_ID, CAT_ID |
| CMP_TCS_STMT_PAGE_DEF_N2 | Non Unique | Default | STMT_PAGE_DEF_ID, BUSINESS_GROUP_ID |
| CMP_TCS_STMT_PAGE_DEF_UK1 | Unique | Default | STMT_PAGE_DEF_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
