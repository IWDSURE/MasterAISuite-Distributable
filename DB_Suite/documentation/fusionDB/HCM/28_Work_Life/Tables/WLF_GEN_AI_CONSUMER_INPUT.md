# WLF_GEN_AI_CONSUMER_INPUT

This table stores the "GEN AI" consumer input configuration details.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgenaiconsumerinput-14718.html#wlfgenaiconsumerinput-14718](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgenaiconsumerinput-14718.html#wlfgenaiconsumerinput-14718)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_GEN_AI_CONSUMER_INPUT_PK | GEN_AI_CONSUMER_INPUT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GEN_AI_CONSUMER_INPUT_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| GEN_AI_CONSUMER_CONFIG_ID | NUMBER |  | 18 | Yes | Reference to the consumer config row in wlf_gen_ai_consumer_config_b. |
| SYNTHETIC_OBJECT_JSON_SCHEMA | CLOB |  |  |  | Represents the normalized JSON schema that represents the transformed and enriched SLDS object. |
| ENRICHMENT_CONFIG | CLOB |  |  |  | Represents the configuration that specifies which fields in the SLDS Json schema need to be enriched. |
| RAG_PUBLISHER_CONFIG | CLOB |  |  |  | Represents the configuration that specifies which fields in the SLDS Json schema need to be published to RAG. |
| INPUT_METADATA_CONFIG | CLOB |  |  |  | Represents the consumer input metadata configurations in json format. |
| ADDITIONAL_INSTRUCTIONS | CLOB |  |  |  | Represents additional instructions that LLM must use while enriching the SDLS object data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_GEN_AI_CONSUMER_INPUT_PK1 | Unique | Default | GEN_AI_CONSUMER_INPUT_ID, ORA_SEED_SET1 |
| WLF_GEN_AI_CONSUMER_INPUT_PK2 | Unique | Default | GEN_AI_CONSUMER_INPUT_ID, ORA_SEED_SET2 |
| WLF_GEN_AI_CONSUMER_INPUT_U1 | Unique | Default | GEN_AI_CONSUMER_CONFIG_ID, ORA_SEED_SET1 |
| WLF_GEN_AI_CONSUMER_INPUT_U2 | Unique | Default | GEN_AI_CONSUMER_CONFIG_ID, ORA_SEED_SET2 |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
