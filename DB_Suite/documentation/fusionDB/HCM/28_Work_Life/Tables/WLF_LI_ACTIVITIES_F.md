# WLF_LI_ACTIVITIES_F

Table to store details of activities in a class

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliactivitiesf-8526.html#wlfliactivitiesf-8526](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliactivitiesf-8526.html#wlfliactivitiesf-8526)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_ACTIVITIES_F_PK | ACTIVITY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | Learning item id pk |
| ACTIVITY_ID | NUMBER |  | 18 | Yes | Activity Id. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PARENT_LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | The learning item that this activity is the child of |
| RELATED_CONTENT_ID | NUMBER |  | 18 |  | RELATED_CONTENT_ID |
| COMPLETION_TYPE | VARCHAR2 | 30 |  |  | Indicate the completion type of this activity (Required, Optional, etc) |
| DUE_DATE | TIMESTAMP |  |  |  | Indicates the due date of the activity |
| VIRTUAL_CLASSROOM_URL | VARCHAR2 | 500 |  |  | VIRTUAL_CLASSROOM_URL |
| ACTIVITY_TYPE | VARCHAR2 | 30 |  |  | Indicates what type of activity this is |
| CONTENT_TYPE | VARCHAR2 | 30 |  |  | Indicates what type of content |
| SERIES_ID | NUMBER |  | 18 |  | Identifier of activity series profile. Foreign key to WLF_ACTIVITY_SERIES_PROFILE_F. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SELF_COMPLETE_FLAG | VARCHAR2 | 1 |  |  | Flag to indicate if the learner able to mark this activity complete |
| SECTION_LI_ID | NUMBER |  | 18 |  | Column value represents section learning item id of the activity |
| TIME_ZONE | VARCHAR2 | 30 |  |  | Time zone of the start and end date |
| ACT_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ACT_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACT_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER1 |
| ACT_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER2 |
| ACT_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER3 |
| ACT_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER4 |
| ACT_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER5 |
| ACT_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER6 |
| ACT_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER7 |
| ACT_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER8 |
| ACT_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER9 |
| ACT_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER10 |
| ACT_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER11 |
| ACT_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER12 |
| ACT_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER13 |
| ACT_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER14 |
| ACT_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER15 |
| ACT_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER16 |
| ACT_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER17 |
| ACT_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER18 |
| ACT_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER19 |
| ACT_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | ACT_ATTRIBUTE_NUMBER20 |
| ACT_ATTRIBUTE_DATE1 | DATE |  |  |  | ACT_ATTRIBUTE_DATE1 |
| ACT_ATTRIBUTE_DATE2 | DATE |  |  |  | ACT_ATTRIBUTE_DATE2 |
| ACT_ATTRIBUTE_DATE3 | DATE |  |  |  | ACT_ATTRIBUTE_DATE3 |
| ACT_ATTRIBUTE_DATE4 | DATE |  |  |  | ACT_ATTRIBUTE_DATE4 |
| ACT_ATTRIBUTE_DATE5 | DATE |  |  |  | ACT_ATTRIBUTE_DATE5 |
| ACT_ATTRIBUTE_DATE6 | DATE |  |  |  | ACT_ATTRIBUTE_DATE6 |
| ACT_ATTRIBUTE_DATE7 | DATE |  |  |  | ACT_ATTRIBUTE_DATE7 |
| ACT_ATTRIBUTE_DATE8 | DATE |  |  |  | ACT_ATTRIBUTE_DATE8 |
| ACT_ATTRIBUTE_DATE9 | DATE |  |  |  | ACT_ATTRIBUTE_DATE9 |
| ACT_ATTRIBUTE_DATE10 | DATE |  |  |  | ACT_ATTRIBUTE_DATE10 |
| ACT_ATTRIBUTE_DATE11 | DATE |  |  |  | ACT_ATTRIBUTE_DATE11 |
| ACT_ATTRIBUTE_DATE12 | DATE |  |  |  | ACT_ATTRIBUTE_DATE12 |
| ACT_ATTRIBUTE_DATE13 | DATE |  |  |  | ACT_ATTRIBUTE_DATE13 |
| ACT_ATTRIBUTE_DATE14 | DATE |  |  |  | ACT_ATTRIBUTE_DATE14 |
| ACT_ATTRIBUTE_DATE15 | DATE |  |  |  | ACT_ATTRIBUTE_DATE15 |
| DISPLAY_PREDECESSOR_ID | NUMBER |  | 18 |  | Used to store predecessor activity calculated by position |
| ELEARNING_TYPE | VARCHAR2 | 30 |  |  | Indicates the elearning type of the content associated with activity |
| CLASSROOM_DISPLAY_NAME | VARCHAR2 | 2000 |  |  | Indicates external event classroom name |
| EXTERNAL_DETAILS_URL | VARCHAR2 | 2000 |  |  | Indicates external event details |
| COMPLETION_RULE | VARCHAR2 | 30 |  |  | Indicates completion rule for event activity |
| AUTO_COMPLETION_RULE_ENABLED | VARCHAR2 | 1 |  |  | Flag to indicate if automated completion based on percentage or minutes of total duration is enabled for VILT event activities |
| AUTO_COMPLETION_RULE_UNITS | VARCHAR2 | 30 |  |  | Indicates whether it is percentage or minutes based completion |
| AUTO_COMPLETION_RULE_VALUE | NUMBER |  | 3 |  | The minimum attendance duration in minutes or percentage required by learner to automatically trigger VILT activity completion |
| BREAKOUT_ROOMS_ENABLED | VARCHAR2 | 1 |  |  | Configuration to specify whether breakout rooms are enabled |
| ONLINE_MEETING_TYPE | VARCHAR2 | 30 |  |  | Indicates if the type of online meeting |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_ACTIVITIES_F_N1 | Non Unique | Default | PARENT_LEARNING_ITEM_ID |
| WLF_LI_ACTIVITIES_F_N2 | Non Unique | Default | RELATED_CONTENT_ID |
| WLF_LI_ACTIVITIES_F_PK | Unique | Default | ACTIVITY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| WLF_LI_ACTIVITIES_F_U1 | Unique | Default | LEARNING_ITEM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
