# CMP_TCS_PER_PERD

Table holds Cmp Tcs Per Perd records.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperperd-27363.html#cmptcsperperd-27363](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperperd-27363.html#cmptcsperperd-27363)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_PER_PERD_PK | PER_PERD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_PERD_ID | NUMBER |  | 18 | Yes | PER_PERD_ID |
| DISPLAY_SALARY_FLAG | VARCHAR2 | 1 |  |  | DISPLAY_SALARY_FLAG |
| STMT_ID | NUMBER |  | 18 | Yes | STMT_ID |
| STMT_PERD_ID | NUMBER |  | 18 | Yes | STMT_PERD_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  | Yes | END_DATE |
| AVAILABILITY_DATE | DATE |  |  |  | AVAILABILITY_DATE |
| XCHG_RATE_DATE | DATE |  |  |  | Currency Conversion Date |
| ONE_LEGAL_ENTITY_ID | NUMBER |  | 18 |  | ONE_LEGAL_ENTITY_ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LOCAL_CURRENCY_CODE | VARCHAR2 | 30 |  |  | Local currency code |
| OTHER_CURRENCY_CODE | VARCHAR2 | 30 |  |  | Other currency code. |
| PDF_LOCAL_CURR_FLAG | VARCHAR2 | 1 |  |  | Stores if the local currency is selected for PDF generation for this statement. |
| PDF_LOCAL_CURR_AVLBL | VARCHAR2 | 30 |  |  | Stores who can view the PDF statement for the local currency. |
| PDF_OTHER_CURR_FLAG | VARCHAR2 | 1 |  |  | Stores if the other currency is selected for PDF generation for this statement. |
| PDF_OTHER_CURR_CODE | VARCHAR2 | 30 |  |  | Stores the value of the other currency code. |
| PDF_OTHER_CURR_AVLBL | VARCHAR2 | 30 |  |  | Stores who can view the PDF statement for the other  currency. |
| HIDE_OL_DRILL_SECTIONS_FLAG | VARCHAR2 | 1 |  |  | Runtime value for display configuration for the behavior of online statement drill sections |
| DISPLAY_JOB_FLAG | VARCHAR2 | 1 |  |  | DISPLAY_JOB_FLAG |
| XCHANGE_RATE_MISSING_FLAG | VARCHAR2 | 1 |  |  | XCHANGE_RATE_MISSING_FLAG |
| DISPLAY_POSITION_FLAG | VARCHAR2 | 1 |  |  | DISPLAY_POSITION_FLAG |
| FEEDBACK_ENABLED_FLAG | VARCHAR2 | 1 |  |  | Determines if the feedback is enabled in setup |
| HIDE_WELCOME_FLAG | VARCHAR2 | 1 |  |  | Determines if the welcome page needs to be displayed |
| HIDE_PDF_ITEM_DETAILS_FLAG | VARCHAR2 | 1 |  |  | Determines if the details in pdf needs to be displayed |
| WELCOME_STATIC_ITEM_FLAG | VARCHAR2 | 1 |  |  | Static Items are added in Welcome Message |
| NNMNTRY_SUMMARY_FLAG | VARCHAR2 | 1 |  |  | Non Monetary Summary is defined |
| MNTRY_SUMMARY_FLAG | VARCHAR2 | 1 |  |  | Monetary Summary is defined |
| CURR_SWITCHER_DEFAULT | VARCHAR2 | 30 |  |  | Stores the value of the Default currency switcher preference. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_PER_PERD_N1 | Non Unique | Default | PERD_RUN_ID, PERSON_ID |
| CMP_TCS_PER_PERD_N3 | Non Unique | Default | PERSON_ID, STMT_PERD_ID |
| CMP_TCS_PER_PERD_UK1 | Unique | Default | PER_PERD_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
