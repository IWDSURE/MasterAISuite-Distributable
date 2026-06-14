# IRC_AGENT_REQUISITIONS

The IRC_AGENT_REQUISITIONS will store the requisitions to which the agencies are invited to submit candidates

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircagentrequisitions-17939.html#ircagentrequisitions-17939](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircagentrequisitions-17939.html#ircagentrequisitions-17939)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AGENT_REQUISITIONS_PK | AGENT_REQUISITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AGENT_REQUISITION_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Stores the REQUISITION_ID to which the Agent is invited to submit candidate profiles. Foreign key to IRC_REQUISITIONS_B table. |
| AGENT_ID | NUMBER |  | 18 |  | Stores the AGENT_ID of the Agent who is invited to submit candidate profiles to the requisition. Foreign key to IRC_AGENTS table. |
| AGENCY_ID | NUMBER |  | 18 |  | Stores the AGENCY_ID of the Agency who is invited to submit candidate profiles to the requisition. Foreign key to IRC_AGENCIES table. |
| INVITED_FLAG | VARCHAR2 | 1 |  |  | Stores if the Agency is invited to Apply for the Requisition |
| DO_NOT_EXPIRE_FLAG | VARCHAR2 | 1 |  |  | Stores the flag that decides  the invite to the agent for the requisition never expires or not. |
| EXPIRATION_DATE | DATE |  |  |  | Stores the date on which the invite to the agent for the requisition expires. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AGENT_REQUISITIONS_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_AGENT_REQUISITIONS_FK2 | Non Unique | Default | AGENT_ID |
| IRC_AGENT_REQUISITIONS_FK3 | Non Unique | Default | AGENCY_ID |
| IRC_AGENT_REQUISITIONS_FK4 | Non Unique | Default | EXPIRATION_DATE |
| IRC_AGENT_REQUISITIONS_U1 | Unique | Default | AGENT_REQUISITION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
