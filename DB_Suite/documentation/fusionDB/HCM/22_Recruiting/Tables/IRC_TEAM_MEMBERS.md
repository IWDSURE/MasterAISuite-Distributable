# IRC_TEAM_MEMBERS

Stores the team members related to a given business object.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircteammembers-21122.html#ircteammembers-21122](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircteammembers-21122.html#ircteammembers-21122)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TEAM_MEMBERS_PK | TEAM_MEMBER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEAM_MEMBER_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_PERSONS table. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Stores the ASSIGNMENT_ID of the team member's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M table. |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | The type of object to which the current team member is related. |
| OBJECT_ID | NUMBER |  | 18 | Yes | The primary key of the object to which the current team member is related. |
| MEMBER_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the owner type as a lookup code. |
| COLLABORATOR_RESP_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the collaborator responsibility type as ORA_IRC_COLLABORATOR_RESP_TYPE lookup code. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TEAM_MEMBERS_N1 | Non Unique | Default | PERSON_ID, OBJECT_TYPE, OBJECT_ID, MEMBER_TYPE_CODE |
| IRC_TEAM_MEMBERS_N2 | Non Unique | Default | ASSIGNMENT_ID |
| IRC_TEAM_MEMBERS_N3 | Non Unique | Default | OBJECT_ID, MEMBER_TYPE_CODE |
| IRC_TEAM_MEMBERS_PK | Unique | Default | TEAM_MEMBER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
