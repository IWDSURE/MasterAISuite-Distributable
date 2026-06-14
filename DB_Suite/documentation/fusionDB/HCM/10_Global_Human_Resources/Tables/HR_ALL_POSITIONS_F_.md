# HR_ALL_POSITIONS_F_

Positions main table storing all position attributes

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrallpositionsf-11754.html#hrallpositionsf-11754](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrallpositionsf-11754.html#hrallpositionsf-11754)

## Primary Key

| Name | Columns |
|------|----------|
| HR_ALL_POSITIONS_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, POSITION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POSITION_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| CATEGORY_CODE | VARCHAR2 | 80 |  |  | Extensible Flexfield Category Code |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Foreign key to HRW_BUSINESS_UNITS table. |
| POSITION_CODE | VARCHAR2 | 30 |  |  | Code of the position. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Foreign Key to HR_ALL_ORGANIZATION_UNITS_F |
| UNION_ID | NUMBER |  | 18 |  | UNION_ID |
| COLLECTIVE_AGREEMENT_ID | NUMBER |  | 18 |  | COLLECTIVE_AGREEMENT_ID |
| JOB_ID | NUMBER |  | 18 |  | Foreign Key to PER_JOBS_F table. |
| LOCATION_ID | NUMBER |  | 18 |  | Foreign Key to PER_LOCATIONS table. |
| ENTRY_GRADE_ID | NUMBER |  | 18 |  | Identifier of the entry grade. |
| ENTRY_STEP_ID | NUMBER |  | 18 |  | Identifier of the entry step. |
| SUPERVISOR_ID | NUMBER |  | 18 |  | Identifier of the manager. |
| SUPERVISOR_ASSIGNMENT_ID | NUMBER |  | 18 |  | Identifier of the manager's assignment. |
| GRADE_LADDER_ID | NUMBER |  | 18 |  | Grade Ladder |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |
| ACTIVE_STATUS | VARCHAR2 | 30 |  |  | Indicates if a position is active or inactive. |
| HIRING_STATUS | VARCHAR2 | 30 |  |  | Indicates the hiring status of the position, for example approved or frozen. |
| POSITION_TYPE | VARCHAR2 | 30 |  |  | Indicates the type of the position for example pooled or single. |
| PERMANENT_TEMPORARY_FLAG | VARCHAR2 | 30 |  |  | Indicates if a position is regular or temporary. |
| FULL_PART_TIME | VARCHAR2 | 30 |  |  | Indicates if a position is full-time or part-time. |
| FTE | NUMBER |  | 30 |  | Position full time equivalent. |
| CALCULATE_FTE | VARCHAR2 | 1 |  |  | Indicates whether FTE should be calculated for this position. |
| MAX_PERSONS | NUMBER |  | 4 |  | Position headcount. |
| STANDARD_WORKING_HOURS | NUMBER |  | 22 |  | Number of standard working hours. |
| STANDARD_WORKING_FREQUENCY | VARCHAR2 | 30 |  |  | Frequency for the standard working hours. |
| WORKING_HOURS | NUMBER |  | 22 |  | Number of actual working hours. |
| FREQUENCY | VARCHAR2 | 30 |  |  | Frequency for the actual working hours. |
| STD_ANNUAL_WORKING_DURATION | NUMBER |  | 8 |  | The standard annual working duration for the position. |
| ANNUAL_WORKING_DURATION_UNITS | VARCHAR2 | 10 |  |  | The unit of measure in hours, days, weeks, or months for the standard annual working duration and annual working duration. |
| ANNUAL_WORKING_DURATION | NUMBER |  | 8 |  | The annual working duration for the position. |
| TIME_NORMAL_START | VARCHAR2 | 5 |  |  | Regular start time. |
| TIME_NORMAL_FINISH | VARCHAR2 | 5 |  |  | Regular end time. |
| PROBATION_PERIOD | NUMBER |  | 22 |  | Number of the probation period. |
| PROBATION_PERIOD_UNIT_CD | VARCHAR2 | 30 |  |  | Unit of measure code for the probation period. |
| BARGAINING_UNIT_CD | VARCHAR2 | 30 |  |  | Code of the bargaining unit. |
| POSITION_SYNCHRONIZATION_FLAG | VARCHAR2 | 30 |  |  | Indicates if a position is enabled for synchronization. This is not in use. |
| SECURITY_CLEARANCE | VARCHAR2 | 30 |  |  | Indicates the security clearance of a position. |
| OVERLAP_ALLOWED | VARCHAR2 | 30 |  |  | Indicates if overlap is allowed. |
| SEASONAL_FLAG | VARCHAR2 | 30 |  |  | Indicates if a position is seasonal. |
| SEASONAL_START_DATE | DATE |  |  |  | Seasonal start date. |
| SEASONAL_END_DATE | DATE |  |  |  | Seasonal end date. |
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
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ASSIGNMENT_CATEGORY | VARCHAR2 | 30 |  |  | ASSIGNMENT_CATEGORY |
| COST_CENTER | VARCHAR2 | 30 |  |  | Indicates Cost Center |
| DELEGATE_POSITION_ID | NUMBER |  | 18 |  | Indicates Delegate Position id |
| BUDGETED_POSITION_FLAG | VARCHAR2 | 1 |  |  | Indicates flag for budgeted flag |
| BUDGET_AMOUNT | NUMBER |  |  |  | Indicates budget amount |
| BUDGET_AMOUNT_CURRENCY | VARCHAR2 | 20 |  |  | Used to identify currency for Budget Amount |
| FUNDED_BY_EXISTING_POSITION | VARCHAR2 | 1 |  |  | Flag to indicate funded by existing position |
| REQUISITION_TEMPLATE_ID | NUMBER |  | 18 |  | Identifier of the Requisition template. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HR_ALL_POSITIONS_FN1_ | Non Unique | Default | POSITION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LAST_UPDATE_DATE |
| HR_ALL_POSITIONS_F_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, POSITION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
