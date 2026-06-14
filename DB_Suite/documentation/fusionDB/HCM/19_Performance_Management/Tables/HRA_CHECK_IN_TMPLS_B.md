# HRA_CHECK_IN_TMPLS_B

This table will store UI field values for creating Check-In Template like Check-In from date, to date, status etc.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hracheckintmplsb-21959.html#hracheckintmplsb-21959](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hracheckintmplsb-21959.html#hracheckintmplsb-21959)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_CHECK_IN_TMPLS_B_PK | CHECK_IN_TEMPLATE_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECK_IN_TEMPLATE_ID | NUMBER |  | 18 | Yes | Primary Key of Check-In Template |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ALL_ORGANIZATION_UNITS |
| TEMPLATE_TYPE_CODE | VARCHAR2 | 30 |  |  | Identifies template type of the CheckIn template. |
| WORKER_QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Foreign Key to Questionnaire table |
| MANAGER_QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Foreign Key to Questionnaire table |
| DATE_FROM | DATE |  |  | Yes | Date from which the Check-In Template is valid |
| DATE_TO | DATE |  |  | Yes | Date till the Check-In Template is valid |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Status of the Check-In Template |
| FREE_FORM_NOTES_FLAG | VARCHAR2 | 30 |  |  | This column is not in use. |
| PERFORMANCE_GOALS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the Check-In Template can add Performance Goals |
| DEVELOPMENT_GOALS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the Check-In Template can add Development Goals |
| GENERAL_DISCUSSION_TOPIC_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the Check-In Template can have General discussion topic |
| QUESTIONNAIRE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the Check-In Template can add Questionnaire |
| PERF_GOALS_AUTO_POPULATE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether check-in meeting will auto populate all performance goals with in a review period if set to yes |
| DEV_GOALS_AUTO_POPULATE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether check-in meeting will auto populate all development goals with in a review period if set to yes |
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
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| INCLUDE_IN_PERF_DOC_FLAG | VARCHAR2 | 30 |  |  | Indicates if the CheckIn Template can be displayed in performance document. |
| ALL_REVIEW_PERIODS_FLAG | VARCHAR2 | 30 |  |  | Indicates if the Checkin Template is available to all review periods |
| ANYTIME_FEEDBACK_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the Check-In Template can add Anytime Feedback. |
| REQUESTED_FEEDBACK_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the Check-In Template can add Requested Feedback. |
| COMPETENCY_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to include Competencies as discussion topics. |
| DEVELOPING_SKILL_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to include skills the employee is developing as discussion topics. |
| DEVELOPED_SKILL_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to include skills the employee developed as discussion topics. |
| ALL_MANAGER_TYPES_CODE | VARCHAR2 | 30 |  |  | Specify all manager types that can access check-in templates. |
| MANAGER_TYPES | VARCHAR2 | 4000 |  |  | Specify manager types that can access check-in templates. |
| WKR_QSTNR_SCORING_FLAG | VARCHAR2 | 30 |  |  | Stores whether the worker questionnaire is scored. |
| WKR_CAN_VIEW_WKR_SCORES_FLAG | VARCHAR2 | 30 |  |  | Stores whether the worker questionnaire score can be viewed by worker. |
| WKR_CAN_VIEW_MGR_SCORES_FLAG | VARCHAR2 | 30 |  |  | Stores whether the manager questionnaire score can be viewed by worker. |
| MGR_QSTNR_SCORING_FLAG | VARCHAR2 | 30 |  |  | Stores whether the manager questionnaire is scored. |
| MGR_CAN_VIEW_WKR_SCORES_FLAG | VARCHAR2 | 30 |  |  | Stores whether the worker questionnaire score can be viewed by manager. |
| MGR_CAN_VIEW_MGR_SCORES_FLAG | VARCHAR2 | 30 |  |  | Stores whether the manager questionnaire score can be viewed by manager. |
| CALENDAR_INVITE_FLAG | VARCHAR2 | 30 |  |  | Identify if the create meeting invite is enabled or not. |
| NUDGES_FLAG | VARCHAR2 | 30 |  |  | Stores whether to include nudges as suggestion in check-in
template. |
| OPEN_TOPICS_NO_OF_MONTHS | NUMBER |  | 3 |  | Stores how many months of open discussion topics to be included as
suggestion in check-in template. |
| SUGGEST_DISCUSSION_TOPICS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to include AI generated general discussion topics as
suggestion in check-in template. |
| SUGGEST_LEARNING_ACTIONS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to display learning actions in
check-in template. |
| SUGGEST_PERF_GOAL_ACTIONS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to display performance goal
actions in check-in template. |
| SUGGEST_DEV_GOAL_ACTIONS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to display development goal
actions in check-in template. |
| TOPICS_PRIOR_CHECK_INS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to include open discussion topics
as suggestion in check-in template. |
| MANAGER_CAN_CREATE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the manager can create a check-in. |
| MANAGER_CAN_UPDATE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the manager can update a check-in. |
| MANAGER_CAN_CLOSE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the manager can close a check-in. |
| MANAGER_CAN_REOPEN_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the manager can reopen a check-in. |
| WORKER_CAN_CREATE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the worker can create a check-in. |
| WORKER_CAN_UPDATE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the worker can update a check-in. |
| WORKER_CAN_CLOSE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the worker can close a check-in. |
| WORKER_CAN_REOPEN_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the worker can reopen a check-in. |
| SUGGESTED_COMPETENCY_FLAG | VARCHAR2 | 30 |  |  | Stores whether to display learning actions in
check-in template. |
| MANAGER_CAN_DELETE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the manager can delete a check-in. |
| WORKER_CAN_DELETE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the worker can delete a check-in. |
| POSITION_PROFILE_COMP_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to include position profile competency as discussion topics. |
| JOB_PROFILE_COMP_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to include job profile competency as discussion topics. |
| WKR_CAN_VIEW_MGR_QSTNR_FLAG | VARCHAR2 | 30 |  |  | Stores whether the manager questionnaire can be viewed by worker. |
| MGR_CAN_VIEW_WKR_QSTNR_FLAG | VARCHAR2 | 30 |  |  | Stores whether the worker questionnaire can be viewed by manager. |
| SHOW_DONE_FOR_WKR_QSTNR_FLAG | VARCHAR2 | 30 |  |  | Stores whether to show mark as done switch for worker. |
| SHOW_DONE_FOR_MGR_QSTNR_FLAG | VARCHAR2 | 30 |  |  | Stores whether to show mark as done switch for manager. |
| HIDE_MGR_QSTNR_UNTIL_DONE_FLAG | VARCHAR2 | 30 |  |  | Stores whether to hide manager questionnaire until manager marks it as done. |
| HIDE_WKR_QSTNR_UNTIL_DONE_FLAG | VARCHAR2 | 30 |  |  | Stores whether to hide worker questionnaire until worker marks it as done. |
| WKR_QSTNR_SUBSCRIBER_CODE | VARCHAR2 | 30 |  |  | Stores the worker questionnaire subscriber code. |
| MGR_QSTNR_SUBSCRIBER_CODE | VARCHAR2 | 30 |  |  | Stores the manager questionnaire subscriber code. |
| SHOW_ATTACHMENTS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to include attachments in checkins or not. |
| SUGGEST_LEARN_ITEMS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to display learn items in
check-in template. |
| ALLOW_TRANSCRIPT_FLAG | VARCHAR2 | 30 |  |  | Stores whether to allow transcript in
check-in template. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_CHECK_IN_TMPLS_B_PK | Unique | Default | CHECK_IN_TEMPLATE_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
