# CMP_TCS_STMT_PAGE_DEF_TL

Stroes translatable inforamtion of CMP_TCS_STMT_PAGE_DEF table

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtpagedeftl-10634.html#cmptcsstmtpagedeftl-10634](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtpagedeftl-10634.html#cmptcsstmtpagedeftl-10634)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STMT_PGEDF_TL_PK | STMT_PAGE_DEF_ID, LANGUAGE, BUSINESS_GROUP_ID, PERD_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STMT_PAGE_DEF_ID | NUMBER |  | 18 | Yes | STMT_PAGE_DEF_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| CATEGORY_TITLE | VARCHAR2 | 240 |  |  | CATEGORY_TITLE |
| DESC_TXT | CLOB |  |  |  | DESC_TXT |
| SMRY_TITLE | VARCHAR2 | 240 |  |  | SMRY_TITLE |
| ADDL_INFO_TITLE | VARCHAR2 | 240 |  |  | ADDL_INFO_TITLE |
| ADDL_INFO | CLOB |  |  |  | ADDL_INFO |
| CHART_RN_TITLE | VARCHAR2 | 240 |  |  | CHART_RN_TITLE |
| CHART1_TITLE | VARCHAR2 | 240 |  |  | CHART1_TITLE |
| CHART2_TITLE | VARCHAR2 | 240 |  |  | CHART2_TITLE |
| DISPLAY_NAME_COLUMN_LABEL | VARCHAR2 | 240 |  |  | DISPLAY_NAME_COLUMN_LABEL |
| DESC_COLUMN_LABEL | VARCHAR2 | 240 |  |  | DESC_COLUMN_LABEL |
| DATE_COLUMN_LABEL | VARCHAR2 | 240 |  |  | DATE_COLUMN_LABEL |
| JOB_COLUMN_LABEL | VARCHAR2 | 240 |  |  | JOB_COLUMN_LABEL |
| COLUMN1_DISPLAY_NAME | VARCHAR2 | 240 |  |  | COLUMN1_DISPLAY_NAME |
| COLUMN2_DISPLAY_NAME | VARCHAR2 | 240 |  |  | COLUMN2_DISPLAY_NAME |
| COLUMN3_DISPLAY_NAME | VARCHAR2 | 240 |  |  | COLUMN3_DISPLAY_NAME |
| COLUMN4_DISPLAY_NAME | VARCHAR2 | 240 |  |  | COLUMN4_DISPLAY_NAME |
| COLUMN5_DISPLAY_NAME | VARCHAR2 | 240 |  |  | COLUMN5_DISPLAY_NAME |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_STMT_PGDF_TL_UK1 | Unique | FUSION_TS_TX_DATA | STMT_PAGE_DEF_ID, LANGUAGE, BUSINESS_GROUP_ID, PERD_RUN_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
