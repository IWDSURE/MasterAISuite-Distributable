# IRC_INTERACTION_TOKEN_VALUES

This table stores tokens and their resolved values for a specific interaction

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircinteractiontokenvalues-20546.html#ircinteractiontokenvalues-20546](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircinteractiontokenvalues-20546.html#ircinteractiontokenvalues-20546)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_INT_TOKEN_VALUES_PK | INTERACTION_TOKEN_VALUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERACTION_TOKEN_VALUE_ID | NUMBER |  | 18 | Yes | Primary Key of the table.System Generated |
| INTERACTION_ID | NUMBER |  | 18 | Yes | Foreign Key to irc_interactions. The interaction id this token is associated to |
| TOKEN_KEY | VARCHAR2 | 100 |  | Yes | Stores the name of the interaction token |
| TOKEN_VALUE | VARCHAR2 | 1024 |  |  | Stores the value of the interaction token |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_INT_TOKEN_VALUES_PK | Unique | Default | INTERACTION_TOKEN_VALUE_ID |
| IRC_INT_TOKEN_VALUES_FK1 | Non Unique | Default | INTERACTION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
