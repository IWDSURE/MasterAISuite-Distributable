# CMP_SALARY_

Salary holds details of salary proposals for Employee or Contingent worker assignments. A salary proposal may have one or more components, held in Salary Components. There can be  one/multiple unapproved salary proposal(s) at any time. When a salary proposal is approved, an element entry of type 'SP' (Salary Proposal) is created or updated to reflect the approval. The effective start date of the change to the salary element entry is the same as that of Salary Change date.

The details of Salary Components cannot be updated or inserted if the overall proposal has already been approved. A Salary may have one or multiple components associated with it. Approval of all components are handled in one transaction and cannot be addressed separately.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalary-15167.html#cmpsalary-15167](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalary-15167.html#cmpsalary-15167)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_SALARY_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, SALARY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Enterprise id FK to HR_ALL_ORGANIZATION_UNITS |
| ADJUSTED_FTE_FLAG | VARCHAR2 | 30 |  |  | If Adjusted FTE is used for salary record |
| ADJ_ANNUAL_SALARY | NUMBER |  |  |  | Adjusted Annual Salary based in Adjusted FTE |
| SALARY_TRANSACTION_STATUS | VARCHAR2 | 20 |  |  | Salary transaction status. |
| ASSIG_GRADE_LADDER_ID | NUMBER |  | 18 |  | ASSIG_GRADE_LADDER_ID |
| ASSIG_GRADE_STEP_ID | NUMBER |  | 18 |  | ASSIG_GRADE_STEP_ID |
| ASSIG_LOCATION_ID | NUMBER |  | 18 |  | ASSIG_LOCATION_ID |
| SALARY_JUSTIFICATION | VARCHAR2 | 2000 |  |  | SALARY_JUSTIFICATION |
| MISC_COMMENT1 | VARCHAR2 | 250 |  |  | MISC_COMMENT1 |
| MISC_COMMENT2 | VARCHAR2 | 250 |  |  | MISC_COMMENT2 |
| MISC_COMMENT3 | VARCHAR2 | 250 |  |  | MISC_COMMENT3 |
| MISC_COMMENT4 | VARCHAR2 | 250 |  |  | MISC_COMMENT4 |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | FK to PER_ACTION_OCCURRENCES |
| ACTION_ID | NUMBER |  | 18 |  | ACTION_ID |
| ACTION_REASON_ID | NUMBER |  | 18 |  | ACTION_REASON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | FK to Person's Work term assignment or Deployment Assignment. |
| SALARY_ID | NUMBER |  | 18 | Yes | Primary Key sequence for Salary. |
| SALARY_BASIS_ID | NUMBER |  | 18 |  | FK to Salary Basis |
| ELEMENT_ENTRY_ID | NUMBER |  | 18 |  | FK to payroll's PAY_ELEMENT_ENTRIES_F |
| DATE_FROM | DATE |  |  |  | Salary Start Date. |
| DATE_TO | DATE |  |  |  | Salary End Date |
| SALARY_REASON_CODE | VARCHAR2 | 30 |  |  | Salary change reason lookup code. |
| SALARY_AMOUNT | NUMBER |  |  |  | Salary Amount entered based on the Salary Basis salary frequency. |
| SALARY_APPROVED | VARCHAR2 | 30 |  |  | Yes or No flag if the Salary is approved or not. |
| MULTIPLE_COMPONENTS | VARCHAR2 | 30 |  |  | Yes or No flag to indicate if Salary Components are used or not. |
| PERFORMANCE_REVIEW_ID | NUMBER |  | 18 |  | FK to Person performance. |
| REVIEW_DATE | DATE |  |  |  | Performance review date. |
| PERFORMANCE_RATING | VARCHAR2 | 30 |  |  | Performance rating code. |
| NEXT_PERF_REVIEW_DATE | DATE |  |  |  | Next performance review date derived based on the frequency and period defined on the assignment. |
| NEXT_SAL_REVIEW_DATE | DATE |  |  |  | Next salary review date derived based on the frequency and period defined on the assignment. |
| FORCED_RANKING | NUMBER |  |  |  | FORCED_RANKING |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| ASSIGNMENT_TYPE | VARCHAR2 | 30 |  |  | ASSIGNMENT_TYPE |
| SALARY_BASIS_CODE | VARCHAR2 | 30 |  |  | SALARY_BASIS_CODE |
| SALARY_BASIS_TYPE | VARCHAR2 | 30 |  |  | SALARY_BASIS_TYPE |
| SALARY_FACTOR | NUMBER |  |  |  | SALARY_FACTOR |
| COMPONENT_USAGE | VARCHAR2 | 30 |  |  | COMPONENT_USAGE |
| PAYROLL_FREQUENCY_CODE | VARCHAR2 | 40 |  |  | PAYROLL_FREQUENCY_CODE |
| PAYROLL_FACTOR | NUMBER |  |  |  | PAYROLL_FACTOR |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | CURRENCY_CODE |
| ELEMENT_USAGE_LEVEL | VARCHAR2 | 1 |  |  | ELEMENT_USAGE_LEVEL |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | ELEMENT_TYPE_ID |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | INPUT_VALUE_ID |
| SALARY_AMOUNT_SCALE | NUMBER |  | 3 |  | SALARY_AMOUNT_SCALE |
| AMOUNT_ROUNDING_CODE | VARCHAR2 | 30 |  |  | AMOUNT_ROUNDING_CODE |
| ADJUSTMENT_AMOUNT | NUMBER |  |  |  | ADJUSTMENT_AMOUNT |
| ADJUSTMENT_AMOUNT_SCALE | NUMBER |  | 3 |  | ADJUSTMENT_AMOUNT_SCALE |
| ADJUSTMENT_PERCENT | NUMBER |  |  |  | ADJUSTMENT_PERCENT |
| ADJUSTMENT_PERCENT_SCALE | NUMBER |  | 3 |  | ADJUSTMENT_PERCENT_SCALE |
| ANNUAL_SALARY | NUMBER |  |  |  | ANNUAL_SALARY |
| ANNUAL_ROUNDING_CODE | VARCHAR2 | 30 |  |  | ANNUAL_ROUNDING_CODE |
| ANNUAL_FT_SALARY | NUMBER |  |  |  | ANNUAL_FT_SALARY |
| QUARTILE | VARCHAR2 | 30 |  |  | QUARTILE |
| QUINTILE | VARCHAR2 | 30 |  |  | QUINTILE |
| COMPA_RATIO | NUMBER |  |  |  | COMPA_RATIO |
| RANGE_POSITION | NUMBER |  |  |  | RANGE_POSITION |
| FTE_VALUE | NUMBER |  |  |  | FTE_VALUE |
| ADJUSTED_FTE_VALUE | NUMBER |  |  |  | Adjusted FTE value |
| GRADE_ID | NUMBER |  | 18 |  | GRADE_ID |
| RATE_ID | NUMBER |  | 18 |  | RATE_ID |
| RATE_FACTOR | NUMBER |  |  |  | RATE_FACTOR |
| RATE_MIN_AMOUNT | NUMBER |  |  |  | RATE_MIN_AMOUNT |
| RATE_MID_AMOUNT | NUMBER |  |  |  | RATE_MID_AMOUNT |
| RATE_MAX_AMOUNT | NUMBER |  |  |  | RATE_MAX_AMOUNT |
| RATE_DEFAULT_AMOUNT | NUMBER |  |  |  | RATE_DEFAULT_AMOUNT |
| SALARY_RANGE_SCALE | NUMBER |  | 3 |  | SALARY_RANGE_SCALE |
| RANGE_ROUNDING_CODE | VARCHAR2 | 30 |  |  | RANGE_ROUNDING_CODE |
| COMPA_RATIO_SCALE | NUMBER |  | 3 |  | COMPA_RATIO_SCALE |
| RANGE_POSITION_SCALE | NUMBER |  | 3 |  | RANGE_POSITION_SCALE |
| RANGE_ERROR_WARNING | VARCHAR2 | 30 |  |  | RANGE_ERROR_WARNING |
| RANGE_ANALYTICS_FOR_EMP | VARCHAR2 | 1 |  |  | RANGE_ANALYTICS_FOR_EMP |
| RANGE_ANALYTICS_FOR_MGR | VARCHAR2 | 1 |  |  | RANGE_ANALYTICS_FOR_MGR |
| DISABLE_QUARTILE | VARCHAR2 | 1 |  |  | DISABLE_QUARTILE |
| DISABLE_QUINTILE | VARCHAR2 | 1 |  |  | DISABLE_QUINTILE |
| DISABLE_COMPA_RATIO | VARCHAR2 | 1 |  |  | DISABLE_COMPA_RATIO |
| DISABLE_RANGE_POSITION | VARCHAR2 | 1 |  |  | DISABLE_RANGE_POSITION |
| TOTAL_BASE_PAY | NUMBER |  |  |  | TOTAL_BASE_PAY |
| TOTAL_COMPONENT_ADJ_AMT | NUMBER |  |  |  | TOTAL_COMPONENT_ADJ_AMT |
| TOTAL_COMPONENT_ADJ_PERCENT | NUMBER |  |  |  | TOTAL_COMPONENT_ADJ_PERCENT |
| GEOGRAPHY_ID | NUMBER |  | 18 |  | Geography Id. |
| GEOGRAPHY_TYPE_ID | NUMBER |  | 18 |  | Geography Type Id. |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Business Unit Id. |
| JOB_ID | NUMBER |  | 18 |  | Job Id. |
| WORK_AT_HOME | VARCHAR2 | 30 |  |  | Work at home. |
| GRADE_RATE_MINIMUM_LIMIT | NUMBER |  |  |  | Grade rate minimum limit. |
| ZONE_GRADE_RATE_ID | NUMBER |  | 18 |  | Zone grade rate id |
| FTE_IMPACT | VARCHAR2 | 30 |  |  | FTE_IMPACT |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| ADJ_ANNUAL_FT_SALARY | NUMBER |  |  |  | Adjusted Annual Fulltime Salary based on adjusted FTE vale |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_SALARYN1_ | Non Unique | Default | SALARY_ID, LAST_UPDATE_DATE |
| CMP_SALARYN2_ | Non Unique | Default | AUDIT_ACTION_TYPE_ |
| CMP_SALARY_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, SALARY_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
