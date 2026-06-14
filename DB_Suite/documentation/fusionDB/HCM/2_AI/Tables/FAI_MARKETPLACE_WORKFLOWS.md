# FAI_MARKETPLACE_WORKFLOWS

This table stores the marketplace workflows

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** fai_marketplace_workflows

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faimarketplaceworkflows-10674.html#faimarketplaceworkflows-10674](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faimarketplaceworkflows-10674.html#faimarketplaceworkflows-10674)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_MARKETPLACE_WORKFLOWS_PK | MARKETPLACE_WORKFLOW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MARKETPLACE_WORKFLOW_ID | NUMBER |  | 18 | Yes | Uniquely identifies the marketplace workflow |
| WORKFLOW_NAME | VARCHAR2 | 200 |  | Yes | Name for the marketplace workflow |
| WORKFLOW_CODE | VARCHAR2 | 200 |  | Yes | Code for the marketplace workflow |
| FAMILY | VARCHAR2 | 80 |  | Yes | The product family associated to the marketplace workflow |
| PRODUCT | VARCHAR2 | 100 |  | Yes | The product associated to the marketplace workflow |
| SPECIFICATION | CLOB |  |  | Yes | JSON specification for the marketplace workflow |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_MARKETPLACE_WORKFLOWS_U1 | Unique | FAI_MARKETPLACE_WORKFLOWS_U1 | MARKETPLACE_WORKFLOW_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
