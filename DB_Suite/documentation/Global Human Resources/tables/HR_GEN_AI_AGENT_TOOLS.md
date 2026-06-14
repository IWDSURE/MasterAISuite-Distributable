# HR_GEN_AI_AGENT_TOOLS

This table stores the Gen AI Agent Tools

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** HR_GEN_AI_AGENT_TOOLS

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenKBtools-23854.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenKBtools-23854.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_GEN_AI_AGENT_TOOLS_PK | AGENT_TOOL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AGENT_TOOL_ID | NUMBER |  | 18 | Yes | The Unique Identifier for the Gen AI Agent Tool |
| AGENT_ID | NUMBER |  | 18 |  | Uniquely identifies the Gen AI Agent |
| TOOL_ID | NUMBER |  | 18 |  | Uniquely identifies the Gen AI Tool |
| ACTIVE | VARCHAR2 | 1 |  |  | Determines whether the Gen AI Agent Tool is active or not |
| READONLY | VARCHAR2 | 1 |  |  | Readonly flag of the Gen AI Agent Tool. Y or N |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_GEN_AI_AGENT_TOOLS_PK | Unique | HR_GEN_AI_AGENT_TOOLS_PK | AGENT_TOOL_ID |

---

[â† Back to HRMS Tables Index](../HRMS_Tables_Index.md)

