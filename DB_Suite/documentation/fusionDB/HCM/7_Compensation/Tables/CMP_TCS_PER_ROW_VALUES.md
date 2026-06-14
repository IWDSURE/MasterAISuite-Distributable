# CMP_TCS_PER_ROW_VALUES

This table stores the person data as per the definition of  cmp_tcs_row_in_cat and cmp_tcs_stmt_tbl_row_def.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperrowvalues-23573.html#cmptcsperrowvalues-23573](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperrowvalues-23573.html#cmptcsperrowvalues-23573)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_PER_ROW_VALUE_PK | PER_ROW_VALUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ROW_VALUE_ID | NUMBER |  | 18 | Yes | PER_ROW_VALUE_ID |
| STMT_PERD_ID | NUMBER |  | 18 | Yes | STMT_PERD_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| PER_PERD_ID | NUMBER |  | 18 | Yes | Foreign key to CMP_TCS_PER_PERD |
| PER_PERD_STMT_ID | NUMBER |  | 18 | Yes | Foreign key to CMP_TCS_PER_PERD_STMT |
| CAT_ID | NUMBER |  | 18 | Yes | CAT_ID |
| ROW_IN_CAT_ID | NUMBER |  | 18 | Yes | ROW_IN_CAT_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| DISPLAY_DATE | DATE |  |  |  | DISPLAY_DATE |
| COLUMN1_NUM_VALUE | NUMBER |  |  |  | COLUMN1_NUM_VALUE |
| COLUMN1_TEXT_VALUE | VARCHAR2 | 2000 |  |  | COLUMN1_TEXT_VALUE |
| COLUMN1_DATE_VALUE | DATE |  |  |  | COLUMN1_DATE_VALUE |
| COLUMN1_UOM | VARCHAR2 | 30 |  |  | COLUMN1_UOM |
| COLUMN2_NUM_VALUE | NUMBER |  |  |  | COLUMN2_NUM_VALUE |
| COLUMN2_TEXT_VALUE | VARCHAR2 | 2000 |  |  | COLUMN2_TEXT_VALUE |
| COLUMN2_DATE_VALUE | DATE |  |  |  | COLUMN2_DATE_VALUE |
| COLUMN2_UOM | VARCHAR2 | 30 |  |  | COLUMN2_UOM |
| COLUMN3_NUM_VALUE | NUMBER |  |  |  | COLUMN3_NUM_VALUE |
| COLUMN3_TEXT_VALUE | VARCHAR2 | 2000 |  |  | COLUMN3_TEXT_VALUE |
| COLUMN3_DATE_VALUE | DATE |  |  |  | COLUMN3_DATE_VALUE |
| COLUMN3_UOM | VARCHAR2 | 30 |  |  | COLUMN3_UOM |
| COLUMN4_NUM_VALUE | NUMBER |  |  |  | COLUMN4_NUM_VALUE |
| COLUMN4_TEXT_VALUE | VARCHAR2 | 2000 |  |  | COLUMN4_TEXT_VALUE |
| COLUMN4_DATE_VALUE | DATE |  |  |  | COLUMN4_DATE_VALUE |
| COLUMN4_UOM | VARCHAR2 | 30 |  |  | COLUMN4_UOM |
| COLUMN5_NUM_VALUE | NUMBER |  |  |  | COLUMN5_NUM_VALUE |
| COLUMN5_TEXT_VALUE | VARCHAR2 | 2000 |  |  | COLUMN5_TEXT_VALUE |
| COLUMN5_DATE_VALUE | DATE |  |  |  | COLUMN5_DATE_VALUE |
| COLUMN5_UOM | VARCHAR2 | 30 |  |  | COLUMN5_UOM |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_ID | NUMBER |  | 18 |  | JOB_ID |
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
| CMP_TCS_PER_ROW_VALUES_N1 | Non Unique | Default | PERSON_ID, PERD_RUN_ID, ROW_IN_CAT_ID |
| CMP_TCS_PER_ROW_VALUES_N2 | Non Unique | Default | ROW_IN_CAT_ID, PER_PERD_ID, LEGAL_ENTITY_ID |
| CMP_TCS_PER_ROW_VALUES_N3 | Non Unique | Default | PER_PERD_ID, PER_PERD_STMT_ID |
| CMP_TCS_PER_ROW_VALUES_N4 | Non Unique | Default | PERD_RUN_ID, PERSON_ID, CAT_ID |
| CMP_TCS_PER_ROW_VALUES_UK1 | Unique | Default | PER_ROW_VALUE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
