# PER_DEPT_TREE_NODE_CF

This table holds the column flattened data for tree nodes of a Department tree hierarchy.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdepttreenodecf-31208.html#perdepttreenodecf-31208](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdepttreenodecf-31208.html#perdepttreenodecf-31208)

## Primary Key

| Name | Columns |
|------|----------|
| PER_DEPT_TREE_NODE_CF_PK | ENTERPRISE_ID, TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID, CF_TREE_NODE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TREE_STRUCTURE_CODE | VARCHAR2 | 30 |  | Yes | Foreign key to TREE_STRUCTURE_CODE on FND_TREE |
| TREE_CODE | VARCHAR2 | 30 |  | Yes | Foreign key to TREE_CODE on FND_TREE. |
| TREE_VERSION_ID | VARCHAR2 | 32 |  | Yes | Foreign key to VERSION_ID on FND_TREE_VERSION |
| CF_TREE_NODE_ID | VARCHAR2 | 32 |  | Yes | Unique identifier for tree node. |
| DEP0_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP0_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP0_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP0_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP0_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP0_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP1_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP1_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP1_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP1_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP1_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP1_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP2_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP2_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP2_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP2_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP2_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP2_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP3_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP3_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP3_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP3_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP3_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP3_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP4_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP4_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP4_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP4_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP4_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP4_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP5_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP5_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP5_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP5_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP5_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP5_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP6_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP6_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP6_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP6_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP6_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP6_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP7_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP7_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP7_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP7_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP7_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP7_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP8_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP8_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP8_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP8_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP8_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP8_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP9_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP9_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP9_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP9_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP9_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP9_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP10_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP10_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP10_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP10_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP10_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP10_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP11_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP11_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP11_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP11_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP11_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP11_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP12_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP12_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP12_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP12_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP12_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP12_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP13_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP13_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP13_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP13_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP13_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP13_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP14_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP14_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP14_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP14_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP14_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP14_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP15_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP15_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP15_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP15_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP15_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP15_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP16_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP16_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP16_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP16_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP16_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP16_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP17_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP17_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP17_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP17_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP17_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP17_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP18_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP18_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP18_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP18_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP18_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP18_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP19_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP19_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP19_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP19_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP19_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP19_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP20_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP20_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP20_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP20_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP20_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP20_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP21_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP21_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP21_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP21_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP21_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP21_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP22_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP22_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP22_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP22_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP22_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP22_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP23_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP23_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP23_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP23_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP23_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP23_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP24_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP24_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP24_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP24_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP24_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP24_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP25_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP25_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP25_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP25_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP25_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP25_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP26_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP26_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP26_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP26_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP26_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP26_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP27_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP27_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP27_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP27_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP27_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP27_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP28_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP28_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP28_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP28_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP28_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP28_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP29_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP29_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP29_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP29_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP29_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP29_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP30_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP30_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP30_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP30_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP30_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP30_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP31_DATA_SOURCE_ID | VARCHAR2 | 32 |  |  | Data Source Id for the Data Source from which this node is coming |
| DEP31_PK1_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP31_PK2_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP31_PK3_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP31_PK4_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| DEP31_PK5_VALUE | VARCHAR2 | 100 |  |  | Stores Organization Id for the node. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| DISTANCE | NUMBER |  | 15 | Yes | Distance between the Node and its Ancestor. |
| DEP0_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP1_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP2_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP3_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP4_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP5_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP6_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP7_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP8_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP9_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP10_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP11_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP12_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP13_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP14_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP15_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP16_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP17_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP18_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP19_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP20_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP21_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP22_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP23_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP24_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP25_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP26_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP27_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP28_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP29_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP30_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |
| DEP31_TREE_NODE_ID | VARCHAR2 | 32 |  |  | Unique identifier for tree node. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_DEPT_TREE_NODE_CF_N1 | Non Unique | FUSION_TS_TX_DATA | TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID, DEP0_TREE_NODE_ID |
| PER_DEPT_TREE_NODE_CF_N2 | Non Unique | FUSION_TS_TX_DATA | DEP0_PK1_VALUE, TREE_VERSION_ID |
| PER_DEPT_TREE_NODE_CF_PK | Unique | FUSION_TS_TX_DATA | ENTERPRISE_ID, TREE_STRUCTURE_CODE, TREE_CODE, TREE_VERSION_ID, CF_TREE_NODE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
