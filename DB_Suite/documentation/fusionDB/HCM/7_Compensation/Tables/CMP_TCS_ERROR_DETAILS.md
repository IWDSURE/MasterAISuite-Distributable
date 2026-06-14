# CMP_TCS_ERROR_DETAILS

Table holds Cmp Tcs Error Details records.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcserrordetails-23765.html#cmptcserrordetails-23765](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcserrordetails-23765.html#cmptcserrordetails-23765)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_ERROR_DETAILS_PK | ERROR_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ERROR_DETAIL_ID | NUMBER |  | 18 | Yes | ERROR_DETAIL_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| REPORT_DETAIL_ID | NUMBER |  | 18 |  | REPORT_DETAIL_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| CAT_ID | NUMBER |  | 18 |  | CAT_ID |
| CAT_NAME | VARCHAR2 | 240 |  |  | CAT_NAME |
| ITEM_ID | NUMBER |  | 18 |  | ITEM_ID |
| ITEM_NAME | VARCHAR2 | 240 |  |  | ITEM_NAME |
| ERR_CODE | VARCHAR2 | 30 |  |  | ERR_CODE |
| ERR_MESSAGE | VARCHAR2 | 600 |  |  | ERR_MESSAGE |
| ERR_TYPE | VARCHAR2 | 30 |  |  | ERR_TYPE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_ERROR_DETAILS_N1 | Non Unique | Default | REQUEST_ID, ERROR_DETAIL_ID |
| CMP_TCS_ERROR_DETAILS_UK1 | Unique | Default | ERROR_DETAIL_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
