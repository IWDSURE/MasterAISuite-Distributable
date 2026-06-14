# IRC_GEO_HIER_NODES

Table for Recruiting Tree Geography Hierarchy node items.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeohiernodes-16575.html#ircgeohiernodes-16575](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeohiernodes-16575.html#ircgeohiernodes-16575)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_GEO_HIER_NODES_PK | GEOGRAPHY_NODE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GEOGRAPHY_NODE_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| GEOGRAPHY_ID | NUMBER |  | 18 | Yes | Foreign key to HZ_GEOGRAPHIES table. |
| PARENT_GEO_NODE_ID | NUMBER |  | 18 |  | Stores the parent node id of current node for hierarchical tree management. |
| HIERARCHY_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_GEO_HIERARCHIES table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_GEO_HIER_NODES_FK1 | Non Unique | Default | HIERARCHY_ID |
| IRC_GEO_HIER_NODES_FK2 | Non Unique | Default | GEOGRAPHY_ID |
| IRC_GEO_HIER_NODES_PK | Unique | Default | GEOGRAPHY_NODE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
