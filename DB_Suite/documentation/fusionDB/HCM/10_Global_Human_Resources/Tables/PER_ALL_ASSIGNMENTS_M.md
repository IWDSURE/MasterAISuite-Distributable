# PER_ALL_ASSIGNMENTS_M

This stores two levels of the 3-Tier Model: Employment/Placement Terms (Level 2) and Assignments (Level 3). The assignment type is used to differentiate between these two levels as well as it continues to differentiate among employee, contingent worker, applicants, and benefits assignments.
This is date-tracked and allows multiple changes in a day.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perallassignmentsm-24924.html#perallassignmentsm-24924](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perallassignmentsm-24924.html#perallassignmentsm-24924)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ALL_ASSIGNMENTS_M_PK | ASSIGNMENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, EFFECTIVE_LATEST_CHANGE, EFFECTIVE_SEQUENCE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | This is a system generated primary key. Surrogate key. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| PERSON_ID | NUMBER |  | 18 | Yes | Identifies person holding an assignment or a set of Employment/Placement Terms. Foreign key to PER_PERSONS. |  |
| PERIOD_OF_SERVICE_ID | NUMBER |  | 18 |  | Identifies the Employment Level. Foreign key to PER_PERIODS_OF_SERVICE. |  |
| ASSIGNMENT_TYPE | VARCHAR2 | 30 |  | Yes | Identifies the type of record: either assignment (employee, CWK, applicant, non-workers) or a set of Terms. |  |
| ASSIGNMENT_NUMBER | VARCHAR2 | 50 |  |  | Uniquely identifies the assignment or terms. Valid for Workers and non-workers. Assignment Level:By default [Person Number ] - [sequence] Work Term Level:[sequence] |  |
| ASSIGNMENT_SEQUENCE | NUMBER |  | 18 | Yes | Used when defaulting assignment number. |  |
| ASSIGNMENT_STATUS_TYPE_ID | NUMBER |  | 18 | Yes | Denormalized status of the assignment. This is derived using the Assignment Status Type ID. |  |
| PRIMARY_FLAG | VARCHAR2 | 30 |  | Yes | Primary flag. Accepts value of ?Y? or ?N? based on ?YES_NO? lookup type. If set to ?Yes?, record represents the primary assignment associated to the primary Work Relationship and primary set of Employment/Placement Terms. |  |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Department Identifier, it is optional. |  |
| JOB_ID | NUMBER |  | 18 |  | Foreign key to PER_JOBS_F. |  |
| LOCATION_ID | NUMBER |  | 18 |  | Foreign key to HR_LOCATIONS_ALL_F. |  |
| POSITION_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_POSITIONS_F. |  |
| GRADE_ID | NUMBER |  | 18 |  | Foreign key to PER_GRADES_F. |  |
| GRADE_LADDER_PGM_ID | NUMBER |  | 18 |  | Link assignment to grade ladder for Benefits. |  |
| PEOPLE_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_PEOPLE_GROUPS. |  |
| COLLECTIVE_AGREEMENT_ID | NUMBER |  | 18 |  | Foreign key to PER_COLLECTIVE_AGREEMENTS. |  |
| BARGAINING_UNIT_CODE | VARCHAR2 | 30 |  |  | Bargaining unit code. |  |
| LABOUR_UNION_MEMBER_FLAG | VARCHAR2 | 30 |  |  | Labour union member flag. Accepts values of ?Y? or ?N?. |  |
| CAGR_GRADE_DEF_ID | NUMBER |  | 18 |  | Foreign key to PER_CAGR_GRADES_DEF. |  |
| CAGR_ID_FLEX_NUM | NUMBER |  | 18 |  | Key flex Structure Identifier for Collectively Agreed Grade. |  |
| CONTRACT_ID | NUMBER |  | 18 |  | Foreign key to PER_CONTRACTS_F. |  |
| MANAGER_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the employee in this assignment is designated a manager. Based on ?YES_NO? lookup type. |  |
| DATE_PROBATION_END | DATE |  |  |  | End date of probation period. |  |
| PROBATION_PERIOD | NUMBER |  | 25 |  | Duration of probation period. |  |
| PROBATION_UNIT | VARCHAR2 | 30 |  |  | Units of probation period duration. Based on QUALIFYING_UNITS lookup type. |  |
| NORMAL_HOURS | NUMBER |  | 22 |  | Normal working hours. |  |
| FREQUENCY | VARCHAR2 | 30 |  |  | Frequency of normal working hours, - week, month, year. Sourced from ?Frequency? lookup type. |  |
| WORK_AT_HOME | VARCHAR2 | 30 |  |  | Work at home flag. |  |
| TIME_NORMAL_FINISH | VARCHAR2 | 5 |  |  | Work day normal end time. |  |
| TIME_NORMAL_START | VARCHAR2 | 5 |  |  | Work day normal start time. |  |
| NOTICE_PERIOD | NUMBER |  | 10 |  | Notice period for the assignment. |  |
| NOTICE_PERIOD_UOM | VARCHAR2 | 30 |  |  | Notice period unit of measure. |  |
| DEFAULT_CODE_COMB_ID | NUMBER |  | 18 |  | Foreign key to GL_CODE_COMBINATIONS. |  |
| EMPLOYEE_CATEGORY | VARCHAR2 | 30 |  |  | Based on Lookup Type = ?EMPLOYEE_CATG?: Blue collar, Civil Servant, etc. |  |
| EMPLOYMENT_CATEGORY | VARCHAR2 | 30 |  |  | User defined category. For example Full-Time Permanent or Part-Time Permanent. Lookup Type = ?EMP_CAT?. |  |
| ESTABLISHMENT_ID | NUMBER |  | 18 |  | Foreign key to HR_ORGANIZATION_UNITS_F. |  |
| HOURLY_SALARIED_CODE | VARCHAR2 | 30 |  |  | Identifies if the assignment is paid by the hour or by a salary. Either maintained at the assignment level or ?Employment/Placement Terms? but not both. |  |
| SAL_REVIEW_PERIOD | NUMBER |  | 18 |  | Length of time between salary reviews. Either maintained at the assignment level or ?Employment/Placement Terms? but not both. |  |
| SAL_REVIEW_PERIOD_FREQUENCY | VARCHAR2 | 30 |  |  | Used with SAL REVIEW PERIOD to define time between salary reviews. Based on ?QUALIFYING_UNITS? lookup type. |  |
| JOB_POST_SOURCE_NAME | VARCHAR2 | 240 |  |  | Job post source name. |  |
| PROJECT_TITLE | VARCHAR2 | 80 |  |  | Obsolete |  |
| PERSON_REFERRED_BY_ID | NUMBER |  | 18 |  | Identifies person who referred applicant. Foreign key to PER_PERSONS. |  |
| PO_HEADER_ID | NUMBER |  | 18 |  | Foreign key reference to po_headers_all. |  |
| PO_LINE_ID | NUMBER |  | 18 |  | Foreign key reference to po_lines_all. |  |
| RECRUITER_ID | NUMBER |  | 18 |  | Identifies recruiter. Foreign Key to PER_PERSONS. |  |
| RECRUITMENT_ACTIVITY_ID | NUMBER |  | 18 |  | Identifies activity associated with the recruitment process. Foreign key to PER_RECRUITMENT_ACTIVITIES. |  |
| VACANCY_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_VACANCIES. |  |
| APPLICANT_RANK | NUMBER |  |  |  | Rank assigned to an applicant based on suitability and other criteria |  |
| POSTING_CONTENT_ID | NUMBER |  | 18 |  | The posting to which the applicant has applied. |  |
| SOURCE_ORGANIZATION_ID | NUMBER |  | 18 |  | Valid for 'Offer' and 'Applicant' Assignments only. Captured as part of the ?Application Source? details. For instance, Agency or Marketing. |  |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | Recruitment activity source for applicant assignment, for example, Advertisement. |  |
| PROJECTED_ASSIGNMENT_END | DATE |  |  |  | The date the assignment is expected to end. |  |
| SET_OF_BOOKS_ID | NUMBER |  | 18 |  | This is called Ledger in Fusion. Defaulted from Business Unit. |  |
| SOFT_CODING_KEYFLEX_ID | NUMBER |  | 18 |  | Obsolete |  |
| SPECIAL_CEILING_STEP_ID | NUMBER |  | 18 |  | Foreign key to PER_GRADE_STEPS_F. |  |
| VENDOR_ASSIGNMENT_NUMBER | VARCHAR2 | 30 |  |  | Assignment number of non-payrolled worker assignment with vending organization. |  |
| VENDOR_EMPLOYEE_NUMBER | VARCHAR2 | 30 |  |  | Employee number of worker with vending organization. |  |
| VENDOR_ID | NUMBER |  | 18 |  | Foreign key reference to po_vendors. |  |
| VENDOR_SITE_ID | NUMBER |  | 18 |  | Foreign key reference to po_vendor_sites_all. |  |
| ASS_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| WORK_TERMS_ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_ASSIGNMENTS_M for a work term. |  |
| ACTION_CODE | VARCHAR2 | 30 |  |  | Specifies the action performed on the particular record. For example: HIRE, ADD PENDING WORKER, MANAGER CHANGE, etc. |  |
| ASSIGNMENT_NAME | VARCHAR2 | 80 |  |  | Describes the type of assignment or set of Terms. Users can configure how to derive this (at setup time). This is optional, by default (out-of-the-box) this is derived as follows: [job name] - [department name]. |  |
| ASSIGNMENT_STATUS_TYPE | VARCHAR2 | 30 |  | Yes | Denormalized status of the assignment. This is derived using the Assignment Status Type ID. |  |
| AUTO_END_FLAG | VARCHAR2 | 30 |  | Yes | Used for temporary assignments. Determines whether to end the temporary job automatically. |  |
| DUTIES_TYPE | VARCHAR2 | 30 |  |  | Duties type. Apply for temporary assignments. Derived from a lookup code.  Enterprise stores types in a specific table rather than a lookup. |  |
| EFFECTIVE_SEQUENCE | NUMBER |  | 4 | Yes | Date Effective Entity: indicates the order of different changes made during a day. The lowest value represents the earliest change in the day. |  |
| EXPENSE_CHECK_ADDRESS | VARCHAR2 | 30 |  |  | Determines whether check is sent to the Home or Office address. Based on ?HOME_OFFICE? lookup. |  |
| INTERNAL_BUILDING | VARCHAR2 | 45 |  |  | Building information associated with Work location. |  |
| INTERNAL_FLOOR | VARCHAR2 | 45 |  |  | Floor information. |  |
| INTERNAL_LOCATION | VARCHAR2 | 80 |  |  | Additional location details. |  |
| INTERNAL_MAILSTOP | VARCHAR2 | 45 |  |  | Internal mail location. |  |
| INTERNAL_OFFICE_NUMBER | VARCHAR2 | 45 |  |  | Office Number. |  |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Represents Legal Entity. Might be null for Applicants. |  |
| LEGISLATION_CODE | VARCHAR2 | 150 |  |  | Legislation code derived from the Legal Entity. Might be null for Applicants. |  |
| LINKAGE_TYPE | VARCHAR2 | 30 |  |  | Determines the type of processing and rules associated with the linking of two assignments. |  |
| PARENT_ASSIGNMENT_ID | NUMBER |  | 18 |  | Allows two assignments to be linked. Used when creating temporary assignments. Also, potentially required when converting the Applicant onto a Worker (i.e. this stores the applicant assignment ID for the worker?s assignment). |  |
| PERSON_TYPE_ID | NUMBER |  | 18 |  | Defines the worker class. Examples: Assignee, Consultant, Expatriate, Agency/Temp, Intern, Apprentice, Contractor, Trainee. This defaults from the person/org relationship. It is defined at either level (Assignment or Employment/Placement Terms). |  |
| PRIMARY_WORK_TERMS_FLAG | VARCHAR2 | 30 |  | Yes | Accepts value of ?Y? or ?N? based on ?YES_NO? lookup type. If set to ?Yes?, then the current row represents a Assignment attached to the primary set of Employment/Placement. |  |
| PRIMARY_ASSIGNMENT_FLAG | VARCHAR2 | 30 |  | Yes | Accepts value of ?Y? or ?N? based on ?YES_NO? lookup type. If set to ?Yes?, then the current row represents the primary deployment. |  |
| PRIMARY_WORK_RELATION_FLAG | VARCHAR2 | 30 |  | Yes | Accepts value of ?Y? or ?N? based on ?YES_NO? lookup type. If set to ?Yes?, then the current row represents an Assignment or Employment/Placement attached to the primary Work Relationship. |  |
| PROJECTED_START_DATE | DATE |  |  |  | Tentative start date (applicants). |  |
| REASON_CODE | VARCHAR2 | 30 |  |  | Specifies the reason for the action performed on the record. |  |
| SYSTEM_PERSON_TYPE | VARCHAR2 | 30 |  |  | Derived from the person type id. It is included in this table to aid in performance. |  |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Determinant for ?Set Enabled? tables and those using BU as a partitioning key. |  |
| BILLING_TITLE | VARCHAR2 | 30 |  |  | Billing Title for assignment. |  |
| STEP_ENTRY_DATE | DATE |  |  |  | obsolete |  |
| TAX_ADDRESS_ID | NUMBER |  | 18 |  | Foreign key to PER_ADDRESSES. This represents the address that is used for taxation purposes. This can be different from a ?mailing address?. |  |
| ASS_ATTRIBUTE31 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE32 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE33 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE34 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE35 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE36 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE37 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE38 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE39 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE40 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE41 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE42 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE43 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE44 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE45 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE46 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE47 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE48 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE49 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE50 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Attributes (PER_ASG_DF) |
| RECORD_CREATOR | VARCHAR2 | 30 |  |  | Record created By Module |  |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |  |
| PROPOSED_WORKER_TYPE | VARCHAR2 | 30 |  |  | Determines whether applicant will be hired/placed as an Employee or Contingent Worker. This represents a SYSTEM PERSON TYPE: EMP or CWK. This is also applicable for Pending Hires (workers). |  |
| RETIREMENT_AGE | NUMBER |  | 18 |  | Represents the age, worker is retiring at. |  |
| RETIREMENT_DATE | DATE |  |  |  | Represents the planned retirement date. |  |
| POSITION_OVERRIDE_FLAG | VARCHAR2 | 30 |  | Yes | Override Position related data. Accepts values of ?Y? and ?N?. |  |
| EFFECTIVE_LATEST_CHANGE | VARCHAR2 | 30 |  | Yes | Date Effective Entity: 'Y' indicates that this row represents the latest change in the day. |  |
| ALLOW_ASG_OVERRIDE_FLAG | VARCHAR2 | 30 |  | Yes | Override Work Term related data. Accepts values of ?Y? and ?N?.  This is set for the Work Term. Default is set to ?N? for rows representing Assignments and it does not change. If row represents a Work Term, then this is user-enterable. |  |
| ASS_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive flex field numeric column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASS_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive flex field date column | Assignment Attributes (PER_ASG_DF) |
| ASG_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive flexfield structure defining column | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION1 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION2 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION3 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION4 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION5 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION6 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION7 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION8 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION9 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION10 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION11 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION12 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION13 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION14 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION15 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION16 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION17 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION18 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION19 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION20 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION21 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION22 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION23 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION24 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION25 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION26 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION27 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION28 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION29 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION30 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION31 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION32 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION33 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION34 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION35 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION36 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION37 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION38 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION39 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION40 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION41 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION42 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION43 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION44 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION45 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION46 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION47 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION48 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION49 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION50 | VARCHAR2 | 150 |  |  | Descriptive flex field column. Store Legislation specific information | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive flex field numeric column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE1 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE2 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE3 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE4 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE5 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE6 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE7 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE8 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE9 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE10 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE11 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE12 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE13 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE14 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| ASG_INFORMATION_DATE15 | DATE |  |  |  | Descriptive flex field date column. | Legislative Assignment Attributes (PER_ASG_LEG_DDF) |
| FREEZE_START_DATE | DATE |  |  | Yes | Represents the Deferred data freeze start date (defaulted to End of time). |  |
| FREEZE_UNTIL_DATE | DATE |  |  | Yes | Represents the Deferred data freeze until date (defaulted to Start of Time). |  |
| ID_FLEX_NUM | NUMBER |  | 18 |  | Represents ID Flex num for PeopleGroup KFF implementation. |  |
| CATEGORY_CODE | VARCHAR2 | 80 |  | Yes | Extensible Flexfield Category Code |  |
| FULL_PART_TIME | VARCHAR2 | 30 |  |  | FULL_PART_TIME |  |
| PERMANENT_TEMPORARY_FLAG | VARCHAR2 | 30 |  |  | PERMANENT_TEMPORARY_FLAG |  |
| GSP_ELIGIBILITY_FLAG | VARCHAR2 | 30 |  |  | Identifies if person is included in grade step progression. |  |
| UNION_ID | NUMBER |  | 18 |  | Union to which a person belongs |  |
| SENIORITY_BASIS | VARCHAR2 | 30 |  |  | Seniority |  |
| OVERTIME_PERIOD | NUMBER |  | 18 |  | Overtime Period |  |
| SOURCE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Identifier (ID) of the source assignment that was used to create the assignment. |  |
| LAST_WORKING_DATE | DATE |  |  |  | Last Date Worked (for terminated workers). |  |
| REVIEW_USER_ACCESS | VARCHAR2 | 30 |  |  | This stores user's option of review user access on Termination. Values accepted are 'I' for Immediately or 'A' for After termination |  |
| REHIRE_RECOMMENDATION | VARCHAR2 | 30 |  |  | Accepts Yes or No values. If Yes, person is recommended for re-hiring. |  |
| REHIRE_REASON | VARCHAR2 | 30 |  |  | If rehire recommendation is 'yes', then reason from recommending person is tracked via this field. |  |
| REHIRE_AUTHORIZER_PERSON_ID | NUMBER |  | 18 |  | Foreign Key to PER_PERSONS. Represents the person who recommends the worker for rehire. |  |
| TERMINATION_DATE | DATE |  |  |  | Actual termination date of  an assignment. |  |
| NOTIFICATION_DATE | DATE |  |  |  | Date when the termination of employment was notified. |  |
| STANDARD_HOURS | NUMBER |  | 22 |  | The standard working hours for the assignment. |  |
| STANDARD_FREQUENCY | VARCHAR2 | 30 |  |  | Frequency of standard working hours, - week, month, year. Sourced from Frequency lookup type. |  |
| STD_ANNUAL_WORKING_DURATION | NUMBER |  | 8 |  | The standard annual working duration for the enterprise, legal employer, department, location, job, position, or assignment. |  |
| ANNUAL_WORKING_DURATION_UNITS | VARCHAR2 | 20 |  |  | The unit of measure in hours, days, weeks, and months for the annual working and standard annual working durations. |  |
| ANNUAL_WORKING_DURATION | NUMBER |  | 8 |  | The annual working duration for the position and assignment. |  |
| ANNUAL_WORKING_RATIO | NUMBER |  | 8 |  | The ratio of annual working hours and standard annual working hours for the assignment. |  |
| ADJUSTED_FTE | NUMBER |  | 30 |  | The Adjusted Full Time Equivalent value calculated by multiplying the FTE and the Annual Working Ratio for the assignment. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| PER_ALL_ASSIGNMENTS_M_FK1 | Non Unique | Default | BUSINESS_GROUP_ID |  |
| PER_ALL_ASSIGNMENTS_M_FK13 | Non Unique | Default | RECRUITMENT_ACTIVITY_ID | Obsolete |
| PER_ALL_ASSIGNMENTS_M_FK14 | Non Unique | Default | SOURCE_ORGANIZATION_ID | Obsolete |
| PER_ALL_ASSIGNMENTS_M_FK15 | Non Unique | Default | ORGANIZATION_ID, EFFECTIVE_END_DATE |  |
| PER_ALL_ASSIGNMENTS_M_FK16 | Non Unique | Default | PEOPLE_GROUP_ID |  |
| PER_ALL_ASSIGNMENTS_M_FK17 | Non Unique | Default | SOFT_CODING_KEYFLEX_ID | Obsolete |
| PER_ALL_ASSIGNMENTS_M_FK18 | Non Unique | Default | VACANCY_ID |  |
| PER_ALL_ASSIGNMENTS_M_FK20 | Non Unique | Default | ESTABLISHMENT_ID |  |
| PER_ALL_ASSIGNMENTS_M_FK21 | Non Unique | Default | COLLECTIVE_AGREEMENT_ID |  |
| PER_ALL_ASSIGNMENTS_M_FK22 | Non Unique | Default | CONTRACT_ID |  |
| PER_ALL_ASSIGNMENTS_M_FK23 | Non Unique | Default | CAGR_GRADE_DEF_ID | Obsolete |
| PER_ALL_ASSIGNMENTS_M_FK3 | Non Unique | Default | GRADE_ID |  |
| PER_ALL_ASSIGNMENTS_M_FK31 | Non Unique | Default | POSTING_CONTENT_ID | Obsolete |
| PER_ALL_ASSIGNMENTS_M_FK4 | Non Unique | Default | POSITION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |  |
| PER_ALL_ASSIGNMENTS_M_FK5 | Non Unique | Default | JOB_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |  |
| PER_ALL_ASSIGNMENTS_M_FK52 | Non Unique | Default | VENDOR_ID | Obsolete |
| PER_ALL_ASSIGNMENTS_M_FK53 | Non Unique | Default | UNION_ID |  |
| PER_ALL_ASSIGNMENTS_M_FK6 | Non Unique | Default | ASSIGNMENT_STATUS_TYPE_ID |  |
| PER_ALL_ASSIGNMENTS_M_FK8 | Non Unique | Default | LOCATION_ID, EFFECTIVE_END_DATE |  |
| PER_ALL_ASSIGNMENTS_M_FK9 | Non Unique | Default | ACTION_OCCURRENCE_ID |  |
| PER_ALL_ASSIGNMENTS_M_N03 | Non Unique | Default | GRADE_LADDER_PGM_ID |  |
| PER_ALL_ASSIGNMENTS_M_N11 | Non Unique | Default | SPECIAL_CEILING_STEP_ID |  |
| PER_ALL_ASSIGNMENTS_M_N12 | Non Unique | Default | PERSON_ID, ASSIGNMENT_TYPE, PRIMARY_FLAG, EFFECTIVE_LATEST_CHANGE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ASSIGNMENT_STATUS_TYPE_ID |  |
| PER_ALL_ASSIGNMENTS_M_N13 | Non Unique | Default | EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, EFFECTIVE_LATEST_CHANGE, EFFECTIVE_SEQUENCE |  |
| PER_ALL_ASSIGNMENTS_M_N2 | Non Unique | Default | RECRUITER_ID | Obsolete |
| PER_ALL_ASSIGNMENTS_M_N4 | Non Unique | Default | PERIOD_OF_SERVICE_ID |  |
| PER_ALL_ASSIGNMENTS_M_N5 | Non Unique | Default | WORK_TERMS_ASSIGNMENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, EFFECTIVE_SEQUENCE |  |
| PER_ALL_ASSIGNMENTS_M_N50 | Non Unique | Default | ASSIGNMENT_NUMBER, EFFECTIVE_END_DATE |  |
| PER_ALL_ASSIGNMENTS_M_N51 | Non Unique | Default | LAST_UPDATE_DATE |  |
| PER_ALL_ASSIGNMENTS_M_N52 | Non Unique | Default | ASSIGNMENT_TYPE | Obsolete |
| PER_ALL_ASSIGNMENTS_M_N53 | Non Unique | Default | ASSIGNMENT_ID, ASSIGNMENT_STATUS_TYPE, EFFECTIVE_LATEST_CHANGE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, FREEZE_UNTIL_DATE, FREEZE_START_DATE |  |
| PER_ALL_ASSIGNMENTS_M_N54 | Non Unique | Default | UPPER("ASSIGNMENT_NUMBER"), EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |  |
| PER_ALL_ASSIGNMENTS_M_N55 | Non Unique | Default | SOURCE_ASSIGNMENT_ID |  |
| PER_ALL_ASSIGNMENTS_M_N6 | Non Unique | Default | UPPER("ASSIGNMENT_NAME") |  |
| PER_ALL_ASSIGNMENTS_M_N7 | Non Unique | Default | LEGAL_ENTITY_ID, ASSIGNMENT_TYPE, EFFECTIVE_END_DATE, ASSIGNMENT_STATUS_TYPE_ID |  |
| PER_ALL_ASSIGNMENTS_M_N9 | Non Unique | Default | PERSON_REFERRED_BY_ID | Obsolete |
| PER_ALL_ASSIGNMENTS_M_PK | Unique | Default | ASSIGNMENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, EFFECTIVE_LATEST_CHANGE, EFFECTIVE_SEQUENCE |  |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
