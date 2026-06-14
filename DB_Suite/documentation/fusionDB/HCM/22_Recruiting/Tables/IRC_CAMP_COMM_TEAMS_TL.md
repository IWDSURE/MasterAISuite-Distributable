# IRC_CAMP_COMM_TEAMS_TL

Translation table for IRC_CAMP_COMM_TEAMS table which stores the translatable data.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampcommteamstl-12023.html#irccampcommteamstl-12023](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampcommteamstl-12023.html#irccampcommteamstl-12023)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_COMM_TEAMS_TL_PK | TEAM_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEAM_ID | NUMBER |  | 18 | Yes | The primary key for this table, System-generated. Foreign Key to irc_camp_comm_teams_b table |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| TEAM_NAME | VARCHAR2 | 240 |  | Yes | Stores the name of the communication teams |
| TEAM_DESCRIPTION | CLOB |  |  |  | Stores the description of communication teams |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_COMM_TEAMS_TL_PK | Unique | Default | TEAM_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
