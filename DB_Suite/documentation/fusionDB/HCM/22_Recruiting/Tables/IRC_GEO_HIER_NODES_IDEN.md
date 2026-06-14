# IRC_GEO_HIER_NODES_IDEN

Table for storing Recruiting Tree Geography Hierarchy TCA geography node name identifiers.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeohiernodesiden-9667.html#ircgeohiernodesiden-9667](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeohiernodesiden-9667.html#ircgeohiernodesiden-9667)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_GEO_HIER_NODES_IDEN_PK | IRC_GEO_HIER_NODES_IDENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| IRC_GEO_HIER_NODES_IDENT_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| GEOGRAPHY_NODE_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_GEO_HIER_NODES table. |
| PRIMARY_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether this name is the default for this geography. |
| GEOGRAPHY_NAME | VARCHAR2 | 360 |  | Yes | Stores the node standard name identifier for this language. |
| LANGUAGE_CODE | VARCHAR2 | 4 |  | Yes | Stores the language in which the geography name is stored. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_GEO_HIER_NODES_IDEN_PK | Unique | Default | IRC_GEO_HIER_NODES_IDENT_ID |
| IRC_GEO_HIER_NODES_IDEN_U1 | Unique | Default | GEOGRAPHY_NODE_ID, LANGUAGE_CODE, GEOGRAPHY_NAME |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
