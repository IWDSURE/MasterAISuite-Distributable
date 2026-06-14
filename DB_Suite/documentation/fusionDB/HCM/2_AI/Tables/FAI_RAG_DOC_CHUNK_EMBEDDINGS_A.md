# FAI_RAG_DOC_CHUNK_EMBEDDINGS_A

Fusion AI Rag Document Chunk Embeddings.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FAI_RAG_DOC_CHUNK_EMBEDDINGS_A

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/fairagdocchunkembeddingsa-15360.html#fairagdocchunkembeddingsa-15360](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/fairagdocchunkembeddingsa-15360.html#fairagdocchunkembeddingsa-15360)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_RAG_DOC_CHNK_EMDB_A_PK | CHUNK_EMBEDDINGS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USE_CASE_PARTITION | VARCHAR2 | 400 |  |  | Partitioning key based on use case segmentations. |
| USE_CASE_ID | VARCHAR2 | 100 |  | Yes | Use case ID. The usual structure is "aa.bb.cc". |
| CHUNK_EMBEDDINGS_ID | NUMBER |  | 18 | Yes | Primary key. Unique identifer for the chunk embeddings. |
| CHUNK_METADATA_ID | NUMBER |  | 18 | Yes | Unique identifier for the chunk metadata. Primary key - fai_rag_doc_chunk_metadata table. |
| CHUNK_ID | NUMBER |  | 18 | Yes | Unique identifier for the chunk. |
| CHUNK_EMBEDDINGS | VECTOR |  |  |  | Generated embeddings for the chunk. |
| EMBEDDINGS_GENERATION_DATE | TIMESTAMP |  |  |  | Date embeddings are generated. |
| EMBEDDINGS_STATUS | VARCHAR2 | 30 |  |  | Status of the embedding. Completed, Inprogress |
| RETRY_COUNT | NUMBER |  | 2 |  | Retry count. This returns the number of times system tried to generate the embeddings. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_RAG_DOC_CHNK_EMBD_A_PK | Unique | FAI_RAG_DOC_CHNK_EMBD_A_PK | CHUNK_EMBEDDINGS_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
