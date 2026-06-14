# PER_CHK_SURVEY_RESP_SUMMARY

Table to store survey responses summary

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchksurveyrespsummary-27723.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchksurveyrespsummary-27723.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_SURVEY_RESP_SUMMARY_PK | SURVEY_RESPONSES_SUMMARY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SURVEY_RESPONSES_SUMMARY_ID | NUMBER |  | 18 | Yes | SURVEY_RESPONSES_SUMMARY_ID |
| CHECKLIST_BATCH_ACTION_ID | NUMBER |  | 18 | Yes | CHECKLIST_BATCH_ACTION_ID |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | QUESTIONNAIRE_ID |
| QUESTIONNAIRE_VERSION_NUM | NUMBER |  | 18 |  | QUESTIONNAIRE_VERSION_NUM |
| TOTAL_ASSIGNEES | NUMBER |  | 9 |  | TOTAL_ASSIGNEES |
| TOTAL_RESPONDENTS | NUMBER |  | 9 |  | TOTAL_RESPONDENTS |
| LAST_COMPUTATION_DATE | TIMESTAMP |  |  |  | LAST_COMPUTATION_DATE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHK_SURVEY_RESP_SUMMARY_PK | Unique | Default | SURVEY_RESPONSES_SUMMARY_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
