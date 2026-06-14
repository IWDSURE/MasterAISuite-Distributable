# BEN_EXTRACT_DETAILS_ARCH

This table holds the archived data from BEN_EXTRACT_REQ_DETAILS table.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** ARCHIVE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benextractdetailsarch-30849.html#benextractdetailsarch-30849](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benextractdetailsarch-30849.html#benextractdetailsarch-30849)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_EXTRACT_DETAILS_ARCH_PK | REQUEST_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQUEST_DETAIL_ID | NUMBER |  | 18 | Yes | REQUEST_DETAIL_ID |
| EXT_REQUEST_ID | NUMBER |  | 18 | Yes | Identifies the Extarct request associated with this request detail. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | identifies enterprise |
| PARENT_REQUEST_DETAIL_ID | NUMBER |  | 18 |  | PARENT_REQUEST_DETAIL_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| CARRIER_ID | NUMBER |  | 18 |  | CARRIER_ID |
| FIRST_NAME | VARCHAR2 | 240 |  |  | FIRST_NAME |
| LAST_NAME | VARCHAR2 | 240 |  |  | LAST_NAME |
| MIDDLE_NAME | VARCHAR2 | 240 |  |  | MIDDLE_NAME |
| SUFFIX | VARCHAR2 | 240 |  |  | SUFFIX |
| GENDER_FLAG | VARCHAR2 | 30 |  |  | GENDER_FLAG |
| NATIONAL_IDENTIFIER | VARCHAR2 | 30 |  |  | NATIONAL_IDENTIFIER |
| DATE_OF_BIRTH | DATE |  |  |  | DATE_OF_BIRTH |
| DATE_OF_DEATH | DATE |  |  |  | DATE_OF_DEATH |
| TERMINATION_DATE | DATE |  |  |  | TERMINATION_DATE |
| MARITAL_STATUS | VARCHAR2 | 30 |  |  | MARITAL_STATUS |
| TOBACCO_USER | VARCHAR2 | 30 |  |  | TOBACCO_USER |
| DISABLED_FLAG | VARCHAR2 | 30 |  |  | DISABLED_FLAG |
| STUDENT_STATUS | VARCHAR2 | 30 |  |  | STUDENT_STATUS |
| EMAIL_ADDRESS_ID | VARCHAR2 | 60 |  |  | EMAIL_ADDRESS_ID |
| EMPLOYEE_ID | NUMBER |  | 18 |  | EMPLOYEE_ID |
| EMPLOYMENT_ORGANIZATION | VARCHAR2 | 240 |  |  | EMPLOYMENT_ORGANIZATION |
| EMPLOYMENT_STATUS | VARCHAR2 | 60 |  |  | EMPLOYMENT_STATUS |
| HIRE_DATE | DATE |  |  |  | HIRE_DATE |
| ORIGINAL_DATE_OF_HIRE | DATE |  |  |  | ORIGINAL_DATE_OF_HIRE |
| JOB | VARCHAR2 | 60 |  |  | JOB |
| GRADE | VARCHAR2 | 60 |  |  | GRADE |
| PAYROLL | VARCHAR2 | 80 |  |  | PAYROLL |
| BASE_SALARY | NUMBER |  |  |  | BASE_SALARY |
| TRANSACTION_CODE | VARCHAR2 | 60 |  |  | TRANSACTION_CODE |
| HOME_ADDRESS_LINE1 | VARCHAR2 | 80 |  |  | HOME_ADDRESS_LINE1 |
| HOME_ADDRESS_LINE2 | VARCHAR2 | 80 |  |  | HOME_ADDRESS_LINE2 |
| HOME_CITY | VARCHAR2 | 80 |  |  | HOME_CITY |
| HOME_STATE | VARCHAR2 | 80 |  |  | HOME_STATE |
| HOME_ZIP_CODE | VARCHAR2 | 80 |  |  | HOME_ZIP_CODE |
| HOME_PHONE | VARCHAR2 | 80 |  |  | HOME_PHONE |
| WORK_ADDRESS_LINE1 | VARCHAR2 | 80 |  |  | WORK_ADDRESS_LINE1 |
| WORK_ADDRESS_LINE2 | VARCHAR2 | 80 |  |  | WORK_ADDRESS_LINE2 |
| WORK_CITY | VARCHAR2 | 80 |  |  | WORK_CITY |
| WORK_STATE | VARCHAR2 | 80 |  |  | WORK_STATE |
| WORK_ZIP_CODE | VARCHAR2 | 80 |  |  | WORK_ZIP_CODE |
| WORK_PHONE | VARCHAR2 | 80 |  |  | WORK_PHONE |
| PLAN | VARCHAR2 | 80 |  |  | PLAN |
| LEVEL_NAME | VARCHAR2 | 80 |  |  | LEVEL_NAME |
| LEVEL_CVG_START_DATE | DATE |  |  |  | LEVEL_CVG_START_DATE |
| LEVEL_CVG_END_DATE | DATE |  |  |  | LEVEL_CVG_END_DATE |
| COVERAGE_START_DATE | DATE |  |  |  | COVERAGE_START_DATE |
| COVERAGE_END_DATE | DATE |  |  |  | COVERAGE_END_DATE |
| COVERAGE_AMOUNT_APPROVED | NUMBER |  |  |  | COVERAGE_AMOUNT_APPROVED |
| COVERAGE_AMOUNT_PENDING | NUMBER |  |  |  | COVERAGE_AMOUNT_PENDING |
| FSA_PLAN_YEAR | NUMBER |  |  |  | FSA_PLAN_YEAR |
| FSA_ANNUAL_TARGET | NUMBER |  |  |  | FSA_ANNUAL_TARGET |
| DIRECT_DEPOSIT_ROUTING | NUMBER |  |  |  | DIRECT_DEPOSIT_ROUTING |
| DIRECT_DEPOST_ACCOUNT | VARCHAR2 | 30 |  |  | DIRECT_DEPOST_ACCOUNT |
| EE_PRETAX_COST | NUMBER |  |  |  | EE_PRETAX_COST |
| EE_POSTTAX_COST | NUMBER |  |  |  | EE_POSTTAX_COST |
| EE_TOTAL_COST | NUMBER |  |  |  | EE_TOTAL_COST |
| PROVIDER_ID | VARCHAR2 | 30 |  |  | PROVIDER_ID |
| PROVIDER_NAME | VARCHAR2 | 60 |  |  | PROVIDER_NAME |
| PROVIDER_START_DATE | DATE |  |  |  | PROVIDER_START_DATE |
| DPNT_RELATIONSHIP_TYPE | VARCHAR2 | 60 |  |  | DPNT_RELATIONSHIP_TYPE |
| DPNT_FULL_TIME_STUDENT | VARCHAR2 | 30 |  |  | DPNT_FULL_TIME_STUDENT |
| ORGANIZATION_IDENTIFIER | VARCHAR2 | 255 |  |  | ORGANIZATION_IDENTIFIER |
| DEP_NAME | VARCHAR2 | 255 |  |  | DEP_NAME |
| MARITAL_STATUS_START_DATE | DATE |  |  |  | MARITAL_STATUS_START_DATE |
| TIER_COVERAGE_TYPE | VARCHAR2 | 80 |  |  | TIER_COVERAGE_TYPE |
| EMPLOYMENT_LEVEL_CODE | VARCHAR2 | 80 |  |  | EMPLOYMENT_LEVEL_CODE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_EXTRACT_DETAILS_ARCH_U1 | Unique | Default | REQUEST_DETAIL_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
