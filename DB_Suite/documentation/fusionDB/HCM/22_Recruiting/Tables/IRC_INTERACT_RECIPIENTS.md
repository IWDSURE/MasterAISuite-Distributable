# IRC_INTERACT_RECIPIENTS

Table for recording recipent list for an interaction.  multiple entries possible for an interaction.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircinteractrecipients-15057.html#ircinteractrecipients-15057](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircinteractrecipients-15057.html#ircinteractrecipients-15057)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_INTERACT_RECIPIENTS_PK | INTERACTION_RECIPIENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERACTION_RECIPIENT_ID | NUMBER |  | 18 | Yes | Primary Key of the table.System generated. |
| INTERACTION_ID | NUMBER |  | 18 | Yes | Foreign key to irc_interactions table |
| PERSON_ID | NUMBER |  | 18 |  | foreign to per_persons table |
| AGENT_ID | NUMBER |  | 18 |  | foreign key to irc_agents table that identify agent as recipient of notification |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_INTERACT_RECIPIENTS_FK1 | Non Unique | Default | PERSON_ID |
| IRC_INTERACT_RECIPIENTS_FK2 | Non Unique | Default | INTERACTION_ID |
| IRC_INTERACT_RECIPIENTS_FK3 | Non Unique | Default | AGENT_ID |
| IRC_INTERACT_RECIPIENTS_PK | Unique | Default | INTERACTION_RECIPIENT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
