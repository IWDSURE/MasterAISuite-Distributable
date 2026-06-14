# IRC_BOT_QUESTIONS_CONFIG_TL

The irc_bot_questions_config_b along with the irc_bot_questions_config_tl table (translated) store the predefined questions and answers that an Admin configures for candidates to be presented with when the candidates want to know more about a requisition. This table stores the translated questions and answers in the different languages that the Recruiting Admin has defined.

Three question categories are available, questions on Standard fields, questions on Flex fields and general questions that are not any tied to any field.

Questions can be enabled/ disabled and the sequence for the questions can be defined within these settings.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbotquestionsconfigtl-26572.html#ircbotquestionsconfigtl-26572](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbotquestionsconfigtl-26572.html#ircbotquestionsconfigtl-26572)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_BOT_QUESTIONS_CONFIG_TL_PK | BOT_QUESTION_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BOT_QUESTION_ID | NUMBER |  |  | Yes | Primary key. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| QUESTION | VARCHAR2 | 4000 |  |  | The question about the requisition. This is configured by the Recruiting Administrator to the candidate as one of the questions that a candidate can ask about the requisition. |
| ANSWER | VARCHAR2 | 4000 |  |  | The answer to the question about the requisition. This is configured by the Recruiting Administrator to the candidate as the answer to the question that a candidate can ask about the requisition. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_BOT_QUESTIONS_CONFIG_TL_PK | Unique | Default | BOT_QUESTION_ID, LANGUAGE, ORA_SEED_SET1 |
| IRC_BOT_QUESTION_CONFIG_TL_PK1 | Unique | Default | BOT_QUESTION_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
