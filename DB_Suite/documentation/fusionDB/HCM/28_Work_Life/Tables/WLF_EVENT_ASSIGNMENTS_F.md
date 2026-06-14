# WLF_EVENT_ASSIGNMENTS_F

Table to store learning item event assignments.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventassignmentsf-29521.html#wlfeventassignmentsf-29521](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventassignmentsf-29521.html#wlfeventassignmentsf-29521)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_EVENT_ASSIGNMENTS_F_PK | EVENT_ASSIGNMENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| CATEGORY | VARCHAR2 | 30 |  |  | This column stores the category of the assignment, this is applicable mainly for recommendations to categorize recommendations |
| INITIAL_ACTUAL_SCORE | NUMBER |  | 9 |  | INITIAL_ACTUAL_SCORE |
| ASSIGNMENT_PROFILE_NUMBER | VARCHAR2 | 30 |  |  | ASSIGNMENT_PROFILE_NUMBER |
| ACCESS_PERMISSION_ID | NUMBER |  | 18 |  | Assignment level access permission id to the learning item |
| PRIORITY | NUMBER |  | 18 |  | PRIORITY |
| IS_ADHOC | VARCHAR2 | 1 |  |  | IS_ADHOC |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EVENT_ID | NUMBER |  | 18 |  | EVENT_ID |
| ASSIGNMENT_RULE_ID | NUMBER |  | 18 |  | ASSIGNMENT_RULE_ID |
| STATUS | VARCHAR2 | 30 |  | Yes | Current status of the profile {NEW, MODIFIED, INPROCESS, ACTIVE, DELETED}. |
| INITIAL_RECORD_STATUS | VARCHAR2 | 30 |  | Yes | Initial assignment record status {ORA_ASSN_REC_ACTIVE,RA_ASSN_REC_REQUESTED}. |
| PROCESSED_DATE | TIMESTAMP |  |  |  | The time the share profile was processed. |
| COMMENTS | VARCHAR2 | 4000 |  |  | Recommendation Comments. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SP_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SP_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ASSIGNMENT_START_DATE | DATE |  |  |  | The Date when the assignment should become Active. |
| REQUEST_DETAIL_ID | NUMBER |  | 18 |  | Identifier of request detail. Foreign key to WLF_REQUEST_DETAILS. |
| PRICING_RULE_ID | NUMBER |  | 18 |  | Identifier of pricing rule. Foreign key to WLF_PRICING_RULES_F. |
| PRICING_RULE_EFFECTIVE_DATE | DATE |  |  |  | Indicates date from which price is effective. |
| LATEST_REQUEST_PROCESS_ID | NUMBER |  | 18 |  | Represent latest ESS Job ID |
| LATEST_ESS_JOB_ID | NUMBER |  | 18 |  | Latest ESS Job Id that has triggered the Event Assignment |
| DYNAMIC_FLAG | VARCHAR2 | 30 |  |  | Populated Dynamic flag value. |
| RUN_AS_ID | NUMBER |  | 18 |  | Person identifier specifying who the user is that the ESS jobs should be run as. |
| PAYMENT_RULE_ID | NUMBER |  | 18 |  | Identifier of pricing rule Payment Type. Foreign key to WLF_PAYMENT_RULES_F. |
| INITIAL_REASON_CODE | VARCHAR2 | 30 |  |  | Initial reason for assignment status completion. |
| INITIAL_COMPLETION_DATE | TIMESTAMP |  |  |  | The date and time of the completion of the assignment. |
| INITIAL_RECORD_SUBSTATUS | VARCHAR2 | 30 |  |  | Initial assignment record substatus. |
| INITIAL_COMMENTS | VARCHAR2 | 4000 |  |  | Comments for assignment status completion. |
| INITIAL_TOTAL_ACTUAL_EFFORT | NUMBER |  | 9 |  | Actual effort learner has spent on an assignment. |
| CATEGORY_ID | NUMBER |  | 18 |  | The category id for the assignment category |
| PROCESS_ADVANCED_RULE_UPDATES | VARCHAR2 | 1 |  |  | This column specify whether to apply advanced rule updates to existing assignment records or not |
| PROCESSING_FREQUENCY | VARCHAR2 | 30 |  |  | Processing frequency |
| IS_SUBORDINATE | VARCHAR2 | 1 |  |  | This column specify whether to event assignment for course created as subordinate while creating assignment for Offering |
| REASON_CODE | VARCHAR2 | 30 |  |  | Status change reason code |
| STATUS_CHANGE_COMMENT | VARCHAR2 | 4000 |  |  | Status change comment |
| RECORD_STATUS_ON_CANCEL | VARCHAR2 | 30 |  |  | Assignment record status on cancel |
| EXCLUDE_ENROLLMENT_FROM_HIST | VARCHAR2 | 1 |  |  | Exclude enrollment from history option |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_EVENT_ASSIGNMENTS_F_N1 | Non Unique | Default | EVENT_ID, ACCESS_PERMISSION_ID |
| WLF_EVENT_ASSIGNMENTS_F_N2 | Non Unique | Default | STATUS |
| WLF_EVENT_ASSIGNMENTS_F_N3 | Non Unique | Default | ASSIGNMENT_RULE_ID |
| WLF_EVENT_ASSIGNMENTS_F_N4 | Non Unique | Default | PROCESSED_DATE |
| WLF_EVENT_ASSIGNMENTS_F_N5 | Non Unique | Default | ASSIGNMENT_PROFILE_NUMBER |
| WLF_EVENT_ASSIGNMENTS_F_N6 | Non Unique | Default | ACCESS_PERMISSION_ID |
| WLF_EVENT_ASSIGNMENTS_F_N7 | Non Unique | Default | RUN_AS_ID |
| WLF_EVENT_ASSIGNMENTS_F_U2 | Unique | Default | EVENT_ASSIGNMENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
