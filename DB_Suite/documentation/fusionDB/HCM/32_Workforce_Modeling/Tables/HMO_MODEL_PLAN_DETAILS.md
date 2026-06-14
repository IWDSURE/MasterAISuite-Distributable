# HMO_MODEL_PLAN_DETAILS

Model plan details table  stores the new proposal details.

## Details

**Schema:** FUSION

**Object owner:** HMO

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hmomodelplandetails-28882.html#hmomodelplandetails-28882](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hmomodelplandetails-28882.html#hmomodelplandetails-28882)

## Primary Key

| Name | Columns |
|------|----------|
| HMO_MODEL_PLAN_DETAILS_PK | MODEL_PLAN_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise of the record. |
| MODEL_PLAN_DETAIL_ID | NUMBER |  | 18 | Yes | Model Plan Detail Id. The primary key. |
| MODEL_PLAN_DETAIL_TYPE | VARCHAR2 | 30 |  | Yes | Column indicates type of the record. The valid values are SNAPSHOT , MODELED , SYNC etc.... |
| MODEL_PLAN_ASG_TYPE | VARCHAR2 | 30 |  |  | Column indicates type of the assignment. The valid values are  INTERNAL ASSIGNMENT ,  EXTERNAL ASSIGNMENT , VACANCY . |
| MODEL_PLAN_ID | NUMBER |  | 18 | Yes | Model Plan Id . This is foreign key to HMO_MODEL_PLANS_B table. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | AssignemntId of the worker. This is foreign key to PER_ALL_ASSIGNMENTS_M. |
| PERSON_ID | NUMBER |  | 18 |  | PersonId of the worker. |
| ASG_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Worker's assignment last update date. |
| ASG_SUPERVISOR_ID | NUMBER |  | 18 |  | Assignment supervisor id |
| ASG_SUP_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment supervisor manager assignment id |
| ASG_SUP_MANAGER_ID | NUMBER |  | 18 |  | Assignment supervisor manager id |
| ASG_SUP_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Assignment supervisor record last update date. |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Legal Entity of the worker. |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | BusinessUnitId of the worker. |
| MANAGER_ID | NUMBER |  | 18 |  | Manager Id |
| MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Manager Assignment Id |
| ASSIGN_GRADE_STEP_ID | NUMBER |  | 18 |  | Assign Grade Step Id primary key |
| GRADE_STEP_ID | NUMBER |  | 18 |  | Worker Grade Step Id |
| GRADE_ID | NUMBER |  | 18 |  | Worker Grade Id |
| GRADE_STEP_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Grade step last update date. |
| JOB_ID | NUMBER |  | 18 |  | Worker Job Id |
| LOCATION_ID | NUMBER |  | 18 |  | Wroker Location Id |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Worker Organization Id |
| POSITION_ID | NUMBER |  | 18 |  | Worker Position Id |
| PEOPLE_GROUP_ID | NUMBER |  | 18 |  | Assignments people group id. |
| WORK_AT_HOME | VARCHAR2 | 30 |  |  | Work At Home Flag. |
| INTERNAL_BUILDING | VARCHAR2 | 45 |  |  | Internal Building |
| INTERNAL_FLOOR | VARCHAR2 | 45 |  |  | Internal Floor. |
| INTERNAL_OFFICE_NUMBER | VARCHAR2 | 45 |  |  | Internal Office Number |
| INTERNAL_MAILSTOP | VARCHAR2 | 45 |  |  | Internal Mail Stop |
| MANAGER_FLAG | VARCHAR2 | 30 |  |  | Manager Flag |
| NORMAL_HOURS | NUMBER |  | 22 |  | Normal Working Hours |
| FREQUENCY | VARCHAR2 | 30 |  |  | Frequency |
| TIME_NORMAL_START | VARCHAR2 | 5 |  |  | TIME_NORMAL_START |
| TIME_NORMAL_FINISH | VARCHAR2 | 5 |  |  | TIME_NORMAL_FINISH |
| HOURLY_SALARIED_CODE | VARCHAR2 | 30 |  |  | HOURLY_SALARIED_CODE |
| ASSIGNMENT_NAME | VARCHAR2 | 240 |  |  | ASSIGNMENT_NAME |
| ASSIGNMENT_STATUS_TYPE | VARCHAR2 | 30 |  |  | ASSIGNMENT_STATUS_TYPE |
| ASSIGNMENT_TYPE | VARCHAR2 | 20 |  |  | Assignment Type |
| LABOUR_UNION_MEMBER_FLAG | VARCHAR2 | 30 |  |  | Labour union Member |
| EMPLOYEE_CATEGORY | VARCHAR2 | 30 |  |  | Worker Category ;   Lookup Type = EMPLOYEE_CATG |
| EMPLOYMENT_CATEGORY | VARCHAR2 | 30 |  |  | Employment Category ; Lookup Type = EMP_CAT |
| ASSIGN_WORK_MEASURE_ID | NUMBER |  | 18 |  | AssignmentWorkMeasure primary key |
| WORK_MEASURE_FTE | NUMBER |  | 30 |  | Work measure FTE |
| ASG_FTE_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Assignment FTE record last update date. |
| BARGAINING_UNIT_CODE | VARCHAR2 | 30 |  |  | Bargaining Unit Code |
| CMP_SALARY_ID | NUMBER |  | 18 |  | Worker Salary Id |
| CMP_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Woker Salary Last Upate Date |
| SALARY_AMOUNT | NUMBER |  |  |  | Worker Salary Amount |
| CURRENCY_CODE | VARCHAR2 | 15 |  |  | Worker Currency  Code. |
| SALARY_REVIEW_DATE | DATE |  |  |  | Worker Salary Review Date |
| SALARY_BASIS_ID | NUMBER |  | 18 |  | Worker Salary Basis Id |
| ACTION_ID | NUMBER |  | 18 |  | Action Id . Foreign key to PER_ACTIONS_VL |
| ACTION_REASON_ID | NUMBER |  | 18 |  | Action Reason Id. Foreign key to PER_ACTION_REASONS_VL. |
| COMMENTS | VARCHAR2 | 240 |  |  | Comments about the changes . |
| REQUISITION_INTERFACE_ID | NUMBER |  | 18 |  | Vacancy identification id. |
| VACANCY_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Last updated date of vacancy. |
| VACANCY_OPEN_HEADCOUNT | NUMBER |  | 18 |  | Headcount for the vacancy. |
| VACANCY_JOB_SCHEDULE | VARCHAR2 | 30 |  |  | FTE value for the vacancy. |
| VACANCY_HIRED_HEADCOUNT | NUMBER |  | 18 |  | Vacancy hired Head count |
| VACANCY_UNLIMITED_HIRE | VARCHAR2 | 30 |  |  | Vacancy Unlimited hire |
| REQUISITION_NUMBER | VARCHAR2 | 20 |  |  | Vacancy Requisition Number |
| VALIDATION_STATUS | VARCHAR2 | 30 |  |  | Validation status like SUCCESS , FAILURE . |
| VALIDATION_ERROR | VARCHAR2 | 240 |  |  | Validation Error Message in case of failure. |
| INCLUDED_IN_BENCH | VARCHAR2 | 1 |  |  | Flag indicates whether the given record included in Bench or Not. Typical values are 'Y'/'N'. |
| LATEST_CHANGE | VARCHAR2 | 1 |  |  | Latest change , the default value is 'Y' |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ACCEPTED_TERMINATION_DATE | DATE |  |  |  | Accepted termination date of the worker. |
| ACTUAL_TERMINATION_DATE | DATE |  |  |  | Actual termination date of the worker. |
| NOTIFIED_TERMINATION_DATE | DATE |  |  |  | Notified termination date of the worker. |
| PROJECTED_TERMINATION_DATE | DATE |  |  |  | Projected termination date of the worker. |
| REHIRE_RECOMMENDATION | VARCHAR2 | 30 |  |  | Rehire Recommendation. Valid values Y or N |
| REHIRE_REASON | VARCHAR2 | 60 |  |  | Reason for Rehire. More description can be provided. |
| REHIRE_AUTHORIZER_PERSON_ID | NUMBER |  | 18 |  | PersonId of rehire authorized person. |
| REVOKE_USER_ACCESS | VARCHAR2 | 30 |  |  | Revoke User Access upon termination. Valid values Y or N |
| POSITION_CODE | VARCHAR2 | 30 |  |  | Unique Code of the Position |
| HIRING_STATUS | VARCHAR2 | 30 |  |  | Hiring status of the position |
| POSITION_TYPE | VARCHAR2 | 30 |  |  | Type of the position |
| FULL_PART_TIME | VARCHAR2 | 30 |  |  | Full time or Part time |
| PERMANENT_TEMPORARY_FLAG | VARCHAR2 | 30 |  |  | Permanent or Temporary Flag |
| PROBATION_UNIT | VARCHAR2 | 30 |  |  | Probation Unit |
| PROBATION_PERIOD | NUMBER |  | 22 |  | Probation Period |
| UNION_ID | NUMBER |  | 18 |  | Union Id of the worker or position |
| COLLECTIVE_AGREEMENT_ID | NUMBER |  | 18 |  | Collectibe agreement of the worker or position |
| GRADE_LADDER_PGM_ID | NUMBER |  | 18 |  | Grade Ladder of the worker or position |
| SECURITY_CLEARANCE | VARCHAR2 | 30 |  |  | Security Cleareance of the position. Valid values Y or N |
| SEASONAL_FLAG | VARCHAR2 | 30 |  |  | Seasonal flag of the position. Valid values Y or N |
| SEASONAL_START_DATE | DATE |  |  |  | Seasonal startdate of the position |
| SEASONAL_END_DATE | DATE |  |  |  | Seasonal enddate of the position |
| POS_EVAL_EVALUATION_ID | NUMBER |  | 18 |  | Position evaluation Id |
| POS_EVAL_EVALUATION_SYSTEM | VARCHAR2 | 30 |  |  | Position evaluation System |
| POS_EVAL_DATE_EVALUATED | DATE |  |  |  | Position evaluation date |
| POS_EVAL_MEASURED_IN | VARCHAR2 | 30 |  |  | Position Evaluation Measure |
| POS_EVAL_OVERALL_SCORE | NUMBER |  | 18 |  | Position Evaluation Overall Scope |
| POS_EVAL_ACCOUNTABILITY | NUMBER |  | 18 |  | Position Evaluation Accountability |
| POS_EVAL_KNOWHOW | NUMBER |  | 18 |  | Position Evaluation Know How |
| POS_EVAL_PROBLEM_SOLVING | NUMBER |  | 18 |  | Position Evaluation Problem Solving |
| POS_EVAL_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Position Evaluation Last Update Date |
| POSITION_OVERRIDE_FLAG | VARCHAR2 | 30 |  |  | Position Sync override flag |
| OPEN_HEAD_COUNT | NUMBER |  | 10 |  | Open Head count |
| OPEN_FTE | NUMBER |  | 30 |  | Open FTE |
| ANNUALIZED_SALARY_AMOUNT | NUMBER |  |  |  | Annualized Salary Amount. |
| PREDICTED_EFFECTIVENESS | NUMBER |  | 10 |  | Predicted Effectiveness |
| TRANSFERRED_OUT | VARCHAR2 | 30 |  |  | Flag used to determine wether given record is moved out of  top manager hierarchy or not. |
| PARENT_ASSIGNMENT_ID | NUMBER |  | 18 |  | Parent Assignment Id of the current Assignment. Used in diagrammer to display hierarchy. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HMO_MODEL_PLAN_DETAILS_N1 | Non Unique | Default | MODEL_PLAN_ID, MANAGER_ASSIGNMENT_ID |
| HMO_MODEL_PLAN_DETAILS_N2 | Non Unique | Default | MODEL_PLAN_ID, ASSIGNMENT_ID |
| HMO_MODEL_PLAN_DETAILS_N3 | Non Unique | Default | MODEL_PLAN_ID, POSITION_ID |
| HMO_MODEL_PLAN_DETAILS_PK | Unique | Default | MODEL_PLAN_DETAIL_ID |

---

[← Back to Index](../32_Workforce_Modeling_Tables_Index.md)
