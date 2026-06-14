# IRC_TN_JA_AGENT_ACTIONS

This is the table for storing actions performed on job application by an agent on Talent Network.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjaagentactions-29817.html#irctnjaagentactions-29817](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjaagentactions-29817.html#irctnjaagentactions-29817)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_JA_AGENT_ACTIONS_PK | JA_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JA_ACTION_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | To store the subscriber id. Foreign Key to IRC_TN_SUBSCRIBERS. |
| JOB_APP_ID | NUMBER |  | 18 | Yes | To store the job app id. Foreign Key to IRC_TN_JOB_APPLICATIONS. |
| AGENCY_ID | NUMBER |  | 18 | Yes | Stores the AGENCY_ID of the Agent who submitted the candidate job application. Foreign key to IRC_TN_AGENCIES table. |
| AGENT_ID | NUMBER |  | 18 | Yes | Stores the AGENT_ID of the Agent who submitted the candidate job application. Foreign key to IRC_TN_AGENTS table. |
| ACTION_CODE | VARCHAR2 | 64 |  | Yes | Stores what type of action performed by an agent actions like CONFIRM or WITHDRAWN as a lookup code. |
| ACTION_DATE | TIMESTAMP |  |  | Yes | Stores the date and time of the agent has performed an action. |
| OBJECT_STATUS | VARCHAR2 | 30 |  | Yes | Indicates the status of the object. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TN_JA_AGENT_ACTIONS_FK1 | Non Unique | Default | SUBSCRIBER_ID |
| IRC_TN_JA_AGENT_ACTIONS_FK2 | Non Unique | Default | JOB_APP_ID |
| IRC_TN_JA_AGENT_ACTIONS_FK3 | Non Unique | Default | AGENCY_ID |
| IRC_TN_JA_AGENT_ACTIONS_FK4 | Non Unique | Default | AGENT_ID |
| IRC_TN_JA_AGENT_ACTIONS_PK | Unique | Default | JA_ACTION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
