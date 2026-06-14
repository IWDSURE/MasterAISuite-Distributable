# CMP_TCS_PER_ITEM_TAG_VALUE

This table stores the item tag values for the rich text.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperitemtagvalue-31528.html#cmptcsperitemtagvalue-31528](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperitemtagvalue-31528.html#cmptcsperitemtagvalue-31528)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ITEM_TAG_VALUE_ID | NUMBER |  | 18 | Yes | PER_ITEM_TAG_VALUE_ID |
| PER_ITEM_CRITERIA_ID | NUMBER |  | 18 | Yes | PER_ITEM_CRITERIA_ID |
| ITEM_ID | NUMBER |  | 18 |  | ITEM_ID |
| CALC_TYPE | VARCHAR2 | 30 |  |  | CALC_TYPE |
| TEXT_VALUE | VARCHAR2 | 2000 |  |  | TEXT_VALUE |
| NUM_VALUE | NUMBER |  |  |  | NUM_VALUE |
| DATE_VALUE | DATE |  |  |  | DATE_VALUE |
| UOM | VARCHAR2 | 30 |  |  | UOM |
| NNMNTRY_UOM | VARCHAR2 | 30 |  |  | This column stories the non monetary uom |
| TAG_PLACE | VARCHAR2 | 30 |  |  | This column stores the place (Welcome, Summary etc) where the tag is created |
| ITEM_TAG_NAME | VARCHAR2 | 80 |  |  | This column stores the name of the item tag |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| JOB_ID | NUMBER |  | 18 |  | JOB_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_PER_ITEM_TAG_VALUE_N1 | Non Unique | Default | PER_ITEM_CRITERIA_ID, ITEM_ID |
| CMP_TCS_PER_ITEM_TAG_VALUE_UK1 | Unique | Default | PER_ITEM_TAG_VALUE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
