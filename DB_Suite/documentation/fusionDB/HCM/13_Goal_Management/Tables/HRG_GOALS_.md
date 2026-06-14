# HRG_GOALS_

Worker goals and its alignment details

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoals-21410.html#hrggoals-21410](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoals-21410.html#hrggoals-21410)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_GOALS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, GOAL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |
| LAST_MODIFIED_BY | NUMBER |  | 18 |  | This field store the person id of the person who modified the goals last time. |
| LAST_MODIFIED_DATE | TIMESTAMP |  |  |  | Field to store value of last goal modification timestamp |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_BUSINESS_GROUPS |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_ASSIGNMENTS_M, which holds assignment of worker. |
| PERSON_ID | NUMBER |  | 18 |  | Person Id of the person to whom the goal is assigned to. |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Reference to the organization to which goal is being created. |
| PUBLISHED_FLAG | VARCHAR2 | 30 |  |  | To Suggest if Organization goal is published. |
| PUBLISH_DATE | TIMESTAMP |  |  |  | The goal publish date |
| GOAL_TYPE_CODE | VARCHAR2 | 30 |  |  | Type of goal. Possible values are Development, Performance, Both and Personal |
| GOAL_NAME | VARCHAR2 | 400 |  |  | Name of goal. |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Description of goal. |
| START_DATE | DATE |  |  |  | Start date of goal. |
| TARGET_COMPLETION_DATE | DATE |  |  |  | Target completion date of gaol. |
| SUCCESS_CRITERIA | VARCHAR2 | 4000 |  |  | Criteria to complete goal. |
| SUCCESS_CRITERIA_TEXT | CLOB |  |  |  | New column for capturing criteria to complete goal. |
| PERCENT_COMPLETE_CODE | VARCHAR2 | 30 |  |  | Goal completion percentage code. |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Status of goal. |
| APPROVAL_STATUS_CODE | VARCHAR2 | 30 |  |  | Approval status code populated when goal is under some approval process |
| ACTUAL_COMPLETION_DATE | DATE |  |  |  | Actual completion date of goal. |
| REQUEST_CONTEXT | VARCHAR2 | 30 |  |  | Goal creation context. |
| GOAL_VERSION_TYPE_CODE | VARCHAR2 | 30 |  |  | Lookup to handle frozen goals and also goals created by HR specialist for mass assignment. |
| VERSION_DATE | TIMESTAMP |  |  |  | Date of goal version creation. |
| PRIORITY_CODE | VARCHAR2 | 30 |  |  | Priority of goal. Possible values are High, Medium and Low. |
| COMMENTS | VARCHAR2 | 4000 |  |  | To capture comments on the goal |
| COMMENTS_TEXT | CLOB |  |  |  | New column to capture comments on the goal. |
| REQUESTER_PERSON_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_PEOPLE_F, which holds the PersonId of requester. |
| ASSIGNED_BY_PERSON_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_PEOPLE_F, which holds the ID of person who assigns goal to worker. |
| GOAL_SOURCE_CODE | VARCHAR2 | 30 |  |  | Source of assignment. Possible values are Admin, HR, Manager and Worker. |
| REFERENCE_CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign key to HRT_CONTENT_ITEMS_B, which holds the ID of a goal in library. It represents the source of this goal record. |
| REFERENCE_GOAL_ID | NUMBER |  | 18 |  | Foreign key to HRT_CONTENT_ITEMS_B, which holds the ID of a goal in library. It represents the source of the goal. |
| PRIVATE_FLAG | VARCHAR2 | 30 |  |  | Flag to indicate whether this goal is accessible to others or not |
| ACCESS_TO_HIERARCHY_FLAG | VARCHAR2 | 30 |  |  | Flag to indicate this goal can be accessible to the hierarchy |
| HRCHY_ACCESS_GRANT_DATE | TIMESTAMP |  |  |  | Hieararchy access grant date. |
| ALLOW_KEY_ATTR_UPDATE_FLAG | VARCHAR2 | 30 |  |  | Key attribute modification is allowed or not. |
| ALLOW_DEL_GOAL_FLAG | VARCHAR2 | 30 |  |  | Manager can delete worker goal or not. |
| INCLUDE_IN_PERFDOC_FLAG | VARCHAR2 | 30 |  |  | Goal is marked to include in performance document. |
| GOAL_URL | VARCHAR2 | 4000 |  |  | URL related to the goal. |
| LEVEL_CODE | VARCHAR2 | 30 |  |  | Leve code i.e Stretch or Maximum |
| LEVEL_MEANING | VARCHAR2 | 240 |  |  | Meaning of Level. |
| CATEGORY_CODE | VARCHAR2 | 30 |  |  | Admin-defined category for a goal. |
| MEASURE_TYPE_CODE | VARCHAR2 | 30 |  |  | Code for the measurement type |
| MEASURE_NAME | VARCHAR2 | 240 |  |  | For qualitative vs. quantitative measures. Target you are trying to hit. |
| MEASURE_COMMENTS | VARCHAR2 | 4000 |  |  | Comments for measurement of a goal |
| TARGET_VALUE | NUMBER |  | 18 |  | Value of the target for the quantitative measures. |
| TARGET_TYPE | VARCHAR2 | 30 |  |  | Type of target for the quantitative measures |
| UOM_CODE | VARCHAR2 | 30 |  |  | Units of measure, %, dollar amounts, etc |
| ACTUAL_VALUE | NUMBER |  | 18 |  | Actual value attained for the quantitative measures |
| MASS_REQUEST_ID | NUMBER |  | 18 |  | Foreign key to HRG_GOAL_MASS_REQUESTS |
| GOAL_EXT_ID | VARCHAR2 | 250 |  |  | Not unique at worker level |
| GOAL_ACCESS_LEVEL_CODE | VARCHAR2 | 30 |  |  | Propagate the read-only status from goal plan. If the goal is part of two contradicting goal plans (Yes wins always - among the read-only or updatable goal plans |
| GOAL_SUB_TYPE_CODE | VARCHAR2 | 30 |  |  | Goal Sub Type Code is to support customer specific requirements like extensibility. |
| MEASURE_CALC_RULE_CODE | VARCHAR2 | 30 |  |  | Aggregated function for aggregating the actual and target values at sub-goal (only AVG or SUM). Looup HRG_CALCULATION_RULE_CODE will list the values. |
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
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ACTIVE_FLAG | VARCHAR2 | 30 |  |  | Active Flag used only for Career Development Goal |
| GOAL_APPROVAL_STATE | VARCHAR2 | 30 |  |  | Goal Approval State included for Mass Goal Approval |
| APPROVER_RESPONSE_CODE | VARCHAR2 | 30 |  |  | Response from Approver on a Goal after Goal is rejected |
| PREVIOUS_STATE_GOAL_ID | NUMBER |  | 18 |  | Previous state goal id value relevant during mass goal approval flow |
| LONG_DESCRIPTION | CLOB |  |  |  | New column to capture long description of the goal. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_GOALSN1_ | Non Unique | Default | GOAL_ID |
| HRG_GOALSU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, GOAL_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
