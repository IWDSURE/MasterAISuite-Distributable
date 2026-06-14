# WLF_ASSIGNMENT_RECORDS_F

Table to store Assignment Records.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfassignmentrecordsf-12610.html#wlfassignmentrecordsf-12610](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfassignmentrecordsf-12610.html#wlfassignmentrecordsf-12610)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ASSIGNMENT_RECS_F_PK | ASSIGNMENT_RECORD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNMENT_RECORD_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| ASSIGNMENT_RECORD_NUMBER | VARCHAR2 | 30 |  |  | ASSIGNMENT_RECORD_NUMBER |
| ACCESS_PERMISSION_ID | NUMBER |  | 18 |  | Learner level access permission id to the learning item. |
| PRE_ASSIGNMENT_RECORD_ID | NUMBER |  | 18 |  | Predecessor assignment record id |
| SUCC_ASSIGNMENT_RECORD_ID | NUMBER |  | 18 |  | Successor assignment record id |
| REASON_CODE | VARCHAR2 | 30 |  |  | Reason for assignment status change |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EVENT_ASSIGNMENT_ID | NUMBER |  | 18 |  | EVENT_ASSIGNMENT_ID |
| EVENT_CREATED_BY_ID | NUMBER |  | 18 |  | EVENT_CREATED_BY_ID |
| VALIDITY_DATE | DATE |  |  |  | The date from which the completed assignment is valid |
| EXPIRATION_DATE | DATE |  |  |  | The date that the assignment will expire. |
| ASSIGNMENT_RULE_ID | NUMBER |  | 18 |  | ASSIGNMENT_RULE_ID |
| LEARNER_ID | NUMBER |  | 18 |  | LEARNER_ID |
| ATTACHMENT_ID | NUMBER |  | 18 |  | ATTACHMENT_ID |
| DATE_STATUS_CHANGED | TIMESTAMP |  |  |  | DATE_STATUS_CHANGED |
| TOTAL_LEARNING_TIME | NUMBER |  |  |  | TOTAL_LEARNING_TIME |
| STATUS | VARCHAR2 | 32 |  | Yes | Current status of the share {ACTIVE, COMPLETED, EXPIRED, REVOKED, DELETED}. |
| NOTIFICATION_STATUS | VARCHAR2 | 32 |  | Yes | Current status of the share's notification {START, ..., END}. |
| CALCULATED_DUE_DATE | DATE |  |  |  | The due date which is calculated based on the rules for the assignment. |
| COMPLETION_DATE | TIMESTAMP |  |  |  | The date and time of the completion of the share. |
| IS_HISTORY_FLAG | VARCHAR2 | 1 |  |  | IS_HISTORY_FLAG |
| SOURCE_INFO | VARCHAR2 | 240 |  |  | Intended for customers to track where their imported records came from. |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | Intended for customers to track where their imported records came from. |
| SOURCE_ID | NUMBER |  | 18 |  | Intended for customers to track where their imported records came from. |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | Associated content object. Denormalized from WLF_EVENTS |
| LEARNING_ITEM_CATEGORY | VARCHAR2 | 30 |  |  | Learning Item Category to differentiate same learning item type objects |
| EVENT_TYPE | VARCHAR2 | 30 |  |  | Polymorphic discriminator column. Denormalized from WLF_EVENTS |
| EVENT_SUB_TYPE | VARCHAR2 | 30 |  |  | EVENT_SUB_TYPE. Denormalized from WLF_EVENTS |
| ATTRIBUTION_ID | NUMBER |  | 18 |  | ATTRIBUTION_ID. Denormalized from WLF_EVENTS |
| ATTRIBUTION_TYPE | VARCHAR2 | 30 |  |  | ATTRIBUTION_TYPE. Denormalized from WLF_EVENTS |
| ATTRIBUTION_LOOKUP_CODE | VARCHAR2 | 30 |  |  | ATTRIBUTION_LOOKUP_CODE. Denormalized from WLF_EVENTS |
| ASSIGNED_ON_DATE | TIMESTAMP |  |  |  | The date that the assignment is assigned and visible to the learner. |
| STATUS_CHANGE_COMMENT | VARCHAR2 | 4000 |  |  | Comments to be captured during status change. For example during Withdrawal or Completion. |
| STATUS_CHANGE_TYPE | VARCHAR2 | 30 |  |  | To capture the change in status like Withdrawal or Completion either by Specialist, Self or Auto. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LI_EFFECTIVE_DATE | TIMESTAMP |  |  |  | indicates the date combined with learning item id  to be referenced with learning item table. |
| SH_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SH_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| REQUEST_DETAIL_ID | NUMBER |  | 18 |  | Identifier of request detail. Foreign key to WLF_REQUEST_DETAILS. |
| TOTAL_ACTUAL_EFFORT | NUMBER |  | 9 |  | Actual effort learner has spent on an assignment. |
| SUB_STATUS | VARCHAR2 | 30 |  |  | Substatus of assignment record. |
| EFFORT_UOM | VARCHAR2 | 30 |  |  | EFFORT_UOM |
| PRICING_RULE_ID | NUMBER |  | 18 |  | Identifier of pricing rule. Foreign key to WLF_PRICING_RULES_F. |
| PRICE_LOCK_DATE | DATE |  |  |  | Indicates date when price is locked. |
| TRANSACTION_DETAILS_RULE_ID | NUMBER |  | 18 |  | Identifier of pricing rule which is specific for assignment. Foreign key to WLF_PRICING_RULES_F. |
| PEND_PREREQ_CUTOFF_DATE | DATE |  |  |  | Cutoff date when prereq has to evaluated |
| PH_DESTINATION_ID | NUMBER |  | 18 |  | Placeholder destination id from WLF_PH_DESTINATION_F table |
| REQUESTED_DATE | DATE |  |  |  | The date on which assignment was requested |
| REQUEST_APPROVED_DATE | DATE |  |  |  | The date on which assignment request was approved |
| REQUEST_REJECTED_DATE | DATE |  |  |  | The date on which assignment request was rejected |
| WAITLISTED_DATE | DATE |  |  |  | The date on which learner was placed on waitlist |
| DELETED_DATE | DATE |  |  |  | The date on which assignment record status was changed to deleted |
| WITHDRAWN_DATE | DATE |  |  |  | The date on which assignment for a learner has been withdrawn |
| WAITLIST_POSITION | VARCHAR2 | 30 |  |  | This columns indicates the waitlisting position for a learner on an offering |
| ADMIN_ACCESS_PERMISSION_ID | NUMBER |  | 18 |  | Admin access permission identifier |
| PENDING_PREREQ_ENTERED_DATE | DATE |  |  |  | Date on which assignment is entered into the pending prerequisite status |
| PENDING_PREREQ_EXITED_DATE | DATE |  |  |  | Date on which assignment is exited out of the pending prerequisite status |
| WAITLIST_EXITED_DATE | DATE |  |  |  | Date on which learner was confirmed with a seat |
| ASSIGNMENT_STARTED_ON_DATE | DATE |  |  |  | Date on which learner started working on the learning assignment |
| CONTENT_COMPLETION_DATE | DATE |  |  |  | Date on which learner moved into the content completion status |
| EVALUATION_SUBMITTED_DATE | DATE |  |  |  | Date on which learner submitted the evaluation |
| PENDING_PAY_ENTERED_DATE | DATE |  |  |  | Date on which assignment record entered to pending payment. |
| STATUS_EXPIRATION_DATE | TIMESTAMP |  |  |  | Date on which current assignment status expires. |
| IS_COURSE_SUBORDINATE | VARCHAR2 | 30 |  |  | Indicates master assignment |
| PAYMENT_RULE_ID | NUMBER |  | 18 |  | Identifier for pricing rule Payment Type.Foreign key to WLF_PAYMENT_RULES_F. |
| BPM_TASK_ID | VARCHAR2 | 64 |  |  | BPM Task Identifier for the approval record |
| WITHDRAW_REQUESTED_DATE | TIMESTAMP |  |  |  | this column is used to store date of when withdraw requested |
| CPE_TYPE | VARCHAR2 | 30 |  |  | This column stores continued professional education type. This column accepts values for lookup ORA_WLF_CPE_TYPE |
| CPE_POINTS | NUMBER |  |  |  | This column stores continued professional education points for the given continued professional education type stored in CPE_TYPE column |
| CATEGORY_ID | NUMBER |  | 18 |  | This column stores the category id of the assignment |
| CATEGORY | VARCHAR2 | 30 |  |  | This column stores the category of the assignment, this is applicable mainly for recommendations to categorize recommendations |
| ACTUAL_SCORE | NUMBER |  | 9 |  | This column represents actual score rolled up from completion engine or user populates for external learning assignments |
| USE_COMPLETED_ATTEMPTS_FLAG | VARCHAR2 | 1 |  |  | This column will be used in the context of assignments auto completion. Assignments will not be auto completed when this flag is set with 'N' value. |
| LI_DEF_USED_DATE | TIMESTAMP |  |  |  | Represents the timestamp of the learning item change used for this assignment record creation/update |
| LAST_RECONCILE_DATE | TIMESTAMP |  |  |  | Represents the time when the reconcile is completed for assignment record. |
| LEARNING_ITEM_TYPE | VARCHAR2 | 32 |  |  | Polymorphic discriminator column { DOCUMENT, VIDEO, TUTORIAL ... }. |
| LEARNING_ITEM_SUB_TYPE | VARCHAR2 | 30 |  |  | Learning Item sub type for the learning item type like ELearning. eg: Tutorial, Video etc. |
| ORIGINAL_EVENT_TYPE | VARCHAR2 | 30 |  |  | Column to populate original denormalized event type when error assginment is created. |
| AC_EXPIRE_OLD_ON_COMPLETION | VARCHAR2 | 1 |  |  | Option to expire all completed assignments on current assignment completion |
| IN_ELASTIC | VARCHAR2 | 1 |  |  | Indicates if access is processed to security index or not |
| IS_FORCE_RETAKE | VARCHAR2 | 1 |  |  | Admin controlled force retake assignment flag |
| EXEMPTED_DATE | TIMESTAMP |  |  |  | The date on which assignment for a learner has been exempted |
| PENDING_SEAT_ACPT_ENTERED_DATE | TIMESTAMP |  |  |  | Represents the date on which assignment is entered into the pending seat acceptance status |
| PENDING_SEAT_ACPT_EXITED_DATE | TIMESTAMP |  |  |  | Represents the date on which assignment is exited out of the pending seat acceptance status |
| ASSIGNMENT_ACTIVATED_ON_DATE | TIMESTAMP |  |  |  | Represents the date when assignment entered to Active status |
| ASSIGNMENT_COMPLETED_BY | VARCHAR2 | 30 |  |  | This column stores how the assignment got completed |
| INCOMPLETE_DATE | TIMESTAMP |  |  |  | Represents the date when assignment entered to Incomplete status |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| WLF_ASSIGNMENT_RECORDS_F_N10 | Non Unique | Default | SUB_STATUS, STATUS |  |
| WLF_ASSIGNMENT_RECORDS_F_N12 | Non Unique | Default | REQUEST_DETAIL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |  |
| WLF_ASSIGNMENT_RECORDS_F_N13 | Non Unique | Default | LEARNER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, STATUS, EVENT_TYPE |  |
| WLF_ASSIGNMENT_RECORDS_F_N14 | Non Unique | Default | ATTRIBUTION_ID, ATTRIBUTION_TYPE |  |
| WLF_ASSIGNMENT_RECORDS_F_N15 | Non Unique | Default | ASSIGNED_ON_DATE |  |
| WLF_ASSIGNMENT_RECORDS_F_N16 | Non Unique | Default | LEARNING_ITEM_TYPE, LEARNING_ITEM_SUB_TYPE |  |
| WLF_ASSIGNMENT_RECORDS_F_N17 | Non Unique | Default | ORIGINAL_EVENT_TYPE |  |
| WLF_ASSIGNMENT_RECORDS_F_N21 | Non Unique | Default | TRUNC("ASSIGNED_ON_DATE") |  |
| WLF_ASSIGNMENT_RECORDS_F_N27 | Non Unique | WLF_ASSIGNMENT_RECORDS_F_N27 | LEARNING_ITEM_CATEGORY |  |
| WLF_ASSIGNMENT_RECS_F_N1 | Non Unique | Default | EVENT_ASSIGNMENT_ID, EFFECTIVE_END_DATE |  |
| WLF_ASSIGNMENT_RECS_F_N11 | Non Unique | Default | ASSIGNMENT_RECORD_NUMBER |  |
| WLF_ASSIGNMENT_RECS_F_N18 | Non Unique | Default | LEARNING_ITEM_ID, LEARNER_ID, ASSIGNMENT_RECORD_ID |  |
| WLF_ASSIGNMENT_RECS_F_N2 | Non Unique | Default | LEARNER_ID, LEARNING_ITEM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, STATUS |  |
| WLF_ASSIGNMENT_RECS_F_N3 | Non Unique | Default | STATUS, SUB_STATUS |  |
| WLF_ASSIGNMENT_RECS_F_N4 | Non Unique | Default | EVENT_CREATED_BY_ID |  |
| WLF_ASSIGNMENT_RECS_F_N5 | Non Unique | Default | COMPLETION_DATE |  |
| WLF_ASSIGNMENT_RECS_F_N7 | Non Unique | Default | NOTIFICATION_STATUS |  |
| WLF_ASSIGNMENT_RECS_F_N8 | Non Unique | Default | EVENT_TYPE |  |
| WLF_ASSIGNMENT_RECS_F_N9 | Non Unique | Default | LEARNING_ITEM_ID, LEARNER_ID, EFFECTIVE_END_DATE, ACCESS_PERMISSION_ID |  |
| WLF_ASSIGNMENT_RECS_F_U1 | Unique | Default | ASSIGNMENT_RECORD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |  |
| WLF_ASSIGNMENT_REC_F_N19 | Non Unique | Default | TRUNC("LAST_UPDATE_DATE"), EVENT_TYPE |  |
| WLF_ASSIGNMENT_REC_F_N20 | Non Unique | Default | CAST("CALCULATED_DUE_DATE" AS TIMESTAMP) | Obsolete |
| WLF_ASSIGNMENT_RECORDS_F_N22 | Non Unique | Default | CREATION_DATE |  |
| WLF_ASSIGNMENT_REC_F_N23 | Non Unique | Default | IN_ELASTIC |  |
| WLF_ASSIGNMENT_REC_F_N24 | Non Unique | Default | LI_DEF_USED_DATE |  |
| WLF_ASSIGNMENT_REC_F_N25 | Non Unique | Default | EVENT_ASSIGNMENT_ID, LEARNER_ID |  |
| WLF_ASSIGNMENT_REC_F_N26 | Non Unique | Default | CAST("CALCULATED_DUE_DATE" AS TIMESTAMP), STATUS, EVENT_TYPE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |  |
| WLF_ASSIGNMENT_REC_F_N27 | Non Unique | Default | EVENT_ASSIGNMENT_ID, EVENT_TYPE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |  |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
