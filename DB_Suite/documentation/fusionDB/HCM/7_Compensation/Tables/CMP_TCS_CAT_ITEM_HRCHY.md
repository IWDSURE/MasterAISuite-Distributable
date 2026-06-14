# CMP_TCS_CAT_ITEM_HRCHY

Table that stores the Category Hierarchy Details to get the aggregate value for the category employee and employer contribution. To get the aggregate value for a category for a person, get the item ids for the category from the hierarchy table and sum up the item values from the item value table.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcscatitemhrchy-13153.html#cmptcscatitemhrchy-13153](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcscatitemhrchy-13153.html#cmptcscatitemhrchy-13153)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_CAT_ITEM_HRCHY_PK | CAT_ITEM_HRCHY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAT_ITEM_HRCHY_ID | NUMBER |  | 18 | Yes | CAT_ITEM_HRCHY_ID |
| STMT_PERD_ID | NUMBER |  | 18 |  | STMT_PERD_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| CAT_ID | NUMBER |  | 18 | Yes | Foreign Key to CMP_TCS_CAT |
| STOCK_HISTORY_CAT_ID | NUMBER |  | 18 |  | to identify the stock history category for the item. Since there is no item involved in stock history, we need this column for the parent hierarchy |
| ITEM_ID | NUMBER |  | 18 |  | Foreign Key to CMP_TCS_ITEM |
| LVL_NUM | NUMBER |  | 18 | Yes | LVL_NUM |
| NUM_OF_OCCURRENCES | NUMBER |  | 18 |  | NUM_OF_OCCURRENCES |
| CONTRIBUTOR_TYPE_CD | VARCHAR2 | 15 |  |  | Indicates the Contribution Type code |
| DATA_TYPE_CD | VARCHAR2 | 30 |  |  | DATA_TYPE_CD |
| UOM | VARCHAR2 | 30 |  |  | UOM |
| NNMNTRY_UOM | VARCHAR2 | 30 |  |  | NNMNTRY_UOM |
| CALC_EXPR | VARCHAR2 | 4000 |  |  | Calculated item expression |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_CAT_ITEM_HRCHY_N1 | Non Unique | Default | PERD_RUN_ID, CAT_ID, CONTRIBUTOR_TYPE_CD, ITEM_ID |
| CMP_TCS_CAT_ITEM_HRCHY_N2 | Non Unique | Default | PERD_RUN_ID, ITEM_ID, CAT_ID |
| CMP_TCS_CAT_ITEM_HRCHY_UK1 | Unique | Default | CAT_ITEM_HRCHY_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
