# WLF_ASSIGNMENT_RULES

Table to store assignment rules with initial dates, expiry dates and renewal options.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfassignmentrules-18759.html#wlfassignmentrules-18759](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfassignmentrules-18759.html#wlfassignmentrules-18759)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ASSIGNMENT_RULES_PK | ASSIGNMENT_RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNMENT_RULE_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_RULE_ID |
| DEFAULT_INITIAL_REC_SUBSTA | VARCHAR2 | 30 |  |  | Initial assignment record substatus. |
| DEFAULT_INITIAL_ACT_SCORE | NUMBER |  | 9 |  | DEFAULT_INITIAL_ACT_SCORE |
| DEFAULT_INITIAL_COMMENTS | VARCHAR2 | 255 |  |  | Comments for assignment status completion. |
| DEFAULT_INITIAL_COMPL_DATE | TIMESTAMP |  |  |  | The date and time of the completion of the assignment. |
| DEFAULT_INITIAL_TOTACT_EFF | NUMBER |  | 9 |  | Actual effort learner has spent on an assignment. |
| DEFAULT_INITIAL_REASON_CODE | VARCHAR2 | 30 |  |  | Initial reason for assignment status completion. |
| INITIAL_DUE_DATE_OPTION | VARCHAR2 | 30 |  |  | INITIAL_DUE_DATE_OPTION |
| INITIAL_DUE_DATE | TIMESTAMP |  |  |  | INITIAL_DUE_DATE |
| INITIAL_DUE_IN_DAYS | NUMBER |  |  |  | INITIAL_DUE_IN_DAYS |
| VALIDITY_OPTION | VARCHAR2 | 30 |  |  | VALIDITY_OPTION |
| EXPIRY_OPTION | VARCHAR2 | 30 |  |  | EXPIRY_OPTION |
| EXPIRY_IN_DAYS | NUMBER |  |  |  | EXPIRY_IN_DAYS |
| EXPIRY_DATE | TIMESTAMP |  |  |  | EXPIRY_DATE |
| EXPIRY_IN_NUM_YRS | VARCHAR2 | 30 |  |  | EXPIRY_IN_NUM_YRS |
| RENEWAL_OPTIONS | VARCHAR2 | 30 |  |  | RENEWAL_OPTIONS |
| RENEWAL_BEFORE_EXPIRY_DAYS | NUMBER |  |  |  | RENEWAL_BEFORE_EXPIRY_DAYS |
| DYN_ENABLED | VARCHAR2 | 1 |  | Yes | DYN_ENABLED |
| DYN_DUE_DATE_OPTION | VARCHAR2 | 30 |  |  | DYN_DUE_DATE_OPTION |
| DYN_DUE_DATE | TIMESTAMP |  |  |  | DYN_DUE_DATE |
| DYN_DUE_IN_DAYS | NUMBER |  |  |  | DYN_DUE_IN_DAYS |
| DYN_MIN_DAYS_TO_COMPLETE | NUMBER |  |  |  | Minimum number of days to complete an ongoing assignment. If the days are not sufficient, then Ongoing due date is set to next Calendar year |
| DYN_WITHDRAW_OPTION | VARCHAR2 | 30 |  |  | DYN_WITHDRAW_OPTION |
| DYN_STOP_NEW_DATE | TIMESTAMP |  |  |  | DYN_STOP_NEW_DATE |
| DYN_STOP_WITHDRAW_DATE | TIMESTAMP |  |  |  | DYN_STOP_WITHDRAW_DATE |
| PLAN_ITEM_WITHDRAW_STATUS | VARCHAR2 | 30 |  |  | PLAN_ITEM_WITHDRAW_STATUS |
| DEFAULT_INITIAL_RECORD_STATUS | VARCHAR2 | 30 |  |  | Default initial assignment record status for the learning item |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CLS_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| CLS_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER1 |
| CLS_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER2 |
| CLS_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER3 |
| CLS_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER4 |
| CLS_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER5 |
| CLS_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER6 |
| CLS_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER7 |
| CLS_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER8 |
| CLS_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER9 |
| CLS_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER10 |
| CLS_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER11 |
| CLS_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER12 |
| CLS_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER13 |
| CLS_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER14 |
| CLS_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER15 |
| CLS_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER16 |
| CLS_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER17 |
| CLS_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER18 |
| CLS_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER19 |
| CLS_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER20 |
| CLS_ATTRIBUTE_DATE1 | DATE |  |  |  | CLS_ATTRIBUTE_DATE1 |
| CLS_ATTRIBUTE_DATE2 | DATE |  |  |  | CLS_ATTRIBUTE_DATE2 |
| CLS_ATTRIBUTE_DATE3 | DATE |  |  |  | CLS_ATTRIBUTE_DATE3 |
| CLS_ATTRIBUTE_DATE4 | DATE |  |  |  | CLS_ATTRIBUTE_DATE4 |
| CLS_ATTRIBUTE_DATE5 | DATE |  |  |  | CLS_ATTRIBUTE_DATE5 |
| CLS_ATTRIBUTE_DATE6 | DATE |  |  |  | CLS_ATTRIBUTE_DATE6 |
| CLS_ATTRIBUTE_DATE7 | DATE |  |  |  | CLS_ATTRIBUTE_DATE7 |
| CLS_ATTRIBUTE_DATE8 | DATE |  |  |  | CLS_ATTRIBUTE_DATE8 |
| CLS_ATTRIBUTE_DATE9 | DATE |  |  |  | CLS_ATTRIBUTE_DATE9 |
| CLS_ATTRIBUTE_DATE10 | DATE |  |  |  | CLS_ATTRIBUTE_DATE10 |
| CLS_ATTRIBUTE_DATE11 | DATE |  |  |  | CLS_ATTRIBUTE_DATE11 |
| CLS_ATTRIBUTE_DATE12 | DATE |  |  |  | CLS_ATTRIBUTE_DATE12 |
| CLS_ATTRIBUTE_DATE13 | DATE |  |  |  | CLS_ATTRIBUTE_DATE13 |
| CLS_ATTRIBUTE_DATE14 | DATE |  |  |  | CLS_ATTRIBUTE_DATE14 |
| CLS_ATTRIBUTE_DATE15 | DATE |  |  |  | CLS_ATTRIBUTE_DATE15 |
| LEARNING_ITEM_EFFECTIVITY | VARCHAR2 | 30 |  |  | Different learning item effectivity options from an assignment |
| PREREQ_EVAL_TYPE | VARCHAR2 | 30 |  |  | Prereq evaluation type , Deferred or Not Deferred |
| PREREQ_EVAL_DAYS | NUMBER |  |  |  | Number of days after assigned on date when prereq has to be evaluated |
| WAIVE_OFF | VARCHAR2 | 1 |  |  | Waive of prereq for a learner |
| WAIVE_OFF_RSN_CODE | VARCHAR2 | 30 |  |  | Reason to waive of prereq for a learner |
| WAIVE_OFF_RSN_COMMENTS | VARCHAR2 | 4000 |  |  | comments for waiving of a prereq for a learner |
| WAIVE_PAYMENT | VARCHAR2 | 30 |  |  | Indicates if payment is waived off. |
| WAIATLIST_DISPOSITION | VARCHAR2 | 64 |  |  | WAIATLIST_DISPOSITION |
| WAITLIST_DISPOSITION_TYPE | VARCHAR2 | 64 |  |  | WAITLIST_DISPOSITION_TYPE |
| EVENT_ASSIGNMENT_ID | NUMBER |  | 18 |  | Stores Event assignment which the rule is related. |
| ASSIGNMENT_RECORD_ID | NUMBER |  | 18 |  | Stores Assignment record for which the rule is related. |
| AC_WITHDRAW_INFLIGHT_ASSIGN | VARCHAR2 | 1 |  |  | Option to withdraw inflight assignments |
| AC_WITHDRAW_HIDE_FROM_TRANS | VARCHAR2 | 1 |  |  | Option to hide withdrawn assignments from transcript |
| AC_EXPIRE_COMPLETED_ASSIGN_NEW | VARCHAR2 | 1 |  |  | Option to expire all completed assignments and create a new assignment |
| AC_ASSIGN_NEW_EXP_OLD_ON_COMPL | VARCHAR2 | 1 |  |  | Option to create a new assignment and expire all completed assignments on the new assignment completion |
| AC_SKIP_ASSIGN_WTH_EXIST_COMPL | VARCHAR2 | 1 |  |  | Option to skip creating new assignment when completed assignments exist |
| AC_COMPL_ASSIGN_CONFLICT_RULE | VARCHAR2 | 30 |  |  | Completed assignments conflict rule |
| COMPL_ASSIGN_EXPIRATION_OPTION | VARCHAR2 | 30 |  |  | This column will be used to capture expiration rule |
| COMPL_ASSIGN_EXEMPT_AFTER_DATE | DATE |  |  |  | This column will be used to capture date beyond with learning will be exempted |
| COMPL_ASSIGN_EXEMPT_AFTER_DAYS | NUMBER |  |  |  | This column will be used to capture days beyond with learning will be exempted |
| SELF_ENROLL_RETAKE_RULE | VARCHAR2 | 30 |  |  | Learners Can Take Again |
| IS_NEW_PROFILE | VARCHAR2 | 1 |  |  | Indicates whether the profile was created in Redwood |
| EXPIRY_VALIDITY_OPTION | VARCHAR2 | 30 |  |  | Indicates the option to calculate the expiration date |
| EXPIRY_IN_UNITS | NUMBER |  |  |  | Expiration units |
| EXPIRY_UOM | VARCHAR2 | 30 |  |  | Expiration unit of measure |
| REASSIGNMENT_RULE | VARCHAR2 | 30 |  |  | Assignment Renewal Period Rule |
| RETAKE_RULE_UNITS | NUMBER |  |  |  | Retake units |
| RETAKE_RULE_UOM | VARCHAR2 | 30 |  |  | Retake unit of measure |
| DYN_DUE_DATE_UNITS | NUMBER |  |  |  | Dynamic Due date units |
| DYN_DUE_DATE_UOM | VARCHAR2 | 30 |  |  | Dynamic Due date unit of measure |
| INITIAL_DUE_DATE_UNITS | NUMBER |  |  |  | Due date units |
| INITIAL_DUE_DATE_UOM | VARCHAR2 | 30 |  |  | Due date unit of measure |
| REASSIGN_NUMBER | NUMBER |  |  |  | Renewal period number |
| REASSIGN_UOM | VARCHAR2 | 30 |  |  | Renewal unit of measure |
| REASSIGN_ON_DAY | NUMBER |  |  |  | Renewal day |
| REASSIGN_ON_MONTH | VARCHAR2 | 30 |  |  | Renewal month |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_ASSIGNMENT_RULES_N1 | Non Unique | Default | DYN_ENABLED |
| WLF_ASSIGNMENT_RULES_U1 | Unique | Default | ASSIGNMENT_RULE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
