# HR_GEN_AI_PROMPTS_SEED_TL

This table stores the seeded prompts label and description.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaipromptsseedtl-25348.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaipromptsseedtl-25348.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_GEN_AI_PROMPTS_SEED_TL_PK | PROMPT_TMPL_AI_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROMPT_TMPL_AI_ID | VARCHAR2 | 32 |  | Yes | This column uniquely a seeded prompt version. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LABEL | VARCHAR2 | 200 |  | Yes | Label for the prompt |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Description for the prompt |
| PROMPT_CODE | VARCHAR2 | 100 |  |  | Label for prompt code |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_GEN_AI_PROMPTS_SEED_TL_U1 | Unique | Default | PROMPT_TMPL_AI_ID, LANGUAGE, ORA_SEED_SET1 |
| HR_GEN_AI_PROMPTS_SEED_TL_U2 | Unique | Default | PROMPT_TMPL_AI_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
