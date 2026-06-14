# HRA_EVALUATIONS_

This table stores the primary data related to Performance Documents.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevaluations-14361.html#hraevaluations-14361](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevaluations-14361.html#hraevaluations-14361)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_EVALUATIONS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, EVALUATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVALUATION_ID | NUMBER |  | 18 | Yes | Primary key of the performance document. |
| TEMPLATE_TYPE_CODE | VARCHAR2 | 30 |  |  | Identifies template type of the performance document. |
| NAME | VARCHAR2 | 30 |  |  | Name of the performance document. |
| USE_CALC_RATINGS_FLAG | VARCHAR2 | 30 |  |  | Indicates if section rating needs to be set based on calculated value. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| TEMPLATE_DEFN_ID | NUMBER |  | 18 |  | Foreign key to HRA_TMPL_DEFNS_B |
| TMPL_PERIOD_ID | NUMBER |  | 18 |  | Foreign key to HRA_TMPL_PERIODS_B |
| WORKER_ID | NUMBER |  | 18 |  | The global ID for the worker.  In the UI this is often represented by the worker's current name |
| MANAGER_ID | NUMBER |  | 18 |  | The global ID for the manager.  In the UI this will be represented as the manager's name |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_ASSIGNMENTS_N, holds the ID of the Assignment on which this evaluation is performed. |
| LANGUAGE_CODE | VARCHAR2 | 30 |  |  | Language code for the performance document. |
| LOCKED_BY_USER_ID | NUMBER |  | 18 |  | The global ID for the person who locks the performance document for making changes to the evaluation criteria |
| STATUS_CODE | VARCHAR2 | 30 |  |  | The status code of the performance document |
| PREV_STATUS_CODE | VARCHAR2 | 30 |  |  | The previous status code of the performance document |
| START_DATE | DATE |  |  |  | The start date of this performance document |
| END_DATE | DATE |  |  |  | The end date of this performance document |
| EVALUATION_DATE | DATE |  |  |  | The date on which the evaluation takes place |
| SELECT_MANAGER_ALLOWED_FLAG | VARCHAR2 | 30 |  |  | Indicates whether worker can select manager when generating document |
| ROUNDING_RULE_CODE | VARCHAR2 | 30 |  |  | Indicates the rounding rule that will be used for ratings that are calculated by the system. Valid values are Standard, Up and Down. |
| DECIMAL_PLACES | NUMBER |  | 18 |  | Indicates the number of decimal places for calculated ratings. |
| CALCULATION_RATINGS_FLAG | VARCHAR2 | 30 |  |  | Indicates that the system should calculate the ratings for a section or a document. |
| MAPPING_METHOD_CODE | VARCHAR2 | 30 |  |  | This applies to the Overall Rating section, where the system must choose an overall rating from the rating model, based on a calculated rating. |
| MANAGER_COMMENTS | VARCHAR2 | 4000 |  |  | Manager comments about the Evaluation |
| WORKER_COMMENTS | VARCHAR2 | 4000 |  |  | Worker comments about the Evaluation |
| STAR_RATING_ENABLED_FLAG | VARCHAR2 | 30 |  |  | Indicates whether star rating should be enabled on the UI or not |
| KUDOS_REGION_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to include Kudos region in the performance document. |
| MEETING_HELD_DATE | DATE |  |  |  | Indicates the date on which the review meeting was held between manager and worker |
| DIGITAL_SIGNATURE_FLAG | VARCHAR2 | 30 |  |  | Indiactes if digital signature is enabled |
| SET_ROLE_MINIMUMS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to set the minimum number for each role and also the total number for the evaluation. |
| SET_ROLE_MAXIMUMS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to set the maximum number for each role and also the total number for the evaluation. |
| TOTAL_MIN_PARTICIPANTS | NUMBER |  | 18 |  | Stores the total minimum number of participants required in the document. |
| TOTAL_MAX_PARTICIPANTS | NUMBER |  | 18 |  | Stores the total maximum number of participants required in the document. |
| ENFORCE_MIN_PCPNS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to enforce minimum number of participants allowed in the document. |
| WRK_SEE_MGR_PCPN_FLAG | VARCHAR2 | 30 |  |  | Stores whether worker can see the participants added by manager. |
| USE_WRK_CONNECTIONS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to show the search by workers' network connections in social product when adding participants |
| PCPN_FEEDBACK_REQ_FLAG | VARCHAR2 | 30 |  |  | Stores whether the participant feedback is required |
| PCPN_DECLINE_OPTION_FLAG | VARCHAR2 | 30 |  |  | Stores whether to give the participant the option whether to Accept/Decline the feedback request |
| AUTO_POPULATE_MM_FLAG | VARCHAR2 | 30 |  |  | Indicate matrix managers are automatically populated as participants when performance document is created. |
| SEND_REQUEST_TO_MM_FLAG | VARCHAR2 | 30 |  |  | Indicates request will be sent to matrix manager particpants when performance document is created, which automatically gives them access to the document. |
| DEFAULT_MATRIX_PCPN_ROLE_ID | NUMBER |  | 18 |  | Indicates default matrix role to use when automatically populating matrix managers as participants. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE11 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE12 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE13 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE14 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE15 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE16 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE17 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE18 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE19 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE20 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE21 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE22 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE23 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE24 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE25 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE26 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE27 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE28 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE29 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE30 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
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
| SHOW_WKR_CALC_RATING_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the Calculated Ratings should be visible to Worker. |
| SHOW_MGR_CALC_RATING_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the Calculated Ratings should be visible to Manager. |
| MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_ASSIGNMENT_M, identifying the assignment of manager who is performing the evaluation |
| SHOW_MM_CALC_RATING_FLAG | VARCHAR2 | 30 |  |  | Indicates whether calculated ratings should be visible to matrix managers. |
| SHOW_PCPN_CALC_RATING_FLAG | VARCHAR2 | 30 |  |  | Indicates whether calculated ratings should be visible to participants. |
| REVIEW_PERIOD_ID | NUMBER |  | 18 |  | Indicates the Review Period that is used for the performance document |
| ACTION_CODE | VARCHAR2 | 30 |  |  | Action Code for performing the action on the evaluation. |
| ACTION_REASON | VARCHAR2 | 30 |  |  | Reason for performing the action on the evaluation. |
| ACTION_PERFORMED_BY | NUMBER |  | 18 |  | Stores the Person Id of the person performing the action. |
| ACTION_PERFORMED_DATE | TIMESTAMP |  |  |  | Timestamp when the action was performed. |
| ENABLE_SYNC_FLAG | VARCHAR2 | 30 |  |  | Indicates if the evaluation is configured to use synchronized goals. |
| CALIBRATION_STATUS | VARCHAR2 | 30 |  |  | Calibration Status |
| CMP_PLAN_ID | NUMBER |  | 18 |  | Compensation Plan Id |
| CMP_PLAN_PERIOD_ID | NUMBER |  | 18 |  | Compensation Plan Period Id |
| CALIBRATION_PERFORMED_BY | VARCHAR2 | 64 |  |  | Calibration Performed By |
| CALIBRATION_PERFORMED_DATE | TIMESTAMP |  |  |  | Calibration Performed Date |
| CALENDAR_INVITE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether calendar invite can be created |
| CALENDAR_INVITE_START_TIME | TIMESTAMP |  |  |  | Calendar Invite Start time |
| CALENDAR_INVITE_END_TIME | TIMESTAMP |  |  |  | Calendar Invite End time |
| CALENDAR_INVITE_LOCATION | VARCHAR2 | 4000 |  |  | Calendar Invite location |
| CALENDAR_INVITE_DESCRIPTION | VARCHAR2 | 4000 |  |  | Calendar invite description |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_EVALUATIONSN1_ | Non Unique | Default | EVALUATION_ID, LAST_UPDATE_DATE |
| HRA_EVALUATIONS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, EVALUATION_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
