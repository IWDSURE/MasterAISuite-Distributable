# BEN_QSTNR_RESPONSES

BEN_QSTNR_RESPONSES contains responses submitted for the benefits questionnaires.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benqstnrresponses-20545.html#benqstnrresponses-20545](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benqstnrresponses-20545.html#benqstnrresponses-20545)

## Primary Key

| Name | Columns |
|------|----------|
| ben_qstnr_responses_PK | QSTNR_RESPONSE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTNR_RESPONSE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BENEFIT_QSTNR_ID | NUMBER |  | 18 | Yes | This column holds Foreign Key to BEN_BENEFIT_QSTNR. |
| PERSON_ID | NUMBER |  | 18 | Yes | This column holds Foreign Key to PER_ALL_PEOPLE_F. |
| SUBJECT_PERSON_ID | NUMBER |  | 18 | Yes | This column holds Foreign Key to PER_ALL_PEOPLE_F. |
| CONTEXTUAL_ACTION | VARCHAR2 | 240 |  | Yes | This column holds the contextual action of the survey. |
| CONTEXT | VARCHAR2 | 240 |  | Yes | This column holds the context of the survey. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | This column holds the foreign key to HRQ_QUESTIONNAIRES_B. |
| QSTNR_PARTICIPANT_ID | NUMBER |  | 18 | Yes | This column holds the foreign key to HRQ_QUESTIONNAIRES_B. |
| SUBMIT_DATE | DATE |  |  | Yes | This column holds the date when survey response is submitted. |
| OBJ_TYPE | VARCHAR2 | 240 |  |  | This columns holds the foreign key object name. |
| OBJ_ID | NUMBER |  | 18 |  | This columns holds the foreign key value. |
| OBJ_CODE | VARCHAR2 | 240 |  |  | This columns holds the foreign key code value. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_6 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_7 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_8 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_9 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_10 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use. |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template ID field for future use. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_QSTNR_RESPONSES_N1 | Non Unique | FUSION_TS_TX_DATA | PERSON_ID, BENEFIT_QSTNR_ID, SUBJECT_PERSON_ID, QUESTIONNAIRE_ID, CONTEXTUAL_ACTION |
| BEN_QSTNR_RESPONSES_N2 | Non Unique | FUSION_TS_TX_DATA | QSTNR_PARTICIPANT_ID |
| BEN_QSTNR_RESPONSES_PK | Unique | FUSION_TS_TX_DATA | QSTNR_RESPONSE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
