# IRC_DOCUMENT_TYPES

This table holds the different document types that canidates can upload for approval.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdocumenttypes-9689.html#ircdocumenttypes-9689](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdocumenttypes-9689.html#ircdocumenttypes-9689)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_DOCUMENT_TYPES_PK | DOCUMENT_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DOCUMENT_TYPE_ID | NUMBER |  | 18 | Yes | Primary key. Uniquely identifies a Document Type. |
| VERIFICATION_REQUIRED_FLAG | VARCHAR2 | 1 |  | Yes | Document category required verification or not. |
| CATEGORY_ID | NUMBER |  | 18 | Yes | Foreign key to FND_DOCUMENT_CATEGORIES table. |
| CATEGORY_NAME | VARCHAR2 | 120 |  |  | Name of the Attachment Category. |
| SYSTEM_DOCUMENT_TYPE | VARCHAR2 | 120 |  | Yes | Name of the document type from hr document types. |
| ACTIVE_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether the Document type is active or not. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_DOCUMENT_TYPES_FK1 | Non Unique | Default | CATEGORY_ID |
| IRC_DOCUMENT_TYPES_N1 | Non Unique | Default | ACTIVE_FLAG, CATEGORY_ID |
| IRC_DOCUMENT_TYPES_PK | Unique | Default | DOCUMENT_TYPE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
