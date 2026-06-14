# IRC_BOT_QUESTIONS_CONFIG_B

The irc_bot_questions_config_b along with the irc_bot_questions_config_tl table (translated) store the predefined questions and answers that an Admin configures for candidates to be presented with when the candidates want to know more about a requisition. This table stores the metadata information for a particular pre-defined question on a requisition-- example QUESTION_CATEGORY.

Three question categories are available, questions on Standard fields, questions on Flex fields and general questions that are not any tied to any field.

Questions can be enabled/ disabled and the sequence for the questions can be defined within these settings.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbotquestionsconfigb-8245.html#ircbotquestionsconfigb-8245](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbotquestionsconfigb-8245.html#ircbotquestionsconfigb-8245)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_BOT_QUESTIONS_CONFIG_B_PK | BOT_QUESTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BOT_QUESTION_ID | NUMBER |  |  | Yes | Primary Key. |
| QUESTION_FLOW_CODE | VARCHAR2 | 50 |  | Yes | This is the flow that the question is asked on. Currently, we will just support requisition questions flow, for which the code is REQUISITION_QUESTIONS. |
| QUESTION_CATEGORY | VARCHAR2 | 50 |  | Yes | The type of requisition question. Thereare three types of questions: one on a Standard Field, one on a Flex Field, the last type is a general question. |
| BOT_INTENT_CODE | VARCHAR2 | 200 |  |  | The intent that this question is associated to. This column is to be used for out-of-the-box intents based on Flex Fields.

The out-of-the-box intent can know which DFF column to rely on to answer the asked question. |
| FIELD_NAME | VARCHAR2 | 200 |  |  | The attribute/field that the question is based on. |
| SEQUENCE_NUMBER | NUMBER |  |  | Yes | The order in which this question should be displayed. |
| IS_ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | Whether the question is enabled or disabled. If enabled then it will be shown/presented to the user. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
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
| IRC_BOT_QUESTIONS_CONFIG_B_PK | Unique | Default | BOT_QUESTION_ID, ORA_SEED_SET1 |
| IRC_BOT_QUESTIONS_CONFIG_B_PK1 | Unique | Default | BOT_QUESTION_ID, ORA_SEED_SET2 |
| IRC_BOT_QUESTIONS_CONFIG_B_U1 | Unique | Default | BOT_INTENT_CODE, ORA_SEED_SET1 |
| IRC_BOT_QUESTIONS_CONFIG_B_U11 | Unique | Default | BOT_INTENT_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
