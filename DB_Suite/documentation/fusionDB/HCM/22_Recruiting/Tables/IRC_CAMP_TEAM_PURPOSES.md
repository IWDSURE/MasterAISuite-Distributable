# IRC_CAMP_TEAM_PURPOSES

Table to store the selected purpose codes selected for the communication teams.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampteampurposes-31402.html#irccampteampurposes-31402](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampteampurposes-31402.html#irccampteampurposes-31402)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_TEAM_PURPOSES_PK | TEAM_ID, PURPOSE_CODE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEAM_ID | NUMBER |  | 18 | Yes | Identifier of communication teams table, Foreign Key to irc_camp_comm_teams_b table |
| PURPOSE_CODE | VARCHAR2 | 40 |  | Yes | Indicates the code of the campaign purpose. Lookup type - ORA_IRC_CAMP_PURPOSE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_TEAM_PURPOSES_PK | Unique | Default | TEAM_ID, PURPOSE_CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
