# HRQ_QUESTIONNAIRES_TL

Translatable table for HRQ_QUESTIONNAIRES_B

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqquestionnairestl-9000.html#hrqquestionnairestl-9000](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqquestionnairestl-9000.html#hrqquestionnairestl-9000)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QUESTIONNAIRES_TL_PK | QUESTIONNAIRE_ID, QSTNR_VERSION_NUM, BUSINESS_GROUP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | Unique identifier for a questionnaire.  System generated id.  This attribute combined with the version number, business group id, and language forms the primary key. |
| QSTNR_VERSION_NUM | NUMBER |  | 18 | Yes | The version number of the questionnaire. This attribute combined with the questionnaire id, business group id, and language forms the primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 240 |  | Yes | A short description of the questionnaire. |
| INTRO_TEXT | VARCHAR2 | 4000 |  |  | The introduction text for the questionnaire. |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | A full description of the questionnaire. |
| KEYWORDS | VARCHAR2 | 2000 |  |  | A list of keywords that are used to identify the questionnaire. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QUESTIONNAIRES_TL_N1 | Non Unique | Default | BUSINESS_GROUP_ID, LANGUAGE, NAME |
| HRQ_QUESTIONNAIRES_TL_PK | Unique | Default | QUESTIONNAIRE_ID, QSTNR_VERSION_NUM, BUSINESS_GROUP_ID, LANGUAGE, ORA_SEED_SET1 |
| HRQ_QUESTIONNAIRES_TL_PK1 | Unique | Default | QUESTIONNAIRE_ID, QSTNR_VERSION_NUM, BUSINESS_GROUP_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
