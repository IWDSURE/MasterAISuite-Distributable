# HR_GEN_AI_AGENT_TOOL_MAPPINGS

This table stores the relationships between Agents and Tools.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaiagenttoolmappings-22444.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaiagenttoolmappings-22444.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_GENAI_AGENTTOOL_MAPPING_PK | AGENT_TOOL_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AGENT_TOOL_MAPPING_ID | NUMBER |  | 18 | Yes | The Unique Identifier for the Agent Tool Mapping in the Agentic Workflow |
| AGENT_ID | NUMBER |  | 18 |  | The Unique Identifier of the Gen AI Agent in the Agentic Workflow |
| TOOL_ID | NUMBER |  | 18 |  | The Unique Identifier of the Gen AI Tool in the Agentic Workflow |
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
|-------|------------|------------|----------|
| HR_GENAI_AGENTTOOL_MAPPING_PK | Unique | Default | AGENT_TOOL_MAPPING_ID, ORA_SEED_SET1 |
| HR_GENAI_AGENTTOOL_MAPPING_PK1 | Unique | Default | AGENT_TOOL_MAPPING_ID, ORA_SEED_SET2 |
| HR_GENAI_AGENTTOOL_MAPPING_U1 | Unique | Default | AGENT_ID, TOOL_ID, ORA_SEED_SET1 |
| HR_GENAI_AGENTTOOL_MAPPING_U11 | Unique | Default | AGENT_ID, TOOL_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
