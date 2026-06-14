# CMP_TCS_COL_IN_CAT

Setup Table that stores the Category Column Details.Captures the Category and the section column details.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcscolincat-6639.html#cmptcscolincat-6639](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcscolincat-6639.html#cmptcscolincat-6639)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_COL_IN_CAT_PK | COL_IN_CAT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COL_IN_CAT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| CAT_ID | NUMBER |  | 18 | Yes | Foreign key to CMP_TCS_CAT |
| ORDR_NUM | NUMBER |  | 18 | Yes | Order number |
| COLUMN_TYPE_CD | VARCHAR2 | 30 |  |  | COLUMN_TYPE_CD |
| DATA_TYPE_CD | VARCHAR2 | 30 |  |  | Compensation Type |
| CONTRIBUTOR_TYPE_CD | VARCHAR2 | 30 |  |  | CONTRIBUTOR_TYPE_CD |
| HIDE_COLUMN_FLAG | VARCHAR2 | 1 |  |  | HIDE_COLUMN_FLAG |
| INCLUDE_IN_CHART1_FLAG | VARCHAR2 | 1 |  |  | compensation item will be included in the chart Y or N. |
| INCLUDE_IN_CHART2_FLAG | VARCHAR2 | 1 |  |  | INCLUDE_IN_CHART2_FLAG |
| AVAIL_FOR_DISP_FLAG | VARCHAR2 | 1 |  |  | AVAIL_FOR_DISP_FLAG |
| HIDE_IN_PDF_FLAG | VARCHAR2 | 1 |  |  | Used in Stock History Category to decide whether a column should be visible in Printable Statement or not. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_COL_IN_CAT_N1 | Non Unique | Default | CAT_ID, COLUMN_TYPE_CD |
| CMP_TCS_COL_IN_CAT_UK1 | Unique | Default | COL_IN_CAT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
