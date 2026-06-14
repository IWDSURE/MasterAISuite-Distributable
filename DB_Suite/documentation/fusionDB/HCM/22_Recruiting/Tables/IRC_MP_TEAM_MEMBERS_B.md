# IRC_MP_TEAM_MEMBERS_B

The table that contains the properties of team members

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpteammembersb-6568.html#ircmpteammembersb-6568](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpteammembersb-6568.html#ircmpteammembersb-6568)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MP_TEAM_MEMBERS_B_PK | TEAM_MEMBER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEAM_MEMBER_ID | NUMBER |  | 18 | Yes | The primary key of the team member which is unique for each member |
| PERSON_ID | NUMBER |  | 18 |  | Foreign key to the table per_persons |
| SOURCE_ID | NUMBER |  | 18 |  | The id of the source that belongs to the team member |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | The type of the source that belongs to the team member |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MP_TEAM_MEMBERS_B_FK1 | Non Unique | Default | PERSON_ID |
| IRC_MP_TEAM_MEMBERS_B_PK | Unique | Default | TEAM_MEMBER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
