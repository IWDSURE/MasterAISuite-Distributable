# IRC_AGENTS

The IRC_AGENTS will store the Agent information.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircagents-24635.html#ircagents-24635](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircagents-24635.html#ircagents-24635)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AGENTS_PK | AGENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AGENT_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| FIRST_NAME | VARCHAR2 | 150 |  |  | First Name of Agent |
| LAST_NAME | VARCHAR2 | 150 |  |  | Last Name of Agent |
| AGENCY_ID | NUMBER |  | 18 | Yes | Stores the AGENCY_ID of the Agency to which the agent belong. Foreign key to IRC_AGENCIES table. |
| USERNAME | VARCHAR2 | 80 |  | Yes | Username of the agent. |
| EMAIL_ADDRESS | VARCHAR2 | 240 |  |  | E-mail address of the agent |
| USER_GUID | VARCHAR2 | 64 |  |  | The user Guid of the agent user. |
| USER_CATEGORY | VARCHAR2 | 64 |  |  | User category of agent user. |
| STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores the status of the Agent as a lookup code. The corresponding lookup type is ORA_IRC_AGENCY_STATUS. |
| AGENT_NOTES | VARCHAR2 | 1000 |  |  | Stores notes for the Agent. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PROV_STATUS_CODE | VARCHAR2 | 100 |  |  | Captures the information of agent based on role provisioning. The corresponding lookup type is ORA_IRC_AGENT_PROV_STATUS. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AGENTS_FK1 | Non Unique | Default | AGENCY_ID |
| IRC_AGENTS_N1 | Non Unique | Default | USERNAME |
| IRC_AGENTS_N2 | Non Unique | Default | EMAIL_ADDRESS |
| IRC_AGENTS_U1 | Unique | Default | AGENT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
