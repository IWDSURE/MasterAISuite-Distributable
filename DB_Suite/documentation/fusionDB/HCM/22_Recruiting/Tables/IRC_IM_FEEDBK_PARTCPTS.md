# IRC_IM_FEEDBK_PARTCPTS

This table stores all the participants for a feedback.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimfeedbkpartcpts-17828.html#ircimfeedbkpartcpts-17828](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimfeedbkpartcpts-17828.html#ircimfeedbkpartcpts-17828)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IM_FEEDBK_PARTCPTS_PK | FEEDBACK_PARTICIPANT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FEEDBACK_PARTICIPANT_ID | NUMBER |  | 18 | Yes | Primary key of this table. System generated. |
| PARTICIPANT_ID | VARCHAR2 | 240 |  | Yes | Similar to the HRQ_QSTNR_PARTICIPANTS.PARTICIPANT_ID table. Created with similar datatype. |
| FEEDBACK_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_IM_FEEDBACKS table. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | Foreign key to HRQ_QUESTIONNAIRES_B table. |
| QSTNR_VERSION_NUM | NUMBER |  | 18 | Yes | Version number of the questionnaire. It identifies the version of the questionaire if it is modified. |
| NOTES | VARCHAR2 | 1000 |  |  | Stores the notes entered by this feedback participant. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IM_FEEDBK_PARTCPTS_FK1 | Non Unique | Default | FEEDBACK_ID |
| IRC_IM_FEEDBK_PARTCPTS_PK | Unique | Default | FEEDBACK_PARTICIPANT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
