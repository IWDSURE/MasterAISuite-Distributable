# HR_GEN_AI_DOCUMENTS_B

This table stores the Gen AI Documents

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** hr_gen_ai_documents_b

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaidocumentsb-14432.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaidocumentsb-14432.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_GEN_AI_DOCUMENTS_B_PK | DOCUMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DOCUMENT_ID | NUMBER |  | 18 | Yes | The Unique Identifier of the Gen AI Document in the Agentic Workflow |
| TOOL_ID | NUMBER |  | 18 |  | Uniquely identifies the Gen AI Tool in the Agentic Workflow |
| STATUS | VARCHAR2 | 20 |  |  | Status of the Gen AI Document in the Agentic Workflow |
| DOCUMENT_CREATED_DATE | DATE |  |  |  | Created Date of the Gen AI Document in the Agentic Workflow |
| DOCUMENT_PUBLISHED_DATE | DATE |  |  |  | Published Date of the Gen AI Document in the Agentic Workflow |
| DOCUMENT_DELETED_DATE | DATE |  |  |  | Deleted Date of the Gen AI Document in the Agentic Workflow |
| OWNER_ID | NUMBER |  | 18 |  | ID of the owner who created the Gen AI Document in the Agentic Workflow |
| OWNER_NAME | VARCHAR2 | 200 |  |  | Name of the owner who created the Gen AI Document in the Agentic Workflow |
| INTERNAL_NAME | VARCHAR2 | 400 |  |  | This column represents the system name of the Document. |
| INTERNAL_DESCRIPTION | VARCHAR2 | 2000 |  |  | This column represents the system description of the Document. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_GEN_AI_DOCUMENTS_B_PK | Unique | Default | DOCUMENT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
