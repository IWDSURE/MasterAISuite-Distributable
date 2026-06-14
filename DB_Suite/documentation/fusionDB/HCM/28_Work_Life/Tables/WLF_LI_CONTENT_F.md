# WLF_LI_CONTENT_F

Web playable information about a learning item content object.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflicontentf-8631.html#wlflicontentf-8631](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflicontentf-8631.html#wlflicontentf-8631)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_CONTENT_F_PK | CONTENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTENT_ID | NUMBER |  | 18 | Yes | CONTENT_ID |
| EFFORT_CALCULATION_RULE | VARCHAR2 | 30 |  |  | Actual effort calculation rule |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| CONTENT_NUMBER | VARCHAR2 | 30 |  |  | Content number |
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | CONTENT_ID |
| TRACKING_TYPE | VARCHAR2 | 30 |  | Yes | TRACKING_TYPE |
| UUID | VARCHAR2 | 64 |  |  | UUID |
| LOCATION | VARCHAR2 | 4000 |  |  | Information about location of the content object. |
| THUMBNAIL_ID | NUMBER |  | 18 |  | Thumbnail associated with the content object. |
| ATTRIBUTION_ID | NUMBER |  | 18 |  | The id of the source/originator of the content (e.g. person, learning item, external provider, etc.) |
| ATTRIBUTION_TYPE | VARCHAR2 | 30 |  |  | The persona of the source which has created the content |
| CONTENT_TYPE | VARCHAR2 | 30 |  |  | The type of the content |
| CONTENT_FORMAT | VARCHAR2 | 30 |  |  | Format of the content |
| STATUS | VARCHAR2 | 30 |  |  | Current status of the content object {ACTIVE, DELETED}. |
| SOURCE_ID | NUMBER |  | 18 |  | Content RICH_MEDIA_OBJECT_ID |
| AUTHOR | VARCHAR2 | 512 |  |  | AUTHOR |
| KEYWORDS | VARCHAR2 | 1000 |  |  | KEYWORDS |
| VERSION | VARCHAR2 | 200 |  |  | VERSION |
| PRICE | NUMBER |  | 16 |  | PRICE |
| EFFORT_IN_SECONDS | NUMBER |  |  |  | Effort required in seconds for the associated content |
| CURRENCY | VARCHAR2 | 30 |  |  | CURRENCY |
| IS_COPYRIGHTED | VARCHAR2 | 1 |  |  | IS_COPYRIGHTED |
| IS_AUTO_COMMIT | VARCHAR2 | 1 |  | Yes | IS_AUTO_COMMIT |
| COPYRIGHT_TEXT | VARCHAR2 | 2000 |  |  | COPYRIGHT_TEXT |
| IS_VISIBLE | VARCHAR2 | 1 |  | Yes | IS_VISIBLE |
| STARTING_URL | VARCHAR2 | 2000 |  |  | STARTING_URL |
| MASTERY_SCORE | NUMBER |  |  |  | MASTERY_SCORE |
| SOURCE_PASSING_SCORE | NUMBER |  |  |  | Mastery Score as defined by Metadata |
| SOURCE_MINIMUM_SCORE | NUMBER |  |  |  | The minimum score is the lowest a learner can get on the DL item. |
| SOURCE_MAXIMUM_SCORE | NUMBER |  |  |  | The maximum score is the highest a learner can get on the DL item. |
| COMPLETION_THRESHOLD | NUMBER |  |  |  | This is a SCORM 2004 completion mastery score.  For SCORM 2004, mastery_score is the scaled passing score (objective_mastery_score) |
| LAUNCH_DATA | VARCHAR2 | 4000 |  |  | LAUNCH_DATA |
| LAST_UPDATE_METHOD | VARCHAR2 | 1 |  |  | LAST_UPDATE_METHOD |
| EXTERNAL_IDENTIFIER | VARCHAR2 | 2000 |  |  | EXTERNAL_IDENTIFIER |
| CATALOG | VARCHAR2 | 1000 |  |  | CATALOG |
| CATALOG_NUMBER | VARCHAR2 | 1000 |  |  | CATALOG_NUMBER |
| TIME_LIMIT_ACTION | VARCHAR2 | 120 |  |  | TIME_LIMIT_ACTION |
| PLAYABLE_ITEMS_COUNT | NUMBER |  | 18 |  | PLAYABLE_ITEMS_COUNT |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| INGESTION_NAME | VARCHAR2 | 250 |  |  | INGESTION_NAME |
| INGESTION_STATUS | VARCHAR2 | 30 |  |  | INGESTION_STATUS |
| INGESTION_STATUS_LOG | CLOB |  |  |  | INGESTION_STATUS_LOG |
| COMPLETION_ON_OPEN | VARCHAR2 | 1 |  |  | Indicates whether content should be marked complete upon open. |
| RELATED_CONTENT_ID | NUMBER |  | 18 |  | Stores related content id, ie questionnaire id |
| SELF_CHECKLIST_CONTENT_ID | NUMBER |  | 18 |  | Stores self assessment checklist questionnaire id |
| RELATED_CONTENT_VERSION_NUMBER | NUMBER |  | 18 |  | Related content id version number |
| TIME_LIMIT | NUMBER |  |  |  | Stores time limit to complete content |
| TIME_LIMIT_UOM | VARCHAR2 | 30 |  |  | Time limit unit of measure |
| MAX_ATTEMPTS | NUMBER |  | 18 |  | Max attempts to retry content ie assessments |
| HIDE_SCORE_LEARNER | VARCHAR2 | 1 |  |  | Hide passing score for learners |
| HIDE_SCORE_ADMIN | VARCHAR2 | 1 |  |  | Hide passing score for admins |
| DISABLE_REVIEW | VARCHAR2 | 1 |  |  | Disable view again of completed content. Y to disable. |
| HIDE_CORRECT_ANSWERS | VARCHAR2 | 1 |  |  | Hide correct answers in feedback for successfully completed assessments |
| RECORDED_ATTEMPT_REVIEW | VARCHAR2 | 120 |  |  | Recorded Attempt Review |
| RECORDED_ATTEMPTS | VARCHAR2 | 120 |  |  | Recorded Attempts |
| ENABLE_SELF_ASSESS_CHECKLIST | VARCHAR2 | 1 |  |  | Value to represent if learner self asses checklist to be taken before observer checklist |
| OBSRVR_USE_CHKLIST_SCORING | VARCHAR2 | 1 |  |  | Value represents to use check-list scoring instead of manual pass / fail |
| OBSRVR_HIDE_SCORE_LEARNER | VARCHAR2 | 1 |  |  | Hide observer given score of passing for learners |
| OBSRVR_HIDE_SCORE_ADMIN | VARCHAR2 | 1 |  |  | Hide observer given score of passing for Admin |
| OBSRVR_HIDE_CORRECT_ANSWERS | VARCHAR2 | 1 |  |  | Observer Hide correct answers in feedback for successfully completed assessments |
| OBSRVR_RECORDED_ATTEMPTS | VARCHAR2 | 120 |  |  | Observer recorded attempts type. |
| OBSRVR_RECORDED_ATTEMPT_REVIEW | VARCHAR2 | 120 |  |  | Represents observer setting for recorded attempt review |
| OBSRVR_MAX_ATTEMPTS | NUMBER |  | 18 |  | Observer max attempts to retry checklist. |
| OBSRVR_DISABLE_REVIEW | VARCHAR2 | 1 |  |  | Observer setting to disable view again of completed content. Y to disable. |
| OBSERVER_TYPE | VARCHAR2 | 30 |  |  | Stores lookup code representing type of observer |
| ROUTING_TYPE | VARCHAR2 | 30 |  |  | Stores lookup-code to represent the actual type of observer chosen. ie., type of Representative or Manager Hierarchy |
| HIERARCHY_LEVELS | VARCHAR2 | 30 |  |  | Stores hierarchy levels for the routing type selected. |
| DISABLE_REASSIGN_CHECKLIST | VARCHAR2 | 1 |  |  | Column to maintain flag to allow  reassign checklist to others. Value Y  when un-checked. |
| ALLOW_REASSIGN_CHECKLIST | VARCHAR2 | 1 |  |  | Allow reassign checklist |
| ALLOW_BROWSE_CONTENT | VARCHAR2 | 30 |  |  | This column represents "Learners to browse content after completing activity" is allowed or not. |
| STORAGE_PROVIDER_ID | NUMBER |  | 18 |  | Storage Provider account ID of content |
| DELIVERY_PROVIDER_ID | NUMBER |  | 18 |  | Delivery Provider account ID of content |
| IS_EMBEDDABLE | VARCHAR2 | 30 |  |  | Indicates if this content can be embeddable in a iframe or not |
| SCORED_CONTENT_COMPLETION | VARCHAR2 | 30 |  |  | Strategy to determine lesson completion status of a scored content |
| LRNR_ATTEMPT_REVIEW_CONDITION | VARCHAR2 | 32 |  |  | Indicates when attempts can be reviewed |
| ALLOW_FWD_SCRUB | VARCHAR2 | 32 |  |  | Allow forward scrub |
| COMPLETION_PERCENTAGE | NUMBER |  | 10 |  | Percentage of video that a learner must watch to get credit for completion |
| SHOW_FEEDBACK_TO_LEARNER | VARCHAR2 | 1 |  |  | Should learner be able to view questionnaire feedback ? |
| TIME_LIMIT_IN_SECONDS | NUMBER |  |  |  | If the content is timed, what is the limit |
| DISPLAY_MODE | VARCHAR2 | 32 |  |  | Display mode |
| ENABLE_SCORING | VARCHAR2 | 1 |  |  | Should this content be scored ? |
| COMPLETION_RULE | VARCHAR2 | 32 |  |  | Completion rule |
| SCORE_VIEW_RULE | VARCHAR2 | 32 |  |  | Score View Rule |
| SHOW_ACTUAL_SCORE_TO_LEARNER | VARCHAR2 | 1 |  |  | Should the learner see the score ? |
| SHOW_ACTUAL_SCORE_TO_ADMIN | VARCHAR2 | 1 |  |  | Should the admin see the score ? |
| COMPLETION_AFFIRMATION | VARCHAR2 | 32 |  |  | Indicate how completions are affirmed |
| OBSRVR_ATMPT_REVIEW_COND_LRNR | VARCHAR2 | 32 |  |  | Indicates condition when observer attempts can be reviewed by learner. |
| OBSRVR_SHOW_FEEDBACK_TO_LRNR | VARCHAR2 | 1 |  |  | Flag that represents if learner can view observer feedback |
| OBSRVR_ALLOW_BROWSE_CONDITION | VARCHAR2 | 32 |  |  | This column represents "Observers to browse content after completing activity" is allowed or not. |
| RETRY_DELAY_IN_SECONDS | NUMBER |  |  |  | The number of seconds delay before which the content can be retried by the learner |
| RETRY_ATTEMPTS_BEFORE_DELAY | NUMBER |  | 18 |  | Number of attempt retried before delay |
| AUTO_LAUNCH_ON_PAGE_OPEN | VARCHAR2 | 1 |  |  | Indicates if the content needs to be auto launched when the enrollment page opens. |
| ENABLE_COMPL_BEFORE_EXITAU | VARCHAR2 | 30 |  |  | Enable completion before Finish Signal |
| MOVE_ON | VARCHAR2 | 80 |  |  | Describes the Move on criteria for a CMI5 AU |
| ENTITLEMENT_KEY | VARCHAR2 | 4000 |  |  | Describes the EntitlementKey value defined for an AU in a CMI5 content |
| LAUNCH_METHOD | VARCHAR2 | 80 |  |  | Describes the launch method defined for an AU in a CMI5 content |
| ACTIVITY_TYPE | VARCHAR2 | 4000 |  |  | Describes the ActivityType value defines for an AU in a CMI5 content |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_CONTENT_F_N1 | Non Unique | Default | EXTERNAL_IDENTIFIER |
| WLF_LI_CONTENT_F_N2 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_LI_CONTENT_F_N3 | Non Unique | WLF_LI_CONTENT_F_N3 | CONTENT_FORMAT |
| WLF_LI_CONTENT_F_N4 | Non Unique | WLF_LI_CONTENT_F_N4 | CONTENT_TYPE |
| WLF_LI_CONTENT_F_N5 | Non Unique | WLF_LI_CONTENT_F_N5 | STATUS |
| WLF_LI_CONTENT_F_N6 | Non Unique | WLF_LI_CONTENT_F_N6 | SOURCE_ID |
| WLF_LI_CONTENT_F_N7 | Non Unique | WLF_LI_CONTENT_F_N7 | UPPER("CONTENT_NUMBER") |
| WLF_LI_CONTENT_F_U1 | Unique | Default | CONTENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
