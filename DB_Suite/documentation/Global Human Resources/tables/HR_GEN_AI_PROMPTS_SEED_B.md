# HR_GEN_AI_PROMPTS_SEED_B

This table stores the seeded prompts.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaipromptsseedb-11483.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaipromptsseedb-11483.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_GEN_AI_PROMPTS_SEED_B_PK | PROMPT_TMPL_AI_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROMPT_TMPL_AI_ID | VARCHAR2 | 32 |  | Yes | This column uniquely a seeded prompt version. |
| BO_HIERARCHY_CLASSPATH | VARCHAR2 | 200 |  |  | This column contains the java classpath that contains Business Objects registered for the prompt |
| PROMPT_CODE | VARCHAR2 | 100 |  | Yes | Unique identifier for prompts |
| PROMPT_TMPL | CLOB |  |  |  | This column contains the prompt text including any substitution variables to be replaced at runtime. |
| PROMPT_TMPL_VERSION | NUMBER |  | 4 |  | This column indicates the prompt design version. |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | This column indicates whether the prompt design version is enabled for use. |
| FAMILY | VARCHAR2 | 80 |  | Yes | Oracle product family to which the prompt belongs to |
| PRODUCT | VARCHAR2 | 100 |  | Yes | Oracle product  to which the prompt belongs to |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| USE_CASE_ID | VARCHAR2 | 100 |  | Yes | AI usecase id |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| PROMPT | VARCHAR2 | 2000 |  |  | Contains the seeded prompt |
| MODEL_CODE | VARCHAR2 | 255 |  |  | This column indicates the LLM model code. |
| MODEL_VERSION | VARCHAR2 | 80 |  |  | This column indicates the LLM model version. |
| MODEL_PROVIDER | VARCHAR2 | 80 |  |  | This column indicates the LLM model provider. |
| CONFIGURABLE | VARCHAR2 | 1 |  | Yes | This column indicates whether the prompt is configurable. |
| PERSIST_DATA | VARCHAR2 | 1 |  | Yes | This column indicates whether the prompt data can be persisted. |
| LANGUAGE_OPT_IN | VARCHAR2 | 4000 |  |  | This column indicates the completion language opt-in. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| AVAILABLE_TOKENS | VARCHAR2 | 2000 |  |  | List of tokens which can be used when its being overridden |
| EXTRA_PROPERTIES | VARCHAR2 | 4000 |  |  | Additional JSON sent with the LLM request (used for resource selectors) |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_GEN_AI_PROMPTS_SEED_B_PK | Unique | Default | PROMPT_TMPL_AI_ID, ORA_SEED_SET1 |
| HR_GEN_AI_PROMPTS_SEED_B_PK1 | Unique | Default | PROMPT_TMPL_AI_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
