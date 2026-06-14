# CMP_TCS_STMT_FEEDBACK_TL

This table stores translatable data of run tinme setup for feedback

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtfeedbacktl-14107.html#cmptcsstmtfeedbacktl-14107](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtfeedbacktl-14107.html#cmptcsstmtfeedbacktl-14107)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STMT_FB_TL_PK | STMT_FEEDBACK_ID, LANGUAGE, PERD_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STMT_FEEDBACK_ID | NUMBER |  | 18 | Yes | STMT_FEEDBACK_ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| RATING_INSTRUCTION | VARCHAR2 | 300 |  |  | RATING_INSTRUCTION |
| QUESTION1 | VARCHAR2 | 300 |  |  | RATING_INSTRUCTION |
| QUESTION2 | VARCHAR2 | 300 |  |  | RATING_INSTRUCTION |
| QUESTION3 | VARCHAR2 | 300 |  |  | RATING_INSTRUCTION |
| QUESTION4 | VARCHAR2 | 300 |  |  | RATING_INSTRUCTION |
| QUESTION5 | VARCHAR2 | 300 |  |  | RATING_INSTRUCTION |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_STMT_FB_TL_FK1 | Non Unique | Default | PERD_RUN_ID |
| CMP_TCS_STMT_FB_TL_UK1 | Unique | Default | STMT_FEEDBACK_ID, LANGUAGE, PERD_RUN_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
