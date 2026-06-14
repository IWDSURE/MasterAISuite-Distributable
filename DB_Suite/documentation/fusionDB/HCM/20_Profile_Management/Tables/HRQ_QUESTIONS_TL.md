# HRQ_QUESTIONS_TL

Translatable table for HRQ_QUESTIONS_B

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqquestionstl-28433.html#hrqquestionstl-28433](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqquestionstl-28433.html#hrqquestionstl-28433)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QUESTIONS_TL_PK | BUSINESS_GROUP_ID, QUESTION_ID, QSTN_VERSION_NUM, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QUESTION_ID | NUMBER |  | 18 | Yes | Unique identifier for a question.  System generated id.  This attribute combined with the version number and business group and language id forms the primary key. |
| QSTN_VERSION_NUM | NUMBER |  | 18 | Yes | The version number of the question. This attribute combined with the question id and business group id and language forms the primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| QUESTION_TEXT | VARCHAR2 | 2000 |  | Yes | The full text of the question. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| INSTRUCTIONS_TEXT | VARCHAR2 | 4000 |  |  | Instructions text for the question. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QUESTIONS_TL_PK | Unique | Default | BUSINESS_GROUP_ID, QUESTION_ID, QSTN_VERSION_NUM, LANGUAGE, ORA_SEED_SET1 |
| HRQ_QUESTIONS_TL_PK1 | Unique | Default | BUSINESS_GROUP_ID, QUESTION_ID, QSTN_VERSION_NUM, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
