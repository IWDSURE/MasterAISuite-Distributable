# IRC_MP_TEAM_MEMBERS_TL

This table contains all translations related to team member properties

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpteammemberstl-6396.html#ircmpteammemberstl-6396](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpteammemberstl-6396.html#ircmpteammemberstl-6396)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MP_TEAM_MEMBERS_TL_PK | TEAM_MEMBER_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEAM_MEMBER_ID | NUMBER |  | 18 | Yes | Foreign Key to the associated Team Member (IRC_MP_TEAM_MEMBERS_TL) of the team |
| ROLE | VARCHAR2 | 240 |  |  | Role of the team member in a given team |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MP_TEAM_MEMBERS_TL_PK | Unique | Default | TEAM_MEMBER_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
