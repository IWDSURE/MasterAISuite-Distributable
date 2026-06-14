# HWR_DI_DOCUMENT_CONTENT

The document table stores serialized document content objects.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdidocumentcontent-23749.html#hwrdidocumentcontent-23749](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdidocumentcontent-23749.html#hwrdidocumentcontent-23749)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_DI_DOC_CONTENT_PK | DOC_CONTENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| DOC_CONTENT_ID | NUMBER |  | 18 | Yes | This is the primary key for the document content table. | Active |
| DOC_CONTENT | BLOB |  |  |  | This is the document binary content. | Active |
| DOC_SIZE | NUMBER |  | 18 |  | This column stores the size for the document content. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_DI_DOCUMENT_CONTENT_U1 | Unique | FUSION_TS_TX_DATA | DOC_CONTENT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
