# CMP_GSP_PERSON_INFO

CMP_GSP_PERSON_INFO table helds details of person with proposed salary progressions which are used for approval.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpgsppersoninfo-3510.html#cmpgsppersoninfo-3510](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpgsppersoninfo-3510.html#cmpgsppersoninfo-3510)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_GSP_PERSON_INFO_PK | GSP_PERSON_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GSP_PERSON_INFO_ID | NUMBER |  | 18 | Yes | GSP_PERSON_INFO_ID |
| ADJUSTED_FTE_FLAG | VARCHAR2 | 30 |  |  | If Adjusted FTE is used for salary record |
| PERSON_NUMBER | VARCHAR2 | 50 |  |  | person number |
| CURRENT_COMP_AMOUNT | NUMBER |  |  |  | Current component amount |
| CURRENT_ANNUAL_COMP_AMOUNT | NUMBER |  |  |  | Current component annual amount |
| CURRENT_AFT_COMP_AMOUNT | NUMBER |  |  |  | Current component annualized amount |
| CURRENT_FT_COMP_AMOUNT | NUMBER |  |  |  | Current component full time amount |
| SALARY_BASIS_TYPE | VARCHAR2 | 30 |  |  | Salary basis type |
| EFFECTIVE_DATE | DATE |  |  |  | EFFECTIVE_DATE |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| ASG_EFFECTIVE_START_DATE | DATE |  |  |  | ASG_EFFECTIVE_START_DATE |
| ASSIGNMENT_OVN | NUMBER |  | 9 |  | ASSIGNMENT_OVN |
| ASSIGNMENT_SEQ | NUMBER |  | 9 |  | ASSIGNMENT_SEQ |
| ASSIGNMENT_NUMBER | VARCHAR2 | 50 |  |  | ASSIGNMENT_NUMBER |
| ASSIGN_GRADE_STEP_ID | NUMBER |  | 18 |  | ASSIGN_GRADE_STEP_ID |
| STEP_EFFECTIVE_START_DATE | DATE |  |  |  | STEP_EFFECTIVE_START_DATE |
| ASSIGN_STEP_OVN | NUMBER |  | 9 |  | ASSIGN_STEP_OVN |
| GRADE_LADDER_ID | NUMBER |  | 18 |  | GRADE_LADDER_ID |
| GRADE_ID | NUMBER |  | 18 |  | GRADE_ID |
| STEP_ID | NUMBER |  | 18 |  | STEP_ID |
| ASG_ACTION_ID | NUMBER |  | 18 |  | ASG_ACTION_ID |
| ASG_ACTION_REASON_ID | NUMBER |  | 18 |  | ASG_ACTION_REASON_ID |
| ASG_ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | ASG_ACTION_OCCURRENCE_ID |
| ASG_ACTION_CODE | VARCHAR2 | 30 |  |  | ASG_ACTION_CODE |
| ASG_ACTION_REASON_CODE | VARCHAR2 | 30 |  |  | ASG_ACTION_REASON_CODE |
| SALARY_ID | NUMBER |  | 18 |  | SALARY_ID |
| SAL_DATE_FROM | DATE |  |  |  | SAL_DATE_FROM |
| SALARY_OVN | NUMBER |  | 9 |  | SALARY_OVN |
| SALARY_BASIS_ID | NUMBER |  | 18 |  | SALARY_BASIS_ID |
| SALARY_BASIS_NAME | VARCHAR2 | 80 |  |  | SALARY_BASIS_NAME |
| SAL_ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | SAL_ACTION_OCCURRENCE_ID |
| SAL_ACTION_ID | NUMBER |  | 18 |  | SAL_ACTION_ID |
| SAL_ACTION_REASON_ID | NUMBER |  | 18 |  | SAL_ACTION_REASON_ID |
| SAL_ACTION_CODE | VARCHAR2 | 30 |  |  | SAL_ACTION_CODE |
| SAL_ACTION_REASON_CODE | VARCHAR2 | 30 |  |  | SAL_ACTION_REASON_CODE |
| PROPOSED_PROGRESSION_DATE | DATE |  |  |  | PROPOSED_PROGRESSION_DATE |
| OVERRIDE_PROGRESSION_DATE | DATE |  |  |  | OVERRIDE_PROGRESSION_DATE |
| UPDATE_SALARY_FLAG | VARCHAR2 | 1 |  |  | UPDATE_SALARY_FLAG |
| PROPOSED_SALARY_CHANGE_DATE | DATE |  |  |  | PROPOSED_SALARY_CHANGE_DATE |
| OVERRIDE_SALARY_CHANGE_DATE | DATE |  |  |  | OVERRIDE_SALARY_CHANGE_DATE |
| ELIGIBLE_FLAG | VARCHAR2 | 1 |  |  | ELIGIBLE_FLAG |
| ERROR_CODE | VARCHAR2 | 30 |  |  | ERROR_CODE |
| ERROR_TYPE | VARCHAR2 | 30 |  |  | ERROR_TYPE |
| APPROVAL_CODE | VARCHAR2 | 30 |  |  | APPROVAL_CODE |
| APPROVAL_DATE | DATE |  |  |  | APPROVAL_DATE |
| APPROVAL_COMMENTS | CLOB |  |  |  | APPROVAL_COMMENTS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| PROCESS_CODE | VARCHAR2 | 30 |  |  | PROCESS_CODE |
| PAYROLL_ID | NUMBER |  | 18 |  | PAYROLL_ID of the person |
| PAYROLL_NAME | VARCHAR2 | 80 |  |  | PAYROLL_NAME |
| ASG_EFFECTIVE_END_DATE | DATE |  |  |  | ASG_EFFECTIVE_END_DATE |
| CUR_ASG_ACTION_ID | NUMBER |  | 18 |  | CUR_ASG_ACTION_ID |
| CUR_ASG_ACTION_REASON_ID | NUMBER |  | 18 |  | CUR_ASG_ACTION_REASON_ID |
| SALARY_ROUNDING_CODE | VARCHAR2 | 30 |  |  | SALARY_ROUNDING_CODE |
| SALARY_PRECISION_SCALE | NUMBER |  | 3 |  | SALARY_PRECISION_SCALE |
| SALARY_BASIS_CODE | VARCHAR2 | 80 |  |  | SALARY_BASIS_CODE |
| FTE | NUMBER |  |  |  | FTE |
| FTE_CALCULATED_FLAG | VARCHAR2 | 1 |  |  | FTE Calculated Flag |
| CUR_SAL_ANNUAL_AMOUNT | NUMBER |  |  |  | CUR_SAL_ANNUAL_AMOUNT |
| CUR_SAL_AMOUNT | NUMBER |  |  |  | CUR_SAL_AMOUNT |
| CUR_SAL_AFT_AMOUNT | NUMBER |  |  |  | CUR_SAL_AFT_AMOUNT |
| CUR_SAL_FT_AMOUNT | NUMBER |  |  |  | CUR_SAL_AFT_AMOUNT |
| CUR_SAL_ACTION_ID | NUMBER |  | 18 |  | CUR_SAL_ACTION_ID |
| CUR_SAL_ACTION_REASON_ID | NUMBER |  | 18 |  | CUR_SAL_ACTION_REASON_ID |
| SALARY_ANNUAL_FACTOR | NUMBER |  |  |  | SALARY_ANNUAL_FACTOR |
| SALARY_CURRENCY | VARCHAR2 | 30 |  |  | SALARY_CURRENCY |
| SALARY_UPDATE_MODE_CODE | VARCHAR2 | 30 |  |  | Salary update mode code, CORRECTION or UPDATE |
| SALARY_DATE_TO | DATE |  |  |  | SALARY_DATE_TO |
| SALARY_BASIS_RATE_ID | NUMBER |  | 18 |  | SALARY_BASIS_RATE_ID |
| AUTO_PROGRESSION_CODE | VARCHAR2 | 30 |  |  | Auro progression code for Ladder progression and Rate Sync. |
| APPR_DATE_VALIDATE_FLAG | VARCHAR2 | 1 |  |  | The flag that derermines that the approval process needs to validate the future date |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_GSP_PERSON_INFO_N1 | Non Unique | Default | GRADE_LADDER_ID, APPROVAL_CODE, REQUEST_ID |
| CMP_GSP_PERSON_INFO_N2 | Non Unique | Default | ASSIGNMENT_ID, GRADE_LADDER_ID, APPROVAL_CODE |
| CMP_GSP_PERSON_INFO_N3 | Non Unique | Default | REQUEST_ID, PERSON_ID |
| CMP_GSP_PERSON_INFO_U1 | Unique | Default | GSP_PERSON_INFO_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
