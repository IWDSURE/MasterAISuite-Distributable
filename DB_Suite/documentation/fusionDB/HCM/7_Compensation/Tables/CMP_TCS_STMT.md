# CMP_TCS_STMT

Setup Table that stores the statement definition. Captures the Eligibility Profile, Summary page description details and the additional information details, latest date on which statement is generated using the setup

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmt-22460.html#cmptcsstmt-22460](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmt-22460.html#cmptcsstmt-22460)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STMT_PK | STMT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STMT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| DISPLAY_SALARY_FLAG | VARCHAR2 | 1 |  |  | DISPLAY_SALARY_FLAG |
| NAME | VARCHAR2 | 240 |  |  | NAME |
| EE_PROFILE_ID | NUMBER |  | 18 |  | Employee Profile id |
| STAT_CD | VARCHAR2 | 30 |  | Yes | Processing Status of the Statement. |
| INDICATE_ESTIMATE_FLAG | VARCHAR2 | 1 |  |  | Indicates to the amounts are esitimated Y or N |
| STMT_GENERATED_FLAG | VARCHAR2 | 1 |  |  | STMT_GENERATED_FLAG |
| HIDE_SMRY_DESC_TXT_FLAG | VARCHAR2 | 1 |  |  | HIDE_SMRY_DESC_TXT_FLAG |
| SMRY_DESC_TXT_ORDR_NUM | NUMBER |  | 18 |  | SMRY_DESC_TXT_ORDR_NUM |
| HIDE_SMRY_FLAG | VARCHAR2 | 1 |  |  | HIDE_SMRY_FLAG |
| HIDE_SMRY_ADDL_INFO_FLAG | VARCHAR2 | 1 |  |  | HIDE_SMRY_ADDL_INFO_FLAG |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PDF_LOCAL_CURR_FLAG | VARCHAR2 | 1 |  |  | Stores if the local currency is selected for PDF generation for this statement. |
| PDF_LOCAL_CURR_AVLBL | VARCHAR2 | 30 |  |  | Stores who can view the PDF statement for the local currency. |
| PDF_OTHER_CURR_FLAG | VARCHAR2 | 1 |  |  | Stores if the other currency is selected for PDF generation for this statement. |
| PDF_OTHER_CURR_CODE | VARCHAR2 | 30 |  |  | Stores the value of the other currency code. |
| PDF_OTHER_CURR_AVLBL | VARCHAR2 | 30 |  |  | Stores who can view the PDF statement for the other  currency. |
| CURR_SWITCHER_DEFAULT | VARCHAR2 | 30 |  |  | Store the default switcher currency type in which the detail page of online statements display. |
| HIDE_PDF_ITEM_DETAILS_FLAG | VARCHAR2 | 1 |  |  | Setup Option to configure the display of line item details section in PDF |
| HIDE_OL_DRILL_SECTIONS_FLAG | VARCHAR2 | 1 |  |  | Setup Option to configure the display of drill sections in Online Statement |
| DISPLAY_JOB_FLAG | VARCHAR2 | 1 |  |  | DISPLAY_JOB_FLAG |
| DISPLAY_POSITION_FLAG | VARCHAR2 | 1 |  |  | DISPLAY_POSITION_FLAG |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_STMT_N1 | Non Unique | Default | STAT_CD |
| CMP_TCS_STMT_N2 | Non Unique | Default | EE_PROFILE_ID |
| CMP_TCS_STMT_UK1 | Unique | Default | STMT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
