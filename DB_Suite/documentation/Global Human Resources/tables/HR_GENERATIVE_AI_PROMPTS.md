# HR_GENERATIVE_AI_PROMPTS

This table stores the prompts customizations.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenerativeaiprompts-28865.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenerativeaiprompts-28865.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_GENERATIVE_AI_PROMPTS_PK | PROMPT_TMPL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROMPT_CODE | VARCHAR2 | 100 |  | Yes | Identifier for prompts. |
| PROMPT_TMPL | CLOB |  |  |  | This column contains the prompt text including any substitution variables to be replaced at runtime. |
| PROMPT_TMPL_ID | VARCHAR2 | 32 |  | Yes | The system generated surrogate key. |
| PROMPT_TMPL_AI_ID | VARCHAR2 | 32 |  |  | This column contains a reference to HR_GEN_AI_PROMPTS_SEED_B table. |
| USE_CASE_ID | VARCHAR2 | 100 |  |  | This column indicates the prompt use case. |
| PROMPT | VARCHAR2 | 2000 |  |  | Actual prompt text set to generative ai. |
| PROMPT_TMPL_VERSION | NUMBER |  | 4 |  | This column indicates the prompt design version. |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | This column indicates whether the prompt design version is enabled for use. |
| LABEL | VARCHAR2 | 200 |  |  | Any string representing this prompt |
| DESCRIPTION | VARCHAR2 | 500 |  |  | Description of this prompt like where its used etc |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_GENERATIVE_AI_PROMPTS_PK | Unique | HR_GENERATIVE_AI_PROMPTS_PK | PROMPT_TMPL_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
