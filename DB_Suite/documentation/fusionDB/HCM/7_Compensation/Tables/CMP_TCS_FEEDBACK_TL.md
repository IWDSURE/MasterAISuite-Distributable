# CMP_TCS_FEEDBACK_TL

Table holds feedack translatable data

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsfeedbacktl-10637.html#cmptcsfeedbacktl-10637](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsfeedbacktl-10637.html#cmptcsfeedbacktl-10637)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_FEDBACK_TL_PK | FEEDBACK_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FEEDBACK_ID | NUMBER |  | 18 | Yes | Primary Key |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| RATING_INSTRUCTION | VARCHAR2 | 300 |  |  | Information for Rating |
| QUESTION1 | VARCHAR2 | 300 |  |  | Feedback Question 1 |
| QUESTION2 | VARCHAR2 | 300 |  |  | Feedback Question 2 |
| QUESTION3 | VARCHAR2 | 300 |  |  | Feedback Question 3 |
| QUESTION4 | VARCHAR2 | 300 |  |  | Feedback Question 4 |
| QUESTION5 | VARCHAR2 | 300 |  |  | Feedback Question 5 |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_FEDBACK_TL_UK1 | Unique | Default | FEEDBACK_ID, LANGUAGE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
