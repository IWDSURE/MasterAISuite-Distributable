# HRA_SECTION_DEFNS_B

This table contains the definition for a section.These sections can be included in a Performance Template.For example it stores whether the section is a competency section or goals section or overall ratings section etc.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrasectiondefnsb-22751.html#hrasectiondefnsb-22751](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrasectiondefnsb-22751.html#hrasectiondefnsb-22751)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_SECTION_DEFNS_B_PK | SECTION_DEF_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| SECTION_DEF_ID | NUMBER |  | 18 | Yes | System generated Primary Key for Section Definition |  |  |
| ENABLE_MGR_REASON_FLAG | VARCHAR2 | 30 |  |  | Indicates whether manger has to give reason if manual Rating is different from Calculated Rating |  |  |
| REFERENCE_SECTION_ID | NUMBER |  |  |  | Indicates the reference to the current section in Profile Management |  |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |  |
| DATE_FROM | DATE |  |  | Yes | This is the date from which the section is valid. |  |  |
| DATE_TO | DATE |  |  |  | End date of the section definition. |  |  |
| STATUS_CODE | VARCHAR2 | 30 |  |  | This field stores the lookup code for the section status. |  |  |
| SECTION_TYPE_CODE | VARCHAR2 | 30 |  |  | This field stores a lookup code for the section type.The section type describes how the system should process this section. |  |  |
| RATE_SECTION_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to allow the user to enter a rating for the section, or for the system to calculate a rating for the section. |  |  |
| CALCULATION_RULE_CODE | VARCHAR2 | 30 |  |  | This field specifies the caluclation rule to be used when the section is to be rated. |  |  |
| FAST_FORMULA_ID | NUMBER |  | 18 |  | Indicates the fast formula to be used when the section is to be rated by means of calculation using a fast formula. |  |  |
| SECTION_RATING_MODEL_ID | NUMBER |  | 18 |  | This field iindicates the default rating model for the section. |  |  |
| WEIGHT_SECTION_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the section can have a weighting relative to other sections within the performance document |  |  |
| SECTION_WEIGHT | NUMBER |  | 20 |  | This is the default weight for a section.  Any numeric value between 1 and 100 can be entered. |  |  |
| SECTION_MIN_WEIGHT | NUMBER |  | 20 |  | This is the minimum weight for a section.  This field is used when ratings are calculated by the system, to ensure that the section weight cannot fall below a minimum value. |  |  |
| ENABLE_ITEMS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the section will contain items such as specific competencies or goals. Typically this would be Yes for Competencies and goals, and No for all other sections such as Worker Final Feedback, Manager Final Feedback, etc. |  |  |
| CONTENT_PROFILE_FLAG | VARCHAR2 | 30 |  |  | This field indicates whether the section will refer to the content library when the user adds items. |  |  |
| CONTENT_TYPE_ID | NUMBER |  | 18 |  | This field stores the ID of a content type to be used in the section. |  |  |
| FREE_FORM_ALLOWED_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the system will allow the user to add free-from items (that is, items that are not held in a library or table in the system), at the performance document. |  |  |
| ADD_ITEMS_CONFIRM_CRIT_FLAG | VARCHAR2 | 30 |  |  | This column describes whether the system will allow users to add items to the section (these items then represent the evaluation criteria for the worker). |  |  |
| RATE_ITEM_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the user can rate each item within the section.  This would be typically used for sections like Competencies and Goals. |  |  |
| RATING_TYPE_CODE | VARCHAR2 | 30 |  |  | This field indicates the rating type to apply for items in this section. |  |  |
| USE_SECRTG_FOR_PERFRTG_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the system will use the rating model specified for section, for all items within this section. |  |  |
| PERF_RATING_MODEL_ID | NUMBER |  | 18 |  | This is the rating model for performance ratings, if the section rating model is not being used. |  |  |
| ITEM_CALCULATION_CODE | VARCHAR2 | 30 |  |  | This field indicates the data that should be used when calculating the rating points for a specific item. |  |  |
| SHOW_TARGET_PERF_RTG | VARCHAR2 | 30 |  |  | Indicates whether the system will display the target performance rating field at the performance template |  |  |
| SHOW_TARGET_PROF_LEVEL | VARCHAR2 | 30 |  |  | Indicates whether the system will display the target proficiency level field at the performance template |  |  |
| SHOW_SECTION_WEIGHT | VARCHAR2 | 30 |  |  | This indicates whether items in the section can have a weighting relative to other items in the same section. |  |  |
| SHOW_SECTION_MIN_WEIGHT | VARCHAR2 | 30 |  |  | Indicates whether the HR specialist can enter minimum weights at the performance template.  These minima are displayed on the performance document. |  |  |
| SHOW_MANDATORY | VARCHAR2 | 30 |  |  | Indicates whether the user can edit or delete items at the performance document.  This setting would typically be used in conjunction with integration with profile content, so that the user was presented with a suite of standard competencies and objectives within the performance document. |  |  |
| SHOW_CRITICAL | VARCHAR2 | 30 |  |  | This field indicates whether a content item is critical at the performance document. |  |  |
| SHOW_DESCRIPTION | VARCHAR2 | 30 |  |  | Indicates whether the system will display the description of the content item from the content library, at the performance document. |  |  |
| SHOW_MEASUREMENT | VARCHAR2 | 30 |  |  | Indicates whether the system will display a Measurement field at the performance template. |  |  |
| SHOW_DUE_DATE | VARCHAR2 | 30 |  |  | Indicates whether the system will display a due date field at the performance document, one date per item. |  |  |
| SHOW_REMINDER_DATE | VARCHAR2 | 30 |  |  | Indicates whether the system will display a reminder date field at the performance document, one date per item. |  |  |
| SHOW_OWNED_BY | VARCHAR2 | 30 |  |  | Indicates whether the system will display an owner field at the performance document. |  |  |
| SHOW_STATUS | VARCHAR2 | 30 |  |  | Indicates whethre the system will display a status field, at the performance document, for each item. |  |  |
| SHOW_PERCENT_COMPLETE | VARCHAR2 | 30 |  |  | Indicates whether the system will display a percent complete field, at the performance document, for each item |  |  |
| USE_PROFILE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the system will identify the most specific profile related to a worker's job data, then copy all content items for this content type, into the performance document. |  |  |
| PROFILE_TYPE_ID | NUMBER |  | 18 |  | This field stores the ID of a model profile that contains the content type specified. |  |  |
| USE_SPEC_PROFILE_FLAG | VARCHAR2 | 20 |  |  | Indicates whether the system will copy all the content items matching the specified content type, into the performance document. |  |  |
| PROFILE_ID | NUMBER |  | 18 |  | This field is the profile ID of a specific model profile, used for copying content when generating performance documents. |  |  |
| USE_WORKER_GOALS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the system will copy goals from worker's goals into the performance document, when generating the performance document. |  |  |
| UPDATE_GOAL_WEIGHTS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to update weights of the existing goals in PD from Goal Management |  |  |
| USE_SPEC_CONTENT_ITEM_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the system will allow the user to add content items of the content type to the section. |  |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Section Definition (HRA_SECTION_DEFNS_B) |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |  |
| USE_WRITING_ASSISTANT_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the system will use writing assistant flag at the section definition |  |  |
| ROUNDING_RULE_CODE | VARCHAR2 | 30 |  |  | Indicates the rounding rule that will be used for ratings that are calculated by the system. Valid values are Standard, Up and Down. |  |  |
| DECIMAL_PLACES | VARCHAR2 | 30 |  |  | Indicates the number of decimal places for calculated ratings. |  |  |
| MAPPING_METHOD_CODE | VARCHAR2 | 30 |  |  | Method to determine the rating when there is no exact match between the calculated rating and a rating level from the rating model used in the section. Valid values are Nearest, Lowest, and Highest.' |  |  |
| CALC_MAPPING_CODE | VARCHAR2 | 30 |  |  | With mapping method code, this field indicates how the calculated numeric score should be mapped to a rating level in the rating model. Valid values are Numeric Rating and Points Range. |  |  |
| USE_SEC_WEIGHTS_FOR_CALC | VARCHAR2 | 30 |  |  | Indicates section weight to be part of calcuation for the ratings of overall summary section. |  |  |
| ENABLE_CHILD_ITEMS_FLAG | VARCHAR2 | 30 |  |  | It indicates whether Behaviors defined as child items for Competencies in Profile Management are displayed in the Competency section. |  |  |
| INCLUDE_FUTURE_ITEMS_FLAG | VARCHAR2 | 30 |  |  | Indicates about future development goals starting after performance document evaluation period. |  |  |
| EXCLUDE_INACTIVE_ITEMS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to exclude development goals whose status is inactive. |  |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  | Obsolete |
| ENABLE_SECTION_COMMENTS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to allow the user to enter a comment for the section. |  |  |
| ENABLE_ITEM_COMMENTS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether item comments is enabled for the section. |  |  |
| EVALUATION_TYPE_CODE | VARCHAR2 | 30 |  |  | Goal evaluation type is to determine how that goal plan should be evaluated in a performance document. |  |  |
| ENABLE_SYNC_FLAG | VARCHAR2 | 30 |  |  | Indicates if the template section is configured to use synchronized goals |  |  |
| INCLUDE_QSTNR_SCORING_FLAG | VARCHAR2 | 30 |  |  | Store whether to enable scoring for the questionnaire section. |  |  |
| INCLUDE_QSTNR_SCORE_OS_FLAG | VARCHAR2 | 30 |  |  | Store whether to include questionnaire score in overall summary ratings calculation. |  |  |
| SKILL_TYPE_CODE | VARCHAR2 | 500 |  |  | This field specifies the skill types to be included in the performance document as required by a model profile. Valid values are Core, Role and Others. |  |  |
| SKILL_PROGRESS_CODE | VARCHAR2 | 30 |  |  | This field specifies the skill progress to be included in the performance document. Valid values are All, Attained, and Developing. |  |  |
| LOCK_EVAL_WHEN_GOAL_SET_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to allow the performance goal section to be evaluated when the goal setting period is taking place. |  |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_SECTION_DEFNS_B_PK | Unique | Default | SECTION_DEF_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
