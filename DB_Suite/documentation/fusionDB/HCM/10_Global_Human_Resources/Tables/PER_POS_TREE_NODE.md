# PER_POS_TREE_NODE

Position Hierarchy Tree Node Table

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpostreenode-7183.html#perpostreenode-7183](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpostreenode-7183.html#perpostreenode-7183)

## Primary Key

| Name | Columns |
|------|----------|
| PER_POS_TREE_NODE_PK | TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID, TREE_NODE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TREE_STRUCTURE_CODE | VARCHAR2 | 30 |  | Yes | Foreign key to TREE_STRUCTURE_CODE on FND_TREE |
| TREE_CODE | VARCHAR2 | 30 |  | Yes | Foreign key to TREE_CODE on FND_TREE. |
| TREE_VERSION_ID | VARCHAR2 | 32 |  | Yes | Foreign key to VERSION_ID on FND_TREE_VERSION |
| TREE_NODE_ID | VARCHAR2 | 32 |  | Yes | Unique identifier for tree node. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PARENT_TREE_NODE_ID | VARCHAR2 | 32 |  |  | ID of the tree node that is the parent of this node. If this value is null, this node is the root node of the tree.If there are multiple rows with this value null, then they are all root nodes, effectively forming a forest of disjoint trees. |
| DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| PK1_START_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. For range-based tree nodes, this is the start of the range and PK1_END_VALUE forms the end. |
| PK2_START_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. For range-based tree nodes, this is the start of the range and PK1_END_VALUE forms the end. |
| PK3_START_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. For range-based tree nodes, this is the start of the range and PK1_END_VALUE forms the end. |
| PK4_START_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. For range-based tree nodes, this is the start of the range and PK1_END_VALUE forms the end. |
| PK5_START_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. For range-based tree nodes, this is the start of the range and PK1_END_VALUE forms the end. |
| PK1_END_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the end of the range for range-based tree nodes. If the node is not range based, then this value is null. |
| PK2_END_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the end of the range for range-based tree nodes. If the node is not range based, then this value is null. |
| PK3_END_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the end of the range for range-based tree nodes. If the node is not range based, then this value is null. |
| PK4_END_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the end of the range for range-based tree nodes. If the node is not range based, then this value is null. |
| PK5_END_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the end of the range for range-based tree nodes. If the node is not range based, then this value is null. |
| REFERENCE_TREE_CODE | VARCHAR2 | 30 |  |  | For tree-in-tree, this is the reference to the tree code. The referenced tree has to belong to the same Tree Structure. |
| REFERENCE_TREE_VERSION_ID | VARCHAR2 | 32 |  |  | For tree-in-tree, this is the reference to the tree version. The referenced tree has to belong to the same Tree Structure. |
| TREE_LABEL_ID | VARCHAR2 | 32 |  |  | Foreign key to the TREE_LABEL_ID in FND_TREE_LABEL.This identifies the label associated with this tree node. |
| PARENT_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Parent data source Id |
| PARENT_PK1_VALUE | VARCHAR2 | 100 |  |  | The column identifies the data source primary key 1. |
| PARENT_PK2_VALUE | VARCHAR2 | 100 |  |  | The column identifies the data source primary key 2. |
| PARENT_PK3_VALUE | VARCHAR2 | 100 |  |  | The column identifies the data source primary key 3. |
| PARENT_PK4_VALUE | VARCHAR2 | 100 |  |  | The column identifies the data source primary key 4. |
| PARENT_PK5_VALUE | VARCHAR2 | 100 |  |  | The column identifies the data source primary key 5. |
| PARENT_TREE_LABEL_ID | VARCHAR2 | 32 |  |  | Tree label Id of the Parent Node |
| SORT_ORDER | NUMBER |  | 18 |  | The sort order of nodes within the tree. |
| DEPTH | NUMBER |  | 18 | Yes | Depth of this tree node. This is useful for breadth-first traversal of the tree. |
| CHILD_COUNT | NUMBER |  | 18 | Yes | Number of children of this tree node. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_POS_TREE_NODE_N02 | Non Unique | FUSION_TS_TX_DATA | TREE_CODE, ENTERPRISE_ID |
| PER_POS_TREE_NODE_N03 | Non Unique | FUSION_TS_TX_DATA | TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID, REFERENCE_TREE_CODE, REFERENCE_TREE_VERSION_ID, ENTERPRISE_ID |
| PER_POS_TREE_NODE_N04 | Non Unique | FUSION_TS_TX_DATA | TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID, PARENT_TREE_NODE_ID, ENTERPRISE_ID |
| PER_POS_TREE_NODE_N05 | Non Unique | FUSION_TS_TX_DATA | TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID, ENTERPRISE_ID, PK1_START_VALUE, PK2_START_VALUE, PK3_START_VALUE, PK4_START_VALUE, PK5_START_VALUE |
| PER_POS_TREE_NODE_N06 | Non Unique | FUSION_TS_TX_DATA | TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID, ENTERPRISE_ID, PARENT_PK1_VALUE, PARENT_PK2_VALUE, PARENT_PK3_VALUE, PARENT_PK4_VALUE, PARENT_PK5_VALUE |
| PER_POS_TREE_NODE_N07 | Non Unique | FUSION_TS_TX_DATA | TREE_NODE_ID, ENTERPRISE_ID |
| PER_POS_TREE_NODE_N09 | Non Unique | FUSION_TS_TX_DATA | TO_NUMBER("PK1_START_VALUE"), TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID |
| PER_POS_TREE_NODE_N13 | Non Unique | FUSION_TS_TX_DATA | PARENT_TREE_NODE_ID, PK1_START_VALUE, TREE_VERSION_ID, TREE_CODE, TREE_STRUCTURE_CODE |
| PER_POS_TREE_NODE_PK | Unique | FUSION_TS_TX_DATA | TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID, TREE_NODE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
