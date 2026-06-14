# HRG_GOAL_PLANS_B

Stores the goal plan definition related details

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalplansb-11954.html#hrggoalplansb-11954](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalplansb-11954.html#hrggoalplansb-11954)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_GOAL_PLANS_B_PK | GOAL_PLAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| GOAL_PLAN_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |  |
| EVALUATION_TYPE | VARCHAR2 | 30 |  |  | This column is to set evaluation type to be used in Performance template |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |  |
| GOAL_PLAN_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Type of Goal Plan. |  |
| START_DATE | DATE |  |  | Yes | Goal Plan start date |  |
| END_DATE | DATE |  |  | Yes | Goal Plan end date |  |
| GOAL_SETTING_START_DATE | DATE |  |  |  | Goal Plan Goal Set Start Date |  |
| GOAL_SETTING_END_DATE | DATE |  |  |  | Goal Plan Goal Set End Date |  |
| RESTRICT_GOAL_CREATION_FLAG | VARCHAR2 | 30 |  |  | Flag Indicate Restricting Goal Creation after Goal Set End Date |  |
| RESTRICT_GOAL_UPDATE_FLAG | VARCHAR2 | 30 |  |  | Flag Indicate Restricting Goal Update after Goal Set End Date |  |
| ENABLE_WEIGHTING_FLAG | VARCHAR2 | 30 |  |  | Flag to indicate whether weighting can be specified with goal. |  |
| PREVIOUS_GOAL_PLAN_ID | NUMBER |  | 18 |  | Foreign key to HRG_GOAL_PLANS_B, which holds the ID of previous goal plan. |  |
| MASS_REQUEST_ID | NUMBER |  | 18 |  | Foreign key to HRG_GOAL_MASS_REQUESTS |  |
| GOAL_PLAN_EXT_ID | VARCHAR2 | 250 |  |  | Unique for goal plan. Need an migration script to populate this value of existing goal plans. |  |
| GOAL_SUB_TYPE_CODE | VARCHAR2 | 30 |  |  | Goal Sub type to support customer specific requirements. Lookup HRG_SUB_TYPE_CODE will list the values. |  |
| GOAL_ACCESS_LEVEL_CODE | VARCHAR2 | 30 |  | Yes | The goals in the goal plan with this column set, would be view-only (no insert/update/delete). Lookup HRG_ACCESS_LEVELS will list the values. |  |
| INCLUDE_IN_PERFDOC_FLAG | VARCHAR2 | 30 |  | Yes | If this flag is set, the goals in the goal plan would be added to PD |  |
| GOAL_PLAN_ACTIVE_FLAG | VARCHAR2 | 30 |  | Yes | This colum is to decide whether plan is active or not |  |
| AUTO_ASSOCIATE_GOAL_FLAG | VARCHAR2 | 30 |  | Yes | This column to identify whether this goal plan can be considered for auto goal assignment |  |
| REQUEST_UI_CONTEXT_CODE | VARCHAR2 | 30 |  |  | this column to identify the request context of the goal plan (UI or File based loader) |  |
| ENFORCE_GOAL_WEIGHT_FLAG | VARCHAR2 | 30 |  |  | This is to enforce thesummation of goal  weight to 100 at goal plan level if set to yes |  |
| PRIMARY_GOAL_PLAN_FLAG | VARCHAR2 | 30 |  |  | This flag indicates whether the goal plan is chosen as primary. |  |
| CAN_DEL_HR_GOAL | VARCHAR2 | 60 |  |  | This value indicates whether HR assigned goals can be deleted or canceled by managers and workers |  |
| MAX_GOALS_NUM_IN_GOAL_PLAN | NUMBER |  | 18 |  | This field is for restricting the number of goals in a goal plan to help support the requirement of limiting the number of performance goals that employees need to focus on during the review period. |  |
| ENFORCE_MAX_GOALS_IN_GP_FLAG | VARCHAR2 | 30 |  |  | This field is for enforcing the number of goals in a goal plan to help support the requirement of limiting the number of performance goals on manager and HR goal assignments. |  |
| ALLOW_PVT_GOAL_MAX_GOAL_FLAG | VARCHAR2 | 30 |  |  | If this flag is set, employee can add the goals in the goal plan as private goals when max goals in goal plan limit is reached. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE1 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE2 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE3 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE4 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE5 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE6 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE7 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE8 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE9 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE10 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE11 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE12 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE13 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE14 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE15 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE16 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE17 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE18 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE19 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE20 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE21 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE22 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE23 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE24 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE25 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE26 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE27 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE28 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE29 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE30 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | HRG_GOAL_PLANS_B (HRG_GOAL_PLANS_B) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| REVIEW_PERIOD_ID | NUMBER |  | 18 |  | Foreign key to HRT_REVIEW_PERIODS_B |  |
| CREATED_BY_SYSTEM | VARCHAR2 | 30 |  | Yes | If this flag is Y, it means that goal plan is created by system. |  |
| ALL_DEPARTMENTS_FLAG | VARCHAR2 | 30 |  |  | ALL_DEPARTMENTS_FLAG |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| REQUEST_STATUS | VARCHAR2 | 30 |  |  | Stores request status of the last ESS job submitted for this goal plan |  |
| MIN_GOALS_NUM_IN_GOAL_PLAN | NUMBER |  | 18 |  | This field is for restricting for minimum number of goals in a goal plan |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_GOAL_PLANS_B_FK1 | Non Unique | Default | MASS_REQUEST_ID |
| HRG_GOAL_PLANS_B_N1 | Non Unique | Default | START_DATE |
| HRG_GOAL_PLANS_B_N2 | Non Unique | Default | END_DATE |
| HRG_GOAL_PLANS_B_N3 | Non Unique | Default | GOAL_PLAN_TYPE_CODE |
| HRG_GOAL_PLANS_B_N4 | Non Unique | Default | REVIEW_PERIOD_ID |
| HRG_GOAL_PLANS_B_N5 | Non Unique | Default | PRIMARY_GOAL_PLAN_FLAG |
| HRG_GOAL_PLANS_B_PK | Unique | Default | GOAL_PLAN_ID |
| HRG_GOAL_PLANS_B_UK1 | Unique | Default | GOAL_PLAN_EXT_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
