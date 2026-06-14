# FAI_PROMPT_TMPL_GUARDRAILS

Configuration of guardrail tests for prompts defined in hr_generative_ai_prompts

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiprompttmplguardrails-26881.html#faiprompttmplguardrails-26881](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiprompttmplguardrails-26881.html#faiprompttmplguardrails-26881)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_PROMPT_TMPL_GUARDRAILS_PK | PROMPT_TMPL_GUARDRAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROMPT_TMPL_GUARDRAIL_ID | VARCHAR2 | 32 |  | Yes | The system generated surrogate key. |
| PROMPT_TMPL_ID | VARCHAR2 | 32 |  | Yes | Foreign key to hr_gen_ai_prompts_seed_b |
| METRIC_NAME | VARCHAR2 | 32 |  |  | Name of metric used for guardrail expression |
| METRIC_VERSION | VARCHAR2 | 32 |  |  | Version of metric used for guardrail expression |
| PROMPT_GUARDRAIL_NAME | VARCHAR2 | 256 |  |  | The guardrail name the property belongs to. |
| PROMPT_GUARDRAIL_VERSION | VARCHAR2 | 32 |  |  | The guardrail version the property belongs to. |
| GUARDRAIL_ACTION | VARCHAR2 | 32 |  |  | Action taken if guardrail expression is true |
| GUARDRAIL_NAME | VARCHAR2 | 256 |  |  | The property name used in guardrail expression. |
| GUARDRAIL_OPERATOR | VARCHAR2 | 32 |  |  | The property operator used in guardrail expression |
| GUARDRAIL_TYPE | VARCHAR2 | 256 |  |  | The property type used in guardrail expression. |
| GUARDRAIL_VALUE_TYPE | VARCHAR2 | 32 |  |  | The property value type used in guardrail expression. |
| GUARDRAIL_VALUE | NUMBER |  | 9 |  | The property numeric value used in guardrail expression. |
| GUARDRAIL_STR_VALUE | VARCHAR2 | 2000 |  |  | The property string value used in guardrail expression. |
| RESPONSE_IF_BLOCKED | VARCHAR2 | 512 |  |  | Response sent by GenAI service if guardrail expression is true |
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
| FAI_PROMPT_TMPL_GUARDRAILS_U1 | Unique | Default | PROMPT_TMPL_GUARDRAIL_ID, ORA_SEED_SET1 |
| FAI_PROMPT_TMPL_GUARDRAILS_U11 | Unique | Default | PROMPT_TMPL_GUARDRAIL_ID, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
