# HWR_DI_DOCUMENT

The document table stores document objects.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdidocument-20652.html#hwrdidocument-20652](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdidocument-20652.html#hwrdidocument-20652)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_DI_DOCUMENT_PK | DOCUMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| DOCUMENT_ID | NUMBER |  | 18 | Yes | This is the primary key for the document table. | Active |
| NAME | VARCHAR2 | 256 |  |  | This is the human readable representation of this document. | Active |
| UUID | VARCHAR2 | 64 |  | Yes | This is the UUID identifying the document. | Active |
| EXPIRATIONDATE | TIMESTAMP |  |  | Yes | This is the expiration date of this document. |  |
| DOC_CONTENT_ID | NUMBER |  | 18 | Yes | This is the id of the content associated to this document. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_DI_DOCUMENT_N1 | Non Unique | FUSION_TS_TX_DATA | DOC_CONTENT_ID |  |
| HWR_DI_DOCUMENT_U1 | Unique | FUSION_TS_TX_DATA | DOCUMENT_ID | Active |
| HWR_DI_DOCUMENT_U2 | Unique | FUSION_TS_TX_DATA | UUID | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
