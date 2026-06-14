# IRC_GEO_HIER_NODES_OPTI

Table for Recruiting Tree Geography Hierarchy denormalized node items with their absolute parent.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeohiernodesopti-17053.html#ircgeohiernodesopti-17053](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeohiernodesopti-17053.html#ircgeohiernodesopti-17053)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_GEO_HIER_NODES_OPTI_PK | IRC_GEO_HIER_NODES_OPTI_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| IRC_GEO_HIER_NODES_OPTI_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| HIERARCHY_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_GEO_HIERARCHIES table. |
| GEOGRAPHY_NODE_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_GEO_HIER_NODES table. |
| PARENT_GEO_NODE_ID | NUMBER |  | 18 | Yes | Stores the parent node id of current node for hierarchical tree management. Foreign key to IRC_GEO_HIER_NODES table. |
| PARENT_GEOGRAPHY_ID | NUMBER |  | 18 | Yes | Stores the parent geography id of parent node for hierarchical tree management. Foreign key to HZ_GEOGRAPHIES table. |
| ABSOLUTE_LEVEL | NUMBER |  | 5 |  | Stores the absolute level of the node in the hierarchy tree. |
| RELATIVE_LEVEL | NUMBER |  | 5 |  | Stores the relative level of the node in the hierarchy tree. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_GEO_HIER_NODES_OPTI_FK2 | Non Unique | Default | GEOGRAPHY_NODE_ID |
| IRC_GEO_HIER_NODES_OPTI_FK3 | Non Unique | Default | PARENT_GEO_NODE_ID |
| IRC_GEO_HIER_NODES_OPTI_FK4 | Non Unique | Default | PARENT_GEOGRAPHY_ID |
| IRC_GEO_HIER_NODES_OPTI_PK | Unique | Default | IRC_GEO_HIER_NODES_OPTI_ID |
| IRC_GEO_HIER_NODES_OPTI_U1 | Unique | Default | HIERARCHY_ID, PARENT_GEO_NODE_ID, GEOGRAPHY_NODE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
