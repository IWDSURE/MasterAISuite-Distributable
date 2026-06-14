# HWR_SRVY_SUMMARY

This table will be used to store main information of the survey.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvysummary-22314.html#hwrsrvysummary-22314](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvysummary-22314.html#hwrsrvysummary-22314)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_SUMMARY_PK | SURVEY_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SURVEY_ID | NUMBER |  | 18 | Yes | This is the Survey Id identifying the Survey entry in this table. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | This is the Questionnaire ID associated with the Survey. |
| QUESTIONNAIRE_VERSION | NUMBER |  | 18 | Yes | This is the Questionnaire Version associated with the Questionnaire ID of this Survey. |
| QUESTIONS | VARCHAR2 | 2000 |  | Yes | This is a comma separated list of Questions associated with the Survey. |
| OWNER_ID | VARCHAR2 | 500 |  | Yes | This is the FUSION id of the owner of the Survey. |
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | This is the Subscriber ID associated with the Survey. Used to differentiate between different survey projects. |
| SUBSCRIBER_CODE | VARCHAR2 | 30 |  | Yes | This is the Subscriber Code associated with the Survey. Used to differentiate between different survey projects. |
| PARTICPANT_COUNT | NUMBER |  | 18 | Yes | Number of participants in the survey being idetntified in this record. |
| PARTICPANT_COMPLETION_COUNT | NUMBER |  | 18 | Yes | Number of participants who have completed this survey. |
| START_DATE | TIMESTAMP |  |  |  | Survey Start Date. In the first run, we are defaulting it to the creation time. |
| EXPIIRATION_DATE | TIMESTAMP |  |  |  | Survey Expiration Date. In the first run, we are defaulting it to the start date+ 3 weeks. |
| ADVANCE_FLAG | NUMBER |  | 18 |  | ADVANCE FLAG for this survey. Not used in the first run. |
| ANALYZED | NUMBER |  | 18 | Yes | This value identifies whether this survey was analyzed or not. |
| MEETING_ID | VARCHAR2 | 500 |  |  | Meeting ID associated with the survey, if this survey is part of meeting project. |
| IS_DELETED | NUMBER |  | 18 | Yes | This indicates if the survey is disabled or not. 0 --> not disabled;   1 --> disabled.   A survey is disabled if its been deleted. |
| SURVEY_BASE_ATTR_1 | VARCHAR2 | 100 |  |  | SURVEY_BASE_ATTR_1. This is the extra attribute in case if needed. |
| SURVEY_BASE_ATTR_2 | VARCHAR2 | 100 |  |  | SURVEY_BASE_ATTR_2.  This is the extra attribute in case if needed. |
| SURVEY_BASE_ATTR_3 | VARCHAR2 | 100 |  |  | SURVEY_BASE_ATTR_3. This is the extra attribute in case if needed. |
| SURVEY_BASE_ATTR_4 | VARCHAR2 | 100 |  |  | SURVEY_BASE_ATTR_4. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SRVY_SUMMARY_N1 | Non Unique | Default | OWNER_ID |
| HWR_SRVY_SUMMARY_N2 | Non Unique | Default | SUBSCRIBER_ID |
| HWR_SRVY_SUMMARY_N3 | Non Unique | Default | ANALYZED |
| HWR_SRVY_SUMMARY_U1 | Unique | Default | SURVEY_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
