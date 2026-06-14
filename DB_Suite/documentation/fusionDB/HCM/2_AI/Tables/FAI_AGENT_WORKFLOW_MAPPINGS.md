# FAI_AGENT_WORKFLOW_MAPPINGS

Define mapping between agents and workflows.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiagentworkflowmappings-31231.html#faiagentworkflowmappings-31231](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiagentworkflowmappings-31231.html#faiagentworkflowmappings-31231)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_AGENT_WF_MAPPINGS_PK | WORKFLOW_ID, AGENT_ID, AGENT_TARGET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORKFLOW_ID | NUMBER |  | 18 | Yes | Primary key: Reference to FAI_WORKFLOWS. |
| AGENT_ID | NUMBER |  | 18 | Yes | Primary key: Source Agent. Reference to HR_GEN_AI_AGENTS. |
| AGENT_TARGET_ID | NUMBER |  | 18 | Yes | Primary key: Target Agent. Reference to HR_GEN_AI_AGENTS. |
| EDGE_ORDER | NUMBER |  | 4 |  | The logic order of edge in the graph node. |
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
| FAI_AGENT_WF_MAPPINGS_U1 | Unique | Default | WORKFLOW_ID, AGENT_ID, AGENT_TARGET_ID, ORA_SEED_SET1 |
| FAI_AGENT_WF_MAPPINGS_U11 | Unique | Default | WORKFLOW_ID, AGENT_ID, AGENT_TARGET_ID, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
