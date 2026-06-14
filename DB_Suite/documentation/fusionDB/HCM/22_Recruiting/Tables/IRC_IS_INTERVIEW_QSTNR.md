# IRC_IS_INTERVIEW_QSTNR

This table stores all the interview questionnaires

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisinterviewqstnr-14978.html#ircisinterviewqstnr-14978](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircisinterviewqstnr-14978.html#ircisinterviewqstnr-14978)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IS_INTERVIEW_QSTNR_PK | INTERVIEW_QSTNR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERVIEW_QSTNR_ID | NUMBER |  | 18 | Yes | The primary key for this table. |
| INTERVIEW_ID | NUMBER |  | 18 | Yes | Foreign key to the schedule template(IRC_IS_INTERVIEWS) that was used to create this schedule. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | Foreign key to the schedule template(HRQ_QUESTIONNAIRES_B) that was used to create this schedule. |
| QSTNR_VERSION_NUM | NUMBER |  | 18 | Yes | Version number of the questionnaire. It identifies the specific version of the questionnaire if it is modified. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IS_INTERVIEW_QSTNR_FK1 | Non Unique | Default | INTERVIEW_ID |
| IRC_IS_INTERVIEW_QSTNR_PK | Unique | Default | INTERVIEW_QSTNR_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
