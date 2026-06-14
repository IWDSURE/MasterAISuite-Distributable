# HWR_TEAM_GOAL_MEMBER

this table is for storing association with team members and team goals for slack communication

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteamgoalmember-24784.html#hwrteamgoalmember-24784](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteamgoalmember-24784.html#hwrteamgoalmember-24784)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_TEAM_GOAL_MEMBER_PK | TEAM_MEMBER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEAM_MEMBER_ID | NUMBER |  | 18 | Yes | unique id for member of team goal assoc |
| PERSON_ID | VARCHAR2 | 20 |  |  | person id for member of team goal assoc |
| TEAM_GOAL_ASSOC_ID | NUMBER |  | 19 |  | unique id for  team and goal assoc |
| ROLE | VARCHAR2 | 20 |  |  | indicates the member role in the team goal assoc |
| STATUS | VARCHAR2 | 20 |  |  | indicates member status |
| IS_DELETED | NUMBER |  | 1 |  | indicates if the member is deleted |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| TEAM_GOAL_SOURCE_ID | NUMBER |  | 18 |  | communication source id |
| TEAM_GOAL_CONVERSATION_ID | VARCHAR2 | 100 |  |  | channel conversation id |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_TEAM_GOAL_MEMBER_U1 | Unique | Default | TEAM_MEMBER_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
