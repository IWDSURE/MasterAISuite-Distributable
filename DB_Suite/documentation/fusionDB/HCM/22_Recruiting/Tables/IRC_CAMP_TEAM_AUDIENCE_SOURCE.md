# IRC_CAMP_TEAM_AUDIENCE_SOURCE

Table stores the audience source for a campaign communication team

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampteamaudiencesource-10355.html#irccampteamaudiencesource-10355](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampteamaudiencesource-10355.html#irccampteamaudiencesource-10355)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_TEAM_AUDIENCE_SO_PK | TEAM_ID, SOURCE_ID, SOURCE_TYPE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEAM_ID | NUMBER |  | 18 | Yes | Identifier of the communication teams table. Foreign Key to irc_camp_comm_teams_b table |
| SOURCE_ID | NUMBER |  | 18 | Yes | Identifier of source e.g. HCM List Id, Eligibility profile id. |
| SOURCE_TYPE | VARCHAR2 | 64 |  | Yes | Indicate the source type. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_TEAM_AUDIENCE_SO_PK | Unique | Default | TEAM_ID, SOURCE_ID, SOURCE_TYPE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
