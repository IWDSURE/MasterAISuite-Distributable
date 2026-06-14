# WLF_DOCUMENTS_B

Table to store document locations

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfdocumentsb-14754.html#wlfdocumentsb-14754](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfdocumentsb-14754.html#wlfdocumentsb-14754)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_DOCUMENTS_B_PK | DOCUMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DOCUMENT_ID | NUMBER |  | 18 | Yes | Document ID PK |
| LOCATION | VARCHAR2 | 2000 |  |  | Stores where this document is located |
| PROVIDER | VARCHAR2 | 30 |  |  | Storage provider of the document |
| FILE_NAME | VARCHAR2 | 256 |  |  | File name of the file uploaded by the user |
| DATATYPE_CODE | VARCHAR2 | 30 |  |  | Type of file, can be FILE, TEXT,URL etc. |
| UUID | VARCHAR2 | 64 |  |  | Unique ID used identify the document at the storage provider |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_DOCUMENTS_B_U1 | Unique | Default | DOCUMENT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
