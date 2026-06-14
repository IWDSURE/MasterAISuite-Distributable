# CMP_GSP_ELIG_PROGRESSIONS

CMP_GSP_ELIG_PROGRESSIONS table helds details of the proposed salary progressions which are used for approval.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpgspeligprogressions-30342.html#cmpgspeligprogressions-30342](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpgspeligprogressions-30342.html#cmpgspeligprogressions-30342)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_GSP_ELIG_PROGRESSIONS_PK | GSP_ELIG_PROGRESSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GSP_ELIG_PROGRESSION_ID | NUMBER |  | 18 | Yes | GSP_ELIG_PROGRESSION_ID |
| PROPOSED_COMP_AMOUNT | NUMBER |  |  |  | Proposed component amount |
| PROPOSED_ANNUAL_COMP_AMOUNT | NUMBER |  |  |  | Proposed annual component |
| PROPOSED_FT_COMP_AMOUNT | NUMBER |  |  |  | Proposed full time component amount |
| PROPOSED_AFT_COMP_AMOUNT | NUMBER |  |  |  | Proposed annualized full time component |
| GSP_PERSON_INFO_ID | NUMBER |  | 18 | Yes | GSP_PERSON_INFO_ID |
| PROPOSED_GRADE_LADDER_ID | NUMBER |  | 18 | Yes | PROPOSED_GRADE_LADDER_ID |
| PROPOSED_GRADE_ID | NUMBER |  | 18 |  | PROPOSED_GRADE_ID |
| PROPOSED_STEP_ID | NUMBER |  | 18 |  | PROPOSED_STEP_ID |
| DEFAULT_PROGRESSION_FLAG | VARCHAR2 | 1 |  |  | DEFAULT_PROGRESSION_FLAG |
| RATE_VALUE_ID | NUMBER |  | 18 |  | RATE_VALUE_ID |
| PROPOSED_SALARY_AMOUNT | NUMBER |  |  |  | PROPOSED_SALARY_AMOUNT |
| PROPOSED_FT_SALARY_AMOUNT | NUMBER |  |  |  | PROPOSED_FT_SALARY_AMOUNT |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | CURRENCY_CODE |
| RATE_FREQUENCY | VARCHAR2 | 30 |  |  | RATE_FREQUENCY |
| OVERRIDE_SALARY_AMOUNT | NUMBER |  |  |  | OVERRIDE_SALARY_AMOUNT |
| ELIGIBLE_FLAG | VARCHAR2 | 1 |  |  | ELIGIBLE_FLAG |
| INELIG_ERROR_CODE | VARCHAR2 | 30 |  |  | INELIG_ERROR_CODE |
| PROPOSED_SAL_ANNUALIZATION_FTR | NUMBER |  |  |  | PROPOSED_SAL_ANNUALIZATION_FTR |
| PROPOSED_ANNUALIZED_FT_SALARY | NUMBER |  |  |  | PROPOSED_ANNUALIZED_FT_SALARY |
| PROPOSED_SAL_FREQUENCY | VARCHAR2 | 30 |  |  | PROPOSED_SAL_FREQUENCY |
| PROPOSED_SAL_CURRENCY_CODE | VARCHAR2 | 30 |  |  | PROPOSED_SAL_CURRENCY_CODE |
| RATE_ANNUALIZATION_FACTOR | NUMBER |  |  |  | RATE_ANNUALIZATION_FACTOR |
| RATE_VALUE | NUMBER |  |  |  | RATE_VALUE |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| PROPOSED_ANNUAL_SALARY | NUMBER |  |  |  | PROPOSED_ANNUAL_SALARY |
| PROGRESSION_DATE | DATE |  |  |  | Assignment Progression date for the Grade or Step |
| SALARY_CHANGE_DATE | DATE |  |  |  | Salary Change Date for the Grade or Step |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_GSP_ELIG_PROGRESSIONS_N1 | Non Unique | Default | GSP_PERSON_INFO_ID |
| CMP_GSP_ELIG_PROGRESSIONS_PK | Unique | Default | GSP_ELIG_PROGRESSION_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
