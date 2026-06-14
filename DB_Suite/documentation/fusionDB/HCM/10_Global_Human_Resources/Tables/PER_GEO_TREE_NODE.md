# PER_GEO_TREE_NODE

Geographic Hierarchy Tree Node Table

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergeotreenode-5917.html#pergeotreenode-5917](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergeotreenode-5917.html#pergeotreenode-5917)

## Primary Key

| Name | Columns |
|------|----------|
| PER_GEO_TREE_NODE_PK | TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID, TREE_NODE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TREE_STRUCTURE_CODE | VARCHAR2 | 30 |  | Yes | Foreign key to TREE_STRUCTURE_CODE on FND_TREE |  |
| TREE_CODE | VARCHAR2 | 30 |  | Yes | Foreign key to TREE_CODE on FND_TREE. | Active |
| TREE_VERSION_ID | VARCHAR2 | 32 |  | Yes | Foreign key to VERSION_ID on FND_TREE_VERSION | Active |
| TREE_NODE_ID | VARCHAR2 | 32 |  | Yes | Unique identifier for tree node. | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| PARENT_TREE_NODE_ID | VARCHAR2 | 32 |  |  | ID of the tree node that is the parent of this node. If this value is null, this node is the root node of the tree.If there are multiple rows with this value null, then they are all root nodes, effectively forming a forest of disjoint trees. | Active |
| DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming | Active |
| PK1_START_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. For range-based tree nodes, this is the start of the range and PK1_END_VALUE forms the end. | Active |
| PK2_START_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. For range-based tree nodes, this is the start of the range and PK1_END_VALUE forms the end. | Active |
| PK3_START_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. For range-based tree nodes, this is the start of the range and PK1_END_VALUE forms the end. | Active |
| PK4_START_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. For range-based tree nodes, this is the start of the range and PK1_END_VALUE forms the end. | Active |
| PK5_START_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. For range-based tree nodes, this is the start of the range and PK1_END_VALUE forms the end. | Active |
| PK1_END_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the end of the range for range-based tree nodes. If the node is not range based, then this value is null. | Active |
| PK2_END_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the end of the range for range-based tree nodes. If the node is not range based, then this value is null. | Active |
| PK3_END_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the end of the range for range-based tree nodes. If the node is not range based, then this value is null. | Active |
| PK4_END_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the end of the range for range-based tree nodes. If the node is not range based, then this value is null. | Active |
| PK5_END_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the end of the range for range-based tree nodes. If the node is not range based, then this value is null. | Active |
| REFERENCE_TREE_CODE | VARCHAR2 | 30 |  |  | For tree-in-tree, this is the reference to the tree code. The referenced tree has to belong to the same Tree Structure. | Active |
| REFERENCE_TREE_VERSION_ID | VARCHAR2 | 32 |  |  | For tree-in-tree, this is the reference to the tree version. The referenced tree has to belong to the same Tree Structure. | Active |
| TREE_LABEL_ID | VARCHAR2 | 32 |  |  | Foreign key to the TREE_LABEL_ID in FND_TREE_LABEL.This identifies the label associated with this tree node. | Active |
| PARENT_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Parent data source Id | Active |
| PARENT_PK1_VALUE | VARCHAR2 | 100 |  |  | The column identifies the data source primary key 1. | Active |
| PARENT_PK2_VALUE | VARCHAR2 | 100 |  |  | The column identifies the data source primary key 2. | Active |
| PARENT_PK3_VALUE | VARCHAR2 | 100 |  |  | The column identifies the data source primary key 3. | Active |
| PARENT_PK4_VALUE | VARCHAR2 | 100 |  |  | The column identifies the data source primary key 4. | Active |
| PARENT_PK5_VALUE | VARCHAR2 | 100 |  |  | The column identifies the data source primary key 5. | Active |
| PARENT_TREE_LABEL_ID | VARCHAR2 | 32 |  |  | Tree label Id of the Parent Node | Active |
| SORT_ORDER | NUMBER |  | 18 |  | The sort order of nodes within the tree. | Active |
| DEPTH | NUMBER |  | 18 | Yes | Depth of this tree node. This is useful for breadth-first traversal of the tree. | Active |
| CHILD_COUNT | NUMBER |  | 18 | Yes | Number of Children of the Node. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| PER_GEO_TREE_NODE_PK | Unique | FUSION_TS_TX_DATA | TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID, TREE_NODE_ID, ORA_SEED_SET1 | Active |
| PER_GEO_TREE_NODE_PK1 | Unique | FUSION_TS_TX_DATA | TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID, TREE_NODE_ID, ORA_SEED_SET2 |  |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
