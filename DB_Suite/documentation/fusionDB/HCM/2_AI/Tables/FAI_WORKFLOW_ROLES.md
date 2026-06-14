# FAI_WORKFLOW_ROLES

This table stores the association between Workflows and Roles for generative AI.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiworkflowroles-27421.html#faiworkflowroles-27421](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiworkflowroles-27421.html#faiworkflowroles-27421)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_WORKFLOW_ROLES_PK | WORKFLOW_ROLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORKFLOW_ROLE_ID | NUMBER |  | 18 | Yes | Primary Key: Uniquely identify the Workflow role. |
| WORKFLOW_ID | NUMBER |  | 18 | Yes | Workflow this role is associated to. Foreign key to FAI_WORKFLOWS_B. |
| ROLE | VARCHAR2 | 80 |  | Yes | This column stores a role associated with the Workflow. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_WORKFLOW_ROLES_PK | Unique | Default | WORKFLOW_ROLE_ID |
| FAI_WORKFLOW_ROLES_U1 | Unique | Default | WORKFLOW_ID, ROLE |

---

[← Back to Index](../2_AI_Tables_Index.md)
