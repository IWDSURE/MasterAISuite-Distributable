# HWR_SRVY_DETAIL

This table will be used to store information related to survey in terms of its participants.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvydetail-26010.html#hwrsrvydetail-26010](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvydetail-26010.html#hwrsrvydetail-26010)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_DETAIL_PK | SURVEY_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, PARTICIPANT_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SURVEY_ID | NUMBER |  | 18 | Yes | This is the Survey Id identifying the Survey entry in this table. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | This is the Questionnaire ID associated with the Survey. |
| QUESTIONNAIRE_VERSION | NUMBER |  | 18 | Yes | This is the Questionnaire Version associated with the Questionnaire ID of this Survey. |
| PARTICIPANT_PROFILE_ID | VARCHAR2 | 500 |  | Yes | This is the Fusion Id of the participant of the Survey. |
| IS_COMPLETED | NUMBER |  | 18 | Yes | This determines if the participant completed the survey or not |
| RESPONSE_ANONYMOUS | NUMBER |  | 18 | Yes | This determines if the participant responses are anonymous or not |
| IS_VIEWED | NUMBER |  | 18 | Yes | This determines if the participant opened the survey or not |
| SURVEY_DETAIL_ATTR_1 | VARCHAR2 | 100 |  |  | SURVEY_DETAIL_ATTR_1. This is the extra attribute in case if needed. |
| SURVEY_DETAIL_ATTR_2 | VARCHAR2 | 100 |  |  | SURVEY_DETAIL_ATTR_2. This is the extra attribute in case if needed. |
| SURVEY_DETAIL_ATTR_3 | VARCHAR2 | 100 |  |  | SURVEY_DETAIL_ATTR_3. This is the extra attribute in case if needed. |
| SURVEY_DETAIL_ATTR_4 | VARCHAR2 | 100 |  |  | SURVEY_DETAIL_ATTR_4. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SRVY_DETAIL_N1 | Non Unique | Default | PARTICIPANT_PROFILE_ID |
| HWR_SRVY_DETAIL_U1 | Unique | Default | SURVEY_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, PARTICIPANT_PROFILE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
