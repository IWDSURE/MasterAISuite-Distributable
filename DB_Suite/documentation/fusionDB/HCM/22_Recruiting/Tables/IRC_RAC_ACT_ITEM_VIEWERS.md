# IRC_RAC_ACT_ITEM_VIEWERS

This table is used to store the mapping of the team members to an individual action item. This will also record the responses to each of the action items done by the team member.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircracactitemviewers-11980.html#ircracactitemviewers-11980](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircracactitemviewers-11980.html#ircracactitemviewers-11980)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_RAC_ACT_ITEM_VIEWERS_PK | ACTION_ITEM_VIEWER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_ITEM_VIEWER_ID | NUMBER |  | 18 | Yes | This column will be used to store the primary key of this table. Auto Generated Key. |
| ACTION_ITEM_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_RAC_ACTION_ITEMS table. |
| VIEWER_ID | NUMBER |  | 18 |  | This column stores either the person_id or owner_id or agent_id based on who is supposed to view the activity. |
| VIEWER_TYPE | VARCHAR2 | 30 |  |  | This column stores the type of the viewer_id,it will either be ORA_PERSON,ORA_AGENT etc.It is not based on a lookup. |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Response of the viewer to an action item. DISMISSED is one example. Lookup used - ORA_IRC_ACTION_ITEM_STATUS |
| STATUS_DATE | TIMESTAMP |  |  |  | Date when the status was changed on this table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_RAC_ACT_ITEM_VIEWERS_FK1 | Non Unique | Default | ACTION_ITEM_ID |
| IRC_RAC_ACT_ITEM_VIEWERS_N1 | Non Unique | Default | VIEWER_ID |
| IRC_RAC_ACT_ITEM_VIEWERS_PK | Unique | Default | ACTION_ITEM_VIEWER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
