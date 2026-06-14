# HWR_SRVY_ELIG_PROFILE

This table is for eligibility profile for organization survey

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvyeligprofile-8783.html#hwrsrvyeligprofile-8783](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvyeligprofile-8783.html#hwrsrvyeligprofile-8783)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_ELIG_PROFILE_PK | SURVEY_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, ELIG_PRFL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SURVEY_ID | NUMBER |  | 18 | Yes | This is the Survey Id identifying the Survey entry in this table. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | This is the Questionnaire ID associated with the Survey. |
| QUESTIONNAIRE_VERSION | NUMBER |  | 18 | Yes | This is the Questionnaire Version associated with the Questionnaire ID of this Survey. |
| ELIG_PRFL_ID | NUMBER |  | 18 | Yes | This is the Eligibility Profile ID which the survey is sent to. |
| ELIG_OBJ_ID | NUMBER |  | 18 | Yes | This is the Eligibility Object ID for which profiles are attached. This is generated from eligibility objects table. |
| ELIG_ESS_JOB_REQUEST_ID | NUMBER |  | 18 | Yes | This is the Eligibility ESS job Request ID for which the eligibility object profiles need to be evaluated. |
| IS_PRFL_RESULT_AVAILABLE | NUMBER |  | 18 | Yes | This determines if the Eligibility ESS evaluation job is completed and Eligibility profiles result is available. |
| SURVEY_ELIG_ATTR_1 | VARCHAR2 | 100 |  |  | SURVEY_ELIG_ATTR_1. This is the extra attribute in case if needed. |
| SURVEY_ELIG_ATTR_2 | VARCHAR2 | 100 |  |  | SURVEY_ELIG_ATTR_2. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SRVY_ELIG_PROFILE_U1 | Unique | Default | SURVEY_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, ELIG_PRFL_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
