# HR_ALL_POSITIONS_F

Positions main table storing all position attributes

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrallpositionsf-30912.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrallpositionsf-30912.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_ALL_POSITIONS_F_PK | POSITION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| POSITION_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| CATEGORY_CODE | VARCHAR2 | 80 |  | Yes | Extensible Flexfield Category Code |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| BUSINESS_UNIT_ID | NUMBER |  | 18 | Yes | Foreign key to HRW_BUSINESS_UNITS table. |  |
| POSITION_CODE | VARCHAR2 | 30 |  | Yes | Code of the position. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| ORGANIZATION_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ALL_ORGANIZATION_UNITS_F |  |
| UNION_ID | NUMBER |  | 18 |  | UNION_ID |  |
| COLLECTIVE_AGREEMENT_ID | NUMBER |  | 18 |  | COLLECTIVE_AGREEMENT_ID |  |
| JOB_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_JOBS_F table. |  |
| LOCATION_ID | NUMBER |  | 18 |  | Foreign Key to PER_LOCATIONS table. |  |
| ENTRY_GRADE_ID | NUMBER |  | 18 |  | Identifier of the entry grade. |  |
| ENTRY_STEP_ID | NUMBER |  | 18 |  | Identifier of the entry step. |  |
| SUPERVISOR_ID | NUMBER |  | 18 |  | Identifier of the manager. |  |
| SUPERVISOR_ASSIGNMENT_ID | NUMBER |  | 18 |  | Identifier of the manager's assignment. |  |
| GRADE_LADDER_ID | NUMBER |  | 18 |  | Grade Ladder |  |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ACTION_OCCURRENCES. |  |
| ACTIVE_STATUS | VARCHAR2 | 30 |  | Yes | Indicates if a position is active or inactive. |  |
| HIRING_STATUS | VARCHAR2 | 30 |  | Yes | Indicates the hiring status of the position, for example approved or frozen. |  |
| POSITION_TYPE | VARCHAR2 | 30 |  |  | Indicates the type of the position for example pooled or single. |  |
| PERMANENT_TEMPORARY_FLAG | VARCHAR2 | 30 |  |  | Indicates if a position is regular or temporary. |  |
| FULL_PART_TIME | VARCHAR2 | 30 |  |  | Indicates if a position is full-time or part-time. |  |
| FTE | NUMBER |  | 30 |  | Position full time equivalent. |  |
| CALCULATE_FTE | VARCHAR2 | 1 |  |  | Indicates whether FTE should be calculated for this position. |  |
| MAX_PERSONS | NUMBER |  | 4 |  | Position headcount. |  |
| STANDARD_WORKING_HOURS | NUMBER |  | 22 |  | Number of standard working hours. |  |
| STANDARD_WORKING_FREQUENCY | VARCHAR2 | 30 |  |  | Frequency for the standard working hours. |  |
| WORKING_HOURS | NUMBER |  | 22 |  | Number of actual working hours. |  |
| FREQUENCY | VARCHAR2 | 30 |  |  | Frequency for the actual working hours. |  |
| STD_ANNUAL_WORKING_DURATION | NUMBER |  | 8 |  | The standard annual working duration for the Position. |  |
| ANNUAL_WORKING_DURATION_UNITS | VARCHAR2 | 10 |  |  | The unit of measure in hours, days, weeks, or months for the standard annual working duration and annual working duration. |  |
| ANNUAL_WORKING_DURATION | NUMBER |  | 8 |  | The annual working duration for the position |  |
| TIME_NORMAL_START | VARCHAR2 | 5 |  |  | Regular start time. |  |
| TIME_NORMAL_FINISH | VARCHAR2 | 5 |  |  | Regular end time. |  |
| PROBATION_PERIOD | NUMBER |  | 22 |  | Number of the probation period. |  |
| PROBATION_PERIOD_UNIT_CD | VARCHAR2 | 30 |  |  | Unit of measure code for the probation period. |  |
| BARGAINING_UNIT_CD | VARCHAR2 | 30 |  |  | Code of the bargaining unit. |  |
| POSITION_SYNCHRONIZATION_FLAG | VARCHAR2 | 30 |  | Yes | Indicates if a position is enabled for synchronization. This is not in use. |  |
| SECURITY_CLEARANCE | VARCHAR2 | 30 |  |  | Indicates the security clearance of a position. |  |
| OVERLAP_ALLOWED | VARCHAR2 | 30 |  |  | Indicates if overlap is allowed. |  |
| SEASONAL_FLAG | VARCHAR2 | 30 |  |  | Indicates if a position is seasonal. |  |
| SEASONAL_START_DATE | DATE |  |  |  | Seasonal start date. |  |
| SEASONAL_END_DATE | DATE |  |  |  | Seasonal end date. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Position Attributes (PER_POSITIONS_DFF) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| ASSIGNMENT_CATEGORY | VARCHAR2 | 30 |  |  | ASSIGNMENT_CATEGORY |  |
| COST_CENTER | VARCHAR2 | 30 |  |  | Indicates Cost Center |  |
| DELEGATE_POSITION_ID | NUMBER |  | 18 |  | Indicates Delegate Position id |  |
| BUDGETED_POSITION_FLAG | VARCHAR2 | 1 |  |  | Indicates flag for budgeted flag |  |
| BUDGET_AMOUNT | NUMBER |  |  |  | Indicates budget amount |  |
| BUDGET_AMOUNT_CURRENCY | VARCHAR2 | 20 |  |  | Used to identify currency for Budget Amount |  |
| FUNDED_BY_EXISTING_POSITION | VARCHAR2 | 1 |  |  | Flag to indicate funded by existing position |  |
| REQUISITION_TEMPLATE_ID | NUMBER |  | 18 |  | Identifier of the Requisition template. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_ALL_POSITIONS_F_FK2 | Non Unique | Default | BUSINESS_GROUP_ID |
| HR_ALL_POSITIONS_F_FK3 | Non Unique | Default | ORGANIZATION_ID |
| HR_ALL_POSITIONS_F_FK4 | Non Unique | Default | BUSINESS_UNIT_ID |
| HR_ALL_POSITIONS_F_N1 | Non Unique | Default | ENTRY_GRADE_ID |
| HR_ALL_POSITIONS_F_N11 | Non Unique | Default | UPPER("ATTRIBUTE1") |
| HR_ALL_POSITIONS_F_N12 | Non Unique | Default | UPPER("ATTRIBUTE2") |
| HR_ALL_POSITIONS_F_N13 | Non Unique | Default | UPPER("ATTRIBUTE3") |
| HR_ALL_POSITIONS_F_N14 | Non Unique | Default | UPPER("ATTRIBUTE4") |
| HR_ALL_POSITIONS_F_N15 | Non Unique | Default | UPPER("ATTRIBUTE5") |
| HR_ALL_POSITIONS_F_N16 | Non Unique | Default | ATTRIBUTE6 |
| HR_ALL_POSITIONS_F_N17 | Non Unique | Default | ATTRIBUTE7 |
| HR_ALL_POSITIONS_F_N18 | Non Unique | Default | ATTRIBUTE8 |
| HR_ALL_POSITIONS_F_N19 | Non Unique | Default | ATTRIBUTE9 |
| HR_ALL_POSITIONS_F_N2 | Non Unique | Default | ENTRY_STEP_ID |
| HR_ALL_POSITIONS_F_N20 | Non Unique | Default | ATTRIBUTE10 |
| HR_ALL_POSITIONS_F_N3 | Non Unique | Default | SUPERVISOR_ID |
| HR_ALL_POSITIONS_F_N31 | Non Unique | Default | ATTRIBUTE_NUMBER1 |
| HR_ALL_POSITIONS_F_N32 | Non Unique | Default | ATTRIBUTE_NUMBER2 |
| HR_ALL_POSITIONS_F_N33 | Non Unique | Default | ATTRIBUTE_NUMBER3 |
| HR_ALL_POSITIONS_F_N34 | Non Unique | Default | ATTRIBUTE_NUMBER4 |
| HR_ALL_POSITIONS_F_N35 | Non Unique | Default | ATTRIBUTE_NUMBER5 |
| HR_ALL_POSITIONS_F_N4 | Non Unique | Default | LOCATION_ID |
| HR_ALL_POSITIONS_F_N41 | Non Unique | Default | ATTRIBUTE_DATE1 |
| HR_ALL_POSITIONS_F_N42 | Non Unique | Default | ATTRIBUTE_DATE2 |
| HR_ALL_POSITIONS_F_N43 | Non Unique | Default | ATTRIBUTE_DATE3 |
| HR_ALL_POSITIONS_F_N44 | Non Unique | Default | ATTRIBUTE_DATE4 |
| HR_ALL_POSITIONS_F_N45 | Non Unique | Default | ATTRIBUTE_DATE5 |
| HR_ALL_POSITIONS_F_N46 | Non Unique | Default | DELEGATE_POSITION_ID |
| HR_ALL_POSITIONS_F_N5 | Non Unique | Default | JOB_ID |
| HR_ALL_POSITIONS_F_N6 | Non Unique | Default | SUPERVISOR_ASSIGNMENT_ID |
| HR_ALL_POSITIONS_F_N7 | Non Unique | Default | UPPER("POSITION_CODE"), BUSINESS_UNIT_ID, BUSINESS_GROUP_ID |
| HR_ALL_POSITIONS_F_PK | Unique | Default | POSITION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HR_ALL_POSITIONS_F_U1 | Unique | Default | LAST_UPDATE_DATE, POSITION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
