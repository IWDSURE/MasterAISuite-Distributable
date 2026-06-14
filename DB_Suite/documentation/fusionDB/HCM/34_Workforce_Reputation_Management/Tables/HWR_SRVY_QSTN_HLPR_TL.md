# HWR_SRVY_QSTN_HLPR_TL

This table will be used to store information associated with the multiple
choice questions being used in the Survey, both single selection and multiple selection - TL version of HWR_SRVY_QSTN_HLPR_B.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvyqstnhlprtl-23518.html#hwrsrvyqstnhlprtl-23518](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvyqstnhlprtl-23518.html#hwrsrvyqstnhlprtl-23518)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_QSTN_HLPR_TL_PK | SUBSCRIBER_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, QUESTION_ID, QUESTION_VERSION, ANSWER_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | SUBSCRIBER_ID associated with the Survey |  |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | This is the Questionnaire ID of the questionnaire being identified. |  |
| QUESTIONNAIRE_VERSION | NUMBER |  | 18 | Yes | This is the Questionnaire Version associated with the Questionnaire ID. |  |
| QUESTION_ID | NUMBER |  | 18 | Yes | This is the Question ID associated with the Questionnaire. |  |
| QUESTION_VERSION | NUMBER |  | 18 | Yes | This is the Question Version associated with the Question ID in the Questionnaire. |  |
| ANSWER_ID | NUMBER |  | 18 | Yes | This is the Answer ID associated with the Question. |  |
| ANSWER_TEXT | VARCHAR2 | 2000 |  |  | This is the text of the Answer Choice in the specified language. |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SRVY_QSTN_HLPR_TL_U1 | Unique | Default | SUBSCRIBER_ID, QUESTIONNAIRE_ID, QUESTIONNAIRE_VERSION, QUESTION_ID, QUESTION_VERSION, ANSWER_ID, LANGUAGE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
