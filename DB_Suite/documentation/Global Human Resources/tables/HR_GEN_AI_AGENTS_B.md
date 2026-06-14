# HR_GEN_AI_AGENTS_B

This table stores the Gen AI Agents

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaiagentsb-27520.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaiagentsb-27520.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_GEN_AI_AGENTS_B_PK | AGENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AGENT_ID | NUMBER |  | 18 | Yes | The Unique Identifier of the Gen AI Agent in the Agentic Workflow |
| AGENT_CODE | VARCHAR2 | 200 |  | Yes | Stores the Agent Code of the Gen AI Agent in the Agentic Workflow |
| FAMILY | VARCHAR2 | 80 |  |  | Product family of the Gen AI Agent in the Agentic Workflow |
| PRODUCT | VARCHAR2 | 100 |  |  | Product area of the Gen AI Agent in the Agentic Workflow |
| AGENT_CREATED_DATE | DATE |  |  |  | Created Date of the Gen AI Agent in the Agentic Workflow |
| OWNER_ID | NUMBER |  | 18 |  | ID of the owner who created the Gen AI Agent in the Agentic Workflow |
| OWNER_NAME | VARCHAR2 | 200 |  |  | Name of the owner who created the Gen AI Agent in the Agentic Workflow |
| STATUS | VARCHAR2 | 32 |  |  | Status of the Gen AI Agent in the Agentic Workflow |
| PROMPT_CODE | VARCHAR2 | 100 |  |  | Prompt Code of the Gen AI Agent in the Agentic Workflow. FK to the prompt table |
| NAMESPACE | VARCHAR2 | 200 |  |  | Namespace of the Gen AI Agent in the Agentic Workflow |
| VERSION | NUMBER |  | 4 | Yes | Version of the Gen AI Agent in the Agentic Workflow |
| SPECIFICATION | CLOB |  |  |  | JSON specification of the Gen AI Agent in the Agentic Workflow |
| MAX_INTERACTIONS | NUMBER |  | 4 |  | Maximum number of interactions with LLM engine. |
| AGENT_TYPE | VARCHAR2 | 32 |  | Yes | This column stores the Agent type. |
| PROMPT | CLOB |  |  |  | Alternate prompt used by this agent. |
| MODEL_CONFIG_ID | NUMBER |  | 18 |  | Reference to a LLM model configuration. Foreign key to FAI_MODEL_CONFIGS table. |
| INTERNAL_NAME | VARCHAR2 | 200 |  |  | This column represents the system name of the Agent. |
| INTERNAL_DESCRIPTION | VARCHAR2 | 2000 |  |  | This column represents the system description of the Agent. |
| REUSABLE_FLAG | VARCHAR2 | 1 |  | Yes | This column indicates whether the Agent is resusable. |
| SEEDED_FLAG | VARCHAR2 | 1 |  |  | Y or N. This column differentiates seeded data from customer created. |
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
|-------|------------|------------|----------|
| HR_GEN_AI_AGENTS_B_N1 | Non Unique | Default | MODEL_CONFIG_ID |
| HR_GEN_AI_AGENTS_B_PK | Unique | Default | AGENT_ID, ORA_SEED_SET1 |
| HR_GEN_AI_AGENTS_B_PK1 | Unique | Default | AGENT_ID, ORA_SEED_SET2 |
| HR_GEN_AI_AGENTS_B_U1 | Unique | Default | AGENT_CODE, VERSION, STATUS, ORA_SEED_SET1 |
| HR_GEN_AI_AGENTS_B_U2 | Unique | Default | AGENT_CODE, VERSION, STATUS, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
