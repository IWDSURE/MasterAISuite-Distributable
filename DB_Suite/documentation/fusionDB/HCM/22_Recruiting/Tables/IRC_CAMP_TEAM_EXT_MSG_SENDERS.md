# IRC_CAMP_TEAM_EXT_MSG_SENDERS

Table to store the mapping of integration user, both with communication teams.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampteamextmsgsenders-16877.html#irccampteamextmsgsenders-16877](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampteamextmsgsenders-16877.html#irccampteamextmsgsenders-16877)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_TEAM_EXT_MSG_SEND_PK | CAMP_TEAM_EXT_MSG_SENDER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMP_TEAM_EXT_MSG_SENDER_ID | NUMBER |  | 18 | Yes | Primary key for this table, system generated. |
| SENDER_TYPE | VARCHAR2 | 30 |  | Yes | Indicates whether sender type is ORA_AZURE_INTG_USER or ORA_AZURE_TEAMS_BOT or ORA_SLACK. |
| SENDER_ID | NUMBER |  | 18 | Yes | Stores either TEAMS_USER_ID or TEAMS_BOT_ID depends on SENDER_TYPE |
| TEAM_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CAMP_TEAMS_B table |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_TEAM_EXT_MSG_SEND_FK1 | Non Unique | Default | TEAM_ID |
| IRC_CAMP_TEAM_EXT_MSG_SEND_PK | Unique | Default | CAMP_TEAM_EXT_MSG_SENDER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
