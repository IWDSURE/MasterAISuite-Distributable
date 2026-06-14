# PER_ORG_TREE_NODE_RF

Organization Hierarchy Tree Node RF Table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perorgtreenoderf-30854.html#perorgtreenoderf-30854](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perorgtreenoderf-30854.html#perorgtreenoderf-30854)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ORG_TREE_NODE_RF_PK | TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID, TREE_NODE_ID, RF_TREE_NODE_ID, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TREE_STRUCTURE_CODE | VARCHAR2 | 30 |  | Yes | Foreign key to TREE_STRUCTURE_CODE on FND_TREE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| TREE_CODE | VARCHAR2 | 30 |  | Yes | Foreign key to TREE_CODE on FND_TREE. |
| TREE_VERSION_ID | VARCHAR2 | 32 |  | Yes | Foreign key to VERSION_ID on FND_TREE_VERSION |
| RF_TREE_NODE_ID | VARCHAR2 | 32 |  | Yes | Unique identifier for tree node. |
| TREE_NODE_ID | VARCHAR2 | 32 |  | Yes | Unique identifier for tree node. |
| DATA_SOURCE_ID | VARCHAR2 | 32 |  | Yes | Data Source Id for the Data Source from which this node is coming |
| PK1_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. |
| PK2_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. |
| PK3_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. |
| PK4_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. |
| PK5_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the node. |
| TREE_LABEL_ID | VARCHAR2 | 32 |  |  | Foreign key to the TREE_LABEL_ID in FND_TREE_LABEL.This identifies the label associated with this tree node. |
| ANCESTOR_TREE_NODE_ID | VARCHAR2 | 32 |  |  | ID of the tree node that is the ancestor of this node. If this value is null, this node is the root node of the tree. |
| ANCESTOR_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Ancestor data source Id |
| ANCESTOR_PK1_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the ancestor node. |
| ANCESTOR_PK2_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the ancestor node. |
| ANCESTOR_PK3_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the ancestor node. |
| ANCESTOR_PK4_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the ancestor node. |
| ANCESTOR_PK5_VALUE | VARCHAR2 | 100 |  |  | Primary key value of the ancestor node. |
| ANCESTOR_TREE_LABEL_ID | VARCHAR2 | 32 |  |  | Tree label of the ancestor node.Foreign key to FND_TREE_LABEL. |
| DISTANCE | NUMBER |  | 18 | Yes | Distance between the Node and its Ancestor. |
| IS_LEAF | VARCHAR2 | 1 |  | Yes | Flag to indicate if this Node is a Leaf Node. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ORG_TREE_NODE_RF_N1 | Non Unique | FUSION_TS_TX_DATA | TO_NUMBER("PK1_VALUE"), TO_NUMBER("ANCESTOR_PK1_VALUE"), TREE_VERSION_ID |
| PER_ORG_TREE_NODE_RF_N2 | Non Unique | FUSION_TS_TX_DATA | TO_NUMBER("PK1_VALUE"), TREE_VERSION_ID, TREE_CODE, TREE_STRUCTURE_CODE |
| PER_ORG_TREE_NODE_RF_N3 | Non Unique | FUSION_TS_TX_IDX | ANCESTOR_TREE_NODE_ID, TREE_VERSION_ID, TREE_CODE, TREE_STRUCTURE_CODE |
| PER_ORG_TREE_NODE_RF_N4 | Non Unique | FUSION_TS_TX_DATA | TO_NUMBER("ANCESTOR_PK1_VALUE"), TREE_VERSION_ID, TREE_CODE |
| PER_ORG_TREE_NODE_RF_PK | Unique | FUSION_TS_TX_DATA | TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID, TREE_NODE_ID, RF_TREE_NODE_ID, ENTERPRISE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
