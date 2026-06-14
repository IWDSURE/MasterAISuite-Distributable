# PER_DOC_TYPE_SEC_PROF_DOCTYPES

This table contains the Document Types selected in the Document Type Security Profile.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdoctypesecprofdoctypes-28981.html#perdoctypesecprofdoctypes-28981](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdoctypesecprofdoctypes-28981.html#perdoctypesecprofdoctypes-28981)

## Primary Key

| Name | Columns |
|------|----------|
| PER_DOCTYP_SEC_PROF_DOCTYP_PK | DOC_TYPE_SEC_PROF_DOC_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| DOC_TYPE_SEC_PROF_DOC_TYPE_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |  |
| DOC_TYPE_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_DOC_TYPE_SECURITY_PROFILE table. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| DOCUMENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_DOCUMENT_TYPES_B table |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_DOC_TYPE_SEC_PROF_DOC_N20 | Non Unique | Default | SGUID |
| PER_DOCTYP_SEC_PROF_DOCTYP_FK2 | Non Unique | FUSION_TS_TX_DATA | DOC_TYPE_SECURITY_PROFILE_ID |
| PER_DOCTYP_SEC_PROF_DOCTYP_PK1 | Unique | FUSION_TS_TX_DATA | DOC_TYPE_SEC_PROF_DOC_TYPE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
