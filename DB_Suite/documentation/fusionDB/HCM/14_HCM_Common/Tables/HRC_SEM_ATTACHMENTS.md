# HRC_SEM_ATTACHMENTS

This table contains the uploaded resume of the person.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemattachments-31257.html#hrcsemattachments-31257](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemattachments-31257.html#hrcsemattachments-31257)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_ATTACHMENTS_PK | ATTACHMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTACHMENT_ID | NUMBER |  | 18 | Yes | This is the primary key of the table. |
| PERSON_ID | NUMBER |  | 18 | Yes | This is the foreign key to person table. |
| ID | NUMBER |  | 18 | Yes | This field is populated with attachment ID of the resume document. |
| ORIGINAL_CONTENT_ID | VARCHAR2 | 256 |  |  | This is the original content id of the attachment. |
| CANONICAL_CONTENT_ID | VARCHAR2 | 256 |  |  | This is the canonical content id of the attachment. |
| DOCUMENT_TYPE | VARCHAR2 | 128 |  |  | This column contains the document type. |
| CONTENT | CLOB |  |  |  | This column contains the content of the attachement. |
| UPLOAD_DATE | TIMESTAMP |  |  |  | This is the time stamp when the resume is uploaded. |
| LAST_MODIFIED_DATE | TIMESTAMP |  |  |  | This is the time stamp when the resume is modified. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SEM_ATTACHMENTS_N1 | Non Unique | FUSION_TS_TX_DATA | PERSON_ID |
| HRC_SEM_ATTACHMENTS_N2 | Non Unique | FUSION_TS_TX_DATA | LAST_MODIFIED_DATE |
| HRC_SEM_ATTACHMENTS_N3 | Non Unique | FUSION_TS_TX_DATA | DOCUMENT_TYPE |
| HRC_SEM_ATTACHMENTS_U1 | Unique | FUSION_TS_TX_DATA | ATTACHMENT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
