# HRE_TOUCHPT_SURVEY_SCORES

It will store the computed team touchpoints survey scores for specified frequency.

## Details

**Schema:** FUSION

**Object owner:** HRE

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hretouchptsurveyscores-31226.html#hretouchptsurveyscores-31226](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hretouchptsurveyscores-31226.html#hretouchptsurveyscores-31226)

## Primary Key

| Name | Columns |
|------|----------|
| hre_touchpt_survey_scores_PK | TOUCHPT_SURVEY_SCORE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TOUCHPT_SURVEY_SCORE_ID | NUMBER |  | 18 | Yes | System generated primary key for this table. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ALL_PEOPLE_F |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_ASSIGNMENTS_M |
| FREQUENCY | VARCHAR2 | 32 |  |  | Period used to calculate aggregation. |
| SURVEY_ID | NUMBER |  | 18 |  | Foreign key to Survey Setup table |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Foreign key to Questionnaire table |
| TEAM_AVG_SCORE | NUMBER |  | 18 |  | Average survey score per team on the survey date. |
| ORG_AVG_SCORE | NUMBER |  | 18 |  | Average survey score per organization on survey date. |
| COMPANY_AVG_SCORE | NUMBER |  | 18 |  | Averrage survey score for all teams on survey date |
| SURVEY_PERIOD_END_DATE | DATE |  |  |  | Date on which survey scores are computed. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRE_TOUCHPT_SURVEY_SCORES_N3 | Non Unique | HRE_TOUCHPT_SURVEY_SCORES_N3 | ASSIGNMENT_ID |
| HRE_TOUCHPT_SURVEY_SCORES_N4 | Non Unique | HRE_TOUCHPT_SURVEY_SCORES_N4 | FREQUENCY |
| HRE_TOUCHPT_SURVEY_SCORES_N5 | Non Unique | HRE_TOUCHPT_SURVEY_SCORES_N5 | SURVEY_PERIOD_END_DATE |
| HRE_TOUCHPT_SURVEY_SCORES_N6 | Non Unique | HRE_TOUCHPT_SURVEY_SCORES_N6 | PERSON_ID, ASSIGNMENT_ID, SURVEY_ID, SURVEY_PERIOD_END_DATE |
| HRE_TOUCHPT_SURVEY_SCORES_N7 | Non Unique | HRE_TOUCHPT_SURVEY_SCORES_N7 | BUSINESS_GROUP_ID |
| HRE_TOUCHPT_SURVEY_SCORES_N8 | Non Unique | HRE_TOUCHPT_SURVEY_SCORES_N8 | SURVEY_ID |
| hre_touchpt_survey_scores_PK | Unique | Default | TOUCHPT_SURVEY_SCORE_ID |

---

[← Back to Index](../27_Touchpoints_Tables_Index.md)
