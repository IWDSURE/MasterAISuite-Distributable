# FAI_PROMPT_TMPLS

This table contains prompt design data. A prompt design consists of a prompt text string optionally containing variable tokens along with a specific LLM name and version.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiprompttmpls-16513.html#faiprompttmpls-16513](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiprompttmpls-16513.html#faiprompttmpls-16513)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_PROMPT_TMPLS_PK | PROMPT_TMPL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROMPT_TMPL_ID | VARCHAR2 | 32 |  | Yes | The system generated surrogate key. |
| PROMPT_CODE_ID | VARCHAR2 | 32 |  | Yes | Foreign key referencing to FAI_PROMPT_CODES table. |
| PROMPT_TMPL | CLOB |  |  | Yes | This column contains the prompt text including any substitution variables to be replaced at runtime. |
| PROMPT_TMPL_VERSION | NUMBER |  |  | Yes | This column indicates the prompt design version. |
| MODEL_CODE | VARCHAR2 | 80 |  | Yes | This column indicates the LLM name being used with the prompt design. |
| MODEL_VERSION | VARCHAR2 | 80 |  | Yes | This column indicates the LLM version being used with the prompt design. |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | This column indicates whether the prompt design version is enabled for use. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_PROMPT_TMPLS_N1 | Non Unique | Default | ENABLED_FLAG |
| FAI_PROMPT_TMPLS_U1 | Unique | Default | PROMPT_TMPL_ID, ORA_SEED_SET1 |
| FAI_PROMPT_TMPLS_U11 | Unique | Default | PROMPT_TMPL_ID, ORA_SEED_SET2 |
| FAI_PROMPT_TMPLS_U2 | Unique | Default | PROMPT_CODE_ID, PROMPT_TMPL_VERSION, ORA_SEED_SET1 |
| FAI_PROMPT_TMPLS_U21 | Unique | Default | PROMPT_CODE_ID, PROMPT_TMPL_VERSION, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
