# HRE_TOUCHPT_EMPL_SVY_SCORES

Touchpoints table storing the surveys of type Touchpoints, Touchpoint surveys are filtered from per_chk_survey_responses and stored here.

## Details

**Schema:** FUSION

**Object owner:** HRE

**Object type:** TABLE

**Tablespace:** hre_touchpt_empl_svy_scores

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hretouchptemplsvyscores-17117.html#hretouchptemplsvyscores-17117](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hretouchptemplsvyscores-17117.html#hretouchptemplsvyscores-17117)

## Primary Key

| Name | Columns |
|------|----------|
| HRE_TOUCHPT_EMPL_SVY_SCORE_PK | SURVEY_RESPONSE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SURVEY_RESPONSE_ID | NUMBER |  | 18 | Yes | Primary Key. The survey response id sourced from per_chk_survey_responses. |
| CHECKLIST_ID | NUMBER |  | 18 | Yes | The survey id sourced from per_chk_survey_responses. |
| PERSON_ID | NUMBER |  | 18 | Yes | The person id of the employee. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | The assignment id of the employee |
| SCORE | NUMBER |  | 18 |  | The response score of the survey |
| PERIOD_END_DATE | DATE |  |  |  | The survey period end date. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRE_TOUCHPT_EMPL_SVY_SCORES_N1 | Non Unique | HRE_TOUCHPT_EMPL_SVY_SCORES_N1 | "CHECKLIST_ID", "PERSON_ID", "ASSIGNMENT_ID", "PERIOD_END_DATE" |
| HRE_TOUCHPT_EMPL_SVY_SCORE_PK | Unique | HRE_TOUCHPT_EMPL_SVY_SCORE_PK | SURVEY_RESPONSE_ID |

---

[← Back to Index](../27_Touchpoints_Tables_Index.md)
