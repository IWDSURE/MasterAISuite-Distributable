# IRC_CAMP_TEAM_VANITY_CFG

Table to store the Vanity Config ids for the communication teams.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampteamvanitycfg-19125.html#irccampteamvanitycfg-19125](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampteamvanitycfg-19125.html#irccampteamvanitycfg-19125)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_TEAM_VANITY_CFG_PK | TEAM_ID, CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEAM_ID | NUMBER |  | 18 | Yes | Identifier of communication teams table. Foreign Key to irc_camp_comm_teams_b table |
| CONFIG_ID | NUMBER |  | 18 | Yes | Identifier of vanity config ID selected for the communication teams. Foreign Key to IRC_CAMP_VANITY_CONFIG table |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_TEAM_VANITY_CFG_FK1 | Non Unique | Default | CONFIG_ID |
| IRC_CAMP_TEAM_VANITY_CFG_PK | Unique | Default | TEAM_ID, CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
