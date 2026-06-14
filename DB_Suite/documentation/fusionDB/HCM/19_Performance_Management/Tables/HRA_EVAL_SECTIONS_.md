# HRA_EVAL_SECTIONS_

This table stores the evaluation sections

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevalsections-18249.html#hraevalsections-18249](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevalsections-18249.html#hraevalsections-18249)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_EVAL_SECTIONS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, EVAL_SECTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVAL_SECTION_ID | NUMBER |  | 18 | Yes | Primary key to Sections |
| ENABLE_SECTION_COMMENTS_FLAG | VARCHAR2 | 30 |  |  | ENABLE_SECTION_COMMENTS_FLAG |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| TMPL_SECTION_ID | NUMBER |  | 18 |  | Foreign key to HRA_TMPL_SECTIONS |
| CONTENT_TYPE_ID | NUMBER |  | 18 |  | Foreign key to HRT_CONTENT_ITEMS_B |
| EVALUATION_ID | NUMBER |  | 18 |  | Foreign key to HRA_EVALUATIONS |
| SEQUENCE_NUMBER | NUMBER |  | 18 |  | Indicates the sequence of the section to be displayed in the performance document |
| SECTION_TYPE_CODE | VARCHAR2 | 30 |  |  | Indicates the type of the section |
| RATE_SECTION_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to allow the user to enter a rating for the section, or for the system to calculate a rating for the section. |
| CALCULATION_RULE_CODE | VARCHAR2 | 30 |  |  | The calculation method for the section.  This value comes from the section configuration at the performance template. |
| FAST_FORMULA_ID | NUMBER |  | 18 |  | Indicates the fast formula that the system should use when the section is to be rated by means of calculation using a fast formula. |
| SECTION_RATING_MODEL_ID | NUMBER |  | 18 |  | The rating model for the section.  (Note this may or may not be the same as the rating model for individual items.) |
| WEIGHT_SECTION_FLAG | VARCHAR2 | 30 |  |  | Indicates if the section can be weighted or not |
| SECTION_WEIGHT | NUMBER |  |  |  | The weight of this section, in relation to other sections in the performance document.  This value comes from the section configuration at the performance template and may be editable, depending on configuration |
| SECTION_MIN_WEIGHT | NUMBER |  |  |  | The minimum weight for this section.  This value comes from the section configuration at the performance template |
| ENABLE_ITEMS | VARCHAR2 | 30 |  |  | Indicates that the section will contain items such as specific competencies or goals. |
| FREE_FORM_ALLOWED_FLAG | VARCHAR2 | 30 |  |  | Indicates if the system will allow the user to add free-from items. |
| RATE_ITEM_FLAG | VARCHAR2 | 30 |  |  | Indicates if the user can rate each item within the section. |
| RATING_TYPE_CODE | VARCHAR2 | 30 |  |  | This field allows the user to choose the rating type they would like to apply to items in this section. |
| USE_SECRTG_FOR_PERFRTG_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the system will use the rating model specified for section, for all items within this section. |
| PERF_RATING_MODEL_ID | NUMBER |  | 18 |  | This is the rating model for performance ratings, if the section rating model is not being used. |
| ITEM_CALCULATION_CODE | VARCHAR2 | 30 |  |  | Indicates the calculation code for the items within the section |
| SHOW_TARGET_PERF_RTG | VARCHAR2 | 30 |  |  | Indicates whether the system will display the target performance rating field in the performance document |
| SHOW_TARGET_PROF_LEVEL | VARCHAR2 | 30 |  |  | Indicates whether the system will display the target proficiency level  field in the performance document |
| ADD_ITEMS_CONFIRM_CRIT_FLAG | VARCHAR2 | 30 |  |  | Indicates if the system will allow users to add items to the section. |
| SECTION_WEIGHT_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the section should be weighted |
| SECTION_MIN_WEIGHT_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the section should have any minimum weight. This applies only when section can be weighted. |
| SHOW_MANDATORY | VARCHAR2 | 30 |  |  | Indicates if the user can edit or delete items at the performance document.  This setting would typically be used in conjunction with integration with profile content. |
| SHOW_CRITICAL | VARCHAR2 | 30 |  |  | Allows the user to indicate if a content item is critical, at the performance document. |
| SHOW_DESCRIPTION | VARCHAR2 | 30 |  |  | Indicates if the system will display the description of the content item from the content library, at the performance document. |
| SHOW_MEASUREMENT | VARCHAR2 | 30 |  |  | Indicates if the system will display a Measurement field at the performance template. This setting is used with free-form items to describe the standard against which performance is measured. |
| SHOW_DUE_DATE | VARCHAR2 | 30 |  |  | Indicates if the system will display a due date field at the performance document, one date per item. |
| SHOW_REMINDER_DATE | VARCHAR2 | 30 |  |  | Indicates if the system will display a reminder date field at the performance document, one date per item. |
| SHOW_OWNED_BY | VARCHAR2 | 30 |  |  | Indicates if the system will display an owner field at the performance document. |
| SHOW_STATUS | VARCHAR2 | 30 |  |  | Indicates if the system will display a status field, at the performance document, for each item. |
| SHOW_PERCENT_COMPLETE | VARCHAR2 | 30 |  |  | Indicates if the system will display a percent complete field, at the performance document, for each item. |
| PROFILE_TYPE_ID | NUMBER |  | 18 |  | Indicates the type of profile to be used for this section. Foreign key to HRT_PROFILE_TYPES_B |
| PROFILE_ID | NUMBER |  | 18 |  | This field is the profile ID of a specific model profile, used for copying content when generating performance documents. |
| RATING_OVERIDE_FLAG | VARCHAR2 | 30 |  |  | This indicates if the rating has been overridden by the user |
| USE_PROFILE_FLAG | VARCHAR2 | 30 |  |  | Indicates if we have to use profile for populating section items |
| USE_SPEC_PROFILE_FLAG | VARCHAR2 | 30 |  |  | Indicates if we can use specific profile for populating section items |
| USE_SPEC_CONTENT_ITEM_FLAG | VARCHAR2 | 30 |  |  | Indicates if we can specific content items |
| USE_WORKER_GOALS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the section should use worker goals from Goal Management. This applies to only Goal type sections. |
| UPDATE_GOAL_WEIGHTS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to update weights of the existing goals in PD from Goal Management |
| COMMENTS | VARCHAR2 | 4000 |  |  | These are the comments entered for this section. Typically this column is used for manager feedback and worker feedback sections. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| USE_WRITING_ASSISTANT_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the system will use writing assistant flag at the performance template |
| COMMENT_TEXT | CLOB |  |  |  | These are the comments entered for this section. Typically this column is used for manager feedback and worker feedback sections. |
| ROUNDING_RULE_CODE | VARCHAR2 | 30 |  |  | Indicates the rounding rule that will be used for ratings that are calculated by the system. Valid values are Standard, Up and Down. |
| DECIMAL_PLACES | VARCHAR2 | 30 |  |  | Indicates the number of decimal places for calculated ratings. |
| MAPPING_METHOD_CODE | VARCHAR2 | 30 |  |  | Method to determine the rating when there is no exact match between the calculated rating and a rating level from the rating model used in the section. Valid values are Nearest, Lowest, and Highest. |
| CALC_MAPPING_CODE | VARCHAR2 | 30 |  |  | With mapping method code, this field indicates how the calculated numeric score should be mapped to a rating level in the rating model. Valid values are Numeric Rating and Points Range. |
| USE_SEC_WEIGHTS_FOR_CALC | VARCHAR2 | 30 |  |  | Indicates section weight to be part of calcuation for the ratings of overall summary section. |
| ENABLE_CHILD_ITEMS_FLAG | VARCHAR2 | 30 |  |  | It indicates whether Behaviors defined as child items for Competencies in Profile Management are displayed in the Competency section. |
| INCLUDE_FUTURE_ITEMS_FLAG | VARCHAR2 | 30 |  |  | Indicates about future development goals starting after performance document evaluation period |
| EXCLUDE_INACTIVE_ITEMS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to exclude development goals whose status is inactive. |
| REFERENCE_SECTION_ID | NUMBER |  |  |  | Indicates the reference to the current section in Profile Management. |
| ENABLE_ITEM_COMMENTS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether item comments is enabled for the section. |
| EVALUATION_TYPE_CODE | VARCHAR2 | 30 |  |  | Goal evaluation type is used to determine how that goal plan should be evaluated in a performance document. |
| GOAL_PLAN_ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign Key to the HRG_GOAL_PLN_ASSIGNMENTS |
| INCLUDE_QSTNR_SCORING_FLAG | VARCHAR2 | 30 |  |  | Store whether to enable scoring for the questionnaire section. |
| INCLUDE_QSTNR_SCORE_OS_FLAG | VARCHAR2 | 30 |  |  | Store whether to include questionnaire score in overall summary ratings calculation. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_EVAL_SECTIONSN1_ | Non Unique | Default | EVAL_SECTION_ID, LAST_UPDATE_DATE |
| HRA_EVAL_SECTIONS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, EVAL_SECTION_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
