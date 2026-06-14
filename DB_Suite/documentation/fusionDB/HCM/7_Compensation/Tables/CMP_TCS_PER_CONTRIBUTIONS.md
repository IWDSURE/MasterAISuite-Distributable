# CMP_TCS_PER_CONTRIBUTIONS

Table stores Contribution  summary of each person for every statement

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcspercontributions-8760.html#cmptcspercontributions-8760](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcspercontributions-8760.html#cmptcspercontributions-8760)

## Primary Key

| Name | Columns |
|------|----------|
| cmp_tcs_per_contributions_PK | PER_CONTRIBUTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_CONTRIBUTION_ID | NUMBER |  |  | Yes | Primary Key |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| PER_PERD_ID | NUMBER |  | 18 | Yes | Foreign key to CMP_TCS_PER_PERD |
| PER_PERD_STMT_ID | NUMBER |  | 18 |  | Foreign key to CMP_TCS_PER_PERD_STMT |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| STMT_TBL_ROW_DEF_ID | NUMBER |  | 18 |  | STMT_TBL_ROW_DEF_ID |
| STMT_PAGE_DEF_ID | NUMBER |  | 18 |  | STMT_PAGE_DEF_ID |
| EMPLOYEE_CNTRB_VALUE | NUMBER |  |  |  | If the data types are currency or number then value for the comp item is stored |
| EMPLOYEE_CNTRB_UOM | VARCHAR2 | 30 |  |  | UOM Of Employee Contribution |
| EMPLOYEE_CNTRB_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | NNMNTRY_UOM of Employee Contribution |
| EMPLOYEE_CNTRB_XCHANGE_FLAG | VARCHAR2 | 1 |  |  | EMPLOYEE_CNTRB_XCHANGE_FLAG |
| EMPLOYEE_CNTRB_TRANS_UOM | VARCHAR2 | 30 |  |  | UOM Of Employee Transaction |
| EMPLOYER_CNTRB_VALUE | NUMBER |  |  |  | If the data types are currency or number then value for the comp item is stored |
| EMPLOYER_CNTRB_UOM | VARCHAR2 | 30 |  |  | UOM Of Employer Contribution |
| EMPLOYER_CNTRB_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | NNMNTRY_UOM of Employer Contribution |
| EMPLOYER_CNTRB_TRANS_UOM | VARCHAR2 | 30 |  |  | UOM Of Employer Transactions |
| EMPLOYER_CNTRB_XCHANGE_FLAG | VARCHAR2 | 1 |  |  | EMPLOYER_CNTRB_XCHANGE_FLAG |
| COLUMN1_VALUE | NUMBER |  |  |  | Compensation Custom Column1 Value |
| COLUMN1_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column1 UOM |
| COLUMN1_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column1 Non Monetary UOM |
| COLUMN1_XCHANGE_FLAG | VARCHAR2 | 1 |  |  | Compensation Custom Column1 Currency Conversion available |
| COLUMN1_TRANS_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column1 Transaction UOM |
| COLUMN2_VALUE | NUMBER |  |  |  | Compensation Custom Column2 Value |
| COLUMN2_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column2 UOM |
| COLUMN2_XCHANGE_FLAG | VARCHAR2 | 1 |  |  | Compensation Custom Column2 Currency conversion Available |
| COLUMN2_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column2 Non Monetary UOM |
| COLUMN2_TRANS_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column2 Transaction UOM |
| COLUMN3_VALUE | NUMBER |  |  |  | Compensation Custom Column3 Value |
| COLUMN3_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column3 UOM |
| COLUMN3_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column3 Non Monetary UOM |
| COLUMN3_XCHANGE_FLAG | VARCHAR2 | 1 |  |  | Compensation Custom Column3 Currency Convesion Available |
| COLUMN3_TRANS_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column5 Transaction UOM |
| COLUMN4_VALUE | NUMBER |  |  |  | Compensation Custom Column4 Value |
| COLUMN4_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column4 UOM |
| COLUMN4_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column4 Non Monetary UOM |
| COLUMN4_XCHANGE_FLAG | VARCHAR2 | 1 |  |  | Compensation Custom Column4 currency conversion available |
| COLUMN4_TRANS_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column4 Transaction UOM |
| COLUMN5_VALUE | NUMBER |  |  |  | Compensation Custom Column5 Value |
| COLUMN5_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column5 UOM |
| COLUMN5_NNMNTRY_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column5 Non Monetary UOM |
| COLUMN5_XCHANGE_FLAG | VARCHAR2 | 1 |  |  | Compensation Custom Column5 currency conversion available |
| COLUMN5_TRANS_UOM | VARCHAR2 | 30 |  |  | Compensation Custom Column5 Transaction UOM |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| EMPLOYEE_CNTRB_DATA_TYPE_CD | VARCHAR2 | 30 |  |  | Employee Contribution Data Type Code |
| EMPLOYER_CNTRB_DATA_TYPE_CD | VARCHAR2 | 30 |  |  | Employer Contribution Data Type Code |
| EMPLOYEE_CNTRB_ESTIMATED_FLAG | VARCHAR2 | 1 |  |  | Employee Contribution Estimated Flag |
| EMPLOYER_CNTRB_ESTIMATED_FLAG | VARCHAR2 | 1 |  |  | Employer Contribution Estimated Flag |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_PER_CONTRIBUTION_N1 | Non Unique | Default | PER_PERD_STMT_ID, STMT_PAGE_DEF_ID, STMT_TBL_ROW_DEF_ID |
| CMP_TCS_PER_CONTRIBUTION_N2 | Non Unique | Default | PERD_RUN_ID, PERSON_ID, PER_PERD_STMT_ID, STMT_TBL_ROW_DEF_ID, STMT_PAGE_DEF_ID |
| CMP_TCS_PER_CONTRIBUTION_N3 | Non Unique | Default | PER_PERD_ID, PERD_RUN_ID |
| CMP_TCS_PER_CONTRIBUTION_UK1 | Unique | Default | PER_CONTRIBUTION_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
