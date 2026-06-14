# WLF_ATTACHED_DOCUMENTS

Table to store details of activity bookings

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfattacheddocuments-9171.html#wlfattacheddocuments-9171](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfattacheddocuments-9171.html#wlfattacheddocuments-9171)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ATTACHED_DOCUMENTS_PK | ATTACHED_DOCUMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTACHED_DOCUMENT_ID | NUMBER |  | 18 | Yes | Attached Document Id PK |
| DOCUMENT_ID | NUMBER |  | 18 |  | Document id |
| ENTITY_NAME | VARCHAR2 | 40 |  | Yes | Name of the business object that the document is attached to. Usually this is the database table name (ie WLF_RESOURCES_B) |
| PK1_VALUE | VARCHAR2 | 150 |  |  | Value of the PK in the entity table |
| ACCESS_LEVEL | VARCHAR2 | 30 |  |  | Indicates who can access this document |
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
| WLF_ATTACHED_DOCUMENTS_FK1 | Non Unique | Default | DOCUMENT_ID |
| WLF_ATTACHED_DOCUMENTS_U1 | Unique | Default | ATTACHED_DOCUMENT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
