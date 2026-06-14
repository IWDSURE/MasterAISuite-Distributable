# HR_GEN_AI_DOCUMENTS

This table stores the Gen AI Documents

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** HR_GEN_AI_DOCUMENTS

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaidocuments-20135.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaidocuments-20135.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_GEN_AI_DOCUMENTS_PK | DOCUMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DOCUMENT_ID | NUMBER |  | 18 | Yes | The Unique Identifier for the Gen AI Document |
| TOOL_ID | NUMBER |  | 18 |  | Uniquely identifies the Gen AI Tool |
| NAME | VARCHAR2 | 200 |  |  | Name of the Gen AI Document |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Description of the Gen AI Document |
| STATUS | VARCHAR2 | 20 |  |  | Status of the Gen AI Document |
| DOCUMENT_CREATED_DATE | DATE |  |  |  | Created Date of the Gen AI Document |
| DOCUMENT_PUBLISHED_DATE | DATE |  |  |  | Published Date of the Gen AI Document |
| DOCUMENT_DELETED_DATE | DATE |  |  |  | Deleted Date of the Gen AI Document |
| OWNER_ID | NUMBER |  | 18 |  | ID of the owner who created the Gen AI Document |
| OWNER_NAME | VARCHAR2 | 200 |  |  | Name of the owner who created the Gen AI Document |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_GEN_AI_DOCUMENTS_PK | Unique | HR_GEN_AI_DOCUMENTS_PK | DOCUMENT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
