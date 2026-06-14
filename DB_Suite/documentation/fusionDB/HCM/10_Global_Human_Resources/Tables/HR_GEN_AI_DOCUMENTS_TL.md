# HR_GEN_AI_DOCUMENTS_TL

This table stores the Gen AI Documents name and description.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** hr_gen_ai_documents_tl

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaidocumentstl-11787.html#hrgenaidocumentstl-11787](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaidocumentstl-11787.html#hrgenaidocumentstl-11787)

## Primary Key

| Name | Columns |
|------|----------|
| HR_GEN_AI_DOCUMENTS_TL_PK | DOCUMENT_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DOCUMENT_ID | NUMBER |  | 18 | Yes | The Unique Identifier of the Gen AI Document in the Agentic Workflow |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 200 |  |  | Name of the Gen AI Document in the Agentic Workflow |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Description of the Gen AI Document in the Agentic Workflow |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HR_GEN_AI_DOCUMENTS_TL_PK | Unique | Default | DOCUMENT_ID, LANGUAGE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
