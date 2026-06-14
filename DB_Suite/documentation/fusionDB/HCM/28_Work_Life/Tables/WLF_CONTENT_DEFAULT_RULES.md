# WLF_CONTENT_DEFAULT_RULES

Table to store learning content default rules.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** wlf_content_default_rules

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcontentdefaultrules-19186.html#wlfcontentdefaultrules-19186](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcontentdefaultrules-19186.html#wlfcontentdefaultrules-19186)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CONTENT_DEFAULT_RULES_PK | CONTENT_RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTENT_RULE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EFFORT_CALCULATION_RULE | VARCHAR2 | 30 |  |  | Actual effort calculation rule |
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | Referece to a learning item. eg: Learning Catalog Profile. |
| CONTENT_TYPE | VARCHAR2 | 30 |  |  | The type of the content |
| RECORDED_ATTEMPTS | VARCHAR2 | 120 |  |  | Recorded Attempts |
| MAX_ATTEMPTS | NUMBER |  | 18 |  | Max attempts to retry content ie assessments |
| RECORDED_ATTEMPT_REVIEW | VARCHAR2 | 120 |  |  | Represents setting for recorded attempt review Attempt Review |
| LRNR_ATTEMPT_REVIEW_CONDITION | VARCHAR2 | 32 |  |  | Indicates when attempts can be reviewed |
| DISABLE_ATTEMPTS_OVERRIDE | VARCHAR2 | 1 |  |  | This column represents if attemps can be overriden |
| COMPLETION_RULE | VARCHAR2 | 32 |  |  | This represents Completion rule |
| ALLOW_BROWSE_CONDITION | VARCHAR2 | 32 |  |  | This column represents "Learner to browse content after completing activity" is allowed or not. |
| SCORED_CONTENT_COMPLETION | VARCHAR2 | 30 |  |  | Strategy to determine lesson completion status of a scored content |
| SCORE_VIEW_RULE | VARCHAR2 | 32 |  |  | This column represents Score View Rule |
| DISABLE_COMPLETION_OVERRIDE | VARCHAR2 | 1 |  |  | This column represents if completion rule can be overriden |
| ALLOW_FWD_SCRUB | VARCHAR2 | 32 |  |  | Tihs column represents Allow forward scrub |
| COMPLETION_THRESHOLD | NUMBER |  | 10 |  | Percentage of video that a learner must watch to get credit for completion |
| SHOW_FEEDBACK_TO_LEARNER | VARCHAR2 | 1 |  |  | Should learner be able to view questionnaire feedback ? |
| OBSRVR_RECORDED_ATTEMPTS | VARCHAR2 | 120 |  |  | Observer recorded attempts type. |
| OBSRVR_MAX_ATTEMPTS | NUMBER |  | 18 |  | Observer max attempts to retry checklist. |
| OBSRVR_RECORDED_ATTEMPT_REVIEW | VARCHAR2 | 120 |  |  | Represents observer setting for recorded attempt review |
| OBSRVR_ATMPT_REVIEW_COND_LRNR | VARCHAR2 | 32 |  |  | Indicates condition when observer attempts can be reviewed by learner. |
| DISABLE_ATTEMPTS_OVERRIDE_OBSR | VARCHAR2 | 1 |  |  | This column represents if observer attemps can be overriden |
| OBSRVR_ALLOW_BROWSE_CONDITION | VARCHAR2 | 32 |  |  | This column represents "Observers to browse content after completing activity" is allowed or not. |
| OBSERVER_TYPE | VARCHAR2 | 30 |  |  | Stores lookup code representing type of observer |
| ROUTING_TYPE | VARCHAR2 | 30 |  |  | Stores lookup-code to represent the actual type of observer chosen. ie., type of Representative or Manager Hierarchy |
| HIERARCHY_LEVELS | VARCHAR2 | 30 |  |  | Stores hierarchy levels for the routing type selected. |
| ALLOW_REASSIGN_CHECKLIST | VARCHAR2 | 1 |  |  | Allow reassign checklist |
| OBSRVR_SHOW_FEEDBACK_TO_LRNR | VARCHAR2 | 1 |  |  | Flag that represents if learner can view observer feedback |
| DISABLE_COMPL_OVERRIDE_OBSR | VARCHAR2 | 1 |  |  | This column represents if completion rule can be overriden |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_CONTENT_DEFAULT_RULES_N1 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_CONTENT_DEFAULT_RULES_N2 | Non Unique | Default | CONTENT_TYPE |
| WLF_CONTENT_DEFAULT_RULES_U1 | Unique | Default | CONTENT_RULE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
