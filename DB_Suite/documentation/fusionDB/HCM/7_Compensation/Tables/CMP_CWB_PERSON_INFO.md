# CMP_CWB_PERSON_INFO

Stores all relevant data of persons in a compensation plan period including their names, IDs and supervisor details.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpersoninfo-15105.html#cmpcwbpersoninfo-15105](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpersoninfo-15105.html#cmpcwbpersoninfo-15105)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_PERSON_INFO_PK | PERSON_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | PERSON_EVENT_ID |  |  |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |  |  |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |  |  |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |  | Active |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |  | Active |
| ASSIGNMENT_ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ASSIGNMENT_ID |  |  |
| CUSTOM_NAME | VARCHAR2 | 480 |  |  | CUSTOM_NAME |  |  |
| EMAIL_ADDRESS | VARCHAR2 | 240 |  |  | EMAIL_ADDRESS |  | Active |
| WORKER_NUMBER | VARCHAR2 | 30 |  |  | WORKER_NUMBER |  | Active |
| PERSON_NUMBER | VARCHAR2 | 30 |  |  | PERSON_NUMBER |  |  |
| WS_MGR_PERSON_ID | NUMBER |  | 18 |  | WS_MGR_PERSON_ID |  | Active |
| WS_MGR_ASSIGNMENT_ID | NUMBER |  | 18 |  | WS_MGR_ASSIGNMENT_ID |  | Active |
| WS_MGR_PERSON_EVENT_ID | NUMBER |  | 18 |  | WS_MGR_PERSON_EVENT_ID |  |  |
| SUPERVISOR_ID | NUMBER |  | 18 |  | SUPERVISOR_ID |  | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  | Active |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | BUSINESS_UNIT_ID |  | Active |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |  |  |
| ORGANIZATION_ID | NUMBER |  | 18 |  | ORGANIZATION_ID |  | Active |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |  | Active |
| JOB_ID | NUMBER |  | 18 |  | JOB_ID |  | Active |
| JOB_SET_ID | NUMBER |  | 18 |  | JOB_SET_ID |  | Active |
| POSITION_ID | NUMBER |  | 18 |  | POSITION_ID |  | Active |
| GRADE_ID | NUMBER |  | 18 |  | GRADE_ID |  | Active |
| GRADE_SET_ID | NUMBER |  | 18 |  | GRADE_SET_ID |  | Active |
| DUE_DATE | DATE |  |  |  | DUE_DATE |  |  |
| ACCESS_CODE | VARCHAR2 | 30 |  |  | ACCESS_CODE |  |  |
| EMP_STATUS_CODE | VARCHAR2 | 30 |  |  | EMP_STATUS_CODE |  |  |
| MGR_STATUS_CODE | VARCHAR2 | 30 |  |  | MGR_STATUS_CODE |  |  |
| INTERCEPT_APPROVAL_FLAG | VARCHAR2 | 1 |  |  | INTERCEPT_APPROVAL_FLAG |  |  |
| APPROVAL_CODE | VARCHAR2 | 30 |  |  | APPROVAL_CODE |  |  |
| APPROVAL_DATE | DATE |  |  |  | APPROVAL_DATE |  |  |
| APPROVAL_COMMENTS | CLOB |  |  |  | APPROVAL_COMMENTS |  |  |
| SUBMIT_CODE | VARCHAR2 | 30 |  |  | SUBMIT_CODE |  |  |
| SUBMIT_DATE | DATE |  |  |  | SUBMIT_DATE |  |  |
| SUBMIT_COMMENTS | CLOB |  |  |  | SUBMIT_COMMENTS |  |  |
| BUDGET_STATUS_DATE | DATE |  |  |  | BUDGET_STATUS_DATE |  |  |
| PROGRESS_STATUS_DATE | DATE |  |  |  | PROGRESS_STATUS_DATE |  |  |
| SUBMIT_STATUS_DATE | DATE |  |  |  | SUBMIT_STATUS_DATE |  |  |
| APPROVAL_STATUS_DATE | DATE |  |  |  | APPROVAL_STATUS_DATE |  |  |
| FULL_APPROVAL_STATUS_DATE | DATE |  |  |  | FULL_APPROVAL_STATUS_DATE |  |  |
| EFFECTIVE_DATE | DATE |  |  |  | EFFECTIVE_DATE |  | Active |
| ASSIGNMENT_STATUS_TYPE_ID | NUMBER |  | 18 |  | ASSIGNMENT_STATUS_TYPE_ID |  | Active |
| PRIMARY_FLAG | VARCHAR2 | 30 |  |  | PRIMARY_FLAG |  | Active |
| PLACEHOLDER_FLAG | VARCHAR2 | 1 |  |  | PLACEHOLDER_FLAG |  |  |
| DATE_OF_BIRTH | DATE |  |  |  | DATE_OF_BIRTH |  |  |
| SEX | VARCHAR2 | 30 |  |  | SEX |  |  |
| ETHNICITY | VARCHAR2 | 30 |  |  | ETHNICITY |  |  |
| RELIGION | VARCHAR2 | 30 |  |  | RELIGION |  |  |
| DISABILITY_STATUS | VARCHAR2 | 30 |  |  | DISABILITY_STATUS |  |  |
| WORK_TELEPHONE | VARCHAR2 | 60 |  |  | WORK_TELEPHONE |  |  |
| NATIONALITY | VARCHAR2 | 30 |  |  | NATIONALITY |  |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |  | Active |
| START_DATE | DATE |  |  |  | START_DATE |  | Active |
| ORIGINAL_START_DATE | DATE |  |  |  | ORIGINAL_START_DATE |  | Active |
| ADJUSTED_SVC_DATE | DATE |  |  |  | ADJUSTED_SVC_DATE |  | Active |
| EMPLOYMENT_CATEGORY | VARCHAR2 | 30 |  |  | EMPLOYMENT_CATEGORY |  | Active |
| YEARS_EMPLOYED | NUMBER |  |  |  | YEARS_EMPLOYED |  | Active |
| YEARS_IN_JOB | NUMBER |  |  |  | YEARS_IN_JOB |  | Active |
| YEARS_IN_POSITION | NUMBER |  |  |  | YEARS_IN_POSITION |  | Active |
| YEARS_IN_GRADE | NUMBER |  |  |  | YEARS_IN_GRADE |  | Active |
| JOB_CHANGE_DATE | DATE |  |  |  | JOB_CHANGE_DATE |  |  |
| POSITION_CHANGE_DATE | DATE |  |  |  | POSITION_CHANGE_DATE |  |  |
| GRADE_CHANGE_DATE | DATE |  |  |  | GRADE_CHANGE_DATE |  |  |
| JOB_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | JOB_ATTRIBUTE1 |  |  |
| JOB_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | JOB_ATTRIBUTE2 |  |  |
| JOB_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | JOB_ATTRIBUTE3 |  |  |
| JOB_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | JOB_ATTRIBUTE4 |  |  |
| JOB_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | JOB_ATTRIBUTE5 |  |  |
| JOB_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | JOB_ATTRIBUTE6 |  |  |
| GRADE_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | GRADE_ATTRIBUTE1 |  |  |
| GRADE_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | GRADE_ATTRIBUTE2 |  |  |
| GRADE_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | GRADE_ATTRIBUTE3 |  |  |
| NORMAL_HOURS | NUMBER |  |  |  | NORMAL_HOURS |  | Active |
| WORKING_HOURS | NUMBER |  |  |  | WORKING_HOURS |  |  |
| FTE_FACTOR | NUMBER |  |  |  | FTE_FACTOR |  | Active |
| BASE_SALARY | NUMBER |  |  |  | BASE_SALARY |  | Active |
| BASE_SALARY_CURRENCY | VARCHAR2 | 30 |  |  | BASE_SALARY_CURRENCY |  | Active |
| BASE_SALARY_FREQUENCY | VARCHAR2 | 30 |  |  | BASE_SALARY_FREQUENCY |  | Active |
| BASE_SALARY_CHANGE_DATE | DATE |  |  |  | BASE_SALARY_CHANGE_DATE |  | Active |
| BASE_SALARY_CHANGE_VAL | NUMBER |  |  |  | BASE_SALARY_CHANGE_VAL |  |  |
| PREVIOUS_BONUS | NUMBER |  |  |  | PREVIOUS_BONUS |  |  |
| CURRENT_SALARY_ID | NUMBER |  | 18 |  | CURRENT_SALARY_ID |  |  |
| SALARY_BASIS_ID | NUMBER |  | 18 |  | SALARY_BASIS_ID |  |  |
| PAYROLL_ID | NUMBER |  | 18 |  | PAYROLL_ID |  |  |
| FREQUENCY | VARCHAR2 | 30 |  |  | FREQUENCY |  | Active |
| PAY_ANNUALIZATION_FACTOR | NUMBER |  |  |  | PAY_ANNUALIZATION_FACTOR |  | Active |
| GRADE_ANNUALIZATION_FACTOR | NUMBER |  |  |  | GRADE_ANNUALIZATION_FACTOR |  | Active |
| GRADE_RATE_ID | NUMBER |  | 18 |  | GRADE_RATE_ID |  |  |
| GRADE_RATE_FREQUENCY | VARCHAR2 | 30 |  |  | GRADE_RATE_FREQUENCY |  | Active |
| GRADE_MIN_VAL | NUMBER |  |  |  | GRADE_MIN_VAL |  |  |
| GRADE_MID_POINT | NUMBER |  |  |  | GRADE_MID_POINT |  |  |
| GRADE_MAX_VAL | NUMBER |  |  |  | GRADE_MAX_VAL |  |  |
| GRADE_QUARTILE | VARCHAR2 | 30 |  |  | GRADE_QUARTILE |  |  |
| GRADE_QUINTILE | VARCHAR2 | 30 |  |  | GRADE_QUINTILE |  |  |
| GRADE_DECILE | VARCHAR2 | 30 |  |  | GRADE_DECILE |  |  |
| GRADE_COMPARATIO | NUMBER |  |  |  | GRADE_COMPARATIO |  |  |
| GRADE_PCT_IN_RANGE | NUMBER |  |  |  | GRADE_PCT_IN_RANGE |  |  |
| PERFORMANCE_RATING | NUMBER |  | 18 |  | PERFORMANCE_RATING |  | Active |
| PERFORMANCE_RATING_TYPE | VARCHAR2 | 30 |  |  | PERFORMANCE_RATING_TYPE |  | Active |
| PERFORMANCE_RATING_DATE | DATE |  |  |  | PERFORMANCE_RATING_DATE |  | Active |
| MGR_OVERRIDE_DATE | DATE |  |  |  | MGR_OVERRIDE_DATE |  |  |
| MGR_OVERRIDE_PERSON_ID | NUMBER |  | 18 |  | MGR_OVERRIDE_PERSON_ID |  |  |
| CUSTOM_SEGMENT1 | VARCHAR2 | 150 |  |  | CUSTOM_SEGMENT1 |  | Active |
| CUSTOM_SEGMENT2 | VARCHAR2 | 150 |  |  | CUSTOM_SEGMENT2 |  | Active |
| CUSTOM_SEGMENT3 | VARCHAR2 | 150 |  |  | CUSTOM_SEGMENT3 |  | Active |
| CUSTOM_SEGMENT4 | VARCHAR2 | 150 |  |  | CUSTOM_SEGMENT4 |  | Active |
| CUSTOM_SEGMENT5 | VARCHAR2 | 150 |  |  | CUSTOM_SEGMENT5 |  | Active |
| CUSTOM_SEGMENT6 | VARCHAR2 | 150 |  |  | CUSTOM_SEGMENT6 |  | Active |
| CUSTOM_SEGMENT7 | VARCHAR2 | 150 |  |  | CUSTOM_SEGMENT7 |  | Active |
| CUSTOM_SEGMENT8 | VARCHAR2 | 150 |  |  | CUSTOM_SEGMENT8 |  | Active |
| CUSTOM_SEGMENT9 | VARCHAR2 | 150 |  |  | CUSTOM_SEGMENT9 |  | Active |
| CUSTOM_SEGMENT10 | VARCHAR2 | 150 |  |  | CUSTOM_SEGMENT10 |  | Active |
| CUSTOM_SEGMENT11 | VARCHAR2 | 150 |  |  | CUSTOM_SEGMENT11 |  | Active |
| CUSTOM_SEGMENT12 | VARCHAR2 | 4000 |  |  | CUSTOM_SEGMENT12 |  | Active |
| CUSTOM_SEGMENT13 | VARCHAR2 | 4000 |  |  | CUSTOM_SEGMENT13 |  | Active |
| CUSTOM_SEGMENT14 | VARCHAR2 | 4000 |  |  | CUSTOM_SEGMENT14 |  | Active |
| CUSTOM_SEGMENT15 | VARCHAR2 | 4000 |  |  | CUSTOM_SEGMENT15 |  | Active |
| CUSTOM_SEGMENT16 | NUMBER |  |  |  | CUSTOM_SEGMENT16 |  | Active |
| CUSTOM_SEGMENT17 | NUMBER |  |  |  | CUSTOM_SEGMENT17 |  | Active |
| CUSTOM_SEGMENT18 | NUMBER |  |  |  | CUSTOM_SEGMENT18 |  | Active |
| CUSTOM_SEGMENT19 | NUMBER |  |  |  | CUSTOM_SEGMENT19 |  | Active |
| CUSTOM_SEGMENT20 | NUMBER |  |  |  | CUSTOM_SEGMENT20 |  | Active |
| CUSTOM_SEGMENT21 | NUMBER |  |  |  | CUSTOM_SEGMENT21 |  | Active |
| CUSTOM_SEGMENT22 | NUMBER |  |  |  | CUSTOM_SEGMENT22 |  | Active |
| CUSTOM_SEGMENT23 | NUMBER |  |  |  | CUSTOM_SEGMENT23 |  | Active |
| CUSTOM_SEGMENT24 | NUMBER |  |  |  | CUSTOM_SEGMENT24 |  | Active |
| CUSTOM_SEGMENT25 | NUMBER |  |  |  | CUSTOM_SEGMENT25 |  | Active |
| CUSTOM_SEGMENT26 | NUMBER |  |  |  | CUSTOM_SEGMENT26 |  | Active |
| CUSTOM_SEGMENT27 | NUMBER |  |  |  | CUSTOM_SEGMENT27 |  | Active |
| CUSTOM_SEGMENT28 | NUMBER |  |  |  | CUSTOM_SEGMENT28 |  | Active |
| CUSTOM_SEGMENT29 | NUMBER |  |  |  | CUSTOM_SEGMENT29 |  | Active |
| CUSTOM_SEGMENT30 | NUMBER |  |  |  | CUSTOM_SEGMENT30 |  | Active |
| CUSTOM_SEGMENT31 | NUMBER |  |  |  | CUSTOM_SEGMENT31 |  | Active |
| CUSTOM_SEGMENT32 | NUMBER |  |  |  | CUSTOM_SEGMENT32 |  | Active |
| CUSTOM_SEGMENT33 | NUMBER |  |  |  | CUSTOM_SEGMENT33 |  | Active |
| CUSTOM_SEGMENT34 | NUMBER |  |  |  | CUSTOM_SEGMENT34 |  | Active |
| CUSTOM_SEGMENT35 | NUMBER |  |  |  | CUSTOM_SEGMENT35 |  | Active |
| CUSTOM_SEGMENT36 | NUMBER |  |  |  | CUSTOM_SEGMENT36 |  | Active |
| CUSTOM_SEGMENT37 | NUMBER |  |  |  | CUSTOM_SEGMENT37 |  | Active |
| CUSTOM_SEGMENT38 | NUMBER |  |  |  | CUSTOM_SEGMENT38 |  | Active |
| CUSTOM_SEGMENT39 | NUMBER |  |  |  | CUSTOM_SEGMENT39 |  | Active |
| CUSTOM_SEGMENT40 | NUMBER |  |  |  | CUSTOM_SEGMENT40 |  | Active |
| CUSTOM_SEGMENT41 | NUMBER |  |  |  | CUSTOM_SEGMENT41 |  | Active |
| CUSTOM_SEGMENT42 | NUMBER |  |  |  | CUSTOM_SEGMENT42 |  | Active |
| CUSTOM_SEGMENT43 | NUMBER |  |  |  | CUSTOM_SEGMENT43 |  | Active |
| CUSTOM_SEGMENT44 | NUMBER |  |  |  | CUSTOM_SEGMENT44 |  | Active |
| CUSTOM_SEGMENT45 | NUMBER |  |  |  | CUSTOM_SEGMENT45 |  | Active |
| CUSTOM_SEGMENT46 | NUMBER |  |  |  | CUSTOM_SEGMENT46 |  | Active |
| CUSTOM_SEGMENT47 | NUMBER |  |  |  | CUSTOM_SEGMENT47 |  | Active |
| CUSTOM_SEGMENT48 | NUMBER |  |  |  | CUSTOM_SEGMENT48 |  | Active |
| CUSTOM_SEGMENT49 | NUMBER |  |  |  | CUSTOM_SEGMENT49 |  | Active |
| CUSTOM_SEGMENT50 | NUMBER |  |  |  | CUSTOM_SEGMENT50 |  | Active |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Workforce Compensation Person Information (CMP_CWB_PERSON_INFO) |  |
| CAREER_LEVEL | VARCHAR2 | 30 |  |  | CAREER_LEVEL |  |  |
| WORKER_POTENTIAL | NUMBER |  | 18 |  | WORKER_POTENTIAL |  |  |
| RISK_OF_LOSS | NUMBER |  | 18 |  | RISK_OF_LOSS |  |  |
| VETERAN_STATUS | VARCHAR2 | 30 |  |  | VETERAN_STATUS |  |  |
| NON_DISCRIMINATION_CODE | VARCHAR2 | 30 |  |  | NON_DISCRIMINATION_CODE |  |  |
| NEW_BASE_SALARY | NUMBER |  |  |  | NEW_BASE_SALARY |  |  |
| NEW_GRADE_QUARTILE | VARCHAR2 | 30 |  |  | NEW_GRADE_QUARTILE |  |  |
| NEW_GRADE_QUINTILE | VARCHAR2 | 30 |  |  | NEW_GRADE_QUINTILE |  |  |
| NEW_GRADE_DECILE | VARCHAR2 | 30 |  |  | NEW_GRADE_DECILE |  |  |
| NEW_GRADE_COMPARATIO | NUMBER |  |  |  | NEW_GRADE_COMPARATIO |  |  |
| NEW_GRADE_PCT_IN_RANGE | NUMBER |  |  |  | NEW_GRADE_PCT_IN_RANGE |  |  |
| ACTION_REASON_ID | NUMBER |  | 18 |  | ACTION_REASON_ID |  |  |
| STMT_TEMPLATE_ID | NUMBER |  | 18 |  | STMT_TEMPLATE_ID |  |  |
| DO_NOT_POST_FLAG | VARCHAR2 | 1 |  |  | DO_NOT_POST_FLAG |  |  |
| DYN_CALC_FLAG | VARCHAR2 | 1 |  |  | DYN_CALC_FLAG |  |  |
| REFRESH_MANAGER_FLAG | VARCHAR2 | 1 |  |  | REFRESH_MANAGER_FLAG |  |  |
| REFRESH_ELIGIBILITY_FLAG | VARCHAR2 | 1 |  |  | REFRESH_ELIGIBILITY_FLAG |  |  |
| ASSIGNMENT_POSTING_DATE | DATE |  |  |  | ASSIGNMENT_POSTING_DATE |  |  |
| ASSIGNMENT_POSTED_DATE | DATE |  |  |  | ASSIGNMENT_POSTED_DATE |  |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  | Active |
| RVW_MGR_ASSIGNMENT_ID | NUMBER |  | 18 |  | REVIEW MANAGER'S ASSIGNMENT ID |  |  |
| RVW_MGR_PERSON_ID | NUMBER |  | 18 |  | REVIEW MANAGER'S PERSON ID |  |  |
| RVW_MGR_PERSON_EVENT_ID | NUMBER |  | 18 |  | REVIEW MANAGER'S PERSON EVENT ID |  |  |
| RVW_MGR_OVERRIDE_DATE | DATE |  |  |  | RVW_MGR_OVERRIDE_DATE |  |  |
| RVW_MGR_OVERRIDE_PERSON_ID | NUMBER |  | 18 |  | RVW_MGR_OVERRIDE_PERSON_ID |  |  |
| SEC_MGR_ASSIGNMENT_ID | NUMBER |  | 18 |  | SECONDARY MANAGER'S ASSIGNMENT ID |  |  |
| SEC_MGR_PERSON_ID | NUMBER |  | 18 |  | SECONDARY MANAGER'S PERSON ID |  |  |
| SEC_MGR_PERSON_EVENT_ID | NUMBER |  | 18 |  | SECONDARY MANAGER'S PERSON EVENT ID |  |  |
| SEC_MGR_ACCESS_CODE | VARCHAR2 | 30 |  |  | SEC_MGR_ACCESS_CODE |  |  |
| RVW_MGR_ACCESS_CODE | VARCHAR2 | 30 |  |  | RVW_MGR_ACCESS_CODE |  |  |
| REFRESH_SEC_MANAGER_FLAG | VARCHAR2 | 1 |  |  | REFRESH_SEC_MANAGER_FLAG |  |  |
| REFRESH_RVW_MANAGER_FLAG | VARCHAR2 | 1 |  |  | REFRESH_RVW_MANAGER_FLAG |  |  |
| SEC_MGR_OVERRIDE_DATE | DATE |  |  |  | SEC_MGR_OVERRIDE_DATE |  |  |
| SEC_MGR_OVERRIDE_PERSON_ID | NUMBER |  | 18 |  | SEC_MGR_OVERRIDE_PERSON_ID |  |  |
| RANGE_DIFF_ID | NUMBER |  | 18 |  | RANGE_DIFF_ID |  |  |
| SALARY_RANGE_DIFFERENTIAL | NUMBER |  |  |  | SALARY_RANGE_DIFFERENTIAL |  |  |
| DUE_DATE_NOTIFIED_FLAG | VARCHAR2 | 1 |  |  | DUE_DATE_NOTIFIED_FLAG |  |  |
| SALARY_BASIS_TYPE | VARCHAR2 | 30 |  |  | SALARY_BASIS_TYPE |  |  |
| OPEN_CLOSE_NOTIFIED_FLAG | VARCHAR2 | 1 |  |  | OPEN_CLOSE_NOTIFIED_FLAG |  |  |
| ASSIGNMENT_NAME | VARCHAR2 | 80 |  |  | ASSIGNMENT_NAME |  |  |
| SALARY_RUN_ID | NUMBER |  | 18 |  | SALARY_RUN_ID |  |  |
| STOCK_RUN_ID | NUMBER |  | 18 |  | STOCK_RUN_ID |  |  |
| PROMOTION_RUN_ID | NUMBER |  | 18 |  | PROMOTION_RUN_ID |  |  |
| REFRESH_WORKER_FLAG | VARCHAR2 | 1 |  |  | REFRESH_WORKER_FLAG |  |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |  |
| DYN_CALC_SRC | VARCHAR2 | 30 |  |  | DYN_CALC_SRC |  |  |
| GRADE_MIN_LIMIT | NUMBER |  |  |  | GRADE_MIN_LIMIT |  |  |
| SOURCE_ASSIGNMENT_ID | NUMBER |  | 18 |  | SOURCE_ASSIGNMENT_ID |  |  |
| GRADE_LADDER_PGM_ID | NUMBER |  | 18 |  | GRADE_LADDER_PGM_ID |  |  |
| GRADE_STEP_ID | NUMBER |  | 18 |  | GRADE_STEP_ID |  |  |
| CUSTOM_DATE_SEGMENT1 | DATE |  |  |  | CUSTOM_DATE_SEGMENT1 |  |  |
| CUSTOM_DATE_SEGMENT2 | DATE |  |  |  | CUSTOM_DATE_SEGMENT2 |  |  |
| CUSTOM_DATE_SEGMENT3 | DATE |  |  |  | CUSTOM_DATE_SEGMENT3 |  |  |
| CUSTOM_DATE_SEGMENT4 | DATE |  |  |  | CUSTOM_DATE_SEGMENT4 |  |  |
| CUSTOM_DATE_SEGMENT5 | DATE |  |  |  | CUSTOM_DATE_SEGMENT5 |  |  |
| CUSTOM_DATE_SEGMENT6 | DATE |  |  |  | CUSTOM_DATE_SEGMENT6 |  |  |
| EVALUATION_ID | NUMBER |  | 18 |  | EVALUATION_ID |  |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_PERSON_INFO_N1 | Non Unique | Default | PERIOD_ID, PLAN_ID, ASSIGNMENT_ASSIGNMENT_ID |
| CMP_CWB_PERSON_INFO_N10 | Non Unique | Default | RVW_MGR_PERSON_EVENT_ID, PERIOD_ID, PLAN_ID |
| CMP_CWB_PERSON_INFO_N2 | Non Unique | Default | ASSIGNMENT_ID, PERIOD_ID, PLAN_ID |
| CMP_CWB_PERSON_INFO_N3 | Non Unique | Default | PERSON_ID |
| CMP_CWB_PERSON_INFO_N4 | Non Unique | Default | WORKER_NUMBER |
| CMP_CWB_PERSON_INFO_N5 | Non Unique | Default | UPPER("EMAIL_ADDRESS") |
| CMP_CWB_PERSON_INFO_N6 | Non Unique | Default | WS_MGR_PERSON_ID |
| CMP_CWB_PERSON_INFO_N7 | Non Unique | Default | WS_MGR_PERSON_EVENT_ID, PERIOD_ID, PLAN_ID |
| CMP_CWB_PERSON_INFO_N8 | Non Unique | Default | UPPER("PERSON_NUMBER") |
| CMP_CWB_PERSON_INFO_N9 | Non Unique | Default | SEC_MGR_PERSON_EVENT_ID, PERIOD_ID, PLAN_ID |
| CMP_CWB_PERSON_INFO_PK | Unique | Default | PERSON_EVENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
