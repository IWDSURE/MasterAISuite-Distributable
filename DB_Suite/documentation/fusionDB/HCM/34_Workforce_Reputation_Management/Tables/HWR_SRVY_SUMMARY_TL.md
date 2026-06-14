# HWR_SRVY_SUMMARY_TL

This is translation table for HWR_SRVY_SUMMARY

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvysummarytl-29447.html#hwrsrvysummarytl-29447](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvysummarytl-29447.html#hwrsrvysummarytl-29447)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_SUMMARY_TL_PK | SURVEY_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SURVEY_ID | NUMBER |  | 18 | Yes | This is the Survey Id identifying the Survey entry in this table. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | This is the Questionnaire ID associated with the Survey. |
| QUESTIONNAIRE_VERSION | NUMBER |  | 18 | Yes | This is the Questionnaire version associated with the Questionnaire ID |
| SURVEY_NAME | VARCHAR2 | 500 |  |  | This is the SURVEY_NAME associated with the Survey which is translatable |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SRVY_SUMMARY_TL_U1 | Unique | Default | SURVEY_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, LANGUAGE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
