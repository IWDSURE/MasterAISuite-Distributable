# IRC_REQUISITIONS_B_

Base table for Requisition details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircrequisitionsb-11805.html#ircrequisitionsb-11805](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircrequisitionsb-11805.html#ircrequisitionsb-11805)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REQUISITIONS_B_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, REQUISITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQUISITION_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| APPROVED_DATE | TIMESTAMP |  |  |  | Approved date of the requisition |
| INT_FIRST_POSTED_DATE | TIMESTAMP |  |  |  | First Internal Posted Date of Requisition |
| FILLED_DATE | TIMESTAMP |  |  |  | Stores the date at which Job Requisition is Filled |
| SUSPENDED_DURATION | NUMBER |  | 18 |  | Suspended duration of the requisition in seconds |
| EXT_FIRST_POSTED_DATE | TIMESTAMP |  |  |  | First External Posted Date of Requisition |
| REQ_SOURCE_TYPE | VARCHAR2 | 30 |  |  | Stores the source type of the Requisition. |
| OBJECT_STATUS | VARCHAR2 | 30 |  |  | Stores the status of the Object as a lookup code. The corresponding lookup type is ORA_IRC_OBJECT_STATUS. |
| REQUISITION_NUMBER | VARCHAR2 | 240 |  |  | Unique readable number for the Requistion. |
| REQ_USAGE_CODE | VARCHAR2 | 30 |  |  | Whether this instance is an actual Requisition or a Requisition Template. Stores the Requisition usage type as a lookup code. The corresponding lookup type is ORA_IRC_REQUISITION_USAGE. |
| RECRUITING_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the type of Recruiting as a lookup code. The corresponding lookup type is ORA_IRC_RECRUITING_TYPE. This colums accept NULL values. |
| CURRENT_PHASE_ID | NUMBER |  | 18 |  | Foreign key to IRC_PHASES_B table. |
| CURRENT_STATE_ID | NUMBER |  | 18 |  | Foreign key to IRC_STATES_B table. |
| PROCESS_ID | NUMBER |  | 18 |  | Foreign Key to process table IRC_PROCESS_B : store the PROCESS_ID use to track the lifecycle of this Requisition. |
| PROCESS_TEMPLATE_ID | NUMBER |  | 18 |  | Foreign Key to process table IRC_PROCESS_B : store the initial PROCESS_ID from which the proper PROCESS_ID of this requisition is an instance. |
| HIRING_MANAGER_ID | NUMBER |  | 18 |  | Stores the PERSON_ID of the hiring manager for this Requisition. Foreign key to PER_PERSONS table. |
| MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Stores the ASSIGNMENT_ID of the hiring manager's assignment for this Requisition. Foreign key to PER_ALL_ASSIGNMENTS_M table. |
| RECRUITER_ID | NUMBER |  | 18 |  | Foreign key to PER_PERSONS table. |
| RECRUITER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Stores the ASSIGNMENT_ID of the recruiter's assignment for this Requisition. Foreign key to PER_ALL_ASSIGNMENTS_M table. |
| REQUISITION_TEMPLATE_ID | NUMBER |  | 18 |  | Stores the ID of the template associated to the requisition. Foreign key to IRC_REQUISITIONS_B table. |
| MANAGER_LEVEL | VARCHAR2 | 30 |  |  | Stores the manager level as a lookup code. The corresponding lookup type is MANAGER_LEVEL. |
| FULL_PART_TIME | VARCHAR2 | 30 |  |  | Stores whether the opening is for a full or part time job, as a lookup code. The corresponding lookup type is FULL_PART_TIME. |
| WORKER_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the worker type as a lookup code. The corresponding lookup type is PER_PERIOD_TYPE. |
| WORK_START_DATE | TIMESTAMP |  |  |  | Work start date of the job. |
| WORK_END_DATE | TIMESTAMP |  |  |  | Work end date of the job. |
| JOB_SHIFT_CODE | VARCHAR2 | 30 |  |  | Stores the job shift for this Requisition as a lookup code. The corresponding lookup type is ORA_IRC_JOB_SHIFT. |
| JOB_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the job type for this Requisition as a lookup code. The corresponding lookup type is ORA_IRC_JOB_TYPE. |
| STUDY_LEVEL_CODE | VARCHAR2 | 30 |  |  | Stores the study level for this Requisition as a lookup code. The corresponding lookup type is HRT_EDUCATION_LEVEL. |
| INT_EMPLOYER_DESC_ID | NUMBER |  | 18 |  | Stores the ID of the internal employer description of the Requisition. Foreign key to IRC_DESCRIPTIONS_B table. |
| EXT_EMPLOYER_DESC_ID | NUMBER |  | 18 |  | Stores the ID of the external employer description of the Requisition. Foreign key to IRC_DESCRIPTIONS_B table. |
| INT_ORGANIZATION_DESC_ID | NUMBER |  | 18 |  | Stores the ID of the internal organization description of the Requisition. Foreign key to IRC_DESCRIPTIONS_B table. |
| EXT_ORGANIZATION_DESC_ID | NUMBER |  | 18 |  | Stores the ID of the external organization description of the Requisition. Foreign key to IRC_DESCRIPTIONS_B table. |
| JOB_ID | NUMBER |  | 18 |  | Foreign key to PER_JOBS_F table. |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Foreign key to HR_ALL_ORGANIZATION_UNITS_F table. |
| JOB_FAMILY_ID | NUMBER |  | 18 |  | Foreign key to PER_JOB_FAMILY_F |
| JOB_FUNCTION_CODE | VARCHAR2 | 30 |  |  | Stores the job function code for this Requisition as a lookup code. The corresponding lookup type is JOB_FUNCTION_CODE. |
| GEOGRAPHY_ID | NUMBER |  | 18 |  | Foreign key to HZ_GEOGRAPHIES table. |
| GEOGRAPHY_NODE_ID | NUMBER |  | 18 |  | Foreign key to IRC_GEO_HIER_NODES table. |
| LOCATION_ID | NUMBER |  | 18 |  | Stores the primary work location of the requisition. Foreign key to PER_LOCATIONS. |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Foreign key to HR_ALL_ORGANIZATION_UNITS_F table. |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | Foreign key to HR_ALL_ORGANIZATION_UNITS_F table. |
| GRADE_ID | NUMBER |  | 18 |  | Foreign key to PER_GRADES_F table. |
| DEPARTMENT_ID | NUMBER |  | 18 |  | Foreign key to HR_ALL_ORGANIZATION_UNITS_F table. |
| JUSTIFICATION_CODE | VARCHAR2 | 30 |  |  | Stores the Justification for this Requisition as a lookup code. The corresponding lookup type is ORA_IRC_REQ_JUSTIFICATION. |
| REGULAR_TEMPORARY | VARCHAR2 | 30 |  |  | Stores whether the opening is for a regular or temporary job, as a lookup code. The corresponding lookup type is REGULAR_TEMPORARY. |
| NUMBER_TO_HIRE | NUMBER |  | 9 |  | Stores the number of people to hire for this Requisition. |
| UNLIMITED_HIRE_FLAG | VARCHAR2 | 1 |  |  | Stores whether this Requisition can hire unlimited number of people. |
| HOT_JOB_FLAG | VARCHAR2 | 1 |  | Yes | Stores whether this Requisition should be considerate as a Hot Job or not |
| WORKPLACE_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the Workplace type value for this Requisition, as a lookup code.The corresponding lookup type is ORA_IRC_WORKPLACE_TYPE. |
| EXT_CONTACT_NAME | VARCHAR2 | 240 |  |  | Stores the External Contact name |
| EXT_CONTACT_EMAIL | VARCHAR2 | 240 |  |  | Stores the External Contact email |
| INT_CONTACT_NAME | VARCHAR2 | 240 |  |  | Stores the Internal contact name |
| INT_CONTACT_EMAIL | VARCHAR2 | 240 |  |  | Stores the Internal contact email |
| INT_PUBLISH_JOB_STATUS | VARCHAR2 | 30 |  |  | Stores the Internal published job status |
| INT_PUBLISH_JOB_START_DATE | DATE |  |  |  | Internal published job start date. |
| INT_PUBLISH_JOB_END_DATE | DATE |  |  |  | Internal published job end date. |
| EXT_PUBLISH_JOB_STATUS | VARCHAR2 | 30 |  |  | Stores the external published job status |
| EXT_PUBLISH_JOB_START_DATE | DATE |  |  |  | External published job start date |
| EXT_PUBLISH_JOB_END_DATE | DATE |  |  |  | External published job end date |
| BUDGET_CURRENCY_CODE | VARCHAR2 | 30 |  |  | Stores the currency code for the budget for this Requisition. Foreign key to FND_CURRENCIES table. |
| SOURCING_BUDGET | NUMBER |  |  |  | Stores the sourcing budget for this Requisition. |
| TRAVEL_BUDGET | NUMBER |  |  |  | Stores the travel budget for this Requisition. |
| RELOCATION_BUDGET | NUMBER |  |  |  | Stores the relocation budget allocated for this Requisition. |
| EMPLOYEE_REFERRAL_BONUS | NUMBER |  |  |  | Stores the amount for employee referral bonus. |
| MIN_SALARY | NUMBER |  |  |  | Stores the minimum salary for this Requisition. |
| MAX_SALARY | NUMBER |  |  |  | Stores the maximum salary for this Requisition. |
| SALARY_FREQUENCY_CODE | VARCHAR2 | 30 |  |  | Stores the salary frequency as a lookup code. The corresponding lookup type is CMP_SALARY_BASIS. |
| SALARY_CURRENCY_CODE | VARCHAR2 | 30 |  |  | Stores the salary currency information. Foreign key to FND_CURRENCIES table. |
| SALARY_PERIOD_CODE | VARCHAR2 | 30 |  |  | Stores the salary period as a lookup code. The corresponding lookup type is ORA_IRC_SALARY_PERIOD. This colums accept NULL values. |
| PROFILE_ID | NUMBER |  | 18 |  | Stores the corresponding job profile ID. Foreign key to HRT_PROFILES_B table. |
| DISPLAY_IN_ORG_CHART_FLAG | VARCHAR2 | 1 |  |  | Stores whether the requisition should appear in the Org Chart or not. |
| SYNC_JOB_VALUES_FLAG | VARCHAR2 | 1 |  |  | Store the boolean to indicate if, for a particular template, the values from "Job" object should always be synched with template |
| COMMENTS | CLOB |  |  |  | Stores comments about this requisition. |
| REQ_LAST_MODIFIED_DATE | TIMESTAMP |  |  |  | Stores the last modified date of the Requisition. It should be considered the equivalent of last update. |
| HIRED_COUNT | NUMBER |  | 9 |  | Stores the number of candidates hired on this Requisition. |
| SUBS_PROCESS_TEMPLATE_ID | NUMBER |  | 18 |  | Stores the ID of the process template that submissions on this requisition will follow. |
| EXTERNAL_APPLY_FLOW_ID | NUMBER |  | 18 |  | Apply Flow used for external candidates applying on this requisition. Foreign key to IRC_APPLY_FLOWS_B table. |
| PIPELINE_REQUISITION_ID | NUMBER |  | 18 |  | Stores the pipeline requisition the hiring requisition was created from Foreign key to IRC_REQUISITIONS_B |
| PIPELINE_REQUISITION_FLAG | VARCHAR2 | 1 |  |  | Stores whether the requisition is a pipeline requisition |
| APPLY_WHEN_NOT_POSTED_FLAG | VARCHAR2 | 1 |  |  | Stores whether the candidate can apply on a requisition when not posted. |
| POSITION_ID | NUMBER |  | 18 |  | Stores the corresponding position ID. Foreign key to HR_ALL_POSITIONS_F table. |
| AUTOMATIC_FILL_FLAG | VARCHAR2 | 1 |  |  | Stores whether the requisition can be auto-filled. |
| EXTERNAL_DESCRIPTION_ID | NUMBER |  | 18 |  | Stores the ID of the external description of the Requisition. Foreign key to IRC_DESCRIPTIONS_B table. |
| INTERNAL_DESCRIPTION_ID | NUMBER |  | 18 |  | Stores the ID of the internal description of the Requisition. Foreign key to IRC_DESCRIPTIONS_B table. |
| REQ_USAGE_TYPE | VARCHAR2 | 30 |  |  | Whether this instance is an actual Stand Alone, Job Based or Position Based requisition template. Stores the Requisition usage type as a lookup code. The corresponding lookup type is ORA_IRC_REQUISITION_USAGE_TYPE. |
| OPEN_DATE | TIMESTAMP |  |  |  | Stores the date at which the job requisition was changed to Open phase. |
| AUTO_OPEN_REQUISITION | VARCHAR2 | 30 |  |  | Stores whether the requisition can be auto posted. |
| AUTO_UNPOST_REQUISITION | VARCHAR2 | 30 |  |  | Stores whether the requisition can be auto unposted.  The corresponding lookup type is ORA_IRC_REQ_AUTO_UNPOST. |
| POSTING_EXPIRE_IN_DAYS | NUMBER |  |  |  | Stores the number of days after which the postings must expire. |
| UNPOST_FORMULA_ID | NUMBER |  | 18 |  | References the formula used to unpost the requisition. |
| TN_AGENCY_STATUS_CODE | VARCHAR2 | 30 |  |  | Stores the Talent Network Agency Status code. The corresponding lookup type is ORA_IRC_AGENCY_REQUISITION_STATUS. This column accepts NULL values. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTRIBUTE_TIMESTAMP1 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP2 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP3 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP4 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP5 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP6 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP7 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP8 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP9 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP10 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
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
| ATTRIBUTE_CHAR1 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR2 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR3 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR4 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR5 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR6 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR7 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR8 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR9 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR10 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR11 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR12 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR13 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR14 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR15 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR16 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR17 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR18 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR19 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR20 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR21 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR22 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR23 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR24 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR25 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR26 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR27 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR28 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR29 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR30 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 150 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REQUISITIONS_BN1_ | Non Unique | Default | REQUISITION_ID, LAST_UPDATE_DATE |
| IRC_REQUISITIONS_B_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, REQUISITION_ID |
| IRC_REQUISITIONS_B_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, REQ_USAGE_CODE, REQUISITION_NUMBER |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
